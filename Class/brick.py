import pygame   
from pygame.locals import *
from Class.object import Object

# Class to create player's Brick
# It call function restart any time that it's instanciate
class Brick(Object):
    def __init__(self, screen, height, width, left, top, color):
        self.restart(screen, height, width, left, top, color)

    # function to move player's brick on Horizontal Axis
    def move(self):
        self.direction = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
            self.direction = -1
        if key[pygame.K_RIGHT] and self.rect.right < self.screen_width:
            self.rect.x += self.speed
            self.direction = 1
    
    # function to reset player's brick
    def restart(self, screen, height, width, left, top, color):
        """
        Args:
            screen - Screen dimensions
            speed - int : Speed of player's Brick
            position_left - float :Position of player's Brick on horizontal Axis
            position_top - float : Position of player's Brick on Vertical Axis
            screen_width - float : Screen width
            screen_height - float : Screen height
            width - float : player's Brick width
            height - float : player's Brick height
            color - tuple(r,g,b) : Color of player's Brick
            direction - int : direction of player's Brick
            rect - Rect() : Pygame Rect function that help to draw player's Brick
        """
        self.screen = screen
        self.speed = 10
        
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.width = width
        self.height = height
        self.position_left = int((self.screen_width / 2) - (self.width / 2))
        self.position_top = self.screen_height - (self.height * 5)
        self.color = color
        self.direction = 0
        self.rect = Rect(self.position_left, self.position_top, self.width, self.height)
