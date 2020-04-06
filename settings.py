FPS = 120		#locks the FPS

CAMERA_SPEED = 20

#define simple color constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHTGREY = (100, 100, 100)
DARKGREY = (40, 40, 40)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)	
YELLOW = (255, 255, 0)
ORANGE = (255, 150, 0)

BASIC_FONT = 'freesansbold.ttf'
"""
Some other font options:
castellar, rod, fangsong, ebrima
pygame.font.match_font('garamondbold')
pygame.font.match_font('freesansbold')
"""

TINY_TEXT = 13 # was tinyText
SMALL_TEXT = 17 # was smallText
MEDIUM_TEXT = 20 # was mediumText
LARGE_TEXT = 32 # was largeText


TILESIZE = 25 	
"""Tilesize 
Should always represent 1" in gameplay; for reference: 25.4 mm / inch
Standard battlefield size is 4' x 6' (48 tiles x 72 tiles) (1200 x 1800 pixels)
Recommend a large terrain feature in each 2' x 2' (24 tiles x 24 tiles) section
Units are deployed 12" away from the line that divides the two halves of the boards
"""

#GRIDWIDTH = WIDTH / TILESIZE
#GRIDHEIGHT = HEIGHT / TILESIZE

