import numpy as np
import sys
import heapq
def showtime(dist,cab,end,graph,v):
    n=len(cab)
    cabDistance=0
    heapq.heapify(cab)
    
    accept=0
    for i in range(n):
        accept=np.random.randint(0,2, size=(1, 1))

        if accept==0:
           print("your driver has canceled ",heapq.heappop(cab))
   
        else:
           print("accepted ",accept)
           print(cab)
           cabDistance=cab[0]
           break

    if accept==1:    
       print("source to destination distance ",dist[end],"meter")  
       print("source to cab distance ",cabDistance,"meter") 
       averagespeak=40
       time=(cabDistance)/averagespeak
       print("your driver will reach within ",time,"minutes\n") 
    else:
        print("driver are not accepting try letter")
        main(graph,v)     



def ditkshtra(graph, v, start,end):
    dist = [sys.maxsize] * v
    visited = [False] * v
    cab=[sys.maxsize]*4
    dist[start] = 0
    heapInd=0
    diameter=200
    for i in range(v):
        index = 0
        mini = sys.maxsize
        for u in range(v):
            if dist[u] < mini and visited[u] == False:
                mini = dist[u]
                index = u
        visited[index] = True
        for j in range(v):
            if graph[index][j] != 0 and visited[j] == False and dist[j] > (dist[index] + graph[index][j]):
                dist[j] = (dist[index] + graph[index][j])

                # cab
                if dist[j] < diameter:
                    if heapInd < len(cab):

                        cab[heapInd] = dist[j]
                        heapInd += 1
                    elif heapInd >= len(cab) and dist[j] < heapq.nlargest(1, cab):
                        num = heapq.nlargest(1, cab)
                        indx = cab.index(num)
                        cab[indx] = dist[j]
    if heapInd==0:
        print("ther are no cab near you")
        main(graph,v) 

    else:                       
        print(dist)
        print("there are ",len(cab),"driver new you ",cab)
        showtime(dist,cab,end,graph,v)


def traffic(graph,v,start,end):
     print("Searching Cab...\n")
     traf=np.random.randint(0, 20, size=(v, v))
     newgraph=graph+traf
     ditkshtra(newgraph, v, start, end)


def takeInput(graph, v,service_availbe):
    print("enter source address, input a number between 0 to", v - 1, "(both 0 and", v - 1, "are inclusive)")
    start = ""
    while (type(start) != int):
        try:
            start = int(input())
        except:
            if type(start) != int:
                print("this is not a valid value between 0 to", v - 1, "enter again")

    


    print("enter destination address, input a number between 0 to", v - 1, "(both 0 and", v - 1, "are inclusive)")
    end=""
    while (type(end) != int):
        try:
            end = int(input())
        except:
            if type(end) != int:
                print("this is not a valid value between 0 to", v - 1, "enter again")


    if start<0 or start>v-1 or end<0 or end>v-1:
        print("this is not a valid value between 0 to", v - 1, "enter again")
        takeInput(graph,v,service_availbe)

    if start == end:
        print("source address can't be equal to destination address")
        takeInput(graph,v,service_availbe)

    if start in service_availbe or end in service_availbe:
        print("cab service is not availble in your area")
        main(graph,v,service_availbe) 

        
    else:
        traffic(graph,v,start,end)


def main(graph, v,service_availbe):
    temp = 'y'
    while(temp == 'y'):
        print('Welcome to cab service, here is the current map: ')
        print(graph)
        temp = input("do you want to search cab, press y or n: ")

        if temp == "y" and type(temp) != int:
            takeInput(graph, v,service_availbe)
        elif temp=='n' and type(temp) != int:
            break
        else :
            print("you can either press 'y' or 'n");
            temp='y'   
        


if __name__ == "__main__":
    v = 100
    service_availbe={0,2,5,7}
    graph = np.random.randint(0, 500, size=(v, v))
    main(graph, v,service_availbe)
