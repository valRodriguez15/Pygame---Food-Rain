import pygame
import random
import config

# Setup
pygame.init()
screen = pygame.display.set_mode((config.screen_width, config.screen_height))
pygame.display.set_caption(config.title)
pygame.display.set_icon(config.icon)

running = True
game_over = False
score = 0

# title = config.presstart_font.render("FOOD RAIN", True, (255, 255, 255))

# Boy
boy_img = config.boy
boy_react = boy_img.get_rect()
boy_react.centerx = config.screen_width // 2
boy_react.bottom = config.screen_height - 10
boy_speed = 7

#Broccoli
broc_img = config.broc
broccolies = []
broc_speed = 6
spawn_delay = 120

# Store broccoli info
class Broccoli:
    def __init__(self, rect):
        self.rect = rect
        self.score = False

# Clock
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # screen.blit(title, (100, 300))
    screen.blit(config.bg1, (0, 0))

    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            boy_react.x -= boy_speed
        if keys[pygame.K_RIGHT]:
            boy_react.x += boy_speed
        
        # Move broccoli
        for broccoli in broccolies:
            broccoli.rect.y += broc_speed
            if broccoli.rect.colliderect(boy_react):
                game_over = True
            if broccoli.rect.y > boy_react.bottom and not broccoli.score:
                broccoli.score = True
                score += 1
        
        score_text = config.presstart_font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (config.screen_width // 2 + 30, config.screen_height - 620))
        
        # Spawn new broccoli
        if pygame.time.get_ticks() % spawn_delay == 0:
            broc_rect = broc_img.get_rect()
            broc_rect.x = random.randint(0, config.screen_width - broc_rect.width)
            broc_rect.y = -broc_rect.height
            broccolies.append(Broccoli(broc_rect))

        # Remove off screen broccolies
        broccolies = [broccoli for broccoli in broccolies if broccoli.rect.y < config.screen_height]

        screen.blit(boy_img, boy_react)
        for broccoli in broccolies:
            screen.blit(broc_img, broccoli.rect)
        
        pygame.display.flip()
        clock.tick(60)

    if game_over:
        game_over_text = config.presstart_font.render("Game over", True, (255, 255, 255))
        score_text = config.presstart_font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(game_over_text, (config.screen_width // 2 - 80, config.screen_height // 2 - 10))
        screen.blit(score_text, (config.screen_width // 2 - 50, config.screen_height // 2 + 18))
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False

pygame.quit()