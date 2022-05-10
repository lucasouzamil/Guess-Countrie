import math
import random
import math

def sorteia_letra(palavra,lista):
    listaespecial=['.', ',', '-', ';', ' ']
    x=palavra.lower()
    listalower=[]
    for e in lista:
        listalower.append(e.lower())
    plistada=[]
    for j in palavra:
        if j not in plistada:
            plistada.append(j)
    lista_final=[]
    for i in plistada:
        if i not in listalower and i not in listaespecial:
            lista_final.append(i)
    if lista_final==[]:
        return ''
    a=random.choice(lista_final)
    return a

def esta_na_lista(pais,lista):
    for i in lista:
        if i[0]==pais:
            return True
    return False

def adiciona_em_ordem(pais,distancia,lista):
    pd=[pais,distancia]
    contador=0
    for i in range(len(lista)):
        if distancia>lista[i][1]:
            contador=i+1
    lista.insert(contador,pd)
    return lista

def normaliza(dic_cont_paises):
    dic_paises_cont = {}

    for continente in dic_cont_paises.keys():
        for pais in dic_cont_paises[continente].keys():
            dic_paises_cont[pais] = dic_cont_paises[continente][pais]
            dic_paises_cont[pais]['continente'] = continente
    
    return dic_paises_cont

def sorteia_pais(dic_paises_infos):
    lista_paises = []

    for pais in dic_paises_infos.keys():
        lista_paises.append(pais)

    return random.choice(lista_paises)

def haversine(r, phi1,lambda1,phi2,lambda2):

    raio = r #km terra

    phi1graus    = phi1     #latitutede ponto A      [-90,   +90]
    lambda1graus = lambda1  #longitude ponto A       [−180, +180]

    phi2graus    = phi2     #latitude ponto B        [-90,   +90]
    lambda2graus = lambda2  #longitude ponto B       [−180, +180]

    phi1rad    = math.radians(phi1graus)       #¦
    lambda1rad = math.radians(lambda1graus)    #¦  CONVERTE OS DADOS PARA RADIANOS                                            
    phi2rad    = math.radians(phi2graus)       #¦  PARA UTILIZAR A BIBLIOTECA MATH  
    lambda2rad = math.radians(lambda2graus)    #¦

    primeiroelemento = (math.sin((phi2rad-phi1rad)/2))**2
    segundoelemento  = math.cos(phi1rad)math.cos(phi2rad)((math.sin((lambda2rad-lambda1rad)/2))**2)

    d = 2*raio*math.asin((primeiroelemento+segundoelemento)**0.5)

    return d

def jogar_denovo():
    a=input('deseja jogar denovo(s/n)')
    while a!='s' and a!='n':
        print('a escolha deve ser s ou n')
        a=input('Deseja jogar denovo?(s/n)')   
    if a =='s':
        return True
    if a=='n':
        print('Até a proxima')
        return False