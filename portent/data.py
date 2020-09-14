"""ANSI codes and static text for portent's welcome messages.
"""

# 8-bit foreground colour codes.
RED = '\033[38;5;196m'
YELLOW = '\033[38;5;226m'
WHITE = '\033[38;5;255m'
BLUE = '\033[38;5;33m'
CYAN = '\033[38;5;51m'
GREEN = '\033[38;5;82m'
PURPLE = '\033[38;5;57m'
MAGENTA = '\033[38;5;163m'

# Formatting codes.
RESET = "\033[0;0m"
BOLD = "\033[;1m"
ITALIC = "\033[;3m"
END_ITALIC = "\033[;23m"
REVERSE = "\033[;7m"

# Variable to ensure the welcome message is printed once
# per session.
HAS_PRINTED = False

# ASCII art
illuminati = r'''
      /\      
     /  \     
    /,--.\    
   /< () >\   
  /  `--'  \  
 /          \ 
/------------\
'''
