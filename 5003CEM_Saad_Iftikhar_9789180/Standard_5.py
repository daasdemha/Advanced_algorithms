class Node:

    def __init__(self, dataval=None):
        self.dataval = dataval  # Instance variable "dataval" is created.
        self.nextval = None  # The default value of 'None' assigned to "self.nextval".


class SLinkedList:
    def __init__(self):
        self.headval = None  # The default value of 'None' assigned to "self.headval".

    def listprint(self):
        printval = self.headval  # Assighning value of the self.headval to printval.
        while printval is not None:  # while the printval varibale is not None.
            print(printval.dataval)  # printing the value of the variable printval.dataval
            printval = printval.nextval  # Assighning value of the self.printval.nextval to printval.

    def AtBeginning(self, newdata):
        NewNode = Node(newdata)  # creating a NewNode variable with the value of Node(newdata) //creating a New Node

    def AtEnd(self, newdata):
        NewNode = Node(newdata)  # creating a NewNode variable with the value of Node(newdata) //creating a New Node
        if self.headval is None:  # if the value of self.headval variable is 'None'
            self.headval = NewNode  # The value of self.headval is assinged to the new node
            return
        last = self.headval  # The variable last is assigned the self.headval varable's value
        while (last.nextval):  # while last.nextval varible's value is not 0.
            last = last.nextval  # The last varible is assigned the value of last.nextval
        last.nextval = NewNode  # The last.nextval variable is assighned the value of NewNode.

    def Insert(self, val_before, newdata):
        if val_before is None:  # if the value of val_before is None
            print("No node to insert after")  # printing a instruction
            return
        else:
            NewNode = Node(newdata)  # creating a NewNode variable with the value of Node(newdata) //creating a New Node
            NewNode.nextval = val_before.nextval  # assighn the value of val_before.nextval to the varible NewNode.nextval.
            val_before.nextval = NewNode  # assighn the value of NewNode to the varible val_before.nextval.


list = SLinkedList()  # new list variable is created using the SLinkedList class
list.headval = Node("Mon")  # the value "Mon" is assighned to the head of the list.headval
# creating variables for the linked list
e2 = Node("Tue")
e3 = Node("Thur")
e4 = Node("Fri")
e5 = Node("Sat")
# linking the list
list.headval.nextval = e2
e2.nextval = e3
e3.nextval = e4
e4.nextval = e5

list.AtEnd("Sun")  # defining the last variable of the linked list

list.listprint()
print("\n")
list.Insert(list.headval.nextval, "Wed")  # inserting the "Wed" value inside our linked list
list.listprint()
