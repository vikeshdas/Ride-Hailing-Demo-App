# Ride-Hailing-Demo-App

#### This is a map 
map is a graph as adjacency matrix  each cell(index i,j) has a value which represent distance between source i to destination j,
if any user enter source as (i) and destination as(j) ,it will pic value of matrix[i][j] which is distance from source to destination of user,
<img src="map.png" width="100%" align="top-left" alt="" title="RNN" />

#### here user will enter their source and destination address  
now we have source ot destination distance,we have to calculate sortest path from source to destination for that i hvae used dikhstra 
algorithm.after applying dikshtra algorithm we will have sortest distance in km or miter according to that we will calculate amount to pay for this ride
and how much time will take to reach source to destination.i have generated a random value 'trafic' if there is value in trafic means thre is trafic in path
so will add that trafic in distance(to reach source to destination).then new time will genereted (to reach destination).

i will fine nearest driver using dikshtra algorithm(i am not calling dikshtra algorithm again when i was nearest path from source to destination same time i will pck four nodes which is near to source)which is four near drivers

<img src="input.png" width="100%" align="top-left" alt="" title="RNN" />


##### nearest driver accepted ride 
out of four nearest driver some driver may cancel,but any one may accept the ride 
for that first i pushed all four near driver in queue,then i generate a random value form 0 to 1 if  random value 
is zero means driver canceled ride and i will pop front of quue which means there are only 3 driver left for user .
if random value is 1 means driver accepted the ride ,then i will calculate time according to distance from user to driver to reach.
<img src="accept.png" width="100%" align="top-left" alt="" title="RNN" />
