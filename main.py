from Binarytree import BinaryTree

def cargar(texto,archivo):
    with open(f"{archivo}.txt", "r") as archivo:
        lineas = archivo.readlines()
        for line in lineas:
            texto.append(line.strip())

texto_1=[]
cargar(texto_1,"texto 1")
texto_2=[]
cargar(texto_2,"texto 2")
texto_3=[]
cargar(texto_3,"texto 3")
texto_4=[]
cargar(texto_4,"texto 4")
texto_5=[]
cargar(texto_5,"texto 5")
texto_6=[]
cargar(texto_6,"texto 6")
texto_7=[]
cargar(texto_7,"texto 7")
texto_8=[]
cargar(texto_8,"texto 8")
texto_9=[]
cargar(texto_9,"texto 9")
texto_10=[]
cargar(texto_10,"texto 10")




binary_tree=BinaryTree()


for i in texto_1:
    a=i.upper()
    binary_tree.insert(a)

for i in texto_2:
    a=i.upper()
    for e in binary_tree.inorder():
        if a!=e:
            binary_tree.insert(a)
for i in texto_3:
    a=i.upper()
    for e in binary_tree.inorder():
        if a!=e:
            binary_tree.insert(a)
for i in texto_4:
    a=i.upper()
    for e in binary_tree.inorder():
        if a!=e:
            binary_tree.insert(a)
for i in texto_5:
    a=i.upper()
    for e in binary_tree.inorder():
        if a!=e:
            binary_tree.insert(a)
for i in texto_6:
    a=i.upper()
    for e in binary_tree.inorder():
        if a!=e:
            binary_tree.insert(a)
for i in texto_7:
    a=i.upper()
    for e in binary_tree.inorder():
        if a!=e:
            binary_tree.insert(a)
for i in texto_8:
    a=i.upper()
    for e in binary_tree.inorder():
        if a!=e:
            binary_tree.insert(a)
for i in texto_9:
    a=i.upper()
    for e in binary_tree.inorder():
        if a!=e:
            binary_tree.insert(a)
for i in texto_10:
    a=i.upper()
    for e in binary_tree.inorder():
        if a!=e:
            binary_tree.insert(a)

binary_tree.graficar_arbol()

text=[]
for i in binary_tree.inorder():
    text.append(i)
with open("texto.txt","w") as archivo:
    for i in text:
        lineas=archivo.writelines(i + "\n")