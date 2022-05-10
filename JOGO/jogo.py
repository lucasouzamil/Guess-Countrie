import json
import math
import random
import fcss



with open('JOGO/DADOS.json', 'r') as data:
    DADOS = data.read()
DADOS = json.loads(DADOS)
DADOS_normalizados = fcss.normaliza(DADOS)

todospaises = []
for pais in DADOS_normalizados.keys():
        todospaises.append(pais)

gameon = True
while gameon:

    inventario = {'distancias':[], 'dicas': []}

    tentivas = 20
    sorteado = random.choice(todospaises)
    print(sorteado)

    while tentivas > 0:

        fcss.printinventario(inventario)
        resposta = input('Qual seu palpite?')

        if resposta == sorteado: #ganhou
            print('Parabens voce acertou')
            gameon=fcss.jogar_denovo()
            break
        
        #elif resposta in DADOS_normalizados.keys(): #se o pais existe

        #elif resposta == 'dica':

        #elif resposta == 'desisto':

        #elif resposta == 'inventario':

        #else: