with open('entrada.txt', 'r') as txt:
    lines = txt.readlines()

qtd_operacoes = int(len(lines)/3)

def union(a, b):
    for i in b:
        a.append(i)
    return a
def intersection(a, b):
    interseccao = []
    for value in a:
        if value in b:
            interseccao.append(value)
    return interseccao
def difference(a, b):
    return list(set(a) - set(b))
def multiply(a, b):
    par = []
    for x in range(len(a)):
        for y in range(len(b)):
            par.append((a[x], b[y]))
    return par
for operacao in range(qtd_operacoes):
    for x in range(3):
        current_line = lines[0 + (operacao * 3) + x]
        if x == 0:
            op = current_line.split()
        elif x == 1:
            a = current_line.split()
        elif x == 2:
            b = current_line.split()
    if op[0] == 'U':
        print(f"União: Conjunto 1 {a}, Conjunto 2 {b}. Resultado = {(union(a, b))}")
    if op[0] == 'I':
        print(f"Interseção: Conjunto 1 {a}, Conjunto 2 {b}. Resultado = {(intersection(a, b))}")
    if op[0] == 'D':
        print(f"Diferença: Conjunto 1 {a}, Conjunto 2 {b}. Resultado = {(difference(a, b))}")
    if op[0] == "C":
       print(f"Produto Cartesiano: Conjunto 1 {a}, Conjunto 2 {b}. Resultado = {(multiply(a, b))}")



