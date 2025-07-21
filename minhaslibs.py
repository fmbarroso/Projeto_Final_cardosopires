"""
Aqui iremos colocar os nosos métodos próprios
"""

def ler_ficheiro(nome_ficheiro):
    """
método para abrir um ficheiro txt em modo leitura e imprimir o seu conteúdo do ficheiro
    """
    meu_ficheiro = open(nome_ficheiro, "r", encoding="utf-8")
    for line in meu_ficheiro:
        print(line.strip())
    meu_ficheiro.close()