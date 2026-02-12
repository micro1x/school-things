#DFS algorithm
import copy
import queue as Q
class Graph:
    def __init__(self):
        self.graph = dict()
        self.cost_dict = dict() 
        self.final_dict = dict()
        
    def addEdge(self, u, v, c):
        if u not in self.graph:
            qu = Q.PriorityQueue()
            self.graph.update({u: qu})
        self.graph[u].put(v)
        self.cost_dict.update({(u, v): c})
        
    def tnode(self, n):
        self.visited = [False] * n
    
    def UCS_util(self, s, visited, path, goal, value): 
        path.append(s)
        visited[s] = True
        if goal == s:
            self.final_dict.update({tuple(path): value})
            return
 
        for i in self.graph[s].queue:
            if visited[i] == False:
                self.UCS_util(i, copy.deepcopy(visited), 
copy.deepcopy(path),goal,value+ self.cost_dict[s, i])
 
    def UCS(self, s, goal):
 
        self.visited[s] = True
        path = [s]
        for i in self.graph[s].queue:
            if self.visited[i] == False:
                value = self.cost_dict[s, i]
                self.UCS_util(i, copy.deepcopy(self.visited), copy.deepcopy(path), 
goal, value)
 
    def all_paths(self):
        if bool(self.final_dict):
            print("All paths to each location from calpheon: ")
            
        for i in self.final_dict:
            print("The route to the last location is: ", i, "feet: ", 
self.final_dict[i])
        else:
            print("No optimal path found.")
            
    def optimal_path(self):
        if bool(self.final_dict):
            print("The fastest trip to each destination is: ", min(self.final_dict, 
key=self.final_dict.get))
        else:
            print("No optimal path found.")

# Creating Graph object and assigning number of nodes
g = Graph()
g.tnode(10)
# Making the Graph
g.addEdge(0, 1, 690); g.addEdge(0, 2, 1040); g.addEdge(1, 3, 1700);
g.addEdge(2, 5, 1320); g.addEdge(3, 6, 2090); g.addEdge(3, 5, 2090);
g.addEdge(4, 6, 1250); g.addEdge(4, 7, 1130); g.addEdge(5, 4, 1770);
g.addEdge(6, 7, 1080); g.addEdge(5, 0, 2070); g.addEdge(5, 8, 3880);
g.addEdge(8, 4, 2660); g.addEdge(8, 9, 3640); g.addEdge(9, 7, 580);
# 0 is start node and 7 is goal node
g.UCS(0,7)
# Find all the path between 0 and 7
g.all_paths()
# Find the most optimal path between 0 and 7
g.optimal_path()