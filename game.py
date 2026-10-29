import pygame, random

pygame.init()

# Create the game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Moving Square")

# Set up our colours
SKY_BLUE = (135, 206, 235)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 128, 0)
# Store the player's and enemy's starting position
player_x = 375
player_y = 275
enemy1_x = 100
enemy1_y = 200
enemy2_x = 500
enemy2_y = 400



bomb_active = False
bomb_x = player_x
bomb_y = player_y
bomb_speed = 6  


bomb_dx = 0
bomb_dy = 0
#Track kills
kill_count = 0

#Draw the bullet on top of the player
bullet_x = player_x
bullet_y = player_y
bullet_speed = 6  # Increased speed so it doesn't move at a crawl
bullet_active = False

# NEW: the bullet's own direction (locked in when fired)
bullet_dx = 0
bullet_dy = 0

# NEW: remembers which way the player last moved
facing_x = 0
facing_y = -1  # player starts facing up

# Control how many pixels the square moves each frame
speed = 3
enemy1_speed = 1
enemy2_speed = 0.5

# Keep the game running
running = True

# Add a clock to regulate frame rate (prevents the game from running too fast)
clock = pygame.time.Clock()

while running:

    # Check for events, including closing the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check which keyboard keys are being pressed
    keys = pygame.key.get_pressed()

    # NEW: update the facing direction (True counts as 1, False as 0)
    dx = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
    dy = keys[pygame.K_DOWN] - keys[pygame.K_UP]
    if dx != 0 or dy != 0:  # only update when the player is actually moving
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
    
          

    # 1. HANDLE INPUT (Only handles the initial trigger)
    if keys[pygame.K_SPACE]:
        if not bullet_active:
            # Reset bullet position to the player's position when fired
            bullet_x = player_x + 17  # roughly centres the bullet on the player
            bullet_y = player_y + 17
            # NEW: lock in the direction the player is facing
            bullet_dx = facing_x * bullet_speed
            bullet_dy = facing_y * bullet_speed
            bullet_active = True

    # 2. UPDATE BULLET POSITION
    if bullet_active:
        # NEW: keep moving in the direction chosen when fired
        bullet_x += bullet_dx
        bullet_y += bullet_dy

        # Check boundaries (If it goes off-screen, deactivate it)
        if bullet_x >= 800 or bullet_y >= 600 or bullet_y <= 0 or bullet_x <= 0:
            bullet_active = False


    screen.fill(SKY_BLUE)

    # Now draw the bullet if it's active
    if bullet_active:
        pygame.draw.rect(screen, BLUE, (bullet_x, bullet_y, 15, 15))  # Small 15x15 bullet

    # 1. Create rectangle objects for both the player and the enemy
    player_rect = pygame.Rect(player_x, player_y, 50, 50)
    enemy_rect = pygame.Rect(enemy1_x, enemy1_y, 30, 30)
    enemy_rect_two = pygame.Rect(enemy2_x, enemy2_y, 30, 30)
    bullet_rect = pygame.Rect(bullet_x, bullet_y, 15, 15)
    bomb_rect = pygame.Rect(bomb_x, bomb_y, 40, 40)
    # 2. Check if the rectangles overlap (collision)
    if player_rect.colliderect(enemy_rect):
        running = False  # Ends the game loop
    if player_rect.colliderect(enemy_rect_two):
        running = False
    # NEW: only count a hit if the bullet is active, and remove it on impact
    if bullet_active and bullet_rect.colliderect(enemy_rect):
        kill_count += 1
        enemy1_x = random.randint(0,800)
        enemy1_y = random.randint(0,600)
        bullet_active = False
    if bullet_active and bullet_rect.colliderect(enemy_rect_two):
        kill_count += 1
        enemy2_x = random.randint(0,800)
        enemy2_y = random.randint(0,800)
        bullet_active = False
    if bomb_active and bomb_rect.colliderect(enemy_rect):
        kill_count += 1
        enemy1_x = random.randint(0,800)
        enemy1_y = random.randint(0,600)
        bomb_active = False
    if bomb_active and bomb_rect.colliderect(enemy_rect_two):
        kill_count += 1
        enemy2_x = random.randint(0,800)
        enemy2_y = random.randint(0,800)
        bomb_active = False
    # Draw the player and enemy on top of the background
    pygame.draw.rect(screen, BLUE, (player_x, player_y, 50, 50))
    pygame.draw.rect(screen, RED, (enemy1_x, enemy1_y, 30, 30))
    pygame.draw.rect(screen, GREEN, (enemy2_x, enemy2_y, 30, 30))

   
    font = pygame.font.SysFont(None,25)
    kill_count_text = font.render(f"Kills: {kill_count}", True, (0,0,0))
    screen.blit(kill_count_text,(10,10))

    if kill_count == 2:
        if keys[pygame.K_e]:
            if not bomb_active:
                            # Reset bullet position to the player's position when fired
                bomb_x = player_x + 17  # roughly centres the bullet on the player
                bomb_y = player_y + 17
                    # NEW: lock in the direction the player is facing
                bomb_dx = facing_y * bullet_speed
                bomb_dy = facing_x * bullet_speed
                bomb_active = True
        if bomb_active:
            pygame.draw.rect(screen, BLUE, (bullet_x, bullet_y, 40, 40))  # Bomb drawing    
            bomb_x += bomb_dx
            bomb_y += bomb_dy
       
    pygame.display.flip()

    # Cap the game at 60 frames per second
    clock.tick(60)

pygame.quit()