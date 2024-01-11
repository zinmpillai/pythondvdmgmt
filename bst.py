# Initiating a Tree node
class BSTnode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    # insert into node
    def insert(self,value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = BSTnode(value)

                else:
                    self.left.insert(value)

            elif value > self.value:
                if self.right is None:
                    self.right = BSTnode(value)

                else:
                    self.right.insert(value)

        else:
            self.value = value

    # printing the binary tree
    def show_tree(self):
        if self.left:
            self.left.show_tree()

        if self.right:
            self.right.show_tree()

        print(self.value)

    # searching for a value node in the binary tree
    def search_node(self, value):
        if self.value.get_account_num() == value.get_account_num():
            return self.value

        if value < self.value:
            if self.left:
                self.left.search_node(value)
                return
            else:
                print('\nNo Registered Customer.....\n')
        elif value > self.value:
            if self.right:
                self.right.search_node(value)
                return
            else:
                print('\nNo Registered Customer.....\n')