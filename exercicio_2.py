class Pessoa():
    def __init__(self,nome,id):
        self.__nome = nome
        self.id = id

    def setNome(self,onome):
        if onome is not None:
            self.__nome = onome
            return onome

    def getNome(self):
        print(f' A pessoa se chama {self.__nome}')

pessoa = Pessoa("Maria", 12)
pessoa.setNome("Maria")
print(f'{pessoa.getNome()}')




