import pygame
import os
HEIGHT=500
WIDTH=850

screen=pygame.display.set_mode((WIDTH,HEIGHT))
BORDER=pygame.Rect(WIDTH//2-5,0,10,HEIGHT)
space=pygame.image.load("images/spaceblu.png")
space=pygame.transform.scale(space,(850,500))
yooreek=pygame.image.load("images/redp1.png")
y=pygame.Rect(100,300,55,40)
gaddzook=pygame.image.load("images/yellowp2.png")
g=pygame.Rect(700,300,55,40)
playing=True
clock=pygame.time.Clock()
while playing==True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            playing=False
            pygame.quit()
    screen.blit(space,(0,0))
    pygame.display.update()   