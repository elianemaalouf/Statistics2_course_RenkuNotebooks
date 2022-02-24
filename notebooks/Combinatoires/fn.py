from math import factorial

def nCr(n,r):
    return factorial(n) / factorial(r) / factorial(n-r)

def permutationNoRep(n):
    return factorial(n)

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

def verify_ex5_1(n, n_choice):
    total = count_with_rep(n, n_choice)
    return total

def verify_ex5_2(n, n_choice, l, l_choice):
    total = count_with_rep(l, l_choice) * count_with_rep(n, n_choice) 
    return total

def verify_ex5_3(pos, n, n_choice, l, l_choice):
    # position the letter 
    # choose the letter and choose the numbers 
    total = count_with_rep(l, l_choice) * count_with_rep(n, n_choice) 
    return total * pos

def verify_ex5_4(n, n_choice, l, l_choice):
    total = 0
    total_let = count_with_rep(l, l_choice) 
    for i in range(n+1):
        total = total + total_let * count_with_rep(i, n_choice) 
    return total 

def verify_ex5_5(pos, n, n_choice, l, l_choice):
    # position the letters
    pos_let = nCr(pos, l)
     # choose the letters and choose the numbers 
    total = count_with_rep(l, l_choice) * count_with_rep(n, n_choice) 
    return total * pos_let

def verify_ex6_1(n, reps_n):
    prod_rep = 1
    for i in reps_n:
        prod_rep = prod_rep * factorial(i)
    total = factorial(n)/prod_rep
    return total