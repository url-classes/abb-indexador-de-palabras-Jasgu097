class Node:
    def __init__(self, value, data):
        #Arbol
        self.value = value
        self.left = None
        self.right = None
class Node_lista:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None