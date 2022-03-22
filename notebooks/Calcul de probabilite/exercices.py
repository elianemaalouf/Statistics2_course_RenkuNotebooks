import ipywidgets as widgets
from ipywidgets import GridspecLayout, Button, Layout, AppLayout
from IPython.display import display, clear_output, Image
import fn as s


class Ex:
    def __init__(self, sol_index, ex_index):
        self.sol_index = sol_index-1 # pour aller chercher la bonne solution
        self.ex_index = ex_index-1 # pour aller chercher la bonne réponse (l'ex 2 en propose plsr) Ex(2,1) va charger la réponse une de l'exercice 2
        self.solutions = s.solutions
        self.ex_answer = widgets.Text(value= '',
                                      placeholder= 'Tapez ici',
                                      description='Réponse',
                                      disabled=False)
        
        self.instruction = widgets.HTML('Entrez votre réponse à la question {} sous forme de fraction (i.e. x/y):'.format(str(self.ex_index + 1)))
        
        self.button = widgets.Button(description='Soumettre',
                                     disabled=False,
                                     button_style='', # 'success', 'info', 'warning', 'danger' or ''
                                     tooltip='Click me',
                                     icon='check' # (FontAwesome names without the `fa-` prefix)
                                    )
        self.counter = 0
        
        def test(change): 
            self.counter += 1
            self.value = str(self.ex_answer.value)        
            self.correct_value = s.solutions[self.sol_index][self.ex_index]
            if self.value == self.correct_value:
                print("Tetantive {}: Bravo! votre réponse est correcte :)".format(self.counter))
            else:
                print("Tetantive {}:Malheureusement, la réponse soumise n'est pas correcte. \n \
                Vous pouvez resoumettre une autre réponse ou procéder étape par étape en cliquant sur 'Show Solution'".format(self.counter))
                
                
        display(self.instruction)
        display(widgets.HBox([self.ex_answer, self.button]))
        self.button.on_click(test)