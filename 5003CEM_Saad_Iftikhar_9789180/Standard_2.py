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

    def find_i(self, data):  # A function to search the entered data iteratively from the Binarytree.
        # The 2nd parameter is the data to be checked.
        cur_node = self.root  # The current node is given the value of the node self.root.
        while self.root:  # While self.root is True/(has a value other than '0' or 'None')
            if data == cur_node.data:  # If the value of data is equal to the value of the current selected Nodes data.
                return True  # return True
            elif data < cur_node.data:  # If the value of data is lees to the value of the current selected Nodes data.
                cur_node = cur_node.left  # Current selected Node is changed to the Node to its left.
            elif cur_node.right is not None:  # If the value of data is equal to the value of the current
                # selected Nodes data.
                cur_node = cur_node.right  # Current selected Node is changed to the Node to its right.
            else:  # otherwise
                return False  # return Flase

    def find_r(self, data):  # A function to search the entered data recursively from the Binarytree. 
                             # The 2nd parameter is the data to be checked.
        if self.root:  # While self.root is True/(has a value other than '0' or 'None')
            search = self._find_r(data, self.root)  # The search variable is assigned the recursive result of
            # the private function _find_r. The First argument being the value of the
            # given data and the 2nd argument being the value of self.root.
            if search:  # if search is True / (has a value other than '0' or 'None')
                return True  # return True
            return False  # if search is False return Flase
        else:  # While self.root is False return Flase
            return None  # return 'None'

    def _find_r(self, data, cur_node):  # A function to search the entered data recursively from the Binarytree.
        # The 2nd parameter is the data to be checked. The third parameter is the current selected Node.
        if data == cur_node.data:  # If the value of data is equal to the value of the current 
            # selected Nodes data.
            return True  # return True

        elif data < cur_node.data and cur_node.left:  # The value of the data variable is less than 
             # the current Selected
            return self._find_r(data, cur_node.left)  # return the private function _find_r recursively. The
            # 1st argument is the data to be checked. The 2nd argument is the Node left to the 
           # current selected Node.

        elif data > cur_node.data and cur_node.right:  # The value of the data variable is greater than the
            # current Selected
            return self._find_r(data, cur_node.right)  # return the private function _find_r 
            # recursively. The 1st argument is the data to be checked. The 2nd argument 
            # is the Node right to the current selected Node.

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

bst.display(bst.root)  # The binary tree bst is printed.

print("The result for the recursive search value 1: ", bst.find_r(1))  # Checks if the arguments value entered 
      # is present in the binary tree using recursive search method.
print("The result for the recursive search value 10: ", bst.find_r(10))  # Checks if the arguments value entered
      # is present in the binary tree using recursive search method.
print("The result for the iterative search value  1: ", bst.find_i(1))  # Checks if the arguments value entered
      # is present in the binary tree using iterative search method.
print("The result for the iterative search value  6: ", bst.find_i(6))  # Checks if the arguments value entered 
    # is present in the binary tree using iterative search method.
print("The result for the iterative search value  10: ", bst.find_i(10))  # Checks if the arguments value entered is present in the binary tree using iterative search method.
