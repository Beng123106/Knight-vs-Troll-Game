#import important modules and initialize pygame
import pygame
import os
pygame.init()

#game handling, creating relevant variables 
text_font = pygame.font.SysFont("Times New Roman", 30)
FPS = 60
vel = 15
RED = (255,0,0)
width = 800
height = 600
surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Game')

 
#animations for player character
background = pygame.image.load(os.path.join('Knight_1', 'background2.PNG'))
background = pygame.transform.scale(background,(width,height))
knight_idle = pygame.image.load(os.path.join('Knight_1', 'attack_1.png'))

knight_run1 = pygame.image.load(os.path.join('Knight_1', 'Run_1.png'))
knight_run2 = pygame.image.load(os.path.join('Knight_1', 'Run_2.png'))
knight_run3 = pygame.image.load(os.path.join('Knight_1', 'Run_3.png'))
knight_run4 = pygame.image.load(os.path.join('Knight_1', 'Run_4.png'))
knight_run5 = pygame.image.load(os.path.join('Knight_1', 'Run_5.png'))
knight_run6 = pygame.image.load(os.path.join('Knight_1', 'Run_6.png'))
knight_run7 = pygame.image.load(os.path.join('Knight_1', 'Run_7.png'))
running = [knight_run1, knight_run2, knight_run3, knight_run4, knight_run5, knight_run6, knight_run7]

knight_block = pygame.image.load(os.path.join('Knight_1', 'Protect.png'))

knight_dead1 = pygame.image.load(os.path.join('Knight_1', 'dead_1.png'))
knight_dead2 = pygame.image.load(os.path.join('Knight_1', 'dead_2.png'))
knight_dead3 = pygame.image.load(os.path.join('Knight_1', 'dead_3.png'))
knight_dead4 = pygame.image.load(os.path.join('Knight_1', 'dead_4.png'))
knight_dead5 = pygame.image.load(os.path.join('Knight_1', 'dead_5.png'))
knight_dead = [knight_dead1, knight_dead2, knight_dead3, knight_dead4, knight_dead5]


knight_attack1 = pygame.image.load(os.path.join('Knight_1', 'attack_1.png'))
knight_attack2 = pygame.image.load(os.path.join('Knight_1', 'attack_2.png'))
knight_attack3 = pygame.image.load(os.path.join('Knight_1', 'attack_3.png'))
knight_attack4 = pygame.image.load(os.path.join('Knight_1', 'attack_4.png'))
knight_attack5 = pygame.image.load(os.path.join('Knight_1', 'attack_5.png'))

knight2_attack1 = pygame.image.load(os.path.join('Knight_1', 'attack1_2.png'))
knight2_attack2 = pygame.image.load(os.path.join('Knight_1', 'attack2_2.png'))
knight2_attack3 = pygame.image.load(os.path.join('Knight_1', 'attack3_2.png'))
knight2_attack4 = pygame.image.load(os.path.join('Knight_1', 'attack4_2.png'))

knight3_attack1 = pygame.image.load(os.path.join('Knight_1', 'attack1_3.png'))
knight3_attack2 = pygame.image.load(os.path.join('Knight_1', 'attack2_3.png'))
knight3_attack3 = pygame.image.load(os.path.join('Knight_1', 'attack3_3.png'))

attack_set1 = [knight_attack2, knight_attack3, knight_attack4, knight_attack5, knight3_attack1, knight3_attack2, knight3_attack3, knight2_attack1, knight2_attack2, knight2_attack3, knight2_attack4]



#animations for enemy
enemy_idle = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
    os.path.join('enemy', 'Idle_001.png')), (240, 240)), True, False)      

enemy_walk1 = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
    os.path.join('enemy', 'Walk_000.png')), (250, 250)), True, False)  
enemy_walk2 = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
    os.path.join('enemy', 'Walk_001.png')), (250, 250)), True, False)   
enemy_walk3 = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
    os.path.join('enemy', 'Walk_002.png')), (250, 250)), True, False)   
enemy_walk4 = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
    os.path.join('enemy', 'Walk_003.png')), (250, 250)), True, False)   
enemy_walk5 = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
    os.path.join('enemy', 'Walk_004.png')), (250, 250)), True, False)   
enemy_walk6 = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
    os.path.join('enemy', 'Walk_005.png')), (250, 250)), True, False)   
enemy_walk7 = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
    os.path.join('enemy', 'Walk_006.png')), (250, 250)), True, False)   
enemy_walk8 = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
    os.path.join('enemy', 'Walk_007.png')), (250, 250)), True, False)   
enemy_walk9 = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
    os.path.join('enemy', 'Walk_008.png')), (250, 250)), True, False)   
enemy_walk10 = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
    os.path.join('enemy', 'Walk_009.png')), (250, 250)), True, False)   
enemy_walk = [enemy_walk1, enemy_walk2, enemy_walk3, enemy_walk4, enemy_walk5, enemy_walk6, enemy_walk7, enemy_walk8, enemy_walk9, enemy_walk10]

dead_1 = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
    os.path.join('enemy', 'Dead_001.png')), (250, 250)), True, False) 
dead_2 = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
    os.path.join('enemy', 'Dead_002.png')), (250, 250)), True, False) 
dead_3 = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
    os.path.join('enemy', 'Dead_003.png')), (250, 250)), True, False) 
dead_4 = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
    os.path.join('enemy', 'Dead_004.png')), (250, 250)), True, False) 
dead_5 = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
    os.path.join('enemy', 'Dead_005.png')), (250, 250)), True, False) 
dead_6 = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
    os.path.join('enemy', 'Dead_006.png')), (250, 250)), True, False) 
dead_7 = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
    os.path.join('enemy', 'Dead_007.png')), (250, 250)), True, False) 
dead_8 = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
    os.path.join('enemy', 'Dead_008.png')), (250, 250)), True, False) 
dead_9 = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
    os.path.join('enemy', 'Dead_009.png')), (250, 250)), True, False) 
dead = [dead_1, dead_2, dead_3, dead_4, dead_5, dead_6, dead_7, dead_8, dead_9]

attack_1 = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
    os.path.join('enemy', 'Attack_000.png')), (350, 350)), True, False) 
attack_2 = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
    os.path.join('enemy', 'Attack_001.png')), (350, 350)), True, False) 
attack_3 = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
    os.path.join('enemy', 'Attack_002.png')), (350, 350)), True, False) 
attack_4 = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
    os.path.join('enemy', 'Attack_003.png')), (350, 350)), True, False) 
attack_5 = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
    os.path.join('enemy', 'Attack_004.png')), (350, 350)), True, False) 
attack_6 = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
    os.path.join('enemy', 'Attack_005.png')), (350, 350)), True, False) 
attack_7 = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
    os.path.join('enemy', 'Attack_006.png')), (350, 350)), True, False) 
attack_8 = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
    os.path.join('enemy', 'Attack_007.png')), (350, 350)), True, False) 
attack_9 = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
    os.path.join('enemy', 'Attack_008.png')), (350, 350)), True, False) 
attack_10 = pygame.transform.flip(pygame.transform.scale(pygame.image.load(
    os.path.join('enemy', 'Attack_009.png')), (350, 350)), True, False) 
enemy_attacks = [attack_1, attack_2, attack_3, attack_4, attack_5, attack_6, attack_7, attack_8, attack_9, attack_10]

#create a function to draw text on the screen
def draw_text(text, font, text_colour, x, y):
    img = font.render(text, True, text_colour)
    surface.blit(img,(x,y))
    
#main function
def main():
    #setting important variables
    character_health = 100
    enemy_health = 100
    knight = pygame.Rect(0,300,10,10)
    enemy = pygame.Rect(500,300, 125, 70)
    clock = pygame.time.Clock()
    clock.tick(FPS)
    
    current_frame = 0
    attack_frame = 0 
    dead_frame = 0
    enemy_attack_frame = 0
    enemy_walk_frame = 0
    
    game = True
    while game:
        #more important variables
        block = False
        attack_hitbox = pygame.Rect(knight.x, knight.y+500, 0, 0)
        enemy_attack_hitbox = pygame.Rect(enemy.x, enemy.y+800, 0,0)
        flag = True
        surface.blit(background, (0,0))
#health bars
        pygame.draw.rect(surface, (250,0,0), pygame.Rect(enemy.x-90, enemy.y-220, enemy_health*3, 40)) 
        pygame.draw.rect(surface, (0,210,0), pygame.Rect(knight.x-30,knight.y-40,character_health, 10)) 
        
#quit the game if this event is the case
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
#animations for different keys 
        keys = pygame.key.get_pressed()
        if character_health <= 0:
            flag = False
            surface.blit(enemy_idle, (enemy.x-120, enemy.y-150))
            surface.blit(knight_dead[dead_frame],(knight.x-40, knight.y - 50))
            dead_frame = dead_frame + 1
            if dead_frame == len(knight_dead):
                dead_frame = 4
            draw_text('LOSER LOSER TURKEY SNOOZER!', text_font, RED, 80, 300)
                                
        if  flag and keys[pygame.K_a] and knight.x > 40:
            knight.x -= vel
        if  flag and keys[pygame.K_d] and knight.x < 700:
            knight.x += vel
        if  flag and keys[pygame.K_w] and knight.y > 250:
            knight.y -= vel
        if flag and keys[pygame.K_s] and knight.y < 470:
            knight.y += vel 
            
        if flag and keys[pygame.K_d] and keys[pygame.K_o]:
            surface.blit(attack_set1[attack_frame], (knight.x-40, knight.y-50))
            pygame.time.delay(100)
            attack_frame += 1
            if attack_frame == len(attack_set1):
                attack_frame = 0
            attack_hitbox = pygame.Rect(knight.x+60, knight.y-30, 50, 40)
           
    
        elif keys[pygame.K_s] and keys[pygame.K_o]:
            if flag:
                surface.blit(attack_set1[attack_frame], (knight.x-40, knight.y-50))
                pygame.time.delay(100)
                attack_frame += 1
                if attack_frame == len(attack_set1):
                    attack_frame = 0
                attack_hitbox = pygame.Rect(knight.x + 60, knight.y-30, 50, 40)
         
            
        elif keys[pygame.K_a] and keys[pygame.K_o]:
            if flag:
                surface.blit(attack_set1[attack_frame], (knight.x-40, knight.y-50))
                pygame.time.delay(100)
                attack_frame += 1
                if attack_frame == len(attack_set1):
                    attack_frame = 0
                attack_hitbox = pygame.Rect(knight.x-40, knight.y-30, 50, 40)
            
            
        elif keys[pygame.K_w] and keys[pygame.K_o]:
            if flag:
                surface.blit(attack_set1[attack_frame], (knight.x-40, knight.y-50))
                pygame.time.delay(100)
                attack_frame += 1
                if attack_frame == len(attack_set1):
                    attack_frame = 0
                attack_hitbox = pygame.Rect(knight.x + 60, knight.y-30,50, 40)
           
   
        elif keys[pygame.K_d] or keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_w]:
            if flag:
                surface.blit(running[current_frame], (knight.x-40, knight.y-50))
            pygame.time.delay(80)
            current_frame = (current_frame + 1) % len(running)

        elif flag and keys[pygame.K_o]:
                surface.blit(attack_set1[attack_frame], (knight.x-40, knight.y-50))
                pygame.time.delay(100)
                attack_frame += 1
                if attack_frame == len(attack_set1):
                    attack_frame = 0
                attack_hitbox = pygame.Rect(knight.x + 60, knight.y-30, 50, 40)
        
        elif keys[pygame.K_p]:
                block = True
                if flag:
                    surface.blit(knight_block, (knight.x-40, knight.y-50))
                    pygame.time.delay(50)
        else:
            if flag:
                surface.blit(knight_idle,(knight.x-40, knight.y-50))
                pygame.time.delay(80)
        

#handling collisions and health + death animation for enemy
        if attack_hitbox.colliderect(enemy):
            enemy_health -= 3
        if enemy_health <= 0:
            flag = False
            surface.blit(dead[dead_frame], (enemy.x-120, enemy.y-150))
            dead_frame = (dead_frame + 1)
            if dead_frame == len(dead):
                dead_frame = 8
            draw_text('WINNER WINNER CHICKEN DINNER!', text_font, RED, 80, 300)
       
            
        
#this code allows the enemy to follow you and move
        if flag:
            if not enemy.colliderect(knight):
                if enemy.x > knight.x:
                    enemy.x -= 5
                    surface.blit(enemy_walk[enemy_walk_frame], (enemy.x-120, enemy.y-180))
                    enemy_walk_frame = (enemy_walk_frame + 1) % len(enemy_walk)
                elif enemy.x < knight.x:
                    enemy.x += 5
                    surface.blit(enemy_walk[enemy_walk_frame], (enemy.x-120, enemy.y-180))
                    enemy_walk_frame = (enemy_walk_frame + 1) % len(enemy_walk)
                if enemy.y > knight.y:
                    enemy.y -= 4
                elif enemy.y < knight.y:
                    enemy.y += 4
#detects when enemy is close enough to attack the player
            elif enemy.colliderect(knight):
                surface.blit(enemy_attacks[enemy_attack_frame], (enemy.x-120, enemy.y-270))
                pygame.time.delay(10)
                enemy_attack_frame = (enemy_attack_frame + 1) % len(enemy_attacks)
                enemy_attack_hitbox = pygame.Rect(enemy.x, enemy.y-40, 100, 80)
                
#player loses health if hit by the enemys attack UNLESS the player is blocking (P key)   
                if block == False:
                    if enemy_attack_hitbox.colliderect(knight):
                        character_health -= 2
                
            else:
                surface.blit(enemy_idle,(enemy.x-120, enemy.y-180))
            
        #update the screen so we can see things
        pygame.display.update()
    
       

                
      
            
    pygame.quit()

main()
