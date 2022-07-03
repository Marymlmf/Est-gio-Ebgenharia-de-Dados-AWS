class passaro:
    def __init__(self, voar, emitir_som):
        self.emitir_som = emitir_som
        self.nomeclasse =  self.__class__.__name__
    def voar(self):
        print(f'{self.nomeclasse} voa')

class Pato(passaro):
    def som(self):
       print(f'{self.nomeclasse} faz quack quack')
    pass

class Pardal(passaro):
    def som(self):
       print(f'{self.nomeclasse} faz piu piu')
    pass

pato=Pato("voa","quack")
pato.som()
pato.voar()
pardal=Pardal("voa","piu piu")
pardal.som()
pardal.voar()