from Binarytree import BinaryTree

a=BinaryTree()
a.insert("Hola")
a.insert("a")
a.insert("todos")
a.insert("como")
a.insert("estan")

print("preorde", a.preorder())
print("inorden", a.inorder())
print("post", a.postorder())
