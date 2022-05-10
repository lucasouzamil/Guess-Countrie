import json
import math
import random
import fcss

with open('JOGO/DADOS.json', 'r') as data:
    DADOS = data.read()

DADOS = json.loads(DADOS)

DADOS_normalizados = fcss.normaliza(DADOS)

gameon = True
while gameon:

    tentivas = 20
    sorteado = random.choice(DADOS_normalizados.keys())

    while tentivas > 0:

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