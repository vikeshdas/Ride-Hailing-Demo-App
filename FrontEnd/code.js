window.addEventListener('load', function () {
   function myFun(e) {
      var val = "Source to Destination Distance " + e.target.innerHTML;
      val = val + " meter"
      document.getElementById('h1').innerHTML = val;
   }
   var maxLength = 10;
   function CreateLottoValues() {
      return Math.floor(Math.random() * 2200);
   }
   function UpdateTable() {

      var table=document.getElementById('table');
      var tablecontent='';
      for(var i=0;i<maxLength;i++)
      {
         tablecontent+="<tr>";
         for(var j=0;j<maxLength;j++)
         {
            tablecontent+="<td><div class='content' id='cell" + String(i) + String(j) + "'></div></td>";
         }
         tablecontent+="</tr>";
      }
      table.innerHTML+=tablecontent;
 

      for (var i = 0; i < maxLength; i++) {
         for (var j = i; j < maxLength; j++) {
            tmp = 'cell' + i + j;
            temp = 'cell' + j + i;
            if (i == j) {
               document.getElementById(tmp).innerHTML = 0;
            }
            else {
               var val = CreateLottoValues();
               document.getElementById(tmp).innerHTML = val;
               document.getElementById(temp).innerHTML = val;
            }

         }
      }
   }

   function checkValid() {
      console.log('inside checkvalid');
      var source = document.getElementById("pick").value;
      var destin = document.getElementById("drope").value;
      if (source > 10) {
         document.getElementById('alt').innerHTML = "!not valid intput source should be less then 11 ";
      }
      else if (destin > 10) {
         document.getElementById('alt').innerHTML = "!not valid intput destination should be less then 11 ";
      }
      else {
         document.getElementById('succ').innerHTML = "finding driver..........";
      }
   }
   UpdateTable();
   var submitButton = document.getElementById("submitbtn");
   submitButton.addEventListener('click', checkValid );
})
