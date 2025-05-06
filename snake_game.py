import pygame # Use pygame to handle the game actions
import time
import random  # We will use random to place the food in different

# Pygame is a tool that helps you make games and other thing in programs using Python.
pygame.init()

# Colors
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
blue = (50, 153, 213)
green = (0, 255, 0)

# the size on the window while play the game.
dis_width = 600
dis_height = 400

# the Screen and also the sets what you see as the title at the top of the window.
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

# Snake settings
clock = pygame.time.Clock() # manages how fast the screen updates.
snake_block = 10            # is the size of one square of the snake
snake_speed = 10            # how fast the game runs

# Font settings and Sets up the text style for showing messages and scores.
font_style = pygame.font.SysFont(None, 25) # For Game Over and messages
score_font = pygame.font.SysFont(None, 25) # For score display

# This displays the score on the screen in the top-left corner. It updates every time based on how much food was eaten.
def Your_score(score):
    value = score_font.render("Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])


# the Loops through the points in snake_list to draw the snake.
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, yellow, [x[0], x[1], snake_block, snake_block])

# it displays a message, such as "Game Over," in the center of the screen.
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 3, dis_height / 3])

# This is the key part that makes the game work. It has a loop that keeps checking for events, moves the snake, looks for any crashes, and refreshes the screen.
def game_loop():
    global Your_score
    game_over = False
    game_close = False

    # the position of the snake
    x1 = dis_width / 2
    y1 = dis_height / 2

    # This part checks for arrow key presses and moves the snake everywhere.
    x1_change = 0
    y1_change = 0

    # Food is placed at a random location
    snake_List = []
    Length_of_snake = 1

    # Here, we check if the snake’s head touches the food. If so, a new food is generated and the snake grows.
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    #When the snake dies, the screen shows a red ‘Game Over’ message and the final score.
    while not game_over:

        while game_close == True:
            dis.fill(blue)
            # Display "Game Over" message
            message("Game Over! Press Q-Quit or P-Play Again", red)

            # Final Score Message
            final_score_text = score_font.render("Final Score: " + str(Length_of_snake - 1), True, yellow)
            dis.blit(final_score_text, [dis_width / 3, dis_height / 2])
            pygame.display.update()

           # This checks if the user quits or presses arrow keys to control the snake.
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        # This updates the snake's position based on key input.
        x1 += x1_change
        y1 += y1_change
         # Ends the game if the snake hits the wall.
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        # this clears the screen and redraws score, food, and snake.
        dis.fill(blue)
        Your_score(Length_of_snake - 1)

        # Draw food
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []

        # The snake grows by adding a new head and getting rid of its tail, unless it has just eaten, which makes it longer.
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # If the snake's head touches its body, the game ends.
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # Draw the snake
        our_snake(snake_block, snake_List)

        # Update the display
        pygame.display.update()

        # Checks if the snake eats the food and grows it by 1 block.
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)
     # the quits pygame and ends the program cleanly.
    pygame.quit()
    quit()


game_loop()
