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
"000000000000000111100000000000",
"011111100000000000000000001111",
"000000000000000000000000000000",
"000000000111111111110000000000",
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
in_plataform = True
#load images
bg2_img = pygame.image.load("BG_Decor.png")
middle_img = pygame.image.load("C:Middle_Decor.png")
bg_img = pygame.image.load("Sky.png")
sun_img = pygame.image.load("Foreground.png")

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
spedy = pygame. image. load("Wraith_01_Idle Blinking_000.png")
spedy = pygame. transform. scale(spedy, (spedy_size_actual_y,spedy_actual_SIZE ))
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

spedy_SIZE == spedy_SIZE-70
spedy_size_y ==spedy_size_y +100

while run:
    #teclado
    screen.blit(merged,(0,0))
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
        elif ev.type == pygame.KEYUP:
            if ev.key == pygame.K_LEFT:
                left_key = False
            elif ev.key == pygame.K_RIGHT:
                right_key = False
    # 2
    dt = clock.tick()
    if left_key:
        spedy_vx = -0.5
    elif right_key:
        spedy_vx = +0.5
    else:
        spedy_vx = 0
    
    if jump_key and in_plataform:
        spedy_vy = -1.5  # impulse
        in_plataform = False
    else:#if not is_in_plataform:
        spedy_vy += 0.01*dt  # gravity

    spedy_oldy = spedy_y
    spedy_x += spedy_vx*dt
    spedy_y += spedy_vy*dt
    
    if spedy_y > SCREEN_SIZE[1]-spedy_SIZE:  # chao
        spedy_y = SCREEN_SIZE[1]-spedy_SIZE
        spedy_vy = 0
        in_plataform = True

    if spedy_vy > 0: #not is_in_plataform and spedy_vy > 0:  # saltar
        for row in range(0, len(blocks)):
            for col in range(0, len(blocks[row])):
                if blocks[row][col] != "0":
                    if spedy_x+spedy_SIZE >= col*BLOCK_SIZE and spedy_x <= (col+1)*BLOCK_SIZE:
                        if spedy_y+spedy_SIZE >= row*BLOCK_SIZE and spedy_oldy< row*BLOCK_SIZE:
                            in_plataform = True
                            spedy_vy = 0
                            spedy_y = row*BLOCK_SIZE - spedy_SIZE
    # 3. desenhar no ecra
    

    
    spedy = pygame. image. load("Wraith_01_Idle Blinking_000.png")
    spedy = pygame. transform. scale(spedy, (spedy_size_actual_y,spedy_actual_SIZE ))
    screen.blit(spedy, (int(spedy_x), int(spedy_y)))
    dt = clock.tick()
    pygame.display.flip()
pygame.quit()
