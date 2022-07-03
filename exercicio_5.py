class aviao:
    def __init__(self,modelo, velocidade_maxima,capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.cor = "azul"
        self.capacidade = capacidade

        list=[]
        list.append(modelo)
        list.append(velocidade_maxima)
        list.append(capacidade)
        list.append(self.cor)

        print('O avião de modelo %s possui uma velocidade máxima de %s, capacidade para %s '
            'passageiros e é da cor %s.'%(list[0],list[1],list[2],list[3]))

a1 = aviao("axe",1400,150)