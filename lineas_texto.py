import main
from Binarytree import BinaryTree
def cargar(texto,archivo):
    with open(f"{archivo}.txt", "r") as archivo:
        lineas = archivo.readlines()
        for line in lineas:
            texto.append(line.strip())

texto=[]
cargar(texto,"texto")

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

b=BinaryTree()



for i in texto:
    b.insert(i)




b.graficar_arbol()