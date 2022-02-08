def verify_ex1(n, n_choice):
    total = n_choice ** n 
    return total 

def verify_ex2(n_arome, agencement = [1,2,3]):
    total = 0
    for i in range(len(agencement)):
        total = total + ex2_count(n_arome,agencement[i])
    return total 

def ex2_count(n_arome, boules):
    # pour un type d'agencement fixé
    total = 1
    while boules > 0:
        total = total * n_arome
        n_arome -= 1
        boules -= 1
    
    return total 

def verify_ex3_1():
    total = 9 * 9 * 8 * 7
    return total 

def verify_ex3_2():
    total = 8 * 8 * 7 * 6
    return total 

def verify_ex3_3():
    total = 9 * 8 * 7 + 8 * 8 * 7 
    return total 

def verify_ex3_4():
    total = 5 * 9 * 8 + 5 * 9 * 8 * 7 + 5 * 9 * 8 * 7 * 6
    return total 

def count_with_rep(n, n_choice):
    total = n_choice**n
    return total

def verify_ex4_1(n, n_choice):
    total = count_with_rep(n, n_choice)
    return total

def verify_ex4_2(n, n_choice, l, _choice):
    total = count_with_rep(l, l_choice) * count_with_rep(n, n_choice) 
    return total

def verify_ex4_3(n, n_choice, l, _choice)