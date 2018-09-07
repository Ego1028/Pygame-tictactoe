import pygame
import time
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((700,800))
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white=(255,255,255)
black=(0,0,0)

def play():
    screen.fill((0,0,0))
    XO='X'
    over=False
    total=0
    count=1
    rect1=pygame.draw.rect(screen,white,(100,125,100,100),5)
    rect2=pygame.draw.rect(screen,white,(200,125,100,100),5)
    rect3=pygame.draw.rect(screen,white,(300,125,100,100),5)
    rect4=pygame.draw.rect(screen,white,(100,225,100,100),5)
    rect5=pygame.draw.rect(screen,white,(200,225,100,100),5)
    rect6=pygame.draw.rect(screen,white,(300,225,100,100),5)
    rect7=pygame.draw.rect(screen,white,(100,325,100,100),5)
    rect8=pygame.draw.rect(screen,white,(200,325,100,100),5)
    rect9=pygame.draw.rect(screen,white,(300,325,100,100),5)
    rects=[rect1,rect2,rect3,rect4,rect5,rect6,rect7,rect8,rect9]
    mark1=''
    mark2=''
    mark3=''
    mark4=''
    mark5=''
    mark6=''
    mark7=''
    mark8=''
    mark9=''
    marks=[mark1,mark2,mark3,mark4,mark5,mark6,mark7,mark8,mark9]
    while over==False:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                print("QUITTING")
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for i in range(len(rects)):
                    x,y=event.pos
                    if rects[i].collidepoint(x,y):
                        print("you clicked rectangle number",i+1)
                        if XO=='X':
                            XO='O'
                        else:
                            XO='X'
                        
                        show_text(XO,(rects[i].left+rects[i].right)/2,(rects[i].top+rects[i].bottom)/2,white)
                        pygame.display.update()
                        marks[i]=XO
                        total+=1
                        if marks[0]==marks[3]==marks[6]!='':
                            who=marks[0]
                            over=True
                        elif marks[0]==marks[1]==marks[2]!='':
                            who=marks[0]
                            over=True
                        elif marks[2]==marks[5]==marks[8]!='':
                            who=marks[2]
                            over=True
                        elif marks[6]==marks[7]==marks[8]!='':
                            who=marks[6]
                            over=True
                        elif marks[0]==marks[4]==marks[8]!='':
                            who=marks[0]
                            over=True
                        elif marks[2]==marks[4]==marks[6]!='':
                            who=marks[2]
                            over=True
                        elif marks[1]==marks[4]==marks[7]!='':
                            who=marks[1]
                            over=True
                        elif marks[2]==marks[5]==marks[8]!='':
                            who=marks[2]
                            over=True
                        elif marks[3]==marks[4]==marks[5]!='':
                            who=marks[3]
                            over=True
                        elif total==9:
                            over=True
                            print("Draw")
                            show_text("Draw",300,50,green)
                            pygame.display.update()
                            time.sleep(3)
                            screen.fill((0,0,0))
                            menu()
                        if over==True and total!=9:
                            print(who + " wins")
                            show_text(who + " wins",300,50,green)
                            pygame.display.update()
                            time.sleep(3)
                            screen.fill((0,0,0))
                            menu()
                        
def menu():
    pygame.display.set_caption("Tic Tac Toe-Menu")
    playRect=pygame.draw.rect(screen,blue, (200,650,80,60),5)
    quitRect=pygame.draw.rect(screen,green, (400,650,80,60),5)
    show_text("Play",200,650,red)
    show_text("Quit",400,650,red)
    show_text("Tic Tac Toe",100,150,white)
    show_text("By Ruolin",280,150,white)
    while True:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x,y=event.pos
                if quitRect.collidepoint(x,y):
                    print("Quit")
                    pygame.quit()
                    exit()
                elif playRect.collidepoint(x,y):
                    print("play")
                    play()
                

def show_text(msg,x,y,color):
    fontobj = pygame.font.SysFont("freesans",32)
    msgobj = fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))

menu()
    
