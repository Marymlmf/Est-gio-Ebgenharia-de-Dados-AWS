class calculo():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def adicao(self,x,y):
        resultado= x+y
        print(f'A soma de x e y é {resultado}')

    def subtracao(self,x,y):
        resultado = x-y
        print(f'A subtração de x e y é {resultado}')

c1=calculo(1,2)
c1.adicao(1,2)
c1.subtracao(1,2)