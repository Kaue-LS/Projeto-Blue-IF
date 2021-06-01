from nave import Nave
import random
from time import sleep
from nave import Darth
def final(): #AQUI É A FUNÇÃO QUE SIMULA O FINAL DO JOGO. O CORPO DO PROGRAMA COMEÇA NA LINHA 73
    print('')
    print(f'Comandante {nomeJogador} Essa é a sua chance!  Seu alvo está a seu alcance.\nSua tripulação aguarda pelas suas ordens',)
    darthV = Darth()
    atk=0
    if jogador.vida > 0:
        while True:
            acao = int(input(f'[1] para Atacar\n[2] para Desistir\n[3] para Status da nave\n'))
            if acao == 1:
                if jogador.arma == 'Laser':
                    atk = random.randint(60,80)
                if jogador.arma == 'Shockwave':
                    atk = random.randint(30,60)
                if jogador.arma == 'Igunfire':
                    atk = random.randint(20,40)
                
                danosofrido = random.randint(30,70)
                darthV.deLife(atk)
                jogador.vidaa(danosofrido)
                print(f'Você infringiu {atk} de dano no seu oponente.')
                print(f'Você recebeu {danosofrido} de dano.')
                print(f'Sua Vida      ----- {jogador.vida}')
                print(f'Vida do Darth ----- {darthV.life}')
                if jogador.vida==0 and darthV.life==0:
                    print("Ambos derrotados.")
                    break
                if jogador.vida <= 0:
                    print('')
                    print("Você foi derrotado em batalha! Se prepare melhor na próxima.")
                    break
                if darthV.life <= 0:
                    print('')
                    print('Grande vitória!!!')
                    break
            if acao == 2:
                print('Nem todos os guerreiros estão preparados para grandes desafios. Volte quando estiver preparado.')
                break
            if acao == 3:
                jogador.status()
    else:
        print('Não foi dessa vez. Você perdeu!')
        

# AQUI COMEÇA O CORPO DO PROGRAMA
listArmas = {'Lazer': 30,'Shockwave': 45,'Igunfire': 100}
nomeJogador = input('Digite seu nome:\n').upper() #nome do jogador/comandante
print(f'Ola, {nomeJogador}, voce foi escolhido para ser o comandante de uma nave espacial em uma missao de captura ao Darth Vader.  Seu objetivo é captura-lo e trazer de volta a terra para julgmento.')
nomeNave = input('Escolha o nome da sua nave:\n') #nome nave
escolhaArma=int(input(f'Escolha sua arma:\n[1] Lazer -- dano: 60-80 -- muniçao: 30\n[2] Shockwave -- dano: 30-60 -- muniçao: 50\n[3] Igunfire -- dano: 20-40 -- muniçao: 150\n').upper())
if escolhaArma == 1: # a variavel jogador é o item que passa os parametros para a classe inicializar os atributos
    jogador = Nave(nomeNave,'Laser',30)
if escolhaArma == 2:
    jogador = Nave(nomeNave,'Shockwave', 45)
if escolhaArma == 3:
    jogador = Nave(nomeNave,'Igunfire',100)
print(jogador.arma)
jogador.status()
print('Definições realizadas. Decolar em:\n')
for c in range(5,0,-1):
    sleep(1)
    print(c)
print('Decolagem com sucesso!!!')
while True:
    direcao=int(input(f'Qual direção deseja seguir:\n[1] para frente\n[2] para Esquerda\n[3] para Direita\n[4] para Status da nave\n'))
    if direcao == 1:
        jogador.combustivel(10)
        num = random.randint(1,15)
        if num in (1,2,3,4,5):
            print(f'Excelente!!! Você conhece a Galáxia como a palma de sua mão.\nVocê conseguiu rastrear seu alvo de forma impecável.')
            final()
            break
        else:
            print('Você está na direção correta! Mas ainda não encontrou o fugitivo')    
    if direcao == 2:
        jogador.combustivel(20)
        print('A nave entra em uma região não mapeada. Você e sua tripulação perdem as linhas de comunicação. A nave começa a perder velocidade. Nenhuma visão é nítida.')
        decisao = int(input(f'Seu sub-comandande pergunta qual melhor decisao.\n[1] para seguir em frente\n[2] para voltar\n'))
        if decisao == 1:
            num = random.randint(1,3)
            print('Uma gravidade esmagadora começa a comprimir a nave, os sistemas de alerta dispararam. Pela sua experiencia, trata-se de um buraco negro.')
            tecla = input(f'Aperte qualquer tecla para tentar a sorte e fugir>>>>\n')
            for c in range(3,0,-1):
                sleep(1)
                print(c)
            if num == 2:
                jogador.combustivel(30)
                print('Uau! Essa foi por pouco. Você conseguiu guiar sua nave para longe do buraco negro.')
                final()
                break
            else:
                jogador.combustivel(30)
                print('Mesmo colocando a nave em sua capacidade máxima, você não conseguiu salvar sua tripulação do buraco negro')
                print(f'A {jogador.nome} foi desintegrada!')
                break
    if direcao == 3:
        jogador.combustivel(10)
        print('Tudo parecia calmo durante a viagem, até que a nave começa a receber impactos do lado externo. A tripulação fica em alerta e após voce pedir para analisarem o radar, descobre que trata-se de um campo de asteróides.')
        asteroides=int(input(f'Seu sub-comandante questiona o que deve ser feito:\n[1] para continuar\n[2] para voltar\n'))
        if asteroides == 1:
            danos = random.randint(0,100)
            jogador.combustivel(30)
            jogador.vidaa(danos)
            print(f'Voce decidiu passar pelo campo de asteróides!')
            for c in range(3,0,-1):
                sleep(1)
                print(c)
            if jogador.vida > 0:
                print(f'Você guiou sua nave com bravura e passou pelo campo de asteroides!\nSua nave recebeu {danos} de dano')
                final()
                break
            else:
                (f'Você lutou bravamente mas nao obteve sucesso na missão. A {jogador.nome} foi destroçada')
                break
        else:
            jogador.combustivel(10)
            
    if direcao == 4:
        jogador.status()   
    if jogador.vida <= 0:
        print('Você ficou sem vida. Sua missão falhou.')
        break
    if jogador.comb <= 0:
        print('Você ficou sem combustível. Sua missão falhou.')
        break

print('FIM DO JOGO')