def leitura(arquivo):
    arquivo = open("amarelo.sce", "r")
    esquerda = []
    direita = []
    cont = 0
    for i in arquivo:
        cont += 1
        linha = i.replace("\n", "").replace(";", "")
        linha = linha.split(" ")
        esquerda.append([float(linha[0]), float(linha[1]), float(linha[2])])
        direita.append([float(linha[3]), float(linha[4]), float(linha[5])])

    return (esquerda, direita)


def rgb(lado):
    r, g, b = [], [], []
    for i in lado:
        r.append(i[0])
        g.append(i[1])
        b.append(i[2])
    return (r, g, b)


def calculos(cor):
    m = 0
    m2 = 0
    for i in cor:
        m += i
        m2 += i * i
    u = m / len(cor)
    si = m2 / len(cor) - u * u
    return u, (si) ** 0.5


def executar(cor):
    miE, sigE = [], []
    miD, sigD = [], []
    esquerda, direita = leitura(cor)
    for i in range(0, 3):
        miSigE = calculos(rgb(esquerda)[i])
        miSigD = calculos(rgb(direita)[i])
        miE.append(miSigE[0])
        sigE.append(miSigE[1])
        miD.append(miSigD[0])
        sigD.append(miSigD[1])

    return miE, sigE, miD, sigD


print("miE:", executar("amarelo.sce")[0])
print("sigE:", executar("amarelo.sce")[1])
print("miD:", executar("amarelo.sce")[2])
print("sigD:", executar("amarelo.sce")[3])
