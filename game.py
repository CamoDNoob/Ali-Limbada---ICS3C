import pygame, random, sys

from button import Button

def play():
    
    PLAY_BACK = Button(image=None, pos=(100, 50), text_input="BACK")

    while True:
        
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    SCREEN.fill("black")
                    

        
                 
        
        # game() logic goes here or call it to draw elements
        game()

        
        pygame.display.update()
        CLOCK.tick(60)
        pygame.display.update()  

def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the Options screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()



def main_menu  ():
    pygame.display.set_caption(" Menu ")

    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    game()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()


        pygame.display.update()

    main_menu()
def enemy1 (enemies,player):
        for enemy1 in enemies:
            if player.colliderect(enemy1):
                running = True
        return False
    
def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)



pygame.init()

# Create the game window
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