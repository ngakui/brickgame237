from enum import Enum       # Import enum Class

# Class to manage Game State
class GameState(Enum):
    """ 
        Args:
            QUIT - Enum called to quit game
            TITLE - Enum called to go to Menu Screen
            NEWGAME = Enum called to go to the Screen Game
    """
    QUIT = -1
    TITLE = 0
    NEWGAME = 1