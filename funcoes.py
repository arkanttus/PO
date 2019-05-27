import math

def exp(num):
    e = 2.718281828
    return e ** num

#FILA M/M/1
def mm1():
    print("FILA M/M/1\n")
    lamb = float(input("Lambda: "))
    u    = float(input("Mi: "))
    t    = float(input("Tempo (0, caso o tempo nao tenha sido informado):  "))
    p    = lamb/u
    ls   = p/(1-p)
    lq   = (p**2)/(1-p)
    ws   = 1/(u-lamb)
    wq   = p/(u-lamb)
    wst  = exp( (-t / ws) ) * 100 #funcao de euler
    wqt  = p * wst

    print("\n P: {:.4f} \n Ls: {:.4f} \n Lq: {:.4f} \n Ws: {:.4f} \n Wq: {:.4f} \n Wst: {:.4f} % \n Wqt: {:.4f} % \n ".format(p,ls,lq,ws,wq,wst,wqt))

#FILA M/M/S
def mms():
    print("FILA M/M/S\n")
    lamb = float(input("Lambda: "))
    u    = float(input("Mi: "))
    S    = int(input("S (atendentes):  "))
    t    = float(input("Tempo (0, caso o tempo nao tenha sido informado):  "))
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

    print("\n P: {:.4f} \n Lq: {:.4f} \n Ls: {:.4f} \n Wq: {:.4f} \n Ws: {:.4f} \n p0: {:.4f} \n Wst: {:.4f} % \n Wqt: {:.4f} % \n".format(p,lq,ls,wq,ws,p0, wst, wqt))

#FILA M/M/1/K
def mm1k():
    print("FILA M/M/1/K\n")
    lamb = float(input("Lambda: "))
    u    = float(input("Mi: "))
    t    = float(input("Tempo (0, caso o tempo nao tenha sido informado):  "))
    k    = int(input("K(Capacidade do sistema: "))
    p = lamb/u
    lambli = lamb*(1-(p*k))

    if p == 1:
       ls = k/2
    else:
        ls = p/(1-p) - ((k+1)*p**(k+1))/ 1 - p**(k+1)

    ws = ls/lambli
    wq = ws - 1/u
    lq = wq*lambli

    print("\n P: {:.4f} \n Lq: {:.4f} \n Ls: {:.4f} \n Wq: {:.4f} \n Ws: {:.4f} \n".format(p,lq,ls,wq,ws))

#FILA M/M/S/K
def mmsk():
    print("FILA M/M/S/K\n")
    lamb = double(input("Lambda: "))
    u    = double(input("Mi: "))
    s    = int(input("S (atendentes):  "))
    k    = int(input("K(Capacidade do sistema: "))
    t    = double(input("Tempo (0, caso o tempo nao tenha sido informado):  "))
    p = lamb/(s*u)
    lambli = lamb*(1-(p*k))
    p0 = 0

    if p != 1:
        soma = 0
        #somatorio
        for n in range(0,s+1):
            soma += (s*p)**n / math.factorial(n)

        p0 = ((( s**s * p**(s+1) ) / (math.factorial(s)*(1-p))) + soma ) ** (-1)
    else:
        soma = 0
        for n in range(0,s):
            soma += (s**s) / math.factorial(n)

        p0 =    ((s**s)/math.factorial(s))*(k-s) + soma

    lq = (( s**s * p**(s+1) ) / math.factorial(s)*((1-p)**2))*((1-p)*(k-s)*(p**(k-s))*p0
    wq = (lq / lambli)
    ws = wq + 1/u
    ls = lambli*ws

    print("\n P: {:.4f} \n Lq: {:.4f} \n Ls: {:.4f} \n Wq: {:.4f} \n Ws: {:.4f} \n p0: {:.4f} \n".format(p,lq,ls,wq,ws,p0))
    '''
