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

EARTH_RADIUS = 6371

gameon = True
while gameon:

    inventario = {'distancias':[], 'dicas': []}

    tentivas = 20
    sorteado = random.choice(todospaises)
    print(sorteado)

    latsorteado = DADOS_normalizados[sorteado]['geo']['latitude']
    longsorteado = DADOS_normalizados[sorteado]['geo']['longitude']

    print(DADOS_normalizados[sorteado])

    while tentivas > 0:

        fcss.printinventario(inventario)
        resposta = input('Qual seu palpite?')

        if resposta == sorteado: #ganhou
            print('Parabens voce acertou')
            gameon=fcss.jogar_denovo()
            break
        
        elif resposta in DADOS_normalizados.keys(): #se o pais existe

            latreposta = DADOS_normalizados[resposta]['geo']['latitude']
            longreposta = DADOS_normalizados[resposta]['geo']['longitude']

            print(latreposta)
            print(longreposta)

            distancia = int(fcss.haversine(EARTH_RADIUS, latsorteado,longsorteado,latreposta,longreposta))
            distancia = float(distancia/1000)


            inventario['distancias'].append(f'{distancia} km -> {resposta}')

            tentivas -= 1  



        #elif resposta == 'dica':

        #elif resposta == 'desisto':

        #elif resposta == 'inventario':

        #else: