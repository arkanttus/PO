import math

def exp(num):
    e = 2.718281828
    return e ** num

#FILA M/M/1
def mm1(help, ler_p):
    print("FILA M/M/1\n")
    lamb = float(input("Lambda" + (" (taxa media de chegada): " if help else ": ")))
    u    = float(input("Mi" + (" (taxa media de clientes atendidos por servidor): " if help else ": ")))
    t    = float(input("Tempo" + (" (0, caso o tempo nao tenha sido informado):  " if help else ": ")))

    p    = lamb/u
    ls   = p/(1-p)
    lq   = (p**2)/(1-p)
    ws   = 1/(u-lamb)
    wq   = p/(u-lamb)
    wst  = exp( (-t / ws) ) * 100 #funcao de euler
    wqt  = p * wst

    if help:
        print("\n P (Probabilidade de se manter ocupado): {:.4f} \n Lq (Comprimento medio da fila): {:.4f} \n Ls (Comprimento medio do sistema): {:.4f} \n Wq (Tempo medio de espera na fila): {:.4f} \n Ws (Tempo medio de espera no sistema): {:.4f} \n Wst (Probabilidade de permanecer 't' unidades de tempo no sistema): {:.4f} % \n Wqt (Probabilidade de permanecer 't' unidades de tempo na fila): {:.4f} % \n".format(p,lq,ls,wq,ws,wst,wqt))

    else:
        print("\n P: {:.4f} \n Lq: {:.4f} \n Ls: {:.4f} \n Wq: {:.4f} \n Ws: {:.4f} \n Ws(t): {:.4f} % \n Wq(t): {:.4f} % \n".format(p,lq,ls,wq,ws,wst,wqt))

    if ler_p:
        if help:
            print("Calculo de Pn (Probabilidade de ter 'n' no sistema): ")
        else:
            print("Calculo de Pn: ")

        while True:
            try:
                n = int(input("n: "))
                pn = (p**n) * (1 - p)
                print("P{:d}: {:.4f} ".format(n, pn))
            except ValueError:
                break

#FILA M/M/S
def mms(help, ler_p):
    print("FILA M/M/S\n")
    lamb = float(input("Lambda" + (" (taxa media de chegada): " if help else ": ")))
    u    = float(input("Mi" + (" (taxa media de clientes atendidos por servidor): " if help else ": ")))
    S    = int(input("S" + (" (atendentes):  " if help else ": ")))
    t    = float(input("Tempo" + (" (0, caso o tempo nao tenha sido informado):  " if help else ": ")))

    p    = lamb/(S*u)

    if p < 1:
        soma = 0
        #somatorio
        for n in range(0,S+1):
            soma += (S*p)**n / math.factorial(n)

        p0 = ((( S**S * p**(S+1) ) / (math.factorial(S)*(1-p))) + soma ) ** (-1)
    else:
        p0 = 0

    lq   = (S**S * p**(S+1) * p0) / ( math.factorial(S) * ((1-p)**2) )
    wq   = lq/lamb
    ws   = wq + (1/u)
    ls   = lamb * ws
    wst  = ( exp(-(u*t)) * ( 1 + ((S*p)**p * p0 * (1 - exp(-u*t*(S-1-S*p))) ) / (math.factorial(S)*(1-p)*(S-1-S*p)) ) ) * 100
    wqt  = (( ( ((S*p)**S) * p0 ) / (math.factorial(S) * (1-p))) * exp( -S*u*t*(1-p) )) * 100

    if help:
        print("\n P (Probabilidade de se manter ocupado): {:.4f} \n Lq (Comprimento medio da fila): {:.4f} \n Ls (Comprimento medio do sistema): {:.4f} \n Wq (Tempo medio de espera na fila): {:.4f} \n Ws (Tempo medio de espera no sistema): {:.4f} \n p0 (Probabilidade de nao ter ninguem): {:.4f} \n Wst (Probabilidade de permanecer 't' unidades de tempo no sistema): {:.4f} % \n Wqt (Probabilidade de permanecer 't' unidades de tempo na fila): {:.4f} % \n".format(p,lq,ls,wq,ws,p0,wst,wqt))
    else:
        print("\n P: {:.4f} \n Lq: {:.4f} \n Ls: {:.4f} \n Wq: {:.4f} \n Ws: {:.4f} \n p0: {:.4f} \n Ws(t): {:.4f} % \n Wq(t): {:.4f} % \n".format(p,lq,ls,wq,ws,p0,wst,wqt))

    if ler_p:
        if help:
            print("Calculo de Pn (Probabilidade de ter 'n' no sistema): ")
        else:
            print("Calculo de Pn: ")

        while True:
            try:
                n = int(input("n: "))
                pn = 0.0
                if n <= S :
                    pn = (((S*p)**n)/math.factorial(n))*p0
                else:
                    pn = (((S**S)*(p**n))/math.factorial(S))*p0
                print("P{:d}: {:.4f} ".format(n, pn))
            except ValueError:
                break

#FILA M/M/1/K
def mm1k(help, ler_p):
    print("FILA M/M/1/K\n")
    lamb = float(input("Lambda" + (" (taxa media de chegada): " if help else ": ")))
    u    = float(input("Mi" + (" (taxa media de clientes atendidos por servidor): " if help else ": ")))
    t    = float(input("Tempo" + (" (0, caso o tempo nao tenha sido informado):  " if help else ": ")))
    k    = int(input("K" + (" (capacidade do sistema): " if help else ": ")))

    p = lamb/u
    p0 = 0.0


    if p == 1:
       ls = k/2
       p0 = 1/(k+1)
    else:
        ls = p/(1-p) - ((k+1)*p**(k+1))/ 1 - p**(k+1)
        p0 = (1-p)/(1-(p**(k+1)))

    pK = ((p**(k))*(1-p))/(1-(p**(k+1)))
    lambli = lamb*(1-(pK))
    ws = ls/lambli
    wq = ws - 1/u
    lq = wq*lambli

    if help:
        print("\n P (Probabilidade de se manter ocupado): {:.4f} \n Lq (Comprimento medio da fila): {:.4f} \n Ls (Comprimento medio do sistema): {:.4f} \n Wq (Tempo medio de espera na fila): {:.4f} \n Ws (Tempo medio de espera no sistema): {:.4f} \n p0 (Probabilidade de nao ter ninguem): {:.4f} \n".format(p,lq,ls,wq,ws,p0))
    else:
        print("\n P: {:.4f} \n Lq: {:.4f} \n Ls: {:.4f} \n Wq: {:.4f} \n Ws: {:.4f} \n p0: {:.4f}".format(p,lq,ls,wq,ws,p0))

    if ler_p:
        if help:
            print("Calculo de Pn (Probabilidade de ter 'n' no sistema): ")
        else:
            print("Calculo de Pn: ")

        while True:
            try:
                n = int(input("n: "))
                pn = 0.0
                if p == 1:
                    pn = 1/(k+1)
                else:
                    pn = ((p**n)*(1-p))/(1-(p**(k+1)))
                print("P{:d}: {:.4f}".format(n,pn))
            except ValueError:
                break

#FILA M/M/S/K
def mmsk(help, ler_p):
    print("FILA M/M/S/K\n")
    lamb = float(input("Lambda" + (" (taxa media de chegada): " if help else ": ")))
    u    = float(input("Mi" + (" (taxa media de clientes atendidos por servidor): " if help else ": ")))
    s    = int(input("S" + (" (atendentes):  " if help else ": ")))
    k    = int(input("K" + (" (capacidade do sistema): " if help else ": ")))
    t    = float(input("Tempo" + (" (0, caso o tempo nao tenha sido informado): " if help else ": ")))

    p = lamb/(s*u)
    p0 = 0.0

    if p != 1:
        soma = 0.0
        #somatorio
        for n in range(0,s+1):
            soma += (s*p)**n / math.factorial(n)

        p0 = ((( (s**s) * (p**(s+1)) * (1-(p**(k-s))) ) / (math.factorial(s)*(1-p))) + soma ) ** (-1)
    else:
        #somatorio
        soma = 0.0
        for n in range(0,s+1):
            soma += (s**n) / math.factorial(n)

        p0 = (((s**s)/math.factorial(s))*(k-s) + soma)**(-1)

    pK = ((p**(k))*(1-p))/(1-(p**(k+1)))
    lambli = lamb*(1-(pK))
    lq = (( s**s * p**(s+1) ) / math.factorial(s)*((1-p)**2))*((1-p)*(k-s)*(p**(k-s)))*p0
    wq = lq/lambli
    ws = wq + 1/u
    ls = lambli*ws

    if help:
        print("\n P (Probabilidade de se manter ocupado): {:.4f} \n Lq (Comprimento medio da fila): {:.4f} \n Ls (Comprimento medio do sistema): {:.4f} \n Wq (Tempo medio de espera na fila): {:.4f} \n Ws (Tempo medio de espera no sistema): {:.4f} \n p0 (Probabilidade de nao ter ninguem): {:.4f} \n".format(p,lq,ls,wq,ws,p0))
    else:
        print("\n P: {:.4f} \n Lq: {:.4f} \n Ls: {:.4f} \n Wq: {:.4f} \n Ws: {:.4f} \n p0: {:.4f} \n".format(p,lq,ls,wq,ws,p0))

    if ler_p:
        if help:
            print("Calculo de Pn (Probabilidade de ter 'n' no sistema): ")
        else:
            print("Calculo de Pn: ")

        while True:
            try:
                n = int(input("n: "))
                pn = 0.0
                if n <= S :
                    pn = (((S*p)**n)/math.factorial(n))*p0
                elif n <= k
                    pn = (((S**S)*(p**n))/math.factorial(S))*p0                                    
                print("P{:d}: {:.4f} ".format(n, pn))
            except ValueError:
                break
