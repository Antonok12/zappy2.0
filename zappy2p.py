import pygame
import os
HEIGHT=500
WIDTH=850

yrbulltet=[]
gdbullet=[]
HEALTH_FONT=pygame.font.SysFont("comicsans",40)
yrhealth=10
gdhealth=10
screen=pygame.display.set_mode((WIDTH,HEIGHT))
BORDER=pygame.Rect(WIDTH//2-5,0,10,HEIGHT)
space=pygame.image.load("images/spaceblu.png")
space=pygame.transform.scale(space,(850,500))
yooreek=pygame.image.load("images/babyyooreeksosmall.png")
yr=pygame.Rect(100,300,55,40)
gaddzook=pygame.image.load("images/gaddzooks.png")
g=pygame.Rect(700,300,55,40)
playing=True
clock=pygame.time.Clock()

def yooreek_handle_movement(keys_pressed,yr):
    if keys_pressed[pygame.K_a] and yr.x>0:
        yr.x-=4 
    if keys_pressed[pygame.K_d] and yr.x<BORDER.x-30:
        yr.x+=4
    if keys_pressed[pygame.K_w] and yr.y>0:
        yr.y-=4
    if keys_pressed[pygame.K_s] and yr.y<450:
        yr.y+=4

def gaddzooks_handle_movement(keys_pressed,g):
    if keys_pressed[pygame.K_LEFT] and g.x>BORDER.x:
        g.x-=4
    if keys_pressed[pygame.K_RIGHT] and g.x<800:
        g.x+=4
    if keys_pressed[pygame.K_UP] and g.y>0:
        g.y-=4
    if keys_pressed[pygame.K_DOWN] and g.y<450:
        g.y+=4

def handle_bullets(yrbulltet,gbullet,yr,g):
    for bullet in yrbulltet:
        bullet.x+=5
        if g.colliderect(bullet):
            yrbulltet.remove(bullet)
            gdhealth-=1
    for bullet in gbullet:
        bullet.x-=5
        if yr.colliderect(bullet):
            gdbullet.remove(bullet)
            yrhealth-=1

while playing==True:

    clock.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            playing=False
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_e:
                bullet=pygame.Rect(yr.x,yr.y+22,10,5)
                yrbulltet.append(bullet)
            if event.key==pygame.K_SPACE:
                bullet=pygame.Rect(g.x,g.y+20,10,6)
                gdbullet.append(bullet)


    screen.blit(space,(0,0))
    screen.blit(yooreek,(yr.x,yr.y))
    screen.blit(gaddzook,(g.x,g.y))
    pygame.draw.rect(screen,"orange",BORDER)
    keys_pressed=pygame.key.get_pressed()
    yooreek_handle_movement(keys_pressed,yr)
    gaddzooks_handle_movement(keys_pressed,g)
    handle_bullets(yrbulltet, gdbullet,yr,g)
    for bullet in yrbulltet:
        pygame.draw.rect(screen,"darkseagreen1",bullet)
    for bullet in gdbullet:
        pygame.draw.rect(screen,"mediumpurple1",bullet)
    yrhealth_txt=HEALTH_FONT.render("YOOREEK HEALTH:"+str(yrhealth),True,"darkseagreen1")
    gdhealth_txt=HEALTH_FONT.render("GADZOOK HEALTH:"+str(gdhealth),True,"mediumpurple1")
    pygame.display.update()   
