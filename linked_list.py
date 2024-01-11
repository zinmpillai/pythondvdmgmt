# Initiate a node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# Initiate a list of node to add into the initaited node

class Linked_list:
    def __init__(self):
        self.head = None

    # Printing the linked list
    def show(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next

    # Adding a node into the linked list
    def add(self, new):
        new_node = Node(new)
        new_node.next = self.head
        self.head = new_node

    # Removing a node from the linked list
    def remove(self, data):
        curr = self.head
        previous = None
        found = False
        while curr is not None and not found:
            if curr.data == data:
                found = True
            else:
                previous = curr
                curr = curr.next
        if found:
            if previous is None:
                self.head = curr.next
            else:
                previous.next = curr.next

    # Searching for the node with the value in the linked list
    def iterate(self):
        curr_node = self.head
        while curr_node:
            yield curr_node.data
            curr_node = curr_node.next

