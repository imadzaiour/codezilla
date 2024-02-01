#import modules necessary for the game
import curses 
import random

#initiliaze the curses library to create our screen 
screen = curses.initscr()

#hide the mouse cursor
curses.curs_set(0)

#getmax screen height and width
screen_height, screen_width = screen.getmaxyx()

#create a new window 
window = curses.newwin(screen_height, screen_width, 0, 0)

#allow window to receive input from the keyboard 
window.keypad(1)

#set the delay for updating the screen 
window.timeout(100)

#set the x,y coordinates of the intial prosition of snake's head
snk_x = screen_width // 4
snk_y = screen_height // 2

#define the intial positions for the snake's body
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x - 1],
    [snk_y, snk_x - 2]
]
#set the coordinates of the food to be in the middle of the window
food = [screen_height // 2, screen_width // 2]

#add the food using PI character from curses module
window.addch(food[0], food[1], curses.ACS_PI)

#set intial movement direction to to be to the right
key = curses.KEY_RIGHT

#create the game loop that loops forever until the player either loses or quits

while True:

    #get the next key that will be pressed by user
    next_key = window.getch()

    #if user doesn't input anyting the key remains the same, otherwise the key will be set to the new pressed key
    key = key if next_key == -1 else next_key

    #check if the snake has collided with the walls or with itself
    if snake[0][0] in [0, screen_height] or snake[0][1] in [0, screen_width] or snake[0] in snake[1:]:
        curses.endwin()
        quit()

#set the new position of the snake's head based on the direction received from the user
    if key == curses.KEY_UP:
        snake.insert(0, [snake[0][0] - 1, snake[0][1]])
    if key == curses.KEY_DOWN:
        snake.insert(0, [snake[0][0] + 1,  snake[0][1]])
    if key == curses.KEY_LEFT:
        snake.insert(0, [snake[0][0], snake[0][1] - 1])
    if key == curses.KEY_RIGHT:
        snake.insert(0, [snake[0][0], snake[0][1] + 1])

#check if the snake has ate the food      
    if snake[0] == food:       
        #remove food if the snake ate it 
        food = None
        #while food is removed, generate new food in a random place on screen
        while food == None:
            new_food = [
            random.randint(1, screen_height-1),
            random.randint(1, screen_width-1)  
            ]
            #set the food to new food if new food generated is not in the snake's body and add it to screen
            food = new_food if new_food not in snake else None

        window.addch(food[0], food[1], curses.ACS_PI)
    #otherwise remove the last segment of the snake's body
    else:
        tail = snake.pop()
        window.addch(tail[0], tail[1], ' ')
    
    #draw the snake on the screen using ASCII characters
    window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
