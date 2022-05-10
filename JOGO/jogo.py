import json
import math
import random

with open('JOGO/DADOS.json', 'r') as data:
    dados = data.read()

dados = json.loads(dados)

print(dados)