import pygame, os
from paddle import Paddle
from ball import Ball

pygame.init()

# Joysticks

pygame.joystick.init()

joystick1 = pygame.joystick.Joystick(0)
joystick2 = pygame.joystick.Joystick(1)

joystick1.init()
joystick2.init()

# Disable mouse
pygame.mouse.set_visible(False)

# Current execution location
def get_current_location():
    location = os.path.dirname(os.path.abspath(__file__))
    return location + "/"

current_location = get_current_location()

# Window
window_width = 1440
window_height = 900

window = pygame.display.set_mode((window_width, window_height))

# Frames Per Second
clock = pygame.time.Clock()
FPS = 60

# Game configuration
font = pygame.font.Font(current_location + "super-legend-boy.otf", 36)

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
hover_blue = (37, 140, 249)

# Settings
menu = True
selectedStart = True

# Objects

paddle1 = Paddle(window_width, window_height, 50, window_height // 2 - 50, 20, 100, 10, blue)
paddle2 = Paddle(window_width, window_height, window_width - 70, window_height // 2 - 50, 20, 100, 10, red)
ball = Ball(window_width, window_height, window_width // 2, window_height // 2, 10, white)

# Player controls

player1 = {
    pygame.K_UP: False,
    pygame.K_DOWN: False
}

player2 = {
    pygame.K_UP: False,
    pygame.K_DOWN: False
}


# Checks for events
def check_event():
    global menu, selectedStart, player1, player2

    # Joysticks         
    pygame.event.get()

    axis1 = joystick1.get_axis(1)
    select1 = joystick1.get_button(0) + joystick1.get_button(1) + joystick1.get_button(2) + joystick1.get_button(3) + joystick1.get_button(4) + joystick1.get_button(5) + joystick1.get_button(6) + joystick1.get_button(7) + joystick1.get_button(8)
    quit1 = joystick1.get_button(2) * joystick1.get_button(3)

    axis2 = joystick2.get_axis(1)
    select2 = joystick2.get_button(0) + joystick2.get_button(1) + joystick2.get_button(2) + joystick2.get_button(3) + joystick2.get_button(4) + joystick2.get_button(5) + joystick2.get_button(6) + joystick2.get_button(7) + joystick2.get_button(8)
    quit2 = joystick2.get_button(2) * joystick2.get_button(3)


    if (menu):
        if (axis1 > 0.8 or axis2 > 0.8):
            selectedStart = True
        elif (axis1 < -0.8 or axis2 < -0.8):
            selectedStart = False
    
        if (select1 >= 1 or select2 >= 1):
            if (selectedStart):
                menu = False
            elif (not selectedStart):
                exit_game()
    elif (not menu):
        if (axis1 > 0.8):
            player1[pygame.K_UP] = True
        elif (axis1 < -0.8):
            player1[pygame.K_DOWN] = True
        else:
            player1[pygame.K_UP] = False
            player1[pygame.K_DOWN] = False

        if (axis2 > 0.8):
            player2[pygame.K_UP] = True
        elif (axis2 < -0.8):
            player2[pygame.K_DOWN] = True
        else:
            player2[pygame.K_UP] = False
            player2[pygame.K_DOWN] = False
        
    if (quit1 == 1 or quit2 == 1):
        exit_game()


# Quits the game
def exit_game():
    pygame.quit()
    quit()


# Set background
def set_background(file):
    background = pygame.image.load(file)
    window.blit(background, (0, 0))


# Create button
def create_button(text, font, width, height, hover=False):
    # Create button surface
    button_surface = pygame.Surface((width, height))
    button_surface.fill((255, 255, 255))

    # Draw border
    if (hover):
        border_rect = pygame.Rect(0, 0, width, height)
        pygame.draw.rect(button_surface, hover_blue, border_rect, 5)

    # Render text
    text_surface = font.render(text, True, black)
    text_rect = text_surface.get_rect(center=(width//2, height//2))
    button_surface.blit(text_surface, text_rect)

    return button_surface

# Handling collision
def handle_collision():
    pass

# Shows the menu
def show_menu():
    set_background(current_location + "background.jpg")

    title_font = pygame.font.Font(current_location + "super-legend-boy.otf", 64)

    # Game title
    title_surface = title_font.render("Pi Pong", True, white)
    title_rect = title_surface.get_rect(center=(window_width//2, 60))
    window.blit(title_surface, title_rect)

    # Hover effect
    if (selectedStart):
        start_button = create_button("START", font, 200, 60, True)
        quit_button = create_button("QUIT", font, 200, 60, False)
    else:
        start_button = create_button("START", font, 200, 60, False)
        quit_button = create_button("QUIT", font, 200, 60, True)

    start_button_x = (window_width - 200) // 2
    start_button_y = (window_height - 120) // 2
    quit_button_x = start_button_x
    quit_button_y = start_button_y + 80

    window.blit(start_button, (start_button_x, start_button_y))
    window.blit(quit_button, (quit_button_x, quit_button_y))

    pygame.display.update()

# Shows the game
def show_game():
    window.fill(black)

    if (player1[pygame.K_UP]):
        paddle1.move_up()
    elif (player1[pygame.K_DOWN]):
        paddle1.move_down()
    
    if (player2[pygame.K_UP]):
        paddle2.move_up()
    elif (player2[pygame.K_DOWN]):
        paddle2.move_down()

    paddle1.draw(window)
    paddle2.draw(window)

    if (ball.rect.colliderect(paddle1.rect)) or (ball.rect.colliderect(paddle2.rect)):
        ball.x_vel *= -1                     

    ball.move()
    ball.draw(window)
    
    pygame.display.update()

# Game loop
while True:
    clock.tick(FPS)

    check_event()
    
    if menu:
        show_menu()
    else:
        show_game()