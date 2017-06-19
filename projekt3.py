#wczytywanie pliku txt
f = open("file.txt")
tablica = []
line = f.readline()
while line!="":
  n_line = line.replace("\n", "")
  tablica.append(n_line)
  line = f.readline()
  
import numpy as np 
import numpy.linalg 
tablica=np.array([[1,0,1,2], [2,0,1,2], [2,1,2,0], [2,1,0,1], [1,3,0,0]])
N=5

class Node:
    def __init__(self, name="Node", parent=None, minimal=Integer):
        self.__parent__=parent
        self.__childs__=[]
        self.min_dep=minimal
        self.name=name #nazwa
    def isRoot(self): #jest korzeniem, czy nie posiada rodzica
        if self.__parent__==None: return True
        return False
    def isNode(self): #jest węzłem, posiada dzieci
        if len(self.__childs__)>=1: return True
        return False
    def getParent(self):
        return self.__parent__
    def getChilds(self):
        return self.__childs__
    def getNext(self): #następny (sąsiad) węzeł z tym samym rodzicem
        if self.__parent__==None: return None
        n=self.__parent__.getChilds()
        this=False
        for child in n:
            if this and child!=self:
                return child
            if child==self:
                this=True
        return None
    def getPrev(self): #poprzedni węzeł z tym samym rodzicem
        if self.__parent__==None: return None
        n=self.__parent__.getChilds()
        p=None
        for child in n:
            if child==self:
                return p
            p=child
        return None
    def removeChild(self, remove): #usuwa z listy dzieci podany węzeł
        if remove in self.__childs__:
            self.__childs__.remove(remove)
    def setParent(self, newParent): #przypisuje węzłowi nowego rodzica
        if newParent.__class__!= Node: return None
        if self.__parent__!=None: #jeśli miał rodzica
            self.__parent__.removeChild(self) #usuwa się z niego
        self.__parent__=newParent #i ustawia nowego
        newParent.addChild(self) #oraz dodaje się do listy jego dzieci
    def addChild(self, newChild): #dodaje dziecko do węzła
        if newChild.__class__!= Node: return None
        if newChild in self.__childs__: return None
        if newChild.getParent()!=None:
            newChild.getParent().removeChild(newChild) #wcześniej musi jednak
                                                       # usunąć je od poprzedniego rodzica
        self.__childs__.append(newChild)
        newChild.__parent__=self
    def getRoot(self): #szuka korzeni
        root=self
        while root.isRoot()==False:#pobiera kolejnych rodziców tak długo, aż trafi
            root=root.getParent()
        return root
    def printTree(self, intend=0): # metoda rysuje całe drzewo od obecnego elementu
        p=""                       # z podanym wcięciem (zaczynając od 0)
        i=intend
        while i>0:
            if i>1: p+="    +"
            else: p+="    ";
            i-=1 #generowanie wcięcia
        if(self.isNode()):
            print(p+"+"+self.name) #jeśli ma dzieci, rysuje +
        else:
            print(p+"-"+self.name) #nie posiada, -
        for c in self.getChilds(): #i to samo dla każdego dziecka
            c.printTree(intend+1)  #ze zwiększonym wcięciem
                        
def WSA_subtree(parent, N, tablica):
    for i in range(N):
        if tab[i][0]==parent.name and i!=parent.name:
            tree=Node()
            tree.__init__(i, parent, tablica[i][2])
            parent.addChild(tree)
            WSA_subtree(tree, N, tablica)
    return parent
                        
def WSA_tree(N, tablica):
    tree=Node()
    for i in range(N):
        if tablica[i][0]==i:
            root=i
            tree.__init__(root,0, tablica[i][2])
    WSA_subtree(tree, N, tablica)
    return tree
    
def union_subtree(parent, N, tablica):
    for i in range(N):
        if tab[i][1]==parent.name and i!=parent.name:
            tree=Node()
            tree.__init__(i, parent, tablica[i][3])
            parent.addChild(tree)
            union_subtree(tree, N, tablica)
    return parent
    
def union_tree(N, tablica):
    tree=Node()
    for i in range(N):
        if tablica[i][1]==i:
            root=i
            tree.__init__(root,0, tablica[i][3])
    union_subtree(tree, N, tablica)
    return tree

  

print "Minimize "
f = True
for i in range(N):
    if f:
        f = False
    else:
        print '+',
    print "x" + str(i),
    
print "Subject To"

def warunek(tree, N):
    x= len(tree.getChilds())
    f=True
    for i in range(x):
        if f:
            f=False
        else:
            print 'x',
        print "x" + str(i),
    print '>=', tree.min_dep
    for i in range(x):
        warunek(tree.getChilds()[i], N)
    return 0
                      
