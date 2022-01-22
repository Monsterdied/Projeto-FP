from turtle import screensize
import pygame
import pygame_menu
import random

pygame.init()
infoObject = pygame.display.Info()
SCREEN_SIZE =(infoObject.current_w, infoObject.current_h)
surface = pygame.display.set_mode((SCREEN_SIZE))
#def set_difficulty(value, difficulty):
    # Do the job here !
    #pass
multi_x = SCREEN_SIZE[0]/1530
multi_y = SCREEN_SIZE[1]/880
run1 = True
def start_the_game(player1,player2):
    #global
    kill_counter = 0
    #josefino
    josefino_SIZE = int(100*multi_x )
    josefino_size_y = int(130*multi_y)
    josefino_size_actual_y = int((josefino_size_y +(30)*multi_y))
    josefino_actual_SIZE = int((josefino_SIZE +(60)*multi_y))
    BLOCK_SIZE = int(50*multi_x)
    josefino_y = int(-650*multi_y)
    josefino_x = int((750+400*(0.5-random.random()))*multi_x)
    clock = pygame.time.Clock()
    #spedy
    spedy_SIZE = int(100*multi_x )
    spedy_size_y = int(130*multi_y)
    spedy_actual_SIZE= int(spedy_SIZE +(60)*multi_x)
    spedy_size_actual_y = int(spedy_size_y+(30) *multi_y)
    BLOCK_SIZE = int(50*multi_x)
    spedy_y = int(-650*multi_y)
    spedy_x = int((750+700*(0.5-random.random()))*multi_x)
    spedy_vx = 0
    spedy_vy = 0
    right_key = left_key = False
    in_plataform = True
    in_ice = False
    score = [0,0]
    blocks = [
    "000000000000000000000000000000",
    "000000000000000000000000000000",
    "000000000000000000000000000000",
    "000000000000000000000000000000",
    "002222220000000000000000002220",
    "000000000000000000000000000000",
    "000000000000000333300000000000",
    "022222200000000000000000002200",
    "000000000000000000000000000000",
    "000000000211111111120000000000",
    "000000000000000000000000001111",
    "011111000000000000000000000000",
    "000000000000000000011111000000",
    "000000000000000000000000000000",
    "000000000001111100000000000000",
    "000000000000000000000000000000",
    "000000000000000000000000000000"
    ]
    shut_down = 0
    #IDLE
    idle_josefino = []
    idle_josefino.append(pygame. transform. scale(pygame. image. load("idle_josefino/Satyr_02_Idle_000.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    idle_josefino.append(pygame. transform. scale(pygame. image. load("idle_josefino/Satyr_02_Idle_001.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    idle_josefino.append(pygame. transform. scale(pygame. image. load("idle_josefino/Satyr_02_Idle_002.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    idle_josefino.append(pygame. transform. scale(pygame. image. load("idle_josefino/Satyr_02_Idle_003.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    idle_josefino.append(pygame. transform. scale(pygame. image. load("idle_josefino/Satyr_02_Idle_004.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    idle_josefino.append(pygame. transform. scale(pygame. image. load("idle_josefino/Satyr_02_Idle_005.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    idle_josefino.append(pygame. transform. scale(pygame. image. load("idle_josefino/Satyr_02_Idle_006.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    idle_josefino.append(pygame. transform. scale(pygame. image. load("idle_josefino/Satyr_02_Idle_007.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    idle_josefino.append(pygame. transform. scale(pygame. image. load("idle_josefino/Satyr_02_Idle_008.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    idle_josefino.append(pygame. transform. scale(pygame. image. load("idle_josefino/Satyr_02_Idle_009.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    idle_josefino.append(pygame. transform. scale(pygame. image. load("idle_josefino/Satyr_02_Idle_010.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    idle_josefino.append(pygame. transform. scale(pygame. image. load("idle_josefino/Satyr_02_Idle_011.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    idle_status_s_josefino = 0

    #img_with_flip = pygame.transform.flip(img_copy, True, False)
    #walking animation
    walking_josefino = []
    walking_josefino.append(pygame. transform. scale(pygame. image. load("Walking_josefino/Satyr_02_Walking_000.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    walking_josefino.append(pygame. transform. scale(pygame. image. load("Walking_josefino/Satyr_02_Walking_001.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    walking_josefino.append(pygame. transform. scale(pygame. image. load("Walking_josefino/Satyr_02_Walking_002.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    walking_josefino.append(pygame. transform. scale(pygame. image. load("Walking_josefino/Satyr_02_Walking_003.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    walking_josefino.append(pygame. transform. scale(pygame. image. load("Walking_josefino/Satyr_02_Walking_004.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    walking_josefino.append(pygame. transform. scale(pygame. image. load("Walking_josefino/Satyr_02_Walking_005.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    walking_josefino.append(pygame. transform. scale(pygame. image. load("Walking_josefino/Satyr_02_Walking_006.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    walking_josefino.append(pygame. transform. scale(pygame. image. load("Walking_josefino/Satyr_02_Walking_007.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    walking_josefino.append(pygame. transform. scale(pygame. image. load("Walking_josefino/Satyr_02_Walking_008.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    walking_josefino.append(pygame. transform. scale(pygame. image. load("Walking_josefino/Satyr_02_Walking_009.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    walking_josefino.append(pygame. transform. scale(pygame. image. load("Walking_josefino/Satyr_02_Walking_010.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    walking_josefino.append(pygame. transform. scale(pygame. image. load("Walking_josefino/Satyr_02_Walking_011.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    walking_josefino.append(pygame. transform. scale(pygame. image. load("Walking_josefino/Satyr_02_Walking_012.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    walking_josefino.append(pygame. transform. scale(pygame. image. load("Walking_josefino/Satyr_02_Walking_013.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    walking_josefino.append(pygame. transform. scale(pygame. image. load("Walking_josefino/Satyr_02_Walking_014.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    walking_josefino.append(pygame. transform. scale(pygame. image. load("Walking_josefino/Satyr_02_Walking_015.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    walking_josefino.append(pygame. transform. scale(pygame. image. load("Walking_josefino/Satyr_02_Walking_016.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    walking_josefino.append(pygame. transform. scale(pygame. image. load("Walking_josefino/Satyr_02_Walking_017.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    walking_josefino_status = 0
    #animation of jump start
    jump_start_josefino = []
    jump_start_josefino.append(pygame. transform. scale(pygame. image. load("jump start_josefino/Satyr_02_Jump Start_000.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    jump_start_josefino.append(pygame. transform. scale(pygame. image. load("jump start_josefino/Satyr_02_Jump Start_001.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    jump_start_josefino.append(pygame. transform. scale(pygame. image. load("jump start_josefino/Satyr_02_Jump Start_002.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    jump_start_josefino.append(pygame. transform. scale(pygame. image. load("jump start_josefino/Satyr_02_Jump Start_003.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    jump_start_josefino.append(pygame. transform. scale(pygame. image. load("jump start_josefino/Satyr_02_Jump Start_004.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    jump_start_josefino.append(pygame. transform. scale(pygame. image. load("jump start_josefino/Satyr_02_Jump Start_005.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    jump_josefino = False
    jump_josefino_status = 0
    #mid air animation
    air_josefino = []
    air_josefino.append(pygame. transform. scale(pygame. image. load("Jump Loop_josefino/Satyr_02_Jump Loop_000.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    air_josefino.append(pygame. transform. scale(pygame. image. load("Jump Loop_josefino/Satyr_02_Jump Loop_001.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    air_josefino.append(pygame. transform. scale(pygame. image. load("Jump Loop_josefino/Satyr_02_Jump Loop_002.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    air_josefino.append(pygame. transform. scale(pygame. image. load("Jump Loop_josefino/Satyr_02_Jump Loop_003.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    air_josefino.append(pygame. transform. scale(pygame. image. load("Jump Loop_josefino/Satyr_02_Jump Loop_004.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    air_josefino.append(pygame. transform. scale(pygame. image. load("Jump Loop_josefino/Satyr_02_Jump Loop_005.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    air_josefino_status = 0

    #death animation
    death_josefino = []
    death_josefino.append(pygame. transform. scale(pygame. image. load("Dying_josefino/Satyr_02_Dying_000.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    death_josefino.append(pygame. transform. scale(pygame. image. load("Dying_josefino/Satyr_02_Dying_001.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    death_josefino.append(pygame. transform. scale(pygame. image. load("Dying_josefino/Satyr_02_Dying_002.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    death_josefino.append(pygame. transform. scale(pygame. image. load("Dying_josefino/Satyr_02_Dying_003.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    death_josefino.append(pygame. transform. scale(pygame. image. load("Dying_josefino/Satyr_02_Dying_004.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    death_josefino.append(pygame. transform. scale(pygame. image. load("Dying_josefino/Satyr_02_Dying_005.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    death_josefino.append(pygame. transform. scale(pygame. image. load("Dying_josefino/Satyr_02_Dying_006.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    death_josefino.append(pygame. transform. scale(pygame. image. load("Dying_josefino/Satyr_02_Dying_007.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    death_josefino.append(pygame. transform. scale(pygame. image. load("Dying_josefino/Satyr_02_Dying_008.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    death_josefino.append(pygame. transform. scale(pygame. image. load("Dying_josefino/Satyr_02_Dying_009.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    death_josefino.append(pygame. transform. scale(pygame. image. load("Dying_josefino/Satyr_02_Dying_010.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    death_josefino.append(pygame. transform. scale(pygame. image. load("Dying_josefino/Satyr_02_Dying_011.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    death_josefino.append(pygame. transform. scale(pygame. image. load("Dying_josefino/Satyr_02_Dying_012.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    death_josefino.append(pygame. transform. scale(pygame. image. load("Dying_josefino/Satyr_02_Dying_013.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    death_josefino.append(pygame. transform. scale(pygame. image. load("Dying_josefino/Satyr_02_Dying_014.png"),(josefino_actual_SIZE,josefino_size_actual_y )))
    josefino_death_status = 0
    in_ice_josefino = False
    josefino_vy = josefino_vx = 0
    death_josefino_anime = 0



    
    screen = pygame.display.set_mode(SCREEN_SIZE)


    left = False
    #spedy
    idle_spedy = []
    idle_spedy.append(pygame. transform. scale(pygame. image. load("idle/Satyr_01_Idle_000.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    idle_spedy.append(pygame. transform. scale(pygame. image. load("idle/Satyr_01_Idle_001.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    idle_spedy.append(pygame. transform. scale(pygame. image. load("idle/Satyr_01_Idle_002.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    idle_spedy.append(pygame. transform. scale(pygame. image. load("idle/Satyr_01_Idle_003.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    idle_spedy.append(pygame. transform. scale(pygame. image. load("idle/Satyr_01_Idle_004.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    idle_spedy.append(pygame. transform. scale(pygame. image. load("idle/Satyr_01_Idle_005.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    idle_spedy.append(pygame. transform. scale(pygame. image. load("idle/Satyr_01_Idle_006.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    idle_spedy.append(pygame. transform. scale(pygame. image. load("idle/Satyr_01_Idle_007.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    idle_spedy.append(pygame. transform. scale(pygame. image. load("idle/Satyr_01_Idle_008.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    idle_spedy.append(pygame. transform. scale(pygame. image. load("idle/Satyr_01_Idle_009.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    idle_spedy.append(pygame. transform. scale(pygame. image. load("idle/Satyr_01_Idle_010.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    idle_spedy.append(pygame. transform. scale(pygame. image. load("idle/Satyr_01_Idle_011.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    idle_status_s = 0

    #img_with_flip = pygame.transform.flip(img_copy, True, False)
    #walking animation
    walking_spedy = []
    walking_spedy.append(pygame. transform. scale(pygame. image. load("Walking/Satyr_01_Walking_000.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    walking_spedy.append(pygame. transform. scale(pygame. image. load("Walking/Satyr_01_Walking_001.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    walking_spedy.append(pygame. transform. scale(pygame. image. load("Walking/Satyr_01_Walking_002.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    walking_spedy.append(pygame. transform. scale(pygame. image. load("Walking/Satyr_01_Walking_003.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    walking_spedy.append(pygame. transform. scale(pygame. image. load("Walking/Satyr_01_Walking_004.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    walking_spedy.append(pygame. transform. scale(pygame. image. load("Walking/Satyr_01_Walking_005.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    walking_spedy.append(pygame. transform. scale(pygame. image. load("Walking/Satyr_01_Walking_006.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    walking_spedy.append(pygame. transform. scale(pygame. image. load("Walking/Satyr_01_Walking_007.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    walking_spedy.append(pygame. transform. scale(pygame. image. load("Walking/Satyr_01_Walking_008.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    walking_spedy.append(pygame. transform. scale(pygame. image. load("Walking/Satyr_01_Walking_009.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    walking_spedy.append(pygame. transform. scale(pygame. image. load("Walking/Satyr_01_Walking_010.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    walking_spedy.append(pygame. transform. scale(pygame. image. load("Walking/Satyr_01_Walking_011.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    walking_spedy.append(pygame. transform. scale(pygame. image. load("Walking/Satyr_01_Walking_012.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    walking_spedy.append(pygame. transform. scale(pygame. image. load("Walking/Satyr_01_Walking_013.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    walking_spedy.append(pygame. transform. scale(pygame. image. load("Walking/Satyr_01_Walking_014.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    walking_spedy.append(pygame. transform. scale(pygame. image. load("Walking/Satyr_01_Walking_015.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    walking_spedy.append(pygame. transform. scale(pygame. image. load("Walking/Satyr_01_Walking_016.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    walking_spedy.append(pygame. transform. scale(pygame. image. load("Walking/Satyr_01_Walking_017.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    walking_spedy_status = 0
    #animation of jump start
    jump_start_spedy = []
    jump_start_spedy.append(pygame. transform. scale(pygame. image. load("jump start/Satyr_01_Jump Start_000.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    jump_start_spedy.append(pygame. transform. scale(pygame. image. load("jump start/Satyr_01_Jump Start_001.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    jump_start_spedy.append(pygame. transform. scale(pygame. image. load("jump start/Satyr_01_Jump Start_002.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    jump_start_spedy.append(pygame. transform. scale(pygame. image. load("jump start/Satyr_01_Jump Start_003.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    jump_start_spedy.append(pygame. transform. scale(pygame. image. load("jump start/Satyr_01_Jump Start_004.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    jump_start_spedy.append(pygame. transform. scale(pygame. image. load("jump start/Satyr_01_Jump Start_005.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    jump_spedy = False
    jump_spedy_status = 0
    #mid air animation
    air_spedy = []
    air_spedy.append(pygame. transform. scale(pygame. image. load("Jump Loop/Satyr_01_Jump Loop_000.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    air_spedy.append(pygame. transform. scale(pygame. image. load("Jump Loop/Satyr_01_Jump Loop_001.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    air_spedy.append(pygame. transform. scale(pygame. image. load("Jump Loop/Satyr_01_Jump Loop_002.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    air_spedy.append(pygame. transform. scale(pygame. image. load("Jump Loop/Satyr_01_Jump Loop_003.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    air_spedy.append(pygame. transform. scale(pygame. image. load("Jump Loop/Satyr_01_Jump Loop_004.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    air_spedy.append(pygame. transform. scale(pygame. image. load("Jump Loop/Satyr_01_Jump Loop_005.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    air_spedy_status = 0
    #death animation
    death_spedy = []
    death_spedy.append(pygame. transform. scale(pygame. image. load("Dying/Satyr_01_Dying_000.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    death_spedy.append(pygame. transform. scale(pygame. image. load("Dying/Satyr_01_Dying_001.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    death_spedy.append(pygame. transform. scale(pygame. image. load("Dying/Satyr_01_Dying_002.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    death_spedy.append(pygame. transform. scale(pygame. image. load("Dying/Satyr_01_Dying_003.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    death_spedy.append(pygame. transform. scale(pygame. image. load("Dying/Satyr_01_Dying_004.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    death_spedy.append(pygame. transform. scale(pygame. image. load("Dying/Satyr_01_Dying_005.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    death_spedy.append(pygame. transform. scale(pygame. image. load("Dying/Satyr_01_Dying_006.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    death_spedy.append(pygame. transform. scale(pygame. image. load("Dying/Satyr_01_Dying_007.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    death_spedy.append(pygame. transform. scale(pygame. image. load("Dying/Satyr_01_Dying_008.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    death_spedy.append(pygame. transform. scale(pygame. image. load("Dying/Satyr_01_Dying_009.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    death_spedy.append(pygame. transform. scale(pygame. image. load("Dying/Satyr_01_Dying_010.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    death_spedy.append(pygame. transform. scale(pygame. image. load("Dying/Satyr_01_Dying_011.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    death_spedy.append(pygame. transform. scale(pygame. image. load("Dying/Satyr_01_Dying_012.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    death_spedy.append(pygame. transform. scale(pygame. image. load("Dying/Satyr_01_Dying_013.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    death_spedy.append(pygame. transform. scale(pygame. image. load("Dying/Satyr_01_Dying_014.png"),(spedy_actual_SIZE,spedy_size_actual_y )))
    death_spedy_status = 0
    death_spedy_anime = 0

    #load images
    winner =pygame.image.load("winner1.png")
    bg2_img = pygame.image.load("BG_Decor.png")
    bg2_img = pygame. transform. scale(bg2_img,SCREEN_SIZE)
    middle_img = pygame.image.load("C:Middle_Decor.png")
    middle_img = pygame. transform. scale(middle_img,SCREEN_SIZE)
    bg_img = pygame.image.load("Cartoon_Forest_BG_01.png")
    bg_img = pygame. transform. scale(bg_img,SCREEN_SIZE)
    sun_img = pygame.image.load("Foreground.png")
    sun_img = pygame. transform. scale(sun_img,SCREEN_SIZE)
    block_without_grass = pygame. image. load("sem relva 2.0.png")
    block_without_grass = pygame. transform. scale(block_without_grass, (BLOCK_SIZE,BLOCK_SIZE+int(7*multi_x) ))
    block_with_grass = pygame. image. load("relva2.0.png")
    block_with_grass = pygame. transform. scale(block_with_grass, (BLOCK_SIZE,BLOCK_SIZE ))
    ice = pygame. image. load("ice2.png")
    ice = pygame. transform. scale(ice, (BLOCK_SIZE,BLOCK_SIZE ))
    gui_name =pygame.image.load("gui_name.png")
    gui_name =pygame. transform. scale(gui_name, (int(300*multi_x),int(80*multi_y) ))
    merged = bg2_img
    spedy1 = pygame. image. load("Jump Loop/Satyr_01_Jump Loop_000.png")
    spedy1 = pygame. transform. scale(spedy1, (spedy_size_actual_y ,spedy_SIZE+int(30*multi_y)))
    josefino1 = pygame. image. load("Jump Loop_josefino/Satyr_02_Jump Loop_000.png")
    josefino1 = pygame. transform. scale(josefino1, (josefino_size_actual_y, josefino_SIZE+int(30*multi_y)))
    merged.blit(middle_img,(0,0))
    merged.blit(bg_img,(0,0))
    merged.blit(sun_img,(0,0))
    merged.blit(gui_name,( int(25*multi_x),  int(30*multi_x)))
    merged.blit(gui_name,( int(1190*multi_x),  int(30*multi_x)))
    merged.blit(josefino1,( int(1050*multi_x),  int(10*multi_x)))
    merged.blit(spedy1,( int(300*multi_x), int(10*multi_x)))
    for row in range(0, len(blocks)):
        for col in range(0, len(blocks[row])):
            if blocks[row][col] == "1":
                merged.blit(block_without_grass,(col*BLOCK_SIZE, row*BLOCK_SIZE-7))
            if blocks[row][col] == "2":
                merged.blit(block_with_grass,(col*BLOCK_SIZE, row*BLOCK_SIZE))
            if blocks[row][col] == "3":
                merged.blit(ice,(col*BLOCK_SIZE, row*BLOCK_SIZE))
    left_josefino = False

    d_key = a_key = False
    in_plataform_josefino = True
    run = True
    while run:
        screen.blit(merged,(0,0))
        #teclado
        jump_key_josefino = False
        jump_key = False
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                run = False
            elif ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    run = False
                elif ev.key == pygame.K_a:
                    a_key = True
                    left_josefino = True
                elif ev.key == pygame.K_d:
                    d_key = True
                elif ev.key == pygame.K_w:
                    jump_key_josefino = True
                    jump_josefino = True

            elif ev.type == pygame.KEYUP:
                if ev.key == pygame.K_a:
                    a_key = False
                elif ev.key == pygame.K_d:
                    d_key = False

            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    run = False
                elif ev.key == pygame.K_LEFT:
                    left_key = True
                    left = True
                elif ev.key == pygame.K_RIGHT:
                    right_key = True
                elif ev.key == pygame.K_UP:
                    jump_key = True
                    jump_spedy = True

            elif ev.type == pygame.KEYUP:
                if ev.key == pygame.K_LEFT:
                    left_key = False
                elif ev.key == pygame.K_RIGHT:
                    right_key = False
        


        # 2
        dt = clock.tick()
        if d_key == False and a_key == False and jump_key_josefino == False and in_plataform_josefino == True :
            if idle_status_s_josefino >= len(idle_josefino):
                idle_status_s_josefino = 0
            josefino = idle_josefino[int(idle_status_s_josefino)]
            idle_status_s_josefino += dt/150
        #right animation
        if d_key == True and a_key == False and jump_key_josefino == False :
            if walking_josefino_status >= len(walking_josefino):
                walking_josefino_status = 0
            josefino = walking_josefino[int(walking_josefino_status)]
            walking_josefino_status += dt/30
            left_josefino = False
        #left_josefino animation
        if d_key == False and a_key == True and jump_key_josefino == False :
            if walking_josefino_status >= len(walking_josefino):
                walking_josefino_status = 0
            josefino = walking_josefino[int(walking_josefino_status)]
            walking_josefino_status += dt/30
            left_josefino = True
            #jump
        if jump_josefino:
            jump_josefino_status += dt/30
            if jump_josefino_status >= len(jump_start_josefino):
                jump_josefino = False
                jump_josefino_status = 0
            else:
                josefino = jump_start_josefino[int(jump_josefino_status)]
        #air animation
        if not jump_josefino and not in_plataform_josefino:
            if air_josefino_status >= len(air_josefino):
                air_josefino_status = 0
            josefino = air_josefino[int(air_josefino_status)]
            air_josefino_status += dt/30
        if left_josefino:
            josefino = pygame.transform.flip(josefino,True,False)
        #death animationw
        if death_josefino_anime == 1:
            josefino_death_status += dt/30
            if josefino_death_status >= len(death_josefino):
                josefino_death_status = 0
                josefino_y = int(-650*multi_y)    
                josefino_x = int((750+400*(0.5-random.random()))*multi_x)
                
                death_josefino_anime = 0
            else:
                josefino = death_josefino[int(josefino_death_status)]
        
        #ice
        if a_key and ( not (in_ice_josefino)):
            josefino_vx = -0.5*multi_x
        elif d_key and (not (in_ice_josefino)):
            josefino_vx = +0.5*multi_x
        elif not (in_ice_josefino):
            josefino_vx = 0
        if d_key and in_ice_josefino:
            josefino_vx += 0.001*dt*multi_x
        if a_key and in_ice_josefino:
            josefino_vx += -0.001*dt*multi_x
        
        if jump_key_josefino and in_plataform_josefino:
            josefino_vy = -1.6*multi_y  # impulse
            in_plataform_josefino = False
        else:#if not is_in_plataform_josefino:
            josefino_vy += 0.01*dt*multi_y  # gravity

        josefino_oldy = josefino_y
        if death_josefino_anime ==0:
            josefino_x += josefino_vx*dt
            josefino_y += josefino_vy*dt
        if josefino_x > SCREEN_SIZE[0]-josefino_size_y+int(0*multi_y):#não sair dos lados
            josefino_x = SCREEN_SIZE[0]-josefino_size_y+int(0*multi_y)
            josefino_vx = 0
        if josefino_x <= int(-60*multi_x):
            josefino_x = int(-60*multi_x)
            josefino_vx = 0

        in_plataform_josefino = False
        if josefino_y > SCREEN_SIZE[1]-josefino_SIZE-int(20*multi_y):  # chao
            josefino_y = SCREEN_SIZE[1]-josefino_SIZE-int(20*multi_y)
            josefino_vy = 0
            in_plataform_josefino = True
            in_ice_josefino = False

        if josefino_vy > 0: #not is_in_plataform_josefino and josefino_vy > 0:  # saltar
            for row in range(0, len(blocks)):
                for col in range(0, len(blocks[row])):
                    if blocks[row][col] != "0" :
                        if josefino_x+(josefino_SIZE+int(0*multi_x)) >= col*BLOCK_SIZE and josefino_x+(josefino_SIZE+int(40*multi_y))/2 <= (col+1)*BLOCK_SIZE:
                            if josefino_y+josefino_SIZE+int(20*multi_y) >= row*BLOCK_SIZE and josefino_oldy+(josefino_SIZE+int(20*multi_y))/2< row*BLOCK_SIZE:
                                if blocks[row][col] =="3":
                                    in_ice_josefino = True
                                else:
                                    in_ice_josefino = False
                                in_plataform_josefino = True
                                josefino_vy = 0
                                josefino_y = row*BLOCK_SIZE - josefino_SIZE-int(20*multi_y)
        
        #spedy

        


        # 2
        if right_key == False and left_key == False and jump_key == False and in_plataform == True :
            if idle_status_s >= len(idle_spedy):
                idle_status_s = 0
            spedy = idle_spedy[int(idle_status_s)]
            idle_status_s += dt/150
        #right animation
        if right_key == True and left_key == False and jump_key == False :
            if walking_spedy_status >= len(walking_spedy):
                walking_spedy_status = 0
            spedy = walking_spedy[int(walking_spedy_status)]
            walking_spedy_status += dt/30
            left = False
        #left animation
        if right_key == False and left_key == True and jump_key == False :
            if walking_spedy_status >= len(walking_spedy):
                walking_spedy_status = 0
            spedy = walking_spedy[int(walking_spedy_status)]
            walking_spedy_status += dt/30
            left = True
            #jump
        if jump_spedy:
            jump_spedy_status += dt/60
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
        #spedy death
        if death_spedy_anime == 1:
            death_spedy_status += dt/30
            if death_spedy_status >= len(death_spedy):
                death_spedy_status = 0
                spedy_y = int(-650*multi_y)    
                spedy_x = int((750+400*(0.5-random.random()))*multi_x)
                death_spedy_anime = 0
            else:
                spedy = death_spedy[int(death_spedy_status)]
        #ice
        if left_key and ( not (in_ice)):
            spedy_vx = -0.5*multi_x
        elif right_key and (not (in_ice)):
            spedy_vx = +0.5*multi_x
        elif not (in_ice):
            spedy_vx = 0
        if right_key and in_ice:
            spedy_vx += 0.001*dt*multi_x
        if left_key and in_ice:
            spedy_vx += -0.001*dt*multi_x
        
        if jump_key and in_plataform:
            spedy_vy = -1.6*multi_y  # impulse
            in_plataform = False
        else:#if not is_in_plataform_spedy:
            spedy_vy += 0.01*dt*multi_y  # gravity

        spedy_oldy = spedy_y
        if death_spedy_anime ==0:
            spedy_x += spedy_vx*dt
            spedy_y += spedy_vy*dt
        if spedy_x > SCREEN_SIZE[0]-spedy_size_y+int(0*multi_y):#não sair dos lados
            spedy_x = SCREEN_SIZE[0]-spedy_size_y+int(0*multi_y)
            spedy_vx = 0
        if spedy_x <= int(-60*multi_x):
            spedy_x = int(-60*multi_x)
            spedy_vx = 0

        in_plataform = False
        if spedy_y > SCREEN_SIZE[1]-spedy_SIZE-int(20*multi_y):  # chao
            spedy_y = SCREEN_SIZE[1]-spedy_SIZE-int(20*multi_y)
            spedy_vy = 0
            in_plataform = True
            in_ice = False

        if spedy_vy > 0: #not is_in_plataform_spedy and spedy_vy > 0:  # saltar
            for row in range(0, len(blocks)):
                for col in range(0, len(blocks[row])):
                    if blocks[row][col] != "0" :
                        if spedy_x+(spedy_SIZE+int(0*multi_x)) >= col*BLOCK_SIZE and spedy_x+(spedy_SIZE+int(40*multi_x))/2 <= (col+1)*BLOCK_SIZE:
                            if spedy_y+spedy_SIZE+int(20*multi_y) >= row*BLOCK_SIZE and spedy_oldy+(spedy_SIZE+int(20*multi_y))/2< row*BLOCK_SIZE:
                                if blocks[row][col] =="3":
                                    in_ice = True
                                else:
                                    in_ice = False
                                in_plataform = True
                                spedy_vy = 0
                                spedy_y = row*BLOCK_SIZE - spedy_SIZE-int(20*multi_y)
        
        die_checker = [[josefino_x,josefino_y],[spedy_x,spedy_y]]
        #dead
        if (spedy_vy > 0) : 
            if spedy_x+spedy_SIZE/2 >= josefino_x  and spedy_x<= josefino_x + spedy_SIZE/2 and spedy_y+(spedy_size_actual_y-int(20*multi_y))/2 >= josefino_y and spedy_y+int(10*multi_y) < josefino_y and death_josefino_anime == 0 and death_spedy_anime ==0:
                score[0]+=1
                death_josefino_anime = 1   
                spedy_vy = -1*multi_y            

        if (josefino_vy > 0) : 
            if josefino_x+josefino_SIZE/2 >= spedy_x  and josefino_x<= spedy_x + josefino_SIZE/2 and josefino_y+(josefino_size_actual_y-int(20*multi_y))/2 >= spedy_y and josefino_y +int(10*multi_y)< spedy_y and death_spedy_anime == 0 and death_josefino_anime ==0:
                score[1]+=1
                josefino_vy = -1*multi_y
                death_spedy_anime = 1
        die_checker = [[spedy_x,spedy_y],[josefino_x,josefino_y]]
        screen.blit(spedy, (int(spedy_x), int(spedy_y)))
        screen.blit(josefino, (int(josefino_x), int(josefino_y)))
        #score
        black = (0,0,0)
        color = (255,211,67)
        score_spedy = pygame.font.SysFont(player1.get_value(),50).render(player1.get_value() + ": "+str(score[0]),True ,black)
        screen.blit(score_spedy,(int(30*multi_x), int(50*multi_y)))
        score_josefino = pygame.font.SysFont(player2.get_value(),50).render(player2.get_value() + ": "+str(score[1]),True ,black)
        screen.blit(score_josefino,(int(1200*multi_x), int(50*multi_y)))     
        if score[0] >=int(number_of_rounds.get_value()) :
            screen.blit(winner,(int(400*multi_x),int(150*multi_y)))
            screen.blit(pygame.font.SysFont(player1.get_value(),int(90*multi_x)).render(player1.get_value(),True ,color),(int(700*multi_x), int(275*multi_y)))
            kill_counter += dt
        if score[1] >=int(number_of_rounds.get_value()):
            screen.blit(winner,(int(400*multi_x),int(150*multi_y)))
            screen.blit(pygame.font.SysFont(player2.get_value(),int(90*multi_x)).render(player2.get_value(),True ,color),(int(660*multi_x), int(275*multi_y)))
            kill_counter += dt
        if int(kill_counter) > 5000:
            run = False
        dt = clock.tick()
        pygame.display.update()
    
    pass
#menu theme
myimage = pygame_menu.baseimage.BaseImage(
    image_path="menu3.0.png",
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_CENTER,
)
mytheme = pygame_menu.themes.THEME_ORANGE.copy()
mytheme.title_background_color=(0, 32, 0)
mytheme.background_color = myimage
menu = pygame_menu.Menu('spedy and Josefino', SCREEN_SIZE[0], SCREEN_SIZE[1],theme=mytheme)
def MyTextValue(name):
    return name
number_of_rounds = menu.add.text_input('Number of rounds: ', default='4', maxchar=2,onchange= MyTextValue)
player1 = menu.add.text_input('Name: ', default='spedy', maxchar=10,onchange= MyTextValue)
player2 = menu.add.text_input('Name: ', default='Josefino', maxchar=10,onchange= MyTextValue)
#menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
menu.add.button('Play', start_the_game,player1,player2)
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(surface)


pygame.quit()