import ipywidgets as widgets
from ipywidgets import GridspecLayout, Button, Layout, AppLayout
from IPython.display import display, clear_output, Image

file_names = [ 
    "Images/basic.jpeg",
    "Images/union.jpeg",
    "Images/intersection.jpeg",
    "Images/addition_rule.jpeg",
    "Images/addition_rule_2.jpeg",
    "Images/property_1.jpeg"
             ]


class ImageButton:
    
    def __init__(self, index):
        
        self.image_index = index-1
        self.file = open(file_names[self.image_index], "rb")
        self.image = self.file.read()
        self.button = widgets.Button(description="Image {}".format(index),
                                     layout=widgets.Layout(width="15%"))
        
        def show_image(change):
            display(widgets.Image(
                value=self.image,
                format='png',
                width=600,
                height=800
            ))

        #display(self.button)
        self.button.on_click(show_image)