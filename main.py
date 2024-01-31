import pygame

pygame.init()

'''РАЗМЕР ЭКРАНА И ЕГО ФОН'''
#Размер Экрана
screen = pygame.display.set_mode((800,375))
#Название Игры
pygame.display.set_caption("Infinite Summer")
#Картинка Игры
game_icon = pygame.image.load('C:\gameguy\gameicon.png')
pygame.display.set_icon(game_icon)

#Штука для ФПС
clock = pygame.time.Clock()

#Фоновая музыка игры
pygame.mixer.music.load("C:\gameguy\guy\song1.mp3")
#Фоновая катринка
ground = pygame.image.load('C:\gameguy\ground.jpg')
pygame.mixer.music.play(-1)


while True:
    #Вывод картинки
    screen.blit(ground,(0,0))
    #Обновленее Экрана
    pygame.display.update()
    #Цикл для того чтобы коректно открывалось окно
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
