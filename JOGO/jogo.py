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

    inventario = {'distancias':{}, 'dicas': {'cor da bandeira':[], 'Letra da capital':[], 'area':'','populacao':'','continente':''}}

    tentivas = 20
    sorteado = random.choice(todospaises)
    print(sorteado)

    latsorteado = DADOS_normalizados[sorteado]['geo']['latitude']
    longsorteado = DADOS_normalizados[sorteado]['geo']['longitude']

    bandeira={}
    bandeira_lista=[]
    bandeira_sorteado_lista=[]
    cont_bandeira=0
    inventario['dicas']['Cor da Bandeira']=[]
    for i in DADOS_normalizados[sorteado]['bandeira'].keys(): # excluindo valores iguais a 0
        if DADOS_normalizados[sorteado]['bandeira'][i]>0 and i!='outros' and i!='outras':
            bandeira[i]=DADOS_normalizados[sorteado]['bandeira'][i]
            bandeira_lista.append(i)
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


    fcss.template()
    print('Você tem' +  '\033[94m' + ' ' + str(tentivas) + ' ' + '\033[0m' + 'tentativa(s)')
    print('')


    while tentivas > 0:

        resposta = input('Qual seu palpite? ')
        resposta = resposta.lower()
        print('')

        if resposta == sorteado: #ganhou
            print('   Y O U    G U E S S    I T !')
            print('             PARABÉNS          ')
            print('')
            gameon=fcss.jogar_denovo()
            break
        
        elif resposta in DADOS_normalizados.keys(): #se o pais existe

            latreposta = DADOS_normalizados[resposta]['geo']['latitude']
            longreposta = DADOS_normalizados[resposta]['geo']['longitude']

            distanciaint = int(fcss.haversine(EARTH_RADIUS, latsorteado,longsorteado,latreposta,longreposta))
            distanciafloat = float(distanciaint/1000)
            distanciastring = str(distanciafloat)
        
            if len(distanciastring) == 3:
                distanciastring = distanciastring+'0'
            elif len(distanciastring) == 5:
                distanciastring = ' ' + distanciastring
            elif len(distanciastring) == 4:
                distanciastring = ' '+' '+distanciastring

            inventario['distancias'][distanciaint] = (f'{distanciastring} km -> {resposta}')

            fcss.printinventario(inventario)

            tentivas -= 1  

            if tentivas <= 5:
                print('Você tem' +  '\033[31m' + ' ' + str(tentivas) + ' ' + '\033[0m' + 'tentativa(s)') #vemelho
            elif tentivas <= 10:
                print('Você tem' +  '\033[33m' + ' ' + str(tentivas) + ' ' + '\033[0m' + 'tentativa(s)') #AMARELO
            elif tentivas <= 20:
                print('Você tem' +  '\033[94m' + ' ' + str(tentivas) + ' ' + '\033[0m' + 'tentativa(s)') #AZUL
            
            print('')

        elif resposta == 'inventario':
            fcss.printinventario(inventario)

        elif resposta == 'desisto': #se o jogador desiste

            certeza = ''
            while certeza != 's' or certeza != 'n':
                certeza = input('Tem certeza de que vai desistir da rodada? [s/n] ')
                print('')

                if certeza == 's':
                    print(f'Que deselgante desistir, o país era {sorteado}')
                    print('')
                    break

                elif certeza == 'n':
                    break

                else:
                    print('Digite (s) ou (n)')
                    print('')
            
            if certeza == 's':
                gameon = fcss.jogar_denovo()
                break


        elif resposta == 'dica' or resposta == 'dicas':
            #achando quais sao as dicas possiveis de serem compradas
            dic_dicas_possiveis={}
            numeros = '['
            print(f'MERCADO DE DICAS        tentativas: {tentivas}')
            print('--------------------------------------')
            for i in dic_dicas.keys():
                if dic_dicas[i]['custo']<tentivas:
                    print('{0}: {1} ----> {2} tentativas'.format(dic_dicas[i]['numero'],i,dic_dicas[i]['custo']))
                    numeros = numeros + str(dic_dicas[i]['numero']) + '|'
                    dic_dicas_possiveis[i]=dic_dicas[i]['numero']
            numeros = numeros + '5]'
            print('5: Sem dicas')
            dica_escolhida=''
            print('--------------------------------------')
            print('Escolha sua opcao: ' + numeros)
            while dica_escolhida not in dic_dicas_possiveis.values():
                print('')
                dica_escolhida = input('Dica escolhida? ' )
                print('')
                if dica_escolhida in dic_dicas_possiveis.values() or dica_escolhida=='5':
                    break
            if dica_escolhida=='0':
                tentivas-=4
                
                inventario['dicas']['cor da bandeira'].append(bandeira_lista[cont_bandeira])
                cont_bandeira+=1
                if cont_bandeira==len(bandeira_lista)-1:
                    del dic_dicas['Cor da bandeira']

            if dica_escolhida=='1':
                tentivas-=3
                letra=fcss.sorteia_letra(capital,letras_sorteadas).lower()
                letras_sorteadas.append(letra)
                inventario['dicas']['Letra da capital']=letras_sorteadas
            if dica_escolhida=='2':
                tentivas-=6
                inventario['dicas']['area']=area
                del dic_dicas['Area']
            if dica_escolhida=='3':
                tentivas-=5
                inventario['dicas']['populacao']=populacao
                del dic_dicas['Populacao']
            if dica_escolhida=='4':
                tentivas-=7
                inventario['dicas']['continente']=continente
                del dic_dicas['Continente']
            fcss.printinventario(inventario)

            if tentivas > 0 and dica_escolhida != '5':

                if tentivas <= 5:
                    print('Você tem' +  '\033[31m' + ' ' + str(tentivas) + ' ' + '\033[0m' + 'tentativa(s)') #vemelho
                elif tentivas <= 10:
                    print('Você tem' +  '\033[33m' + ' ' + str(tentivas) + ' ' + '\033[0m' + 'tentativa(s)') #AMARELO
                elif tentivas <= 20:
                    print('Você tem' +  '\033[34m' + ' ' + str(tentivas) + ' ' + '\033[0m' + 'tentativa(s)') #AZUL
            
            print('')

        else:
            print('Esse pais nao existe\n')

        if tentivas == 0:
            print(f'Você perdeu, o país era: {sorteado}')
            gameon = fcss.jogar_denovo()