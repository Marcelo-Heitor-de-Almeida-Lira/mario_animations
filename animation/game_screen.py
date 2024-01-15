import pygame
import spritesheet

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Spritesheets")

BG = (50, 50, 50)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

sprite_sheet_image = pygame.image.load('../spritesheets/mario_spritesheet.png').convert_alpha()
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)

animation_list = []
animation_list_back = []
animation_steps = 7
action = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 175
frame = 0

for i in range(7, 14, 1):
    animation_list.append(sprite_sheet.get_image(i, 26.5, 34, 3, BLACK, WHITE))

for i in range(6, -1, -1):
    animation_list_back.append(sprite_sheet.get_image(i, 26, 34, 3, BLACK, WHITE))

run = True
while run:

    screen.fill(BG)

    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(animation_list):
            frame = 0

    # temporário
    screen.blit(animation_list[frame], (0, 0))
    screen.blit(animation_list_back[frame], (100,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
