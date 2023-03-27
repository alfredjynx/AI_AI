from aigyminsper.search.SearchAlgorithms import BuscaGananciosa, AEstrela
from aigyminsper.search.Graph import State
from aigyminsper.search.Graph import State
from copy import deepcopy
import numpy as np

class Knuth(State):

    def __init__(self,op,n:4,numero):
        self.operator = op
        self.n = n
        self.meta = numero

    def fact(self,n):return 1 if n<=0 else n*self.fact(n-1)


    def sucessors(self):
        sucessors = []

        sucessors.append(Knuth('raiz',np.sqrt(self.n),self.meta))
        sucessors.append(Knuth('fatorial',self.fact(self.n),self.meta))
        sucessors.append(Knuth('arredondando',self.n-1,self.meta))
        
        return sucessors

    def is_goal(self):
        if self.n == self.meta:
            return True
        return False

    def description(self):
        return "Este é um agente simples que sabe fazer um número inteiro qualquer virar 4"

    def cost(self):
        return 1

    def env(self):
        return self.operator + f'{self.n}'
    
    def h(self):
        return abs(self.n-self.meta)
    
    

def main():

    state = Knuth('',4,5)
    algorithm = AEstrela()
    result = algorithm.search(state)
    if result != None:
        r = result.show_path()
    else:
        r = 'Nao achou solucao'
    print(r)
if __name__ == '__main__':
    main()
