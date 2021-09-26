import pygame                           # Import Pygame librarie
from menu_screen import menu_screen     # Import Menu Screen function
from game_screen import game_screen     # Import Game Screen function
from Class.game_state import GameState  # Import GameState Class

# Main function which manage all App's Screens
def main():
    pygame.init()

    screen = pygame.display.set_mode((500, 500))        # Set defaut screen height and width
    global game_state                                   # Global variable of type Enum which help to change Screen
    game_state = GameState.TITLE

    while True:
        # Show Menu Screen
        if game_state == GameState.TITLE:
            game_state = menu_screen(screen,game_state)

        # Show Game Screen
        if game_state == GameState.NEWGAME:
            game_state = game_screen(screen,game_state)

        # Quit the game
        if game_state == GameState.QUIT:
            pygame.quit()
            return

# call main when the script is run
if __name__ == "__main__":
    main()