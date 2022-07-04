// function UpdateTable() {
//    let maxLength = 10;
//    let val;
//    let table = document.getElementById('table');
//    let tablecontent = '';
//    for (let i = 0; i < maxLength; i++) {
//       tablecontent += "<tr>";
//       for (let j = 0; j < maxLength; j++) {
//          tablecontent += "<td><div class='content' id='cell" + String(i) + String(j) + "'></div></td>";
//       }
//       tablecontent += "</tr>";
//    }
//    table.innerHTML += tablecontent;

//    for (let i = 0; i < maxLength; i++) {
//       for (let j = i; j < maxLength; j++) {
//          tmp = 'cell' + i + j;
//          temp = 'cell' + j + i;

//          val = graph[i][j];
//          document.getElementById(tmp).innerHTML = val;
//          document.getElementById(temp).innerHTML = val;

//       }
//    }
// }