import pygame
import random
pygame.init()
blocks = [
"000000000000000000000000000000",
"000000000000000000000000000000",
"000000000000000000000000000000",
"000000000000001000100000000000",
"001111110000000000000000001110",
"000000000000000000000000000000",
"000000000000000122100000000000",
"011111100000000000000000001111",
"000000000000000000000000000000",
"000000000333333333330000000000",
"000000000000000000000000001111",
"011111000000000000000000000000",
"000000000000000000001111000000",
"000000000000000000000000000000",
"000000000001111100000000000000",
"000000000000000000000000000000",
"000000000000000000000000000000"
]
left_key = right_key = False
running = True
in_ice = False

spedy_SIZE = 100 
spedy_size_y = 130
spedy_actual_SIZE = spedy_SIZE +30
spedy_size_actual_y = spedy_size_y +30
BLOCK_SIZE = 50
spedy_y = -650
spedy_x = 750
SCREEN_SIZE = (1530, 880)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("platformer")
run = True
spedy_vx = 0
spedy_vy = 0

left_key = right_key = False
running = True
in_plataform = True
clock = pygame.time.Clock()
#load images
bg2_img = pygame.image.load("BG_Decor.png")
middle_img = pygame.image.load("C:Middle_Decor.png")
bg_img = pygame.image.load("Sky.png")
sun_img = pygame.image.load("Foreground.png")
block_without_grass = pygame. image. load("sem relva.jpg")
block_without_grass = pygame. transform. scale(block_without_grass, (BLOCK_SIZE,BLOCK_SIZE ))
block_with_grass = pygame. image. load("relva.jpg")
block_with_grass = pygame. transform. scale(block_with_grass, (BLOCK_SIZE,BLOCK_SIZE ))
ice = pygame. image. load("gelo.jpg")
ice = pygame. transform. scale(ice, (BLOCK_SIZE,BLOCK_SIZE ))
spedy_idle = pygame. image. load("idle/Satyr_01_Idle_000.png")
spedy_idle = pygame. transform. scale(spedy_idle, (spedy_size_actual_y,spedy_actual_SIZE ))
spedy = spedy_idle
merged = bg2_img
merged.blit(bg2_img,(0,0))
merged.blit(middle_img,(0,0))
merged.blit(bg_img,(0,0))
merged.blit(sun_img,(0,0))
for row in range(0, len(blocks)):
    for col in range(0, len(blocks[row])):
        if blocks[row][col] == "1":
            merged.blit(block_without_grass,(col*BLOCK_SIZE, row*BLOCK_SIZE))
        if blocks[row][col] == "2":
            merged.blit(block_with_grass,(col*BLOCK_SIZE, row*BLOCK_SIZE))
        if blocks[row][col] == "3":
            merged.blit(ice,(col*BLOCK_SIZE, row*BLOCK_SIZE))
spedy_SIZE == spedy_SIZE
spedy_size_y ==spedy_size_y
left = False
#idle animation
idle_spedy = []
idle_spedy.append(pygame. transform. scale(pygame. image. load("idle/Satyr_01_Idle_000.png"),(spedy_size_actual_y,spedy_actual_SIZE )))
idle_spedy.append(pygame. transform. scale(pygame. image. load("idle/Satyr_01_Idle_001.png"),(spedy_size_actual_y,spedy_actual_SIZE )))
idle_spedy.append(pygame. transform. scale(pygame. image. load("idle/Satyr_01_Idle_002.png"),(spedy_size_actual_y,spedy_actual_SIZE )))
idle_spedy.append(pygame. transform. scale(pygame. image. load("idle/Satyr_01_Idle_003.png"),(spedy_size_actual_y,spedy_actual_SIZE )))
idle_spedy.append(pygame. transform. scale(pygame. image. load("idle/Satyr_01_Idle_004.png"),(spedy_size_actual_y,spedy_actual_SIZE )))
idle_spedy.append(pygame. transform. scale(pygame. image. load("idle/Satyr_01_Idle_005.png"),(spedy_size_actual_y,spedy_actual_SIZE )))
idle_spedy.append(pygame. transform. scale(pygame. image. load("idle/Satyr_01_Idle_006.png"),(spedy_size_actual_y,spedy_actual_SIZE )))
idle_spedy.append(pygame. transform. scale(pygame. image. load("idle/Satyr_01_Idle_007.png"),(spedy_size_actual_y,spedy_actual_SIZE )))
idle_spedy.append(pygame. transform. scale(pygame. image. load("idle/Satyr_01_Idle_008.png"),(spedy_size_actual_y,spedy_actual_SIZE )))
idle_spedy.append(pygame. transform. scale(pygame. image. load("idle/Satyr_01_Idle_009.png"),(spedy_size_actual_y,spedy_actual_SIZE )))
idle_spedy.append(pygame. transform. scale(pygame. image. load("idle/Satyr_01_Idle_010.png"),(spedy_size_actual_y,spedy_actual_SIZE )))
idle_spedy.append(pygame. transform. scale(pygame. image. load("idle/Satyr_01_Idle_011.png"),(spedy_size_actual_y,spedy_actual_SIZE )))
idle_status_s = 0

#img_with_flip = pygame.transform.flip(img_copy, True, False)
#walking animation
walking_spedy = []
walking_spedy.append(pygame. transform. scale(pygame. image. load("Walking/Satyr_01_Walking_000.png"),(spedy_size_actual_y,spedy_actual_SIZE )))
walking_spedy.append(pygame. transform. scale(pygame. image. load("Walking/Satyr_01_Walking_001.png"),(spedy_size_actual_y,spedy_actual_SIZE )))
walking_spedy.append(pygame. transform. scale(pygame. image. load("Walking/Satyr_01_Walking_002.png"),(spedy_size_actual_y,spedy_actual_SIZE )))
walking_spedy.append(pygame. transform. scale(pygame. image. load("Walking/Satyr_01_Walking_003.png"),(spedy_size_actual_y,spedy_actual_SIZE )))
walking_spedy.append(pygame. transform. scale(pygame. image. load("Walking/Satyr_01_Walking_004.png"),(spedy_size_actual_y,spedy_actual_SIZE )))
walking_spedy.append(pygame. transform. scale(pygame. image. load("Walking/Satyr_01_Walking_005.png"),(spedy_size_actual_y,spedy_actual_SIZE )))
walking_spedy.append(pygame. transform. scale(pygame. image. load("Walking/Satyr_01_Walking_006.png"),(spedy_size_actual_y,spedy_actual_SIZE )))
walking_spedy.append(pygame. transform. scale(pygame. image. load("Walking/Satyr_01_Walking_007.png"),(spedy_size_actual_y,spedy_actual_SIZE )))
walking_spedy.append(pygame. transform. scale(pygame. image. load("Walking/Satyr_01_Walking_008.png"),(spedy_size_actual_y,spedy_actual_SIZE )))
walking_spedy.append(pygame. transform. scale(pygame. image. load("Walking/Satyr_01_Walking_009.png"),(spedy_size_actual_y,spedy_actual_SIZE )))
walking_spedy.append(pygame. transform. scale(pygame. image. load("Walking/Satyr_01_Walking_010.png"),(spedy_size_actual_y,spedy_actual_SIZE )))
walking_spedy.append(pygame. transform. scale(pygame. image. load("Walking/Satyr_01_Walking_011.png"),(spedy_size_actual_y,spedy_actual_SIZE )))
walking_spedy.append(pygame. transform. scale(pygame. image. load("Walking/Satyr_01_Walking_012.png"),(spedy_size_actual_y,spedy_actual_SIZE )))
walking_spedy.append(pygame. transform. scale(pygame. image. load("Walking/Satyr_01_Walking_013.png"),(spedy_size_actual_y,spedy_actual_SIZE )))
walking_spedy.append(pygame. transform. scale(pygame. image. load("Walking/Satyr_01_Walking_014.png"),(spedy_size_actual_y,spedy_actual_SIZE )))
walking_spedy.append(pygame. transform. scale(pygame. image. load("Walking/Satyr_01_Walking_015.png"),(spedy_size_actual_y,spedy_actual_SIZE )))
walking_spedy.append(pygame. transform. scale(pygame. image. load("Walking/Satyr_01_Walking_016.png"),(spedy_size_actual_y,spedy_actual_SIZE )))
walking_spedy.append(pygame. transform. scale(pygame. image. load("Walking/Satyr_01_Walking_017.png"),(spedy_size_actual_y,spedy_actual_SIZE )))
walking_spedy_status = 0
#animation of death
jump_start_spedy = []
jump_start_spedy.append(pygame. transform. scale(pygame. image. load("jump start/Satyr_01_Jump Start_000.png"),(spedy_size_actual_y,spedy_actual_SIZE )))
jump_start_spedy.append(pygame. transform. scale(pygame. image. load("jump start/Satyr_01_Jump Start_001.png"),(spedy_size_actual_y,spedy_actual_SIZE )))
jump_start_spedy.append(pygame. transform. scale(pygame. image. load("jump start/Satyr_01_Jump Start_002.png"),(spedy_size_actual_y,spedy_actual_SIZE )))
jump_start_spedy.append(pygame. transform. scale(pygame. image. load("jump start/Satyr_01_Jump Start_003.png"),(spedy_size_actual_y,spedy_actual_SIZE )))
jump_start_spedy.append(pygame. transform. scale(pygame. image. load("jump start/Satyr_01_Jump Start_004.png"),(spedy_size_actual_y,spedy_actual_SIZE )))
jump_start_spedy.append(pygame. transform. scale(pygame. image. load("jump start/Satyr_01_Jump Start_005.png"),(spedy_size_actual_y,spedy_actual_SIZE )))
jump_spedy = False
jump_spedy_status = 0
#mid air animation
air_spedy = []
air_spedy.append(pygame. transform. scale(pygame. image. load("Jump Loop/Satyr_01_Jump Loop_000.png"),(spedy_size_actual_y,spedy_actual_SIZE )))
air_spedy.append(pygame. transform. scale(pygame. image. load("Jump Loop/Satyr_01_Jump Loop_001.png"),(spedy_size_actual_y,spedy_actual_SIZE )))
air_spedy.append(pygame. transform. scale(pygame. image. load("Jump Loop/Satyr_01_Jump Loop_002.png"),(spedy_size_actual_y,spedy_actual_SIZE )))
air_spedy.append(pygame. transform. scale(pygame. image. load("Jump Loop/Satyr_01_Jump Loop_003.png"),(spedy_size_actual_y,spedy_actual_SIZE )))
air_spedy.append(pygame. transform. scale(pygame. image. load("Jump Loop/Satyr_01_Jump Loop_004.png"),(spedy_size_actual_y,spedy_actual_SIZE )))
air_spedy.append(pygame. transform. scale(pygame. image. load("Jump Loop/Satyr_01_Jump Loop_005.png"),(spedy_size_actual_y,spedy_actual_SIZE )))
air_spedy_status = 0


while run:
    #teclado
    screen.blit(merged,(0,0))

    jump_key = False
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            run = False
        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                run = False
            elif ev.key == pygame.K_LEFT:
                left_key = True
            elif ev.key == pygame.K_RIGHT:
                right_key = True
            elif ev.key == pygame.K_SPACE:
                jump_key = True
                jump_spedy = True

        elif ev.type == pygame.KEYUP:
            if ev.key == pygame.K_LEFT:
                left_key = False
            elif ev.key == pygame.K_RIGHT:
                right_key = False



    # 2
    dt = clock.tick()
    if right_key == False and left_key == False and jump_key == False and in_plataform == True :
        if idle_status_s >= len(idle_spedy):
            idle_status_s = 0
        spedy = idle_spedy[int(idle_status_s)]
        idle_status_s += dt/150
    #right animation
    if right_key == True and left_key == False and jump_key == False and in_plataform == True:
        if walking_spedy_status >= len(walking_spedy):
            walking_spedy_status = 0
        spedy = walking_spedy[int(walking_spedy_status)]
        walking_spedy_status += dt/30
        left = False
    #left animation
    if right_key == False and left_key == True and jump_key == False and in_plataform == True:
        if walking_spedy_status >= len(walking_spedy):
            walking_spedy_status = 0
        spedy = walking_spedy[int(walking_spedy_status)]
        walking_spedy_status += dt/30
        left = True
        #jump
    if jump_spedy:
        jump_spedy_status += dt/30
        if jump_spedy_status >= len(jump_start_spedy):
            jump_spedy = False
            jump_spedy_status = 0
        else:
            spedy = jump_start_spedy[int(jump_spedy_status)]
    #air animation
    if not jump_spedy and not in_plataform:
        if air_spedy_status >= len(air_spedy):
            air_spedy_status = 0
        spedy = air_spedy[int(air_spedy_status)]
        air_spedy_status += dt/30
    if left:
        spedy = pygame.transform.flip(spedy,True,False)
    #ice
    if left_key and ( not (in_ice)):
        spedy_vx = -0.5
    elif right_key and (not (in_ice)):
        spedy_vx = +0.5
    elif not (in_ice):
        spedy_vx = 0
    if right_key and in_ice:
        spedy_vx += 0.001*dt
    if left_key and in_ice:
        spedy_vx += -0.001*dt
    
    if jump_key and in_plataform:
        spedy_vy = -1.6  # impulse
        in_plataform = False
    else:#if not is_in_plataform:
        spedy_vy += 0.01*dt  # gravity

    spedy_oldy = spedy_y
    spedy_x += spedy_vx*dt
    spedy_y += spedy_vy*dt
    if spedy_x > SCREEN_SIZE[0]-spedy_size_y+30:#não sair dos lados
        spedy_x = SCREEN_SIZE[0]-spedy_size_y+30
        spedy_vx = 0
    if spedy_x <= -60:
        spedy_x = -60
        spedy_vx = 0

    in_plataform = False
    if spedy_y > SCREEN_SIZE[1]-spedy_SIZE:  # chao
        spedy_y = SCREEN_SIZE[1]-spedy_SIZE
        spedy_vy = 0
        in_plataform = True
        in_ice = False

    if spedy_vy > 0: #not is_in_plataform and spedy_vy > 0:  # saltar
        for row in range(0, len(blocks)):
            for col in range(0, len(blocks[row])):
                if blocks[row][col] != "0" :
                    if spedy_x+spedy_SIZE >= col*BLOCK_SIZE and spedy_x+spedy_SIZE/2 <= (col+1)*BLOCK_SIZE:
                        if spedy_y+spedy_SIZE >= row*BLOCK_SIZE and spedy_oldy+spedy_SIZE/2< row*BLOCK_SIZE:
                            if blocks[row][col] =="3":
                                in_ice = True
                            else:
                                in_ice = False
                            in_plataform = True
                            spedy_vy = 0
                            spedy_y = row*BLOCK_SIZE - spedy_SIZE

    # 3. desenhar no ecra
    

    
    spedy = pygame. transform. scale(spedy, (spedy_size_actual_y,spedy_actual_SIZE ))
    screen.blit(spedy, (int(spedy_x), int(spedy_y)))
    dt = clock.tick()
    pygame.display.flip()
pygame.quit()
