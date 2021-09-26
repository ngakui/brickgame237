import pygame
from pygame.locals import *

# Class to create instantiation of objects
class Object:
    # Constructor
    def __init__(self, screen, height, width, left, top, color):
        """
        Args:
            screen - Screen dimensions
            position_left - float :Position of object on horizontal Axis
            position_top - float : Position of object on Vertical Axis
            screen_width - float : Screen width
            screen_height - float : Screen height
            width - float : Object width
            height - float : Object height
            color - tuple(r,g,b) : Color of Object
            rect - Rect() : Pygame Rect function that help to draw object
        """
        self.screen = screen                                       
        self.position_left = left                                   
        self.position_top = top                                     
        self.screen_width = self.screen.get_width()                 
        self.screen_height = self.screen.get_height()              
        self.width = width
        self.height = height
        self.color = color
        self.rect = Rect(self.position_left, self.position_top, self.width, self.height)

    # function to draw an object    
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)