"""
785. Is Graph Bipartite?
There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

There are no self-edges (graph[u] does not contain u).
There are no parallel edges (graph[u] does not contain duplicate values).
If v is in graph[u], then u is in graph[v] (the graph is undirected).
The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.

MEDIUM


"""

"""
Time complexity : O(V+E) where V is vertices in the graph and E is edges
Space compelxity: O(V)


"""

from collections import deque
class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        
        
        N = len(graph)
        colorMap = {}
        
        if N==0 or N==1 or N==2:
            return True
        
        q = deque()
        
        ## Iterating over each node just to take care of disconnected components
        for nodes in range(N):
            if len(graph[nodes])==0:
                colorMap[nodes] = 1
                continue
                
            if nodes not in colorMap:
                colorMap[nodes]=1
                q.append(nodes)
                
            
            while(q):
                
                curr_node = q.popleft()
                curr_color = colorMap[curr_node]
                
                
                for adj in graph[curr_node]:
                    if adj not in colorMap:
                        colorMap[adj] = ~curr_color
                        q.append(adj)
                        
                    else:
                        if colorMap[adj] == curr_color:
                            return False
                        
        return True
                        
