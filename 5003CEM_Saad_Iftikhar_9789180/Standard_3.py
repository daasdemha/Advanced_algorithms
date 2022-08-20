class Graph(object): # A class object called "Graph" is created.
    # The first parameter "self" is a reference to the current instance of the class.
    def __init__(self, size): # The class is initialized with the parameter defined. The 2nd
        # parameter is called "size".

        self.adjMatrix = [] # The default value of a empty list assigned to to the variable "self.adjMatrix".
        if size <= 0: # if the number entered is less then or equal to 0
        	print("enter a postive number greater then or equal to 1") # printing a instruction

        for i in range(size):                                               # looping from 0 to the value of the "size" variable.
            self.adjMatrix.append([0 for i in range(size)])                 # Making empty lists with the number value of the size variable and filling list's with 0's equal to the value of the size varible.
        self.size = size                                                    # Instance variable "size" is assighned.

    #methods for (1) adding a vertex; (2) adding an edge; (3) removing an edge; and (4) printing the
    #matrix should appear here
    
    def addVertex(self, number_to_append): # A function to append vertex into the matrix,
        # with the second parameter 'number_to_append'.


        matrix_length = len(self.adjMatrix)  # matrix_length variable is assighned the value of the length of the self.adjMatrix
        inserted_row = number_to_append - matrix_length           # inserted_row variable is created and assighned the value of number_to_append - matrix_length variable

        for i in range(matrix_length):                           # looping from 0 to to the value of the matrix_length varibale.
            for j in range(inserted_row):                        # looping from 0 to to the value of the inserted_row varibale.
                self.adjMatrix[i].append(0)                      # appending the newly added vertex to each list in the matrix.
                                   
        self.adjMatrix.append([0 for i in range(number_to_append)]) # adding the new vertix to the matix and appedning 0's to it.


    def addEdge(self, vertex1, vertex2):# A function to add edges into the matrix,
        # with the second parameter 'vertex1' and the third paramenter 'vertex2'.

        if vertex1 > len(self.adjMatrix) or vertex1 > len(self.adjMatrix) or vertex1 < 0 or vertex1 < 0: # checking if the first and the secound argument added to the parameter is greater then or less then the size of the elements in the matrix.
            print("vertex does not exist") # printing a instruction

        elif vertex1 == vertex2:   # checking if both vertexes are equal in value                                                    
            print("Same vertex",vertex1," and vertex ", vertex2)  # printing a instruction
        
        elif self.adjMatrix[vertex1-1][vertex2-1] == 1: # if there is a edge present between vertex 1 and vertex 2
            print("Edge already present between vertex",vertex1," and vertex ", vertex2)  # printing a instruction

        else: #otherwise
            self.adjMatrix[vertex1-1][vertex2-1] = 1  # assighning the vaule of 1 into the first selected vertex 'vertex 1'
            self.adjMatrix[vertex2-1][vertex1-1] = 1  # assighning the vaule of 1 into the secound selected vertex 'vertex 2'
    
    def removeEdge(self, vertex1, vertex2):   # A function to remove edges from the matrix,
        # with the second parameter 'vertex1' and the third paramenter 'vertex2'.
        
        if vertex1 > len(self.adjMatrix) or vertex1 > len(self.adjMatrix) or vertex1 < 0 or vertex1 < 0: # checking if the first and the secound argument added to the parameter is greater then or less then the size of the elements in the matrix.
            print("vertex does not exist") # printing a instruction

        elif vertex1 == vertex2:   # checking if both vertexes are equal in value                                                    
            print("Same vertex",vertex1," and vertex ", vertex2)  # printing a instruction

        elif self.adjMatrix[vertex1-1][vertex2-1] == 0: # if there is a edge present between vertex 1 and vertex 2
            print("No edge between vertex",vertex1," and vertex ", vertex2)  # printing instructions

        else: # otherwise
           self.adjMatrix[vertex1-1][vertex2-1] = 0 # assighning the vaule of 0 into the first selected vertex 'vertex 1'
           self.adjMatrix[vertex2-1][vertex1-1] = 0 # assighning the vaule of 0 into the secound selected vertex 'vertex 2'

    def display(self):   # A function to return the matrix
        title = [] # The default value of a empty list assigned to  the variable "title". 
        title.append([i for i in range(1, len(self.adjMatrix)+1)]) # appending the numbers from 1 to one item more then length of the self.adjMatrix varible to make a title for the number of edges.
        a = 1 # the variable a is set to 1
        print("  ",title) # the title varaibles value is printed
        print("-" * (len(self.adjMatrix) * 4)) # '-' symbol is printed times the length of the list times 4.
        for i in range(len(self.adjMatrix)): # elemenets are looped throught to the lenghth of the self.adjMatrix and assighned to i.
        	print(a,"|", self.adjMatrix[i]) # the value of a then a '|' symbol and the self.adjMatrix lists single element is printed in each itteration of the loop.
        	a += 1 # a is added to the value of a
        	
  
def main(): # main function is created

    new_graph = Graph(4) # new graph variable is created using the Graph class

    new_graph.addEdge(2, 3)  # edges are inserted inside the Graph.
    new_graph.addEdge(3, 4)  # edges are inserted inside the Graph.
    new_graph.addEdge(4, 2)  # edges are inserted inside the Graph.
    new_graph.addEdge(1, 3)  # edges are inserted inside the Graph.


    new_graph.display()# the graph is printed.

    new_graph.removeEdge(2, 3)  # edges are removed from the Graph.

    print("\n")
    new_graph.display()  # the graph is printed.
    
    new_graph.addVertex(5)   # vertex are inserted inside the Graph.
    
    print("\n")
    new_graph.display() # the graph is printed.



if __name__ == '__main__':
   main() # main function is called.