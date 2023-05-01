import pygame

pygame.init()

# Window
window_width = 640
window_height = 480

window = pygame.display.set_mode((window_width, window_height))

# Game configuration
font = pygame.font.Font("super-legend-boy.otf", 36)

white = (255, 255, 255)
black = (0, 0, 0)
blue = (37, 140, 249)

score = 0

menu = True
selectedStart = True

# Quits the game
def exit_game():
    pygame.quit()
    quit()

# Checks for events
def check_event():
    global menu, selectedStart

    for event in pygame.event.get():
        if (menu and event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_s):
                menu = False
            elif (event.key == pygame.K_x):
                exit_game()
            elif (event.key == pygame.K_DOWN):
                selectedStart = False
            elif (event.key == pygame.K_UP):
                selectedStart = True

# Set background
def set_background(file):
    background = pygame.image.load(file)
    background = pygame.transform.scale(background, (window_width, window_height))
    window.blit(background, (0, 0))

# Create button
def create_button(text, font, width, height, hover=False):
    # Create button surface
    button_surface = pygame.Surface((width, height))
    button_surface.fill((255, 255, 255))

    # Draw border
    if (hover):
        border_rect = pygame.Rect(0, 0, width, height)
        pygame.draw.rect(button_surface, blue, border_rect, 4)

    # Render text
    text_surface = font.render(text, True, black)
    text_rect = text_surface.get_rect(center=(width//2, height//2))
    button_surface.blit(text_surface, text_rect)

    return button_surface

# Shows the menu
def show_menu():
    global selectedStart

    set_background("background.jpg")

    menu_font = pygame.font.Font('super-legend-boy.otf', 64)

    # Game title
    title_surface = menu_font.render("Pi Pong", True, white)
    title_rect = title_surface.get_rect(center=(window_width//2, 60))
    window.blit(title_surface, title_rect)

    # Hover effect
    if (selectedStart):
        start_button = create_button("START", font, 200, 60, True)
        quit_button = create_button("QUIT", font, 200, 60)
    else:
        start_button = create_button("START", font, 200, 60,)
        quit_button = create_button("QUIT", font, 200, 60, True)

    start_button_x = (window_width - 200) // 2
    start_button_y = (window_height - 120) // 2
    quit_button_x = start_button_x
    quit_button_y = start_button_y + 80

    window.blit(start_button, (start_button_x, start_button_y))
    window.blit(quit_button, (quit_button_x, quit_button_y))

    pygame.display.update()

# Draws a paddle
def draw_paddle(left=False, right=False):
    paddle_width = 15
    paddle_height = 60

    if left:
        paddle_x = 50
    elif right:
        paddle_x = window_width - 50 - paddle_width

    paddle_y = window_height // 2 - paddle_height // 2

    paddle_rect = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)
    pygame.draw.rect(window, white, paddle_rect)

# Shows the game
def show_game():
    window.fill(black)

    draw_paddle(left=True)
    draw_paddle(right=True)
    
    pygame.display.update()

while True:
    check_event()
    
    if menu:
        show_menu()
    else:
        show_game()
