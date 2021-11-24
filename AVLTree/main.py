# ADEMIR GUIMARÃES DA COSTA JUNIOR - 2015080075

class TreeNode(object):  # Criação do nó
    def __init__(self, key):
        self.key = key  # Chave do nó
        self.left = None  # Filho a esquerda
        self.right = None  # Filho a direita
        self.height = 1  # Cada nó possui um de altura


class AVLTree(object):  # Criação da classe AVL
    def insert_node(self, root, key):  # Inserção de um nó
        if not root:
            return TreeNode(key)
        elif key < root.key:
            root.left = self.insert_node(root.left, key)
        else:
            root.right = self.insert_node(root.right, key)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balanceFactor = self.getBalance(root)  # Diferença de tamanho
        if balanceFactor > 1:
            if key < root.left.key:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        if balanceFactor < -1:
            if key > root.right.key:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root

    def delete_node(self, root, key):  # Remoção de um nó

        if not root:
            return root
        elif key < root.key:
            root.left = self.delete_node(root.left, - key)
        elif key > root.key:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinimumValue(root.right)
            root.key = temp.key
            root.right = self.delete_node(root.right, temp.key)

        if root is None:
            return root

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balanceFactor = self.getBalance(root)  # Diferença de tamanho

        if balanceFactor > 1:
            if self.getBalance(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if self.getBalance(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root

    def leftRotate(self, z):  # Rotação para a esquerda
        y = z.right
        temp = y.left
        y.left = z
        z.right = temp
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def rightRotate(self, z):  # Rotação para a direita
        y = z.left
        temp = y.right
        y.right = z
        z.left = temp
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def getHeight(self, root):  # Altura da árvore
        if not root:
            return 0
        return root.height

    def getBalance(self, root):  # Diferença de altura entre a esquerda e a direita para balanceamento
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def getMinimumValue(self, root):  # Menor valor da árvore
        if root is None or root.left is None:
            return root
        return self.getMinimumValue(root.left)

    def countLeaf(self, root):  # Contar os nós folhas
        if root is None:
            return 0
        if (root.left and root.right) is None:
            return 1
        else:
            return self.countLeaf(root.left) + self.countLeaf(root.right)


if __name__ == '__main__':
    myTree = AVLTree()  # Instanciação de um objeto AVL
    raiz = None  # Árvore não possui raiz em sua criação

    num = int(input())  # Quantidade de leituras a ser realizada
    for i in range(num):
        entrada = input()  # Entrada do usuário
        if entrada[0] == 'i':  # Caso 'i', considere inserir
            num = [int(s) for s in entrada.split() if
                   s.isdigit()]  # Considere apenas os números da String para inserção
            raiz = myTree.insert_node(raiz, num[0])
        elif entrada[0] == 'r':  # Caso 'r', considere remoção
            num = [int(s) for s in entrada.split() if s.isdigit()]  # Apenas os números da String para remoção
            raiz = myTree.delete_node(raiz, num[0])

    print(myTree.countLeaf(raiz))  # Saída = quantidade de nós folhas.
