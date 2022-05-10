import random
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