class Pilha:

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty('Pilha vazia')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty('Pilha vazia')
        return self._data.pop()

    def content(self):
        return self._data


if __name__ == '__main__':
    string = input()
    string = string.lower()

    pilha = Pilha()
    temp = Pilha()

    for i in range(len(string)):
        if (string[i]) != " ":
            pilha.push(string[i])
            temp.push(string[i])

    pilha2 = Pilha()

    for i in range(len(pilha)):
        pilha2.push(temp.top())
        temp.pop()

    if pilha.content() == pilha2.content():
        print('sim')
    else:
        print('nao')
