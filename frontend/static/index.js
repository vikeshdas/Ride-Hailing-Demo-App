/**
method of this model hit flask API and get the graph from the back end and display on * frontend, find a cab for the user and calculate distance from source to destination, source to cab and path from source to destination and  display on  the front end  
*/
let search_cab;
let reset;
let graph=[[]];
let edge = [[]];
let v = 10;
let traffic=[];

let backend_ip="127.0.0.1";
let backend_port="5000";

if(graph.length===1)
{
   mpa();
}
 
/**
* This function creates a network graph using Highcharts.chart API
*/
function networkGraph() {
   f = Highcharts.chart('container', {
      chart: {
         height: 700,
         width: 865,
         type: 'networkgraph',
      },

      title: {
         text: 'Map'
      },
      plotOptions: {
         networkgraph: {
            keys: ['from', 'to', 'color', 'label'],
            layoutAlgorithm: {
               friction: -1.0,
               integration: 'verlet',
               linkLength: 370,
            }
         }
      },
      series: [{

         marker: {
            radius: 20
         },
         link: {
            width: 3,
         },
         dataLabels: {
            enabled: true,
            linkFormat: '{point.label}'
         },
         data: edge
      }]
   });
}

/**
 This function makes the source to destination path color green and  remaining    edges color makes black color
*/
function source_to_des_path(path) {
   v = 10;
   edge = [[]];
   let l=0;
   let k = 0;
   for (let i = 0; i < v; i++) {
      for (let j = 0; j < v; j++) {
         if (graph[i][j] != 0) {  
               edge[k] = [i, j, 'black', graph[i][j]];
         }
         k++;
      }
   }
   let n=path.length;
      for (let i = 0; i < n - 1; i++) {
      edge[k] = [path[i], path[i + 1], '#C1FA0E',graph[path[i]][path[i + 1]]];
      k++;
   }
   networkGraph();
}

/**
This function color edges of the graph according to the traffic in three color green, red, yellow, green path means the path is traffic less, yellow edge means there is little bit of traffic on the path, red means there is more 
traffic
*/
function colorEdge() {
   let n = path.length;
   edge = [[]];
   let k = 0;
   for (let i = 0; i < v; i++) {
      for (let j = 0; j < v; j++) {
         if (graph[i][j] != 0) {
            if (traffic[i][j] < 0.4) {
               edge[k] = [i, j, 'green', graph[i][j]];
            }
            else if ((traffic[i][j] >= 0.4) && (traffic[i][j] < 0.7)) {
               edge[k] = [i, j, 'yellow', graph[i][j]];
            }
            else{
               edge[k] = [i, j, 'red', graph[i][j]];
            }
         }
         k++;
      }
   }

   networkGraph();
}

/**
 This function sends the request to flask API and get a response as a graph as matrix and traffic as matrix and display matrix as a network graph  on the front end using Highchart. chart API with traffic
*/
function mpa() {
   let xmlHttp = new XMLHttpRequest();
   xmlHttp.open("POST", "http://" + backend_ip + ":" + backend_port + "/map", true);
   xmlHttp.onprogress = function () {

   }
   xmlHttp.onload = function () {
      let res = this.responseText;
      res=JSON.parse(res);
      graph = res.graph;
      traffic=res.traffic;
      colorEdge();
   };
   xmlHttp.send(" ");
}

/**
this function validates the user input, for example, the user can input the source and destination node between zero and 9 if the user enters more than 9 or less than 0 or the input is a string it will give an alert 
*/
function validation(src, des) {
   let v = 10;
   if (src >= v || src < 0) {
      window.alert("source location should be less then 9 and greter then 0");
      return false;
   }
   if (des >= v || src < 0) {
      window.alert("destination location should be less then 9 and greter then 0");
      return false;
   }
   if (src === des) {
      window.alert("your pick up and drop point are same");
      return false;
   }
   if (isNaN(src)) {
      window.alert("string is not allow");
      return false;
   }
   if (isNaN(des)) {
      window.alert("destination address is string ");
      return false;
   }
   return true;
}

/**
This function sends a request to flask API and get the source to the destination distance and source to cab distance and path node from source to destination in response and display on the front end
*/
function find_cab() {
   let src;
   let res;
   let des;
   let formData;
   let xmlHttp;

   src = document.getElementById("pickup").value;
   des = document.getElementById("drop").value;
   document.getElementById("acpt").textContent='';
   document.getElementById("source_to_cab_dis").textContent='';
   document.getElementById("dist").textContent='';
   document.getElementById('path').textContent='';

   if (validation(src, des) === false)
      return;

   document.getElementById("pickup").value = '';
   document.getElementById("drop").value = '';

   formData = new FormData();
   formData.append("source", src);
   formData.append("destination", des);
   xmlHttp = new XMLHttpRequest();
      xmlHttp.open("POST", "http://" + backend_ip + ":" + backend_port +/find-driver", true);
   xmlHttp.onprogress = function () {
   }
   xmlHttp.onload = function () {
      res = this.responseText;
      res = JSON.parse(res);
      source_to_des_path(res.path);
      if (res.accep == 1) {
         document.getElementById("acpt").innerHTML = "driver coming...";
         document.getElementById("source_to_cab_dis").innerHTML = "Source to Cab: " + res.source_to_cab + " Km";
         document.getElementById("dist").innerHTML = "Source to Destination: " + res.srctodes + " Km";

         let Path = res.path;
         document.getElementById('path').innerHTML="Path: "
         for (var i = 0; i < Path.length; i++) {
            var newspan = document.createElement('path');
            if (i == Path.length - 1)
               newspan.innerHTML = Path[i];
            else
               newspan.innerHTML = Path[i] + '->';

            document.getElementById('path').appendChild(newspan);
         }

      }
      else {
         document.getElementById("acpt").innerHTML = "Cab is not availble right now";
      }
   };
   xmlHttp.send(formData);

}

/**
This function reset the graph and HTML contents as it was before the cab searching 
*/
function refresh()
{
   colorEdge();
   document.getElementById("acpt").textContent='';
   document.getElementById("source_to_cab_dis").textContent='';
   document.getElementById("dist").textContent='';
   document.getElementById('path').textContent='';
}


window.addEventListener('load', (event) => {
   search_cab = document.getElementById("submitbtn");
   search_cab.addEventListener("click", find_cab);

   reset=document.getElementById("reset");
   reset.addEventListener("click",refresh);
});
