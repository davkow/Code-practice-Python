
# Automate the boring stuff. Chapter 3 - Functions

import time, sys
indent = 0 # How many spaces to indent.
indentIncreasing = True # Whether the indentation is increasing or not.

try:
    while True: # The main program loop.
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) # Pause for 1/10 of a second.

        if indentIncreasing:
            # Increase the number of spaces:
            indent = indent + 1
            if indent == 20:
                # Change direction:
                indentIncreasing = False

        else:
            # Decrease the number of spaces:
            indent = indent - 1
            if indent == 0:
                # Change direction:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()

# If the user presses CTRL-C at any point that the program execution is in the try block, 
# the KeyboardInterrrupt exception is raised and handled by this except statement. 
# The program execution moves inside the except block, which runs sys.exit() and quits the program. 
# This way, even though the main program loop is an infinite loop, the user has a way to shut down the program.   