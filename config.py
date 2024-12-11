import pygame

pygame.init()

#
title = "FOOD RAIN"
icon = pygame.image.load("assets/img/broccoli.png")

# Screen values
screen_width = 350
screen_height = 660

# Fonts
## Press start 2p
presstart_path = "assets/fonts/presstart.ttf"
presstart_size = 16
presstart_font = pygame.font.Font(presstart_path, presstart_size)

# Backgrounds
bg1_path = "assets/img/bg1.jpg"
bg1 = pygame.image.load(bg1_path)

# Objects
boy_path = "assets/img/boy.png"
boy_load = pygame.image.load(boy_path)
boy = pygame.transform.scale(boy_load, (90, 90))

broc_path = "assets/img/broccoli.png"
broc_load = pygame.image.load(broc_path)
broc = pygame.transform.scale(broc_load, (60, 60))