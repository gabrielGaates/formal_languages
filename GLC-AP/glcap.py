from greibach import *
from pda import *
from termcolor import colored


def pegarT(p):
    producoesT = []
    percorrer = p.values()
    alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','w','y','z']
    for a in percorrer:
        for b in a:
            for c in b:
                if(alfabeto.__contains__(c) and not producoesT.__contains__(c)):
                    producoesT.append(c)

    return producoesT

def transformarEntrada(p):
    v = []

    prod = {}
    prodaux = []
    for key in p.keys():
        prodaux = []
        v.append(key)
        for rhs in p[key]:
            prodaux.append(rhs)
        prod[key] = prodaux


    s = v[0]

    t = pegarT(prod)
    return v,prod,s,t

def calcDeltas(oProd,s2):
    per = {}
    listatransicoes = []
    per['q0'] = [('epsilon','epsilon',s2,'q1')]
    for i in oProd:
        salvar = '0'
        contador = 0
        principal = ''
        oquevemdepois = []
        for j in oProd[i]:

            if contador==0:
                salvar = j[0]

            if contador == 0:
                if(len(j)>1):
                    principal = j[1]
                else:
                    principal = 'epsilon'
            contador = contador + 1
        listatransicoes.append((salvar,principal,i,'q1'))
    listatransicoes.append(("?", "?", "epsilon", "qf"))
    per['q1'] = listatransicoes
    return per

if __name__ == "__main__":
    pp = pprint.PrettyPrinter()


    print("Transformando a forma normal de Greibach do exemplo para PDA")
    ################## 1 exemplo
    v_0 = ["A", "S"]
    t = ["a", "b"]
    p_0 = {"S": [["A", "A"], ["a"]], "A": [["S", "S"], ["b"]]}
    s = "S"
    var = mk_example(1, v_0, p_0)



    vP,prodP,sP,tP = transformarEntrada(var)
    Q = {"q0", "q1", "qf"}
    Sigma = tP
    q0 = "q0"
    F = {"qf"}
    V = vP
    palavra2 = "aba"
    per = calcDeltas(prodP,sP)
    print(per)

    pp.pprint(lifted_delta_clos([(palavra2, "q0", [])], per))


    ############################# 2 exemplo
    v1 = ["A", "B", "C"]
    t1 = ["a", "b"]
    p1 = {"A": [["B", "C"]], "B": [["C", "A"], ["b"]], "C": [["A", "B"], ["a"]]}
    s1 = "A"
    var2 = mk_example(2, v1, p1)

    vP, prodP, sP, tP = transformarEntrada(var2)
    Q = {"q0", "q1", "qf"}
    Sigma = tP
    q0 = "q0"
    F = {"qf"}
    V = vP
    palavra = "aab"
    per = calcDeltas(prodP, sP)
    print(per)

    pp.pprint(lifted_delta_clos([(palavra, "q0", [])], per))