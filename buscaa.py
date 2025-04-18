# -*- coding: utf-8 -*-
"""BuscaA.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10JzmrI4LvkfBC0nzcFA4QwBs8pl1dSN6
"""

# heuristica → estimativa do quanto falta até Bucharest (Em linha reta)

# grafo → caminhos disponíveis entre cidades e seus custos

# a_estrela_simples() → a função que executa a busca

# aberto → lista de caminhos possíveis a explorar

# sort() → ordena pela prioridade (menor f = g + h)

# print() → mostra passo a passo o caminho sendo formado

# Heurística: distância em linha reta de cada cidade até Bucharest
# Essa função é usada para "estimar" o quanto falta até o objetivo
heuristica = {
    "Arad": 366,
    "Zerind": 374,
    "Oradea": 380,
    "Sibiu": 253,
    "Fagaras": 178,
    "Bucharest": 0,
    "Timisoara": 329,
    "Rimnicu Vilcea": 193,
    "Craiova": 160,
    "Pitesti": 98
}

# Grafo com os caminhos possíveis entre as cidades e seus respectivos custos reais (g(n))
# Aqui estão apenas alguns trechos do mapa da Romênia (simplificado)
grafo = {
    "Arad": [("Zerind", 75), ("Sibiu", 140), ("Timisoara", 118)],
    "Zerind": [("Arad", 75), ("Oradea", 71)],
    "Oradea": [("Zerind", 71), ("Sibiu", 151)],
    "Sibiu": [("Arad", 140), ("Oradea", 151), ("Fagaras", 99), ("Rimnicu Vilcea", 80)],
    "Fagaras": [("Sibiu", 99), ("Bucharest", 211)],
    "Timisoara": [("Arad", 118), ("Lugoj", 111)],  # incluímos para completar
    "Rimnicu Vilcea": [("Sibiu", 80), ("Craiova", 146), ("Pitesti", 97)],
    "Craiova": [("Rimnicu Vilcea", 146), ("Pitesti", 138)],
    "Pitesti": [("Rimnicu Vilcea", 97), ("Craiova", 138), ("Bucharest", 101)],
    "Bucharest": []  # destino final, sem vizinhos
}

# Função da busca A* simplificada

def a_estrela_simples(inicio, objetivo):
    # Lista de cidades a visitar, começando com a cidade inicial, setado ali em baixo
    # Cada item da lista é uma tupla com: (cidade atual, caminho feito até aqui, custo total g), no começo ("Arad", ["Arad"], 0)
    aberto = [(inicio, [inicio], 0)]
     # Enquanto houver cidades para visitar
    while aberto:
        # Ordena a lista de caminhos do menor para o maior com base em f(n) = g(n)- Custo real que você gastou até essa cidade + h(n) Estimativa de quanto ainda falta pra chegar até o objetivo (usando a heurística).
        # Menor f(n) será o primeiro a ser explorado
        # X é cada item da lista "aberto"
        # X[0] = Cidade atual // heuristica[x[0]] = Distância estimada até o objetivo
        # X[2] custo g(n)

        aberto.sort(key=lambda x: x[2] + heuristica[x[0]])

        # Pega o caminho com menor f(n)
        # aberto = [("Arad", ["Arad"], 0)] = No .pop fica: atual = "Arad", caminho = ["Arad"], custo =0
        atual, caminho, custo = aberto.pop(0)

        # Exibe no terminal o que está acontecendo em cada passo
        print(f"Visitando: {atual} | Caminho: {caminho} | Custo: {custo}")

        # Se chegou na cidade objetivo, encerra com sucesso
        if atual == objetivo:
            print("\n Objetivo alcançado!")
            print("Caminho final:", " -> ".join(caminho))
            print("Custo total do caminho:", custo)
            return

        # Para cada vizinho da cidade atual
        # grafo é o dicionário com todas as conexões entre cidades.
        # grafo.get(atual, []) pega os vizinhos da cidade atual
        # Cada vizinho é uma tupla: (nome, custo) Ex: de "Sibiu" vem [("Fagaras", 99), ("Rimnicu Vilcea", 80)]
        for vizinho, custo_vizinho in grafo.get(atual, []):
            # Se ainda não passou por esse vizinho (evita voltar para trás)
            if vizinho not in caminho:
                # Cria um novo caminho incluindo esse vizinho
                novo_caminho = caminho + [vizinho]
                # Soma o novo custo com o custo atual
                novo_custo = custo + custo_vizinho
                # Adiciona essa nova possibilidade à lista de caminhos a explorar
                aberto.append((vizinho, novo_caminho, novo_custo))

# Chamando a função para buscar o caminho de Arad até Bucharest
a_estrela_simples("Arad", "Bucharest")