import pygame, random, sys, os



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
