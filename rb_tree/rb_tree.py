class TreeRB:

    class Node:
        BLACK = 1;
        RED = 0;
        def __init__(self, value, color=RED):

            self.value = value
            self.left = None
            self.right = None
            self.color = color
    
    def __init__(self):
        self.root = None

    def balance(self, node):
        if node.color == BLACK:
            return
        
        parent = self.parent(node)
        if parent is None:
            node.color = BLACK
            return
        
        grandparent = self.parent(parent)
        if grandparent is None:
            return

        uncle = self.sibling(parent)
        if uncle is not None and uncle.color == RED:
            parent.color = BLACK
            uncle.color = BLACK
            grandparent.color = RED
            self.balance(grandparent)
        else:
            if parent == grandparent.left:
                if node == parent.right:
                    self.rotate_left(parent)
                    node, parent = parent, node
                self.rotate_right(grandparent)
            else:
                if node == parent.left:
                    self.rotate_right(parent)
                    node, parent = parent, node
                self.rotate_left(grandparent)
            parent.color = BLACK
            grandparent.color = RED


    def rotate_left(self, node):
        if node is None or node.right is None:
            return
        
        right_child = node.right
        node.right = right_child.left
        
        if right_child.left is not None:
            right_child.left.parent = node
        
        right_child.parent = node.parent
        
        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child
        
        right_child.left = node
        node.parent = right_child           

    def rotate_right(self, node):
        if node is None or node.left is None:
            return
        
        left_child = node.left
        node.left = left_child.right
        
        if left_child.right is not None:
            left_child.right.parent = node
        
        left_child.parent = node.parent
        
        if node.parent is None:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child
        
        left_child.right = node
        node.parent = left_child

    def sibling(self, node):
        if node.parent is not None:
            if node == node.parent.left:
                return node.parent.right
            else:
                return node.parent.left
        return None

        def parent(self, node):
            if node is not None:
                return node.parent
            return None  

    def add_elem(self, value):
        new_node = self.Node(value)

        if self.root is None:
            self.root = new_node
            new_node.color = BLACK
        else:
            node = self.root
            while node is not None:
                if value < node.value:
                    if node.left is None:
                        node.left = new_node
                        new_node.parent = node
                        break
                    node = node.left
                else:
                    if node.right is None:
                        node.right = new_node
                        new_node.parent = node
                        break
                    node = node.right
            self.balance(new_node)

    def balance_remove(self, node):
        while node != self.root and node.color == BLACK:
            if node == node.parent.left:
                sibling = node.parent.right
                if sibling.color == RED:
                    sibling.color = BLACK
                    node.parent.color = RED
                    self.rotate_left(node.parent)
                    sibling = node.parent.right
                
                if sibling.left.color == BLACK and sibling.right.color == BLACK:
                    sibling.color = RED
                    node = node.parent
                else:
                    if sibling.right.color == BLACK:
                        sibling.left.color = BLACK
                        sibling.color = RED
                        self.rotate_right(sibling)
                        sibling = node.parent.right
                    sibling.color = node.parent.color
                    node.parent.color = BLACK
                    sibling.right.color = BLACK
                    self.rotate_left(node.parent)
                    node = self.root
            else:
                sibling = node.parent.left
                if sibling.color == RED:
                    sibling.color = BLACK
                    node.parent.color = RED
                    self.rotate_right(node.parent)
                    sibling = node.parent.left
                
                if sibling.right.color == BLACK and sibling.left.color == BLACK:
                    sibling.color = RED
                    node = node.parent
                else:
                    if sibling.left.color == BLACK:
                        sibling.right.color = BLACK
                        sibling.color = RED
                        self.rotate_left(sibling)
                        sibling = node.parent.left
                    sibling.color = node.parent.color
                    node.parent.color = BLACK
                    sibling.left.color = BLACK
                    self.rotate_right(node.parent)
                    node = self.root
        node.color = BLACK        

    def find_elem(self, value):
        node = self.root
        while node is not None:
            if node.value == value:
                return node
            elif value < node.value:
                node = node.left
            else:
                node = node.right
        return None                              

    def del_elem(self, value):
        node = self.find_elem(value)
        if node is None:
            return
        
        if node.left is not None and node.right is not None:
            successor = self.get_successor(node)
            node.value = successor.value
            node = successor
        
        replacement = node.left if node.left is not None else node.right
        if replacement is None:
            if node.color == BLACK:
                self.balance_remove(node)
            if node.parent is not None:
                if node == node.parent.left:
                    node.parent.left = None
                else:
                    node.parent.right = None
            else:
                self.root = None
        else:
            replacement.parent = node.parent
            if node.parent is None:
                self.root = replacement
            else:
                if node == node.parent.left:
                    node.parent.left = replacement
                else:
                    node.parent.right = replacement
            if node.color == BLACK:
                if replacement.color == RED:
                    replacement.color = BLACK
                else:
                    self.balance_remove(replacement)    