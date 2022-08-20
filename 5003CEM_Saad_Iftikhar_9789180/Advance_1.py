""" 

    Basic BST code for inserting (i.e. building) and printing a tree

    second standard viva task*** (of 5) will be to implement a find method into
    the class BinaryTree from pseudocode. See the STD_2 task sheet for Week 5. 

"""

import math  # The Maths module is imported.

""" Node class
"""


class Node:  # A class object called "Node" is created.

    # The first parameter "self" is a reference to the current instance of the class.

    def __init__(self, data=None):  # The class is initialized with the parameter defined. The 2nd
        # parameter is called "data" which has a default value of 'None'.
        self.data = data  # Instance variable "data" is created.
        self.left = None  # The default value of 'None' assigned to "self.left".
        self.right = None  # The default value of 'None' assigned to "self.right".


""" BST class with insert and display methods. display pretty prints the tree
"""


class BinaryTree:  # A class object called "BinaryTree" is created.

    def __init__(self):  # The class is initialized with the parameter defined.
        self.root = None  # The default value of 'None' assigned to the instance variable "root".

    def insert(self, data):  # A function to insert data into the root,
        # branch and leaf Nodes of the BinaryTree with the second parameter 'data'.
        if self.root is None:  # It's checked that if the "self.root" is pointing towards the object 'None'.
            self.root = Node(data)  # The value of the "data" instance of the "Node" class is 
            # assigned to "self.root".
        else:  # Otherwise do the following.
            self._insert(data, self.root)  # The "data" is inserted in a "Node" of BinaryTree class using the
            # private function "_insert".

    def _insert(self, data, cur_node):  # A private function to insert data into the branch 'Nodes' of the
        # BinaryTree with the parameters defined. The 2nd parameter is the "data" to be inserted and the
        # third parameter is initially the "root Node" in our BinaryTree.
        if data < cur_node.data:  # if the data to be inserted in the Node is less than the current
            # selected Node's data.
            if cur_node.left is None:  # It's checked that if the left branch or leaf of the current node is
                # pointing towards the object 'None'.
                cur_node.left = Node(data)  # The left branch or leaf of the current 'Node' is assigned the
                # 'Node(data)' value.
            else:  # Otherwise do the following.
                self._insert(data, cur_node.left)  # The private function "_insert" calls is called
                # recursively. with 2 arguments, the value of the selected "data" variable and
                # "cur_node.left"/(the left of the current Node) until the data has been placed inside a
                # Node with 'None' value on a left branch or leaf of the BinaryTree.

        elif data > cur_node.data:  # if the data to be inserted in the Node is greater 
                                   # than the current selected Node's data.
            if cur_node.right is None:  # It's checked that if the right branch or leaf of the current 'Node' is
                # pointing towards the object 'None'.
                cur_node.right = Node(data)  # The right branch or leaf of the current node is assigned the Node                               
            # data value.
            else:  # Otherwise do the following.
                self._insert(data,
                             cur_node.right)  # The private function _insert calls is called recursively.
                # with 2 arguments, data and cur_node.right until the data has been placed inside a 
                # Node with 'None'
                # value on a right branch or leaf of the BinaryTree.
        else:  # Otherwise do the following.
            print(data, "Already present in tree")  # print the data to be inserted is already present in the 
               # tree. The same element can't be entered more than once.

    def remove(tree, target):  # The function to remove data from the Binarytree. The second parameter is the 
                               # target the user enters to be removed.
	    if tree.root is None:     # If tree.root node is None
	        return False           # Then return Flase
	    elif tree.root.data == target:  # if tree.root node's value is the same as the target variable's value.
	        if tree.root.left is None and tree.root.right is None:  #if the left node of the tree.root value is None 
	                                                           # and the right node of the tree.root is None.
	            tree.root = None  # then the tree.root's is assigned the value None.
	        elif tree.root.left and tree.root.right is None:  # if the left node of the tree.root's node has a value 
	             # other then None and right nodes's with respect to tree.root's node has a value of None.
	            tree.root = tree.root.left # then tree.root's node is assigned the left node's value with 
	                                       # respect to tree.root.

	        elif tree.root.left is None and tree.root.right: # if the left node of the tree.root node's value is 
	                          # None and the right node of the tree.root's node has a value other then None.
	            tree.root = tree.root.right  # Then tree.root is assigned the value of the node on the right in 
	                                         # respect to it.
	        elif tree.root.left and tree.root.right:  # if the left node and the right node with
	                                         # respect to the tree.root node has a value other then None.
	            tree.if_left_and_right(tree.root) # the function if_left_and_right is called with 
	                                              # tree.root as it's given argument.
	    parent = None       # The parent variable is created and assigned the value of None.
	    node = tree.root    # The node variable is created and assigned the tree.root's value.
	     # case 1: Target not found
	    while node and node.data != target:  # if the node and 'node.data' hold values equal to the target
	        parent = node                    # The parent variable stores the node value
	        if target < node.data:           # if the target is less than the 'node.data' data
	            node = node.left             # then the node variable is assigned
	        elif target > node.data:         # if target is more than the value in node.data
	            node = node.right            # node variable is given 'node.right' value

	    if node is None or node.data != target:  # if the node is empty, or node.data is not equal to target
	        return False

	    # case 2: Target has no children
	    elif node.left is None and node.right is None: # if node.left has a value of None and node.right  has a 
	                                                  # value of None.
	        if target < parent.data:      # if the value of the target variable is less than the parent.data 
	                                      # variable's value.
	            parent.left = None # then assigns parent.left value to None
	        else:                  # otherwise
	            parent.right = None       # assighn parent.right variable's value to None
	        return True

	    # case 3: Target has left child only
	    elif node.left and node.right is None: # if node.left has a value other then None and node.right's 
	                                           # value is None
	        if target < parent.data: # if the target varbiles value is less than the parent varibles value.
	            parent.left = node.left  # the node.left data is added to the parent.left node
	        else:                        # otherwise
	            parent.right = node.left   # parent.right varible is Assighned the node.left varible's value.
	        return True   # return True

	    # case 4: Target has right child only
	    elif node.left is None and node.right:  # if node.left has a value of None and node.right has a value other 
	                                            # then None.
	        if target < parent.data:            # if target variables value is less than parent.data varibles value.
	            parent.left = node.right        # parent.left variable is Assigned the node.right varible's value.
	        else:                               # otherwise
	            parent.right = node.right       # parent.right variable is Assigned the node.right variable’s value.
	        return True                         # return True
	   # case 5: Target has left and right children
	    else:                                   # otherwise
	        tree.if_left_and_right(node)        # The function if_left_and_right is called with node as the argument
    def if_left_and_right(tree,node): # This is a subfunction to the remove function. This function helps in the 
	                            # deletion of a node. The second parameter is obtained from the remove function.
	    delNodeParent = node  # delNodeParent variable is created and assigned the node variables value
	    delNode = node.right  # delNode variable created and assigned the value of node.right

	    while delNode.left:   # while delNode.left varibles has a value other then None.
	        delNodeParent = delNode   # delNodeParent is assigned the value of the variable delNode.
	        delNode = delNode.left    # delNode variable is assigned the value of delNode.left variable.
	    node.data = delNode.data      # the node.data variable is assigned the delNode.data variables value
	    if delNode.right:             # if delNode.right varible has a value other then None.
	        if delNodeParent.data > delNode.data:  # if the delNodeParent.data variables value greater than the 
	                                               # delNode.data varibles value.
	            delNodeParent.left = delNode.right # delNodeParent.left variable is assigned the delNode.right 
	                                               # varibles value
	        else:                                   # otherwise
	            delNodeParent.right = delNode.right # delNodeParent.right variable is assigned delNode.right 
	                                                # variables value.
	    else:                                       # otherwise
	        if delNode.data < delNodeParent.data:   # if the delNode.data variable’s value is lesser than the 
	                                                # delNodeParent.data varible's value.
	            delNodeParent.left = None           # delNodeParent.left variable is assigned the value of None.
	        else:                                   # otherwise
	            delNodeParent.right = None          # delNodeParent.right variables is assigned the Value None.

    def display(self, cur_node):  # A function to display the current selected Node, all 
	    # the left and right Nodes with data present in them. It has to parameters
	    lines, _, _, _ = self._display(cur_node)  # The variable is created and assigned to 
	    # recursively call the self._display(cur_node)private function. The last three 
	    # value's returned by the call are ignored in each call.
	    for line in lines:  # going through each line(value) in the variable lines.
	        print(line)  # print each line(value)
    def _display(self, cur_node):  # The first parameter being self is a reference to 
	    # the current instance of the class and the 2nd being the currently selected Node.

	    if cur_node.right is None and cur_node.left is None:  # if both the right and the left 
	        # Node to the current selected Node is the object 'None'.
	        line = '%s' % cur_node.data  # The line variable is created and assigned with the 
	        # cur_node.data value after it has been converted to a string.
	        width = len(line)  # The width variable created and assigned with the length of 
	        # the value assigned to the line variable.
	        height = 1  # The height variable created with the value 1 assigned to it.
	        middle = width // 2  # The middle variable created and assigned with the 
	        # width variable's value floor divided by 2.
	        return [line], width, height, middle  # The line variable’s value is converted to a list type, the
	        # width variable’s value, the height variables value and the middle variables value is returned.

	    if cur_node.right is None:  # if the right Node to the current selected Node is the object 'None'.
	        lines, n, p, x = self._display(cur_node.left)  # The variables lines, n, p, x are assigned the value returned by function call.
	        s = '%s' % cur_node.data  # The s variable is created and assigned with the cur_node.data value
	        # after it has been converted to a string.
	        u = len(s)  # The u variable created and assigned with the length of the value 
	        # assigned to the line variable.
	        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s  # basic addition, subtraction and multiplication 
	        # is done. The result of this calculation is a string value assigned to the variable first_line.
	        second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '  # basic addition, subtraction, and
	        # multiplication is done. The result of this calculation is a string value assigned to the variable 
	        # second_line.
	        shifted_lines = [line + u * ' ' for line in lines]  # basic addition and multiplication is done.
	        # The result of this calculation is a string value assigned to the variable shifted_lines.
	        return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2  # Values of the written 
	        # variables and calculated values are returned.

	    if cur_node.left is None:  # if the left Node to the current selected Node is the object 'None'.
	        lines, n, p, x = self._display(cur_node.right)  # The variables lines, n, p, x 
	          # are assigned the vaule returned by function call.
	        s = '%s' % cur_node.data  # The s variable is created and assigned with the cur_node.data value 
	# after it has been converted to a string.
	        u = len(s)  # The u variable created and assigned with the length of the value 
	                    # assigned to the line variable.
	        first_line = s + x * '_' + (n - x) * ' '  # basic addition, subtraction and multiplication 
	        # is done. The result of this calculation is a string value assigned to the variable first_line.
	        second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '  # basic addition, subtraction, 
	          # and multiplication is done. The result of this
	        # calculation is a string value assigned to the variable second_line.
	        shifted_lines = [u * ' ' + line for line in lines]  # basic addition and multiplication is done. The 
	         # result of this calculation is a string value assigned to the variable shifted_lines.
	        return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2  # Values of the written 
	        # variables and calculated values are returned.

	    left, n, p, x = self._display(cur_node.left)  # The variables left, n, p, x are assigned the 
	                       # value returned by function call.
	    right, m, q, y = self._display(cur_node.right)  # The variables right, m, q, y are assigned the 
	           # value returned by function call.
	    s = '%s' % cur_node.data  # The s variable is created and assigned with the cur_node.data value after
	    # it has been converted to a string.
	    u = len(s)  # The u variable created and assigned with the length of the 
	    # value assigned to the line variable.
	    first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '  # basic addition, 
	    # subtraction and multiplication are done. The result of this calculation is a 
	    # string value assigned to the variable first_line.
	    second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '  # basic addition, 
	    # subtraction, and multiplication is done. The result of this calculation is a string value assigned to 
	    # the variable second_line.
	    if p < q:  # If the value of the variable p is less then he value of the variable q.
	        left += [n * ' '] * (q - p)  # The value inside the variable left is inserted inside
	        # an array with the number of elements = (q-p) and the string space between each 
	        # string = n * ' '. where the value of the variable left is the first element of the array.
	    elif q < p:  # If the value of the variable q is less then he value of the variable p.
	        right += [m * ' '] * (p - q)  # The value inside the variable right is inserted inside 
	       # a array with the number of elements = (p-q) and the string space between each 
	      # string = m * ' '. where the value of the variable right is the first element of the array.
	    zipped_lines = zip(left, right)  # Join two left and right together.
	    lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]  # The lines variable is
	    # assigned the value using addition, multiplication and a for loop to string.
	    return lines, n + m + u, max(p, q) + 2, n + u // 2  # A graphical binary tree is returned.


bst = BinaryTree()  # The variable bst created from using the BinaryTree class.
bst.insert(4)  # Data is inserted in the root of the tree
bst.insert(2)  # Data is inserted in a tree node
bst.insert(6)  # Data is inserted in a tree node
bst.insert(1)  # Data is inserted in a tree node
bst.insert(3)  # Data is inserted in a tree node
bst.insert(5)  # Data is inserted in a tree node
bst.insert(7)  # Data is inserted in a tree node
bst.insert(8)  # Data is inserted in a tree node

bst.display(bst.root) # The binary tree bst is printed.
bst.remove(6)         # Data is removed from a node of the tree
bst.display(bst.root) # The binary tree bst is printed.
