import pygame

pygame.init()

screen = pygame.display.set_mode((800,375))
pygame.display.set_caption("Game")
game_icon = pygame.image.load('C:\gameguy\gameicon.png')
pygame.display.set_icon(game_icon)
clock = pygame.time.Clock()
pygame.mixer.music.load("C:\gameguy\guy\song1.mp3")
pygame.mixer.music.play(-1)



ground = pygame.image.load('C:\gameguy\ground.jpg')
while True:
    screen.blit(ground,(0,0))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()