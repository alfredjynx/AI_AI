from aigyminsper.search.SearchAlgorithms import BuscaGananciosa, AEstrela
from aigyminsper.search.Graph import State
from aigyminsper.search.Graph import State
from copy import deepcopy

class Bike(State):

    def __init__(self,tabuleiro,op,meta,ciclista):
        self.operator = op
        self.table = tabuleiro
        self.meta = meta
        self.ciclista = ciclista

    def move(self,op):
        t = deepcopy(self.table)
        i0 = self.ciclista[1]
        l0 = self.ciclista[0]

        ciclista = [l0,i0]

        if op == 'cima':
            if -1<l0-1:
                t[l0][i0],t[l0-1][i0] = t[l0-1][i0],t[l0][i0]
                ciclista = [l0-1,i0]

            else:
                return False
        
        elif op == 'baixo':
            if len(t)>l0+1:
                t[l0][i0],t[l0+1][i0] = t[l0+1][i0],t[l0][i0]
                ciclista = [l0+1,i0]
            else:
                return False

        elif op == 'esquerda':
            if -1<i0-1:
                t[l0][i0-1],t[l0][i0] = t[l0][i0],t[l0][i0-1]
                ciclista = [l0,i0-1]
            else:
                return False
        
        elif op == 'direita':
            if len(t[l0])>i0+1:
                t[l0][i0+1],t[l0][i0] = t[l0][i0],t[l0][i0+1]
                ciclista = [l0,i0+1]
            else:
                return False

        return t,ciclista
        

    def sucessors(self):
        sucessors = []

        if self.move('cima')!=False:
            t,c = self.move('cima')
            sucessors.append(Bike(t,'cima',self.meta,c))

        if self.move('baixo')!=False:
            t,c = self.move('baixo')
            sucessors.append(Bike(t,'baixo',self.meta,c))
        
        if self.move('esquerda')!=False:
            t,c = self.move('esquerda')
            sucessors.append(Bike(t,'esquerda',self.meta,c))
        
        if self.move('direita')!=False:
            t,c = self.move('direita')
            sucessors.append(Bike(t,'direita',self.meta,c))
        
        return sucessors

    def is_goal(self):
        if self.ciclista == self.meta:
            return True
        return False

    def description(self):
        return "Este é um agente simples que sabe fazer um ciclista chegar em seu lugar de almoço"

    def cost(self):
        if self.table[self.ciclista[0]][self.ciclista[1]]=='lama':
            return 10
        return 1

    def env(self):
        return self.table
    
    def h(self):
        dif = abs((self.ciclista[0]-self.meta[0])+(self.ciclista[1]-self.meta[1]))
        poss = ['cima','baixo','esquerda','direita']
        for p in poss:
            try:
                t,c = self.move(p)
                if self.table[c[0]][c[1]]=='lama':
                    dif+=10
            except:
                pass
        return dif


def main():
    a = [
        ['ciclista','a','lama','lama','lama','almoço','a'],
        ['a','a','lama','lama','a','a','a'],
        ['a','a','a','lama','a','a','a'],
        ['a','a','a','a','a','a','a'],
        ['a','a','a','a','a','a','a']]
    state = Bike(a,'',[0,5],[0,0])
    algorithm = AEstrela()
    result = algorithm.search(state)
    print(state.table)
    if result != None:
        r = result.show_path()
        print(result.show_path())
    else:
        r = 'Nao achou solucao'
        print(r)
    print(r == 'Nao achou solucao')

if __name__ == '__main__':
    main()
