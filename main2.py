import pygame
import os
pygame.init()



FPS = 30
vel = 1
GRAY = (127, 127, 127)
width = 800
height = 600
surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Game')

knight_idle = pygame.image.load(os.path.join('Knight_1', 'Idle.png'))
knight_run1 = pygame.image.load(os.path.join('Knight_1', 'Run_1.png'))
knight_run2 = pygame.image.load(os.path.join('Knight_1', 'Run_2.png'))
knight_run3 = pygame.image.load(os.path.join('Knight_1', 'Run_3.png'))
knight_run4 = pygame.image.load(os.path.join('Knight_1', 'Run_4.png'))
knight_run5 = pygame.image.load(os.path.join('Knight_1', 'Run_5.png'))
knight_run6 = pygame.image.load(os.path.join('Knight_1', 'Run_6.png'))
knight_run7 = pygame.image.load(os.path.join('Knight_1', 'Run_7.png'))

running = [knight_run1, knight_run2, knight_run3, knight_run4, knight_run5, knight_run6, knight_run7]




def draw_surface(knight):
    surface.fill(GRAY)
    current_frame = 0
    key_pressed = True
    #keys = pygame.key.get_pressed() 
    
    #for event in pygame.event.get():
        #if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            #key_pressed = True
        #elif event.type == pygame.KEYUP and event.key == pygame.K_d:
            #key_pressed = False

    if key_pressed:
        surface.blit(running[current_frame], (knight.x, knight.y))
        current_frame += 1
   
    
    #if keys[pygame.K_d]:
        #while current_frame <= len(running):
            #surface.blit(running[current_frame], (knight.x, knight.y))
            #current_frame += 1
            #if current_frame == len(running):
                #current_frame = 0
                
    
    elif key_pressed == False:
        surface.blit(knight_idle,(knight.x, knight.y)) 
    
       
    pygame.display.update()

    
def main():
    knight = pygame.Rect(0,0,60,60)
    clock = pygame.time.Clock()
    clock.tick(FPS)
    game = True
    while game:
        draw_surface(knight)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and knight.x > 0:
            knight.x -= vel
        if keys[pygame.K_d] and knight.x < 660:
            knight.x += vel
        if keys[pygame.K_w] and knight.y > 0:
            knight.y -= vel
        if keys[pygame.K_s] and knight.y < 300:
            knight.y += vel
            
    pygame.quit()

main()

import pygame
import os
import sys
pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
knight_idle = pygame.image.load(os.path.join('Knight_1', 'Idle.png'))
knight_run1 = pygame.image.load(os.path.join('Knight_1', 'Run_1.png'))
knight_run2 = pygame.image.load(os.path.join('Knight_1', 'Run_2.png'))
knight_run3 = pygame.image.load(os.path.join('Knight_1', 'Run_3.png'))
knight_run4 = pygame.image.load(os.path.join('Knight_1', 'Run_4.png'))
knight_run5 = pygame.image.load(os.path.join('Knight_1', 'Run_5.png'))
knight_run6 = pygame.image.load(os.path.join('Knight_1', 'Run_6.png'))
knight_run7 = pygame.image.load(os.path.join('Knight_1', 'Run_7.png'))

images = [knight_run1, knight_run2, knight_run3, knight_run4, knight_run5, knight_run6, knight_run7]

# Set up the animation loop
clock = pygame.time.Clock()
current_frame = 0
frame_rate = 10

# Set up the key state variables
key_pressed = False
key = pygame.K_SPACE

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # Check for key press events
        if event.type == pygame.KEYDOWN and event.key == key:
            key_pressed = True
        elif event.type == pygame.KEYUP and event.key == key:
            key_pressed = False
    
    # Only animate the PNG if the key is pressed
    if key_pressed:
        # Display the current image
        screen.blit(images[current_frame], (0, 0))
        pygame.display.update()

        # Wait for a short delay
        pygame.time.delay(100)

        # Cycle to the next image
        current_frame = (current_frame + 1) % len(images)

    # Set the frame rate
    clock.tick(frame_rate)










