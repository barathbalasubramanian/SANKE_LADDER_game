import pygame
import random
import time
pygame.init()

# backgroung img
background_img = pygame.image.load("snakeladder 1.png")

#creating screen
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("SNAKE LADDER")
pygame.display.set_icon(background_img)
    
# creating background

background_x = 50
background_y = 50
def background(x,y) :
    screen.blit(background_img,(x,y))
print(background_img.get_height())
print(background_img.get_width())
 

# player
player_img = pygame.image.load("bullet.png")
player_x = 35
player_y = 554
player_change_x = 0
player_change_y = 0
def player1(x,y) :
    screen.blit(player_img,(x,y))
player_img = pygame.image.load("bullet.png")
player_x2 = 55
player_y2 = 554
player_change_x2 = 0
player_change_y2 = 0
def player2(x,y) :
    screen.blit(player_img,(x,y))
# font 
font = pygame.font.Font("freesansbold.ttf",32)
show_x = 600
show_y = 100
value = 0
def show(x,y) :
    show = font.render(" ITS : " + str(value) , True , (255,0, 0))
    screen.blit(show,(x,y))
    
font_won = pygame.font.Font("freesansbold.ttf",32)
def won () :
    show_won = font_won.render(" YOU WON THE WIN ", True ,(255,0,0))
    screen.blit(show_won,(150,660))
    
    
    


play1 = True
play2 = True
game = "waiting"
game2 = "waiting"
game_started = "waiting"
game_started2 =  "waiting"

running = True
while running :
    
    screen.fill((0,0,0))
    background(background_x,background_y)    
    for event in pygame.event.get():
        choice_pos = [0,1,2,3,4,5,6]
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_SPACE :
                value = random.choice(choice_pos)
                time.sleep(1)
        
                if play1 :  
                    if value == 0 :
                        game = "start"
                        game_started = "started"
                        play1 = False
                    
                if game_started == "started" :
                    for i in range(1,value+1) :
                        
                        if player_y == 510 or player_y == 410 or player_y == 310 or player_y == 210 or player_y == 110 :
                            player_change_x = 1*50
                            player_x += player_change_x
                        
                        if player_y == 460 or player_y == 360 or player_y == 260 or player_y == 160 or player_y == 60 :
                            player_change_x  = 1*(-50)
                            player_x += player_change_x
                        
                        if player_y < 480 :       
                            if player_x == 10 :
                                player_y -= 50
                                player_x = 60
                                
                        if player_x == 560 :
                            player_y -= 50
                            player_x = 510
            
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_s :
                value = random.choice(choice_pos)
                time.sleep(1)
                
                if play2 :  
                    if value == 0 :
                        game2 = "start"
                        game_started2 = "started"
                        play2 = False
                 
                if game_started2 == "started" :
                    for i in range(1,value+1) :
                        
                        if player_y2 == 510 or player_y2 == 410 or player_y2 == 310 or player_y2 == 210 or player_y2 == 110 :
                            player_change_x2 = 1*50
                            player_x2 += player_change_x2
                        
                        if player_y2 == 460 or player_y2 == 360 or player_y2 == 260 or player_y2 == 160 or player_y2 == 60 :
                            player_change_x2  = 1*(-50)
                            player_x2 += player_change_x2
                        
                        if player_y2 < 480 :       
                            if player_x2 == 10 :
                                player_y2 -= 50
                                player_x2 = 60
                                
                        if player_x2 == 560 :
                            player_y2 -= 50
                            player_x2 = 510    
                
    if game == "start" :
        player_x = 10
        player_y = 510
        game = "waiting"
    if game2 == "start" :
        player_x2 = 10
        player_y2 = 510
        game2 = "waiting"
    # ladder position changing     
             
    if player_x == 60  and player_y == 510 :
        player_x = 160
        player_y = 360 
    if player_x == 210 and player_y == 510 :
        player_x = 360
        player_y = 460
    if player_x == 460 and player_y == 510 :
        player_x = 510
        player_y = 360
    if player_x == 60  and player_y == 410 :
        player_x = 110
        player_y = 410
    if player_x == 410  and player_y == 410 :
        player_x = 210
        player_y = 110
    if player_x == 510 and player_y == 260 :
        player_x = 360
        player_y = 210
    if player_x == 460  and player_y == 160 :
        player_x = 510
        player_y = 60
    if player_x == 60 and player_y == 160 :
        player_x = 110
        player_y = 60
    
    # sanke bitting changes
    
    if player_x == 210 and player_y == 460 :
        player_x = 360
        player_y = 510    
    if player_x == 110 and player_y == 210 :
        player_x = 110
        player_y = 460 
    if player_x == 360 and player_y == 260 :
        player_x = 360
        player_y = 360
    if player_x == 210 and player_y == 210 :
        player_x = 60
        player_y = 260  
    if player_x == 360 and player_y == 110 :
        player_x = 260
        player_y = 360
    if player_x == 410 and player_y == 60 :
        player_x = 410
        player_y = 160
    if player_x == 310 and player_y == 60 :
        player_x = 310
        player_y = 160
    if player_x == 160 and player_y == 60 :
        player_x = 110
        player_y = 160
        
    if player_x == 60 and player_y == 60 :
        won()
    # player 2 
    
    if player_x2 == 60  and player_y2 == 510 :
        player_x2 = 160
        player_y2 = 360 
    if player_x2 == 210 and player_y2 == 510 :
        player_x2 = 360
        player_y2 = 460
    if player_x2 == 460 and player_y2 == 510 :
        player_x2 = 510
        player_y2 = 360
    if player_x2 == 60  and player_y2 == 410 :
        player_x2 = 110
        player_y2 = 410
    if player_x2 == 410  and player_y2 == 410 :
        player_x2 = 210
        player_y2 = 110
    if player_x2 == 510 and player_y2 == 260 :
        player_x2 = 360
        player_y2 = 210
    if player_x2 == 460  and player_y2 == 160 :
        player_x2 = 510
        player_y2 = 60
    if player_x2 == 60 and player_y2 == 160 :
        player_x2 = 110
        player_y2 = 60

    # sanke bitting changes

    if player_x2 == 210 and player_y2 == 460 :
        player_x2 = 360
        player_y2 = 510    
    if player_x2 == 110 and player_y2 == 210 :
        player_x2 = 110
        player_y2 = 460 
    if player_x2 == 360 and player_y2 == 260 :
        player_x2 = 360
        player_y2 = 360
    if player_x2 == 210 and player_y2 == 210 :
        player_x2 = 60
        player_y2 = 260  
    if player_x2 == 360 and player_y2 == 110 :
        player_x2 = 260
        player_y2 = 360
    if player_x2 == 410 and player_y2 == 60 :
        player_x2 = 410
        player_y2 = 160
    if player_x2 == 310 and player_y2 == 60 :
        player_x2 = 310
        player_y2 = 160
    if player_x2 == 160 and player_y2 == 60 :
        player_x2 = 110
        player_y2 = 160
        
    if player_x2 == 60 and player_y2 == 60 :
        won()

    player1(player_x,player_y)
    player2(player_x2,player_y2)
    show(show_x,show_y)
            
    pygame.display.update()