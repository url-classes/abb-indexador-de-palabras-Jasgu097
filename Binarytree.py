from node import Node

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(value, self.root)

    def _insert_recursive(self, value, current_node):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(value, current_node.left)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(value, current_node.right)
        else:
            # Ignore duplicate values
            pass

    def preorder(self):
        return self._preorder_recursive(self.root)

    def _preorder_recursive(self, node):
        if node is None:
            return []
        return [node.value] + self._preorder_recursive(node.left) + self._preorder_recursive(node.right)

    def inorder(self):
        return self._inorder_recursive(self.root)

    def _inorder_recursive(self, node):
        if node is None:
            return []
        return self._inorder_recursive(node.left) + [node.value] + self._inorder_recursive(node.right)

    def postorder(self):
        return self._postorder_recursive(self.root)

    def _postorder_recursive(self, node):
        if node is None:
            return []
        return self._postorder_recursive(node.left) + self._postorder_recursive(node.right) + [node.value]

    def buscar(self, value):
        return self._buscar_recursive(value, self.root, [])

    def _buscar_recursive(self, value, current_node, path):
        if current_node is None:
            return None

        path.append(current_node.value)

        if current_node.value == value:
            return path

        if value < current_node.value:
            return self._buscar_recursive(value, current_node.left, path)
        else:
            return self._buscar_recursive(value, current_node.right, path)
