import pandas as pd
def sol_24():
    
    return [str(round(1/3, 2)), str(round(1/3, 2)), str(round(2/3, 2)), str(1)]


def sol_26a():
    
    sol = pd.DataFrame(
        index = [r'$G$', r'$\overline{\rm G}$', r'$Total$'], 
        data={r'$J$': [160, 200, 360], r'$\overline{\rm J}$': [80, 60, 140], r'$Total$' :[240, 260, 500]})

    sol_list = [sol.iloc[j,i] for i in range(2) for j in range(2)]
    return sol_list

def sol_26b():
    
    return [str(round(360/500, 2)), str(round(160/500, 2)),  str(round(160/360, 2)), str(round(160/240, 2))]
            

def sol_27a():
    
    sol = pd.DataFrame(
        index = [r'$G$', r'$\overline{\rm G}$', r'$Total$'], 
        data={r'$\varphi$': [0.12, 0.15, 0.27], r'$\overline{\rm \varphi}$': [0.28, 0.45, 0.73], r'$Total$' :[0.4, 0.6, 1]})
    
    return sol 
            
            
def sol_27b():
    
    return [str(0.15), str(0.27), str(0.72), str(0.25), str(0.56), str(0.38)]
            
def sol_28a():
    
    return [str(0.3), str(0.1), str(0.4), str(0.29)]
            
            
sol_dec = [sol_24(), sol_26b(),  sol_27b(), sol_28a()]
            
sol_tab = [sol_26a(), sol_27a()]
