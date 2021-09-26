import pygame                           # import of pygame librarie
from pygame.locals import *             # import all pygame locals functions 
from Class.brick import Brick           # import of Class Brick
from Class.object import Object         # import of Class Object

# Class to create ball
# It call function restart any time that it's instanciate
class Ball(Object):
    def __init__(self, screen, left, top, color, raduis):
        self.restart(screen, left, top, color, raduis)
    
    # function to move ball on the screen
    def move(self, brick, bricks):
        """
            Args:
                brick - type Brick : Player's Brick
                bricks - type [Brick] : Brick Array
        """
        collision = 5                       # variable to manage collision detection
        brick_destroyed = 1                 # variable to know if brick is destroy or not
        item_count = 0                      # count number of destroyed brick
        for br in bricks:
            if pygame.Rect(self.position_left, self.position_top, self.raduis * 2, self.raduis * 2).colliderect(br.rect):
                if abs(pygame.Rect(self.position_left, self.position_top, self.raduis * 2, self.raduis * 2).bottom  - br.rect.top) < collision and self.speed_y > 0:
                    self.speed_y *= -1
                if abs(pygame.Rect(self.position_left, self.position_top, self.raduis * 2, self.raduis * 2).top  - br.rect.bottom) < collision and self.speed_y < 0:
                    self.speed_y *= -1  
                if abs(pygame.Rect(self.position_left, self.position_top, self.raduis * 2, self.raduis * 2).right  - br.rect.left) < collision and self.speed_x > 0:
                    self.speed_x *= -1  
                if abs(pygame.Rect(self.position_left, self.position_top, self.raduis * 2, self.raduis * 2).left  - br.rect.right) < collision and self.speed_x < 0:
                    self.speed_x *= -1
            # pygame.sprite.spritecollideany(self, bricks)
                # Destroy block
                # if br[item_count][1] > 1:
                #     br[item_count][1] -= 1
                # else:
                br.rect = (0,0,0,0)
            if br.rect != (0,0,0,0):
                brick_destroyed = 0
            item_count += 1
        if brick_destroyed == 1:
            self.game_over = 1
        if self.position_left <= 0 or self.position_left > 480:
            self.speed_x *= -1
        if self.position_top <= 0:
            self.speed_y *= -1
        if self.position_top > self.screen.get_height():
            self.game_over = -1
        
        if pygame.Rect(self.position_left, self.position_top, self.raduis * 2, self.raduis * 2).colliderect(brick.rect):
            # check top collision
            if abs(pygame.Rect(self.position_left, self.position_top, self.raduis * 2, self.raduis * 2).bottom - brick.rect.top) < collision and self.speed_y > 0:
                self.speed_y *= -1
                self.speed_x += brick.direction
                if self.speed_x > self.speed_max:
                    self.speed_x = self.speed_max
                elif self.speed_x < 0 and self.speed_x < self.speed_max:
                    self.speed_x = -self.speed_max
            else:
                self.speed_x *= -1
        self.position_top += self.speed_y
        self.position_left += self.speed_x

        return self.game_over
   
    def restart(self, screen, left, top, color, raduis):
        """
        Args:
            screen - Screen dimensions
            speed_x - int : Speed of ball on horizontal axis
            speed_y - int : Speed of ball on vertical axis
            speed_max - int : Max Speed of ball 
            raduis - float : raduis of ball
            position_left - float : Position of ball on Horizontal Axis
            position_top - float : Position of ball on Vertical Axis
            color - tuple(r,g,b) : Color of player's Brick
            game_over - boolean : help to know if ball is fallen
            rect - Rect() : Pygame Rect function that help to draw player's Brick
        """
        self.screen = screen
        self.speed_x = 4
        self.speed_y = -4
        self.speed_max = 5
        self.raduis = raduis
        self.position_left = left - self.raduis
        self.position_top = top
        self.color = color
        self.game_over = 0
        self.rect = Rect(self.position_left, self.position_top, self.raduis * 2, self.raduis * 2)


    def draw(self):
        pygame.draw.circle(self.screen, self.color, (pygame.Rect(self.position_left, self.position_top, self.raduis * 2, self.raduis * 2).x + self.raduis, pygame.Rect(self.position_left, self.position_top, self.raduis * 2, self.raduis * 2).y + self.raduis), self.raduis)