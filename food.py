from turtle import Turtle
import random
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)      # all functions inherited from Turtle 
        self.color('Yellow')
        self.speed('fastest')
        self.refresh()
    
    def refresh(self):
        random_x = random.randint(-280,280)   #screen size 600 * 600
        random_y = random.randint(-280,280)
        self.goto(random_x,random_y)
