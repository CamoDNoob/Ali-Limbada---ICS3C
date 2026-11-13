import pygame, random, sys, os

from button import Button

def draw_button(rect, text, mouse_pos, font_size=50):
    """Draw a simple button and return its rectangle."""
    if rect.collidepoint(mouse_pos):
        text_colour = "White"
    else:
        text_colour = "#d7fcd4"

    pygame.draw.rect(SCREEN, "#b68f40", rect, border_radius=10)
    button_text = get_font(font_size).render(text, True, text_colour)
    button_text_rect = button_text.get_rect(center=rect.center)
    SCREEN.blit(button_text, button_text_rect)


def options():
    back_rect = pygame.Rect(250, 420, 300, 80)

    while True:
        mouse_pos = pygame.mouse.get_pos()
        SCREEN.fill("white")

        options_text = get_font(45).render("This is the Options screen.", True, "Black")
        options_rect = options_text.get_rect(center=(400, 260))
        SCREEN.blit(options_text, options_rect)

        draw_button(back_rect, "BACK", mouse_pos, 55)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if back_rect.collidepoint(event.pos):
                    return

        pygame.display.update()
        CLOCK.tick(60)


def main_menu():
    pygame.display.set_caption("Menu")

    play_rect = pygame.Rect(200, 180, 400, 80)
    options_rect = pygame.Rect(200, 290, 400, 80)
    quit_rect = pygame.Rect(200, 400, 400, 80)

    while True:
        SCREEN.blit(BG, (0, 0))
        mouse_pos = pygame.mouse.get_pos()

        menu_text = get_font(100).render("MAIN MENU", True, "#b68f40")
        menu_rect = menu_text.get_rect(center=(400, 90))
        SCREEN.blit(menu_text, menu_rect)

        draw_button(play_rect, "PLAY", mouse_pos, 65)
        draw_button(options_rect, "OPTIONS", mouse_pos, 65)
        draw_button(quit_rect, "QUIT", mouse_pos, 65)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if play_rect.collidepoint(event.pos):
                    game()
                elif options_rect.collidepoint(event.pos):
                    options()
                elif quit_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        CLOCK.tick(60)


def enemy1 (enemies,player):
        for enemy1 in enemies:
            if player.colliderect(enemy1):
                running = True
        return False
    
def get_font(size): # Uses the custom font if available, otherwise a system font
    font_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "font.ttf")

    if os.path.exists(font_path):
        return pygame.font.Font(font_path, size)
    else:
        return pygame.font.SysFont("Arial", size) 






    



pygame.init()
def game():

    # Track kills
    kill_count = 0

    # Draw the bullet on top of the player
    bullet_x = player_x
    bullet_y = player_y
    bullet_speed = 6  
    bullet_active = False

    # The bullet's own direction
    bullet_dx = 0
    bullet_dy = 0

    # Remembers which way the player last moved
    facing_x = 0
    facing_y = -1  # player starts facing up

    # Control how many pixels the square moves each frame
    speed = 3
    enemy1_speed = 1
    enemy2_speed = 1.5
    enemy3_speed = 1

    enemies = []
    # Keep the game running
    running = True

    # Add a clock to regulate frame rate
    clock = pygame.time.Clock()

    while running:

        # Check for events, including closing the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Check which keyboard keys are being pressed
        keys = pygame.key.get_pressed()

        # Update the facing direction
        dx = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
        dy = keys[pygame.K_DOWN] - keys[pygame.K_UP]
        if dx != 0 or dy != 0:  
            facing_x = dx
            facing_y = dy

        # Move left by decreasing the X position
        if keys[pygame.K_LEFT]:
            player_x = player_x - speed

        # Move right by increasing the X position
        if keys[pygame.K_RIGHT]:
            player_x = player_x + speed

        # Move up by decreasing the Y position
        if keys[pygame.K_UP]:
            player_y = player_y - speed

        # Move down by increasing the Y position
        if keys[pygame.K_DOWN]:
            player_y = player_y + speed

        # Move the enemy toward the player
        if enemy1_x < player_x:
            enemy1_x += enemy1_speed
        elif enemy1_x > player_x:
            enemy1_x -= enemy1_speed
        if enemy1_y < player_y:
            enemy1_y += enemy1_speed
        elif enemy1_y > player_y:
            enemy1_y -= enemy1_speed

        if enemy2_x < player_x:
            enemy2_x += enemy2_speed
        elif enemy2_x > player_x:
            enemy2_x -= enemy2_speed
        if enemy2_y < player_y:
            enemy2_y += enemy2_speed
        elif enemy2_y > player_y:
            enemy2_y -= enemy2_speed

        if enemy3_x < player_x:
            enemy3_x += enemy3_speed
        elif enemy3_x > player_x:
            enemy3_x -= enemy3_speed
        if enemy3_y < player_y:
            enemy3_y += enemy3_speed
        elif enemy3_y > player_y:
            enemy3_y -= enemy3_speed
        
        # 1. HANDLE BULLET INPUT
        if keys[pygame.K_SPACE]:
            if not bullet_active:
                bullet_x = player_x + 17  
                bullet_y = player_y + 17
                bullet_dx = facing_x * bullet_speed
                bullet_dy = facing_y * bullet_speed
                bullet_active = True

        # 2. UPDATE BULLET POSITION
        if bullet_active:
            bullet_x += bullet_dx
            bullet_y += bullet_dy

            if bullet_x >= 800 or bullet_y >= 600 or bullet_y <= 0 or bullet_x <= 0:
                bullet_active = False

        # 3. HANDLE BOMB INPUT (Available when kill_count is 2 or more)
        if kill_count >= 10:
            if keys[pygame.K_e] and not bomb_active:
                bomb_x = player_x + 5  # centers the 40x40 bomb roughly on the player
                bomb_y = player_y + 5
                bomb_dx = facing_x * bomb_speed
                bomb_dy = facing_y * bomb_speed
                bomb_active = True


        

        

        # 4. UPDATE BOMB POSITION
        if bomb_active:
            bomb_x += bomb_dx
            bomb_y += bomb_dy

            # Deactivate bomb if it goes off-screen
            if bomb_x >= 800 or bomb_y >= 600 or bomb_y <= 0 or bomb_x <= 0:
                bomb_active = False

        screen.fill(SKY_BLUE)

        # Draw the bullet if it's active
        if bullet_active:
            pygame.draw.rect(screen, BLUE, (bullet_x, bullet_y, 15, 15))

        # Draw the bomb if it's active
        if bomb_active:
            pygame.draw.rect(screen, GREY, (bomb_x, bomb_y, 40, 40))

        # Create rectangle objects for collisions
        player_rect = pygame.Rect(player_x, player_y, 50, 50)
        enemy_rect_one = pygame.Rect(enemy1_x, enemy1_y, 40, 40)
        enemy_rect_two = pygame.Rect(enemy2_x, enemy2_y, 30, 30)
        enemy_rect_three = pygame.Rect(enemy3_x, enemy3_y, 40, 40)
        bullet_rect = pygame.Rect(bullet_x, bullet_y, 15, 15)
        bomb_rect = pygame.Rect(bomb_x, bomb_y, 40, 40)
        if enemy_rect_one in enemies == False:
            enemies.append(enemy_rect_one)
        if enemy_rect_two in enemies == False:
            enemies.append(enemy_rect_two)




        # Check if the player collides with enemies
        if player_rect.colliderect(enemy_rect_one) or player_rect.colliderect(enemy_rect_two) or player_rect.colliderect(enemy_rect_three):
            running = False  

        # Bullet collisions
        if bullet_active and bullet_rect.colliderect(enemy_rect_one):
            kill_count += 1
            enemy1_x = random.randint(795, 800)
            enemy1_y = random.randint(0, 600)
            bullet_active = False
        if bullet_active and bullet_rect.colliderect(enemy_rect_two):
            kill_count += 1
            enemy2_x = random.randint(0, 2)
            enemy2_y = random.randint(0, 800)
            bullet_active = False
        if bullet_active and bullet_rect.colliderect(enemy_rect_three):
            kill_count += 1
            enemy3_x = random.randint(0, 800)
            enemy3_y = random.randint(600,600)
            bullet_active = False
        # Bomb collisions
        if bomb_active and bomb_rect.colliderect(enemy_rect_one):
            kill_count += 1
            enemy1_x = random.randint(795, 800)
            enemy1_y = random.randint(0, 600)
        if bomb_active and bomb_rect.colliderect(enemy_rect_two):
            kill_count += 1
            enemy2_x = random.randint(0, 2)
            enemy2_y = random.randint(0, 800)
        if bomb_active and bomb_rect.colliderect(enemy_rect_three):
            kill_count += 1
            enemy3_x = random.randint(0, 800)
            enemy3_y = random.randint (600, 600)

        if enemy1(enemies,player_rect) == True:
            quit()





        if kill_count >= 2:
            pygame.draw.rect(screen, RED, (enemy3_x, enemy3_y, 40, 40))


            



        

        # Draw the player and enemies
        pygame.draw.rect(screen, BLUE, (player_x, player_y, 50, 50))
        pygame.draw.rect(screen, RED, (enemy1_x, enemy1_y, 40, 40))
        pygame.draw.rect(screen, GREEN, (enemy2_x, enemy2_y, 30, 30))

        # Render kill count text
        font = pygame.font.SysFont(None, 25)
        kill_count_text = font.render(f"Kills: {kill_count}", True, (0, 0, 0))
        screen.blit(kill_count_text, (10, 10))

        pygame.display.flip()

        # Cap the game at 60 frames per second
        clock.tick(60)

    pygame.quit()








SCREEN = pygame.display.set_mode((800, 600))
CLOCK = pygame.time.Clock()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BG = pygame.image.load("Background.png").convert()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Moving Square")

# Set up our colours
SKY_BLUE = (135, 206, 235)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 128, 0)
GREY = (169,169,169)
BLACK = (0, 0, 0)
# Store the player's and enemy's starting position
player_x = 375
player_y = 275
enemy1_x = 100
enemy1_y = 200
enemy2_x = 500
enemy2_y = 400
enemy3_x = 400
enemy3_y = 600
# Bomb variables
bomb_active = False
bomb_x = player_x
bomb_y = player_y
bomb_speed = 4 # Set to a low number so it moves very slowly
bomb_dx = 0
bomb_dy = 0















