from random import randint
class Nave:
    def __init__(self, n, a, m): # nomejogador / armaes colhida / munição
        self.nome = n
        self.vida = 200
        self.comb = 100
        self.mun = m
        self.arma = a 
    def vidaa(self,dano):
        self.vida -= dano
        if self.vida <= 0:
            self.vida = 0
    def combustivel(self,g):
        self.comb -= g
    def municao(self, g):
        self.mun -= g
    def status(self):
        print(f'Nome da nave ---- {self.nome}')
        print(f'vida         ---- {self.vida}')
        print(f'Combustível  ---- {self.comb}')
        print(f'Arma         ---- {self.arma}')        
class Darth:
    def __init__(self):
        self.life = 200
        self.atk = randint(30,50)

    def deLife(self, d):
        self.life -= d
        if self.life<0:
            self.life=0