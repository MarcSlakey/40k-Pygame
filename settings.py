

#Create and set Window size and FPS constants
TITLE = "40k pygame"
WIDTH = 1900	#Should be evenly divisible by TILESIZE value below 
HEIGHT = 900	
FPS = 120		#locks the FPS

#define simple color constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHTGREY = (100, 100, 100)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)	
YELLOW = (255, 255, 0)
ORANGE = (255, 150, 0)


TILESIZE = 25 	#should always represent 1" in gameplay; for reference: 25.4 mm / inch
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE
