from sympy.functions.combinatorial.numbers import nC

def ex_1():
    return ["11111/40000"]

def ex_2():
    
    a = nC(4, 2) / nC(36, 2)
    b = nC(9, 2) / nC(36, 2)
    c = (nC(1, 1) * nC(1, 1)) / nC(36, 2)
    d = (nC(36, 2) - nC(34, 2)) / nC(36, 2)
    e = nC(18, 2) / nC(36, 2)
    f = (nC(18, 1) * nC(18, 1)) / nC(36, 2)
    
    results = [a, b, c, d, e, f]
    
    final = [str(result) for result in results]
    
    return final


def ex_3():
    return  ["1/6"]


def ex_4():
    return ["19/24"]

solutions = [ex_1(), ex_2(), ex_3(), ex_4()]