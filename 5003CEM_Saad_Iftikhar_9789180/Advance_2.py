from collections import defaultdict
import sys


class Graph():
    def __init__(self, size):
        self.edges = defaultdict(list)  # dictionary of all connected nodes e.g. {'X': ['A', 'B', 'C', 'E'], ...}
        self.weights = {}  # dictionary of edges and weights e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}
        self.size = size  # Instance variable "size" is created.
        self.dist = []  # The varible "self.dist"is created and the default value of an empty list assigned to the
        # variable "self.dist".
        for i in range(size):  # looping from 0 to the value of the "size" variable.
            self.dist.append(sys.maxsize)  # appending the value of"sys.maxsize" varible to the self.dist varible.
        self.previous = []  # The varible "self.previous" is created and the default value of an empty list assigned
        # to the variable "self.previous"
        for i in range(size):  # looping from 0 to the value of the "size" variable.
            self.previous.append(None)  # appending "None" value to the self.dist varible.

    def add_edge(self, from_node, to_node, weight):  # bidirectional
        self.edges[from_node].append(to_node)  # connecting the edges between nodes.
        self.edges[to_node].append(from_node)  # connecting the edges between nodes.
        self.weights[(from_node, to_node)] = weight  # inserting weights in between two nodes.
        self.weights[(to_node, from_node)] = weight  # inserting weights in between two nodes.

    def findSmallestNode(self):
        smallest = self.dist[self.getIndex(self.Q[0])]  # assighning the value of smallest weight's of Node's starting
        # from our initial node to our end Node
        result = self.getIndex(self.Q[0])  # assighning indexes as we move through the Node
        node = self.dist  # assighning the value of smallest weight's of Node's starting from our initial node to our
        # end Node inside lists.
        for i in range(len(self.dist)):  # looping from 0 to the length of the "self.dist" variable
            if self.dist[i] < smallest:  # if the value of "self.dist[i]"  is less than
                # the value of the "smallest" varible.
                if node in self.Q:  # if the node varible's value is present in the Q varible.
                    smallest = self.dist[i]  # assighn the current value of the
                    # "self.dist[i]" varible to the smallest varible.
                    result = self.getIndex(node)  # assighning the value of "self.getIndex(node)"
                    # varible to the result varible.
        return result  # retruning th result varible's value

    def getIndex(self, neighbour):
        for i in range(len(self.unpoppedQ)):  # looping from 0 to the length of the "self.unpoppedQ" variable
            if neighbour == self.unpoppedQ[i]:  # if the value of both the varibles "neighbour" and
                # "self.unpoppedQ[i]" is equal.
                return i  # returning the i varibles value.

    def getPopPosition(self, uNode):
        result = 0  # assighning the value of 0 to the result varible.
        for i in range(len(self.Q)):  # looping from 0 to the length of the "self.Q" variable
            if self.Q[i] == uNode:  # if the value of both the varibles "self.Q[i]" and "uNode" is equal.
                return i  # returning the i varibles value.
        return result  # returning the result varibles value.

    def getUnvisitedNodes(self, uNode):
        resultList = []  # The varible "resultList"is created and is assighned the value of an empty list.
        allNeighbours = self.edges[uNode]  # assigning the edges of the nodes to the "allNeighbours" varible.
        for neighbour in allNeighbours:  # looping  through each element in the "allNeighbours" varible using the
            # vraible "neighbour".
            if neighbour in self.Q:  # if the neighbour varible's value is present in the self.Q varible.
                resultList.append(neighbour)  # appending the neighbour variable's value to the resultList varible.
        return resultList  # returning the resultList varibles value.

    def dijsktra(self, start, end):
        self.Q = []  # The varible "self.Q "is created and is assighned the value of an empty list.
        for key in self.edges:  # looping  through each element in the "self.edges" varible using the vraible "key".
            self.Q.append(key)  # appending the key variable's value to the self.Q varible.
        for i in range(len(self.Q)):  # looping from 0 to the length of the "self.Q" variable
            if self.Q[i] == start:  # if Q[i] varible's value is equal to the start varible's value
                # (in our case it's O).
                self.dist[i] = 0  # self.dist[i] varible is assighned the value 0.
        self.unpoppedQ = self.Q[0:]  # assighning the value of "self.Q[0:]" varible to the "self.unpoppedQ" varible.

        while self.Q:  # while self.Q not equal to 0 or False. (can also be broken by using a break statement)
            u = self.findSmallestNode()  # using the findSmallestNode() function to assign the value of the smallest
            # Node to u.
            if self.dist[u] == sys.maxsize:  # if the value of the varibles "self.dist[u]" and "sys.maxsize" are equal.
                break  # break from the loop.                                      
            if self.unpoppedQ[u] == end:  # if the "self.unpoppedQ[u]" varible's value is equal to the
                # "end" varibles value.
                break  # break from the loop.
            uNode = self.unpoppedQ[u]  # assighning the value of "self.unpoppedQ[u]" varible to the "uNode" varible.

            for i in self.edges[uNode]:  # looping  through each element in the "self.edges[uNode]"
                # varible using the vraible "i".
                if i in self.Q:  # if the "i" varible's value is present in the self.Q varible.
                    if i in self.getUnvisitedNodes(uNode):  # if the "i" varible's value is present in
                        # the self.getUnvisitedNodes(uNode).
                        if self.dist[self.unpoppedQ.index(uNode)] + self.weights[(uNode, i)] < self.dist[self.unpoppedQ.index(i)]:
                            # if the combined value of both the "(self.dist[self.unpoppedQ.index(uNode)])" and
                            # "self.weights[(uNode,i)]" vaibles
                            # is less then the value of the "self.dist[self.unpoppedQ.index(i)" varible
                            # (distance + weight < unpoped).
                            self.dist[self.unpoppedQ.index(i)] = self.dist[self.unpoppedQ.index(uNode)] + self.weights[(uNode,i)]
                            # the varible "self.dist[self.unpoppedQ.index(i)]" is assighned the combined
                            # value of the "self.dist[self.unpoppedQ.index(uNode)]" and
                            # "self.weights[(uNode,i)]" varibles.
                            self.previous[self.unpoppedQ.index(i)] = uNode  # The
                            # "self.previous[self.unpoppedQ.index(i)]" varible is assighned the value of
                            # the variable "uNode".
            self.Q.pop(self.Q.index(uNode))  # The value of "self.Q.index(uNode)" is poped from the self.Q list.

        weight = self.dist[self.unpoppedQ.index(uNode) + 1]  # assighing the value of the
        # "self.dist[self.unpoppedQ.index(uNode)+1]" varible to the "weight" varible.
        shortest_path = []  # The varible "shortest_path"is created and is assighned the value of an empty list.
        shortest_path.insert(0, end)  # inserting the 0 as the start and the end varible's value as to the shortest
        # path varible.
        u = self.getIndex(end)  # The varible u is assighned the value of "self.getIndex(end)".

        while self.previous[u] != None:  # as long as the value of "self.previous[u]" varible is not None
            shortest_path.insert(0, self.previous[u])  # insert the "self.previous[u]" varible's value to
            # the "shortest_path" varible.
            u = self.getIndex(self.previous[u])  # assigning the value of "self.previous[u]" varible to the "u" varible.

        return shortest_path, weight  # returning the values of the "shortest_path" and the "weight" varibles


graph = Graph(8)  # new graph variable is created using the Graph class

# Assighning the weights of the edges.
edges = [
    ('O', 'A', 2),
    ('O', 'B', 5),
    ('O', 'C', 4),
    ('A', 'B', 2),
    ('A', 'D', 7),
    ('A', 'F', 12),
    ('B', 'C', 1),
    ('B', 'D', 4),
    ('B', 'E', 3),
    ('C', 'E', 4),
    ('D', 'E', 1),
    ('D', 'T', 5),
    ('E', 'T', 7),
    ('F', 'T', 3),
]

for edge in edges:  # looping  through each element in the "edges" varible using the vraible "edge".
    graph.add_edge(*edge)  # adding the required edges to the graph
print(graph.dijsktra('O', 'T'))  # printing the path and the total number of weight for the path.