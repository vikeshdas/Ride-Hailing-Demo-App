"""
    model find the cab for the user and calculate  source to destination distance,source to cab distance and path from source to destination.
"""
import heapq
import numpy as np
import random

from sortestpath import Sortestpath


class Cab:
    """
        initialize graph as matrix and makes source to destination equal edge weight to destination to source if ith, jth cell is not zero that means the ith node is connected to jth node else there is no connection between ith node to jth node
    """
    def __init__(self):
        self.v=10
        self.srtPath=Sortestpath()
        self.graph = np.random.randint(1, 6, size=(self.v, self.v))
        for i in range((self.v)-1):
            for j in range(i+1,self.v):
                self.graph[i][j]=self.graph[j][i]

        for i in range(15):
            row = random.randint(0, 9)
            col= random.randint(0, 9)
            self.graph[row][col]=0
            self.graph[col][row]=0

    
    def traffic(self,traffic):
        """
        This funciton makes trafic value from node 'a' to node 'b' 
        and node 'b' to node 'a' equal trafic value,
        and remove edge from trafic which are not in map but are in trafic matrix 

        Args:
            traffic:
                matrix with integer cell value between 1 to 3

        Returns:
            matrix of integer one with diagnol cell zero
        """
        for i in range((self.v)-1):
            for j in range(i+1,self.v):
                traffic[i][j]=traffic[j][i]

        for i in range(self.v):
            for j in range(self.v):
                if(self.graph[i][j]==0):
                    traffic[i][j]=0     
        return traffic       
         

    def map(self):
        """
        makes the diagonal element of graph zero that represents ith node is not connected to itself, which means source to source distance always will be zero. Generate a traffic matrix,ith, jth index represent the amount of traffic on the ith, jth edge in the graph, and normalize the traffic matrix 

        Returns:
            graph: matrix of integer represent a graph
            traffic: matrix of integer represent a traffic value on graph edge
        """
        for i in range(self.v):
            for j in range(self.v):
                if (i == j):
                    self.graph[i][j] = 0  

        #generate traffic
        traffic=np.random.randint(1, 4, size=(self.v, self.v))
        traffic=self.traffic(traffic)
        traffic=self.normalizetraffic(traffic)                        
        return self.graph,traffic  


    def normalizetraffic(self, trafic):
        """
        normalize the traffic matrix between zerot to one using 
        (trafic[i][j]-min)/(max-min),where max and min is smallest
        and largest value in the matrix 

        Args:
            traffic:
                matrix with integer cell value between 1 to 3

        Returns:
            trafic: normalize traffic matrix of integer 
        """
        trafic=np.asfarray(trafic)
        min=10**9;
        max=-10**9;
        for i in range(self.v):
            for j in range(self.v):
                if(trafic[i][j]<min):
                    min=trafic[i][j]
                if(trafic[i][j]>max):
                    max=trafic[i][j]

        for i in range(self.v):
            for j in range(self.v):
                trafic[i][j]=float((trafic[i][j]-min)/(max-min))
        return trafic                    



    def find_cab(self,start,end):
        """
        find the nearest can near source node, and calculate source to destination distance, source to cab distance and shortest path between source to destination using Dijkstra's algorithm

        Args:
            start:
                source node 
            end: 
                destination node
        Returns:
            accpept: interger value ,1 means driver acceptec rider else 
                     canceled ride
            source_to_cab:ineger value source to cab distance
            source_to_destination: integer value source to destination distance
            Path: list of integer value source to destination sortest path
            traf: normalize traffic matrx with float value in each cell betwee 
                  zero to one
        """
        accpept=0
        traf=np.random.randint(1, 4, size=(self.v, self.v))
        traf=self.traffic(traf)
        newgraph=self.graph+traf
        cab,sortdist,heapInd,Path=self.srtPath.dijkstra(newgraph, self.v, start)
        stack=[]
        Path=self.srtPath.printPath(Path, end,stack)
        if heapInd==0:
            return 0
        else:                       
            source_to_cab,source_to_destination,accpept=self.showdist(sortdist,
                                                        cab,end)   

            source_to_cab=source_to_cab                                  

        traf=self.normalizetraffic(traf)    
        return accpept,source_to_cab,source_to_destination,Path,traf


    def showdist(self,sortdist,cab,end):
        """
        we have some cab in the heap which is top small distance node from source, generate a random number between zero and one if a value is zero then a top cab from heap will be removed that means driver canceled the ride, if the value is 1 means driver accepted the ride and that distance will be source to cab distance 

        Args:
            sortdist:
                list of integer value,sortest distance from soruce to all node
            cab: 
                list of integer value,top sortest node distance from source
            end:
                destination node 
        Returns:
            source_to_cab: 
                        integer value,source node to cab node distaance

            source_to_destinatino: 
                        sortest distance between source to destination
            accept:
                integer value,if it is 1 then driver a driver accepted ride if it is zero then no driver accepted ride            
        """
        source_to_destination=0
        source_to_cab=0
        accept=0
        n=len(cab)
        cabDistance=0
        heapq.heapify(cab)
        
        for i in range(n):
            accept=np.random.randint(0,2, size=(1, 1))

            if not accept:
                heapq.heappop(cab)
            else:
                cabDistance=cab[0]
                break

        if accept:
            source_to_destination=sortdist[end]
            source_to_cab=cabDistance

        return source_to_cab,source_to_destination,accept           
