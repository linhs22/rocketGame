import sys

import pygame 

class AlienInvasion: 
    # Overall all class to manage game assets and behavior
    
    def __init__(self): 
        # Initialize the game, and create game resources
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        # Set the background color.
        self.bg_color = (230, 230, 230)

    def run_game(self):
        # Start the main loop for the game.
        while True:
            # This watches for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
        
            #Redraw the screen during each pass through the loop
            self.screem.fill(self.bg_color)
                
            # This makes the most recently drawn screen available
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance and run the game.
    ai =AlienInvasion()
    ai.run_game()

