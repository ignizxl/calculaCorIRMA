
#criando a função calcularCor que recebe como parâmetro uma cor
def calcularCor(cor):
    #criando os acumulador m e m2 que iniciam valendo 0 e vão sendo incrementado a iteração do laço for
    m = 0
    m2 = 0
    #criando um laço for para 'varrer' cada elemento da 'cor' iniciando do 0 até o tamanho da cor
    for i in range(0, len(cor)):
        # o m incrementa a cada iteração recebendo a cor na posição i    
        m += cor[i]
        # o m incrementa a cada iteração recebendo a cor na posição i vezes a cor na posição i
        m2 += cor[i] * cor[i]
    #rm recebe o valor de m sobre o tamanho da cor 
    rm = m / len(cor)
    #rm recebe o valor de m2 sobre o tamanho da cor menos rm vezes rm
    si = m2 / len(cor) - rm * rm
    #e por fim, retorno o valor de rm e o valor de si(mas extraindo a raiz do si)
    return rm, si ** (1/2)
