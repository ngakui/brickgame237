import pygame                           # Import Pygame librarie
from Class.boutton import Button        # import of Class Button
from Class.game_state import GameState  # import of Class GameState

# Function for Menu Screen
def menu_screen(screen, game_state):
    """
        Args:
            screen - Screen dimensions
            game_state - GameState : State which allow to know on which screen we are
    """

    pygame.display.set_caption("Brick Space 237")               # Add a title to Windows

    BLUE = (106, 159, 181)                                      # Color of type (r, g, b)
    WHITE = (255, 255, 255)                                     # Color of type (r, g, b)

    green = (0, 255, 0)                                         # Color of type (r, g, b)
    blue = (0, 0, 128)                                          # Color of type (r, g, b)
    font = pygame.font.Font('freesansbold.ttf', 32)             # Set font Style of type (Policy, Size)

    text = font.render('Brick Space 237', True, green, blue)    # Add a text on Menu Screen
    
    start = Button(                                             # Instance of Button to Start Game
            center_position=(250, 150),
            font_size=30,
            bg_rgb=BLUE,
            text_rgb=WHITE,
            text="Start",
            action=GameState.NEWGAME,
        )
    
    close = Button(                                             # Instance of Button to Close Game
            center_position=(250, 300),
            font_size=30,
            bg_rgb=BLUE,
            text_rgb=WHITE,
            text="Quit",
            action=GameState.QUIT,
        )
    buttons = [start, close]
    bg = pygame.image.load('assets/space2.jpg')                 # Load local image with Pygame
    textRect = text.get_rect()
    textRect.center = (250, 50)
    while True:
        mouse_up = False
        # completely fill the surface object
        # with white color
        screen.blit(bg, (0,0))                                  # Draw image in background
    
        # copying the text surface object
        # to the display surface object
        # at the center coordinate.
        screen.blit(text, textRect)

        # iterate over the list of Event objects
        # that was returned by pygame.event.get() method.
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
            # if event object type is QUIT
            # then quitting the pygame
            # and program both.
            if event.type == pygame.QUIT:
    
                # deactivates the pygame library
                pygame.quit()
    
                # quit the program.
                quit()
        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                game_state = ui_action                                # Update game_state when button is cliked
                return ui_action     
            button.draw(screen)
            
        pygame.display.update()                                       # Draws the surface object to the screen.
