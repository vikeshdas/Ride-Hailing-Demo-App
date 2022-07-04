
"""
    mode find the sortest distanc from source to all node and path between sorce to all node 
"""
import heapq
import sys

class Sortestpath:

        def minDistance(self,dist,queue):
            """
                find the node with minimum value which is not visited yet

                Arg: 
                    dist:
                        array of integer ,sortest distance from source to ith node
                    queuue:
                        queu with integer value ,represent the node 
                return:
                    integer value,node with minimum weight which is not visited yet       
            """
            minimum = float("Inf")
            min_index = -1
            
            for i in range(len(dist)):
                if dist[i] < minimum and i in queue:
                    minimum = dist[i]
                    min_index = i
            return min_index

        def dijkstra(self, graph, v, src):
            """
                find the sortest distance from source to all node using dijkshtra algorithm
                Args:
                    graph:
                        matrix of integer value,graph with v number of node
                    v:
                        integer value,number of node in graph    
                    src:
                       integer value,source node

                Return:
                    cab:
                        list of integer value(node)top sortest distance node from source
                    dist: 
                        list of integer,sortest distance from source to all node
                    heapInd:
                        integer value pointing to the array's(cab) last element
                    Parent:
                        array of integer node,value of ith index of array represent second last node in sortest path from source to ithe node               

            """
            row = v
            col = v
            diameter=200
            cab=[sys.maxsize]*4
            heapInd=0
            dist = [float("Inf")] * row
            parent = [-1] * row
            dist[src] = 0
        
            # Add all vertices in queue
            queue = []
            for i in range(row):
                queue.append(i)
                
            #Find shortest path for all vertices
            while queue:
                u = self.minDistance(dist,queue)
    
                # remove min element    
                queue.remove(u)
                for i in range(col):
                    if graph[u][i] and i in queue:
                        if dist[u] + graph[u][i] < dist[i]:
                            dist[i] = dist[u] + graph[u][i]
                            parent[i] = u

                            # cab
                            largest=heapq.nlargest(1,cab)
                            largest=largest[0]
                            if dist[i] < diameter:
                                if heapInd < len(cab):
                                    cab[heapInd] = dist[i]
                                    heapInd += 1
    
                                elif heapInd >= len(cab) and dist[i]< largest:
                                    num = largest
                                    indx = cab.index(num)
                                    cab[indx] = dist[i]
    
    

            return cab,dist,heapInd,parent 

        def printPath(self, parent, j,stack):
            """
                find the sortest path using the second last connected node in path 

                Args:
                    Parent:
                        array of integer node,value of ith index of array represent second last node in sortest path from source to ithe node
                    j:
                        destination node
                    stack:
                        list,all node in path from source to jth node
                return:
                    list,all node in path from source to jth node                
            """
            #Base Case : If j is source
            if parent[j] == -1 :
                stack.append(j)
                return stack
            self.printPath(parent , parent[j],stack)
            stack.append(j)
            return stack
                                
                