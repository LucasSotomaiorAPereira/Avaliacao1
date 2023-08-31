# Eduardo Pianovski Netto, Lucas Sotomaior Pereira
# Avaliação em grupo - 1

def calcular_conjuntos(conjunto):
    for i, linha in enumerate(conjunto):
        if i == 0:
            continue
        elif i % 3 == 1:
            operador = linha
            A = conjunto[i + 1]
            A = set(A.split(","))
            B = conjunto[i + 2]
            B = set(B.split(","))

            if operador == 'U':
                resultado = A.union(B)
                print(f"União: conjunto 1 {A}, conjunto 2 {B}. Resultado: {resultado}\n")
            elif operador == 'I':
                resultado = A.intersection(B)
                print(f"Intersecção: conjunto 1 {A}, conjunto 2 {B}. Resultado: {resultado}\n")
            elif operador == 'D':
                resultado = A.difference(B)
                print(f"Diferença: conjunto 1 {A}, conjunto 2 {B}. Resultado: {resultado}\n")
            elif operador == 'C':
                resultado = [(i, j) for i in B for j in A]
                print(f"Produto Cartesiano: conjunto 1 {A}, conjunto 2 {B}. Resultado: {resultado}\n")


if __name__ == "__main__":

    arquivo_url = "2.txt"

    linhas = []
    with open(arquivo_url, "r") as arquivo:
        for linha in arquivo:
            linhas.append(linha)
    conjunto = []
    for linha in linhas:
        linha = linha.replace('\n', '')
        conjunto.append(linha)
    print(f"Arquivo {arquivo_url}: \n")
    calcular_conjuntos(conjunto)
    print()
    