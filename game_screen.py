import pygame                           # import of pygame librarie
from pygame.locals import *             # import all pygame locals functions 
from Class.boutton import Button        # import of Class Button
from Class.game_state import GameState  # import of Class GameState
from Class.brick import Brick           # import of Class Brick
from Class.object import Object         # import of Class Object
from Class.ball import Ball             # import of Class Ball
import random                           # import random librarie

# Function to add text 
def add_text(screen, font, text, color, left, top):
    """
        Args:
            font - type Font : use to add font to text
            text - type String: use to add custom text
            color - type (r,g,b): use to edit text Color
            left - type float: position on horizontal axis
            top - type float: position on vertical axis
    """
    txt = font.render(text, True, color)
    screen.blit(txt, (left, top))

# Function to add Brick Randomly
def add_brick(screen, lefts=[], tops=[]):
    """
        Args:
            lefts - Array:  Array of float for the horizontal axis
            tops - Array:  Array of float for the vertical axis
    """
    total = []
    for j in range(0,3):
        for i in range(0,5):
            total.append(Object(screen, 15, 40, lefts[i], tops[j], (255,255,255)))
    return total 

def game_screen(screen, game_state):

    BLUE = (106, 159, 181)
    WHITE = (255, 255, 255)
    lefts = [10, 60, 110, 160, 210, 260, 310, 360, 410]         # Array of horizontal float 
    tops = [10, 30, 50, 70]                                     # Array of vertical float
    random.shuffle(lefts)                                       # Shuffle Array
    random.shuffle(tops)                                        # Shuffle Array
    action = False
    clock = pygame.time.Clock()
    fps = 60
    font = pygame.font.Font('freesansbold.ttf', 20)
    brick = Brick(screen, 15, 60, 200, 400,(255,0,0))
    rect = pygame.Rect(brick.position_left, brick.position_top, brick.width, brick.height)
    ball = Ball(screen,pygame.Rect(brick.position_left, brick.position_top, brick.width, brick.height).x +(brick.width // 2), pygame.Rect(brick.position_left, brick.position_top, brick.width, brick.height).y - brick.height,(0,255,0),8)
    cibles = []
    cibles = add_brick(screen,lefts=lefts, tops=tops)
    ball_live = False                                           # Boolean to know ball state
    game_over = 0
    bg = pygame.image.load('assets/space1.jpg')                 # Load image Background
    
    return_btn = Button(
        center_position=(120, 450),
        font_size=20,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Back to main menu",
        action=GameState.TITLE,
    )

    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
            if (event.type == pygame.KEYDOWN) :
                
                # Restart ball position and player's break position if if [ball_live] is False.
                if event.key == pygame.K_SPACE and ball_live == False:
                    ball_live = True
                    ball.restart(screen,brick.rect.x +(brick.width // 2), brick.rect.y - brick.height,(0,255,0),8)
                    brick.restart(screen, 15, 60, 200, 400,(255,0,0))
                    cibles = add_brick(screen,lefts=lefts, tops=tops)
            
        clock.tick(fps)        
        screen.blit(bg, (0,0))

        # Drawing Objects
        brick.draw()
        for cible in cibles:
            cible.draw()
        ball.draw()

        # Move player's brick and ball
        if ball_live:
            brick.move()
            game_over = ball.move(brick, cibles)
            if game_over != 0:
                ball_live = False
        
        # Show differents messages when player enter in game, win or lose the game.
        if not ball_live:
            if game_over == 0:
                add_text(screen, font, "Press SPACE key to start", (106, 159, 181), 130, screen.get_height() // 2 +100)
            elif game_over == 1:
                add_text(screen, font, "You Won!!!", (106, 159, 181), 200, screen.get_height() // 2 +50)
                add_text(screen, font, "Press SPACE key to restart", (106, 159, 181), 120, screen.get_height() // 2 +100)
            elif game_over == -1:
                add_text(screen, font, "You Lost!!!", (106, 159, 181), 200, screen.get_height() // 2 +50)
                add_text(screen, font, "Press SPACE key to retry", (106, 159, 181), 122, screen.get_height() // 2 +100)
        ui_action = return_btn.update(pygame.mouse.get_pos(), mouse_up)

        # Change variable [game_state value] to update the screen.
        if ui_action is not None:
            game_state = ui_action
            return ui_action
        return_btn.draw(screen)

        pygame.display.flip()
