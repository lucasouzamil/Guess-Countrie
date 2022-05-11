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

    inventario = {'distancias':[], 'dicas':{}}

    tentivas = 20
    sorteado = random.choice(todospaises)
    print(sorteado)

    latsorteado = DADOS_normalizados[sorteado]['geo']['latitude']
    longsorteado = DADOS_normalizados[sorteado]['geo']['longitude']

    print(DADOS_normalizados[sorteado])
    bandeira={}
    for i in DADOS_normalizados[sorteado]['bandeira'].keys(): # excluindo valores iguais a 0
        if DADOS_normalizados[sorteado]['bandeira'][i]>0:
            bandeira[i]=DADOS_normalizados[sorteado]['bandeira'][i]
    capital=DADOS_normalizados[sorteado]['capital'] # Achando a capital
    area=DADOS_normalizados[sorteado]['area']#achando a area
    populacao=DADOS_normalizados[sorteado]['populacao']#achando a populacao
    continente=DADOS_normalizados[sorteado]['continente']#achando continente
    letras_sorteadas=[] # Letras sorteadas da dica capital
    dic_dicas={}
    dic_dicas['Cor da bandeira']={'informacoes':bandeira, 'custo':4, 'numero':'0'}
    dic_dicas['Letra da capital']={'informacoes':letras_sorteadas, 'custo':3,'numero':'1'}
    dic_dicas['Area']={'informacoes':area, 'custo':6,'numero':'2'}
    dic_dicas['Populacao']={'informacoes':populacao,'custo':5,'numero':'3'}
    dic_dicas['Continente']={'informacoes':continente,'custo':7, 'numero':'4'}
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



        elif resposta == 'dica':
            #achando quais sao as dicas possiveis de serem compradas
            dic_dicas_possiveis={}
            for i in dic_dicas.keys():
                if dic_dicas[i]['custo']<tentivas:
                    print('{0}:{1}---->{2} tentativas'.format(dic_dicas[i]['numero'],i,dic_dicas[i]['custo']))
                    dic_dicas_possiveis[i]=dic_dicas[i]['numero']
            print('5: Sem dicas')
            dica_escolhida=''
            while dica_escolhida not in dic_dicas_possiveis.values():
                dica_escolhida = input('Dica escolhida?' )
                if dica_escolhida in dic_dicas_possiveis.values() or dica_escolhida=='5':
                    break
            if dica_escolhida=='0':
                tentivas-=4
                inventario['dicas']['Cor da Bandeira']=dic_dicas['Cor da bandeira']['informacoes']
            if dica_escolhida=='1':
                tentivas-=3
                letra=fcss.sorteia_letra(capital,letras_sorteadas)
                letras_sorteadas.append(letra)
                inventario['dicas']['Letra da capital']=letras_sorteadas
            if dica_escolhida=='2':
                tentivas-=6
                inventario['dicas']['area']=area
            if dica_escolhida=='3':
                tentivas-=5
                inventario['dicas']['populacao']=populacao
            if dica_escolhida=='4':
                tentivas-=7
                inventario['dicas']['continente']=continente
                    
        #elif resposta == 'desisto':

        #elif resposta == 'inventario':

        #else: