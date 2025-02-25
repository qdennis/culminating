import pygame
from pygame.locals import *
from pygame.font import *
import time
import random

# display
pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
info_object = pygame.display.Info()

width, height = info_object.current_w, info_object.current_h

screen = pygame.display.set_mode((width, height))
fps = 60
pygame.display.set_caption('Mastering Balance')
clock = pygame.time.Clock()

# custom cursor
cursor_up = pygame.image.load('gui_images/cursorUp.png')
cursor_down = pygame.image.load('gui_images/cursorDown.png')
current_cursor = cursor_up
cursor_rect = cursor_up.get_rect()
pygame.mouse.set_visible(False)

# buttons
play_button = pygame.image.load('gui_images/play_button4x.png')  # play button
play_button_rect = play_button.get_rect(center=(info_object.current_w // 2, info_object.current_h // 2 + 150))
pressed_play_button = pygame.image.load('gui_images/pressed_play.png')

settings_button = pygame.image.load('gui_images/settings_button.png')  # settings button
settings_button_rect = settings_button.get_rect(center=(info_object.current_w // 2, (info_object.current_h // 2) + 300))
pressed_settings_button = pygame.image.load('gui_images/pressed_settings.png')

credits_button = pygame.image.load('gui_images/credits_button.png')  # credits button
credits_button_rect = credits_button.get_rect(center=(info_object.current_w // 2, (info_object.current_h // 2) + 450))
pressed_credits_button = pygame.image.load('gui_images/pressed_credits.png')

fps_30 = pygame.image.load('gui_images/30_fps_button.png')  # 30 fps button
fps_30_rect = fps_30.get_rect(center=(info_object.current_w // 2 - 150, (info_object.current_h // 2) + 100))
fps_30_pressed = pygame.image.load('gui_images/30_fps_pressed.png')

fps_60 = pygame.image.load('gui_images/60_fps_button.png')  # 60 fps button
fps_60_rect = fps_30.get_rect(center=(info_object.current_w // 2 + 100, (info_object.current_h // 2) + 100))
fps_60_pressed = pygame.image.load('gui_images/60_fps_pressed.png')

fps_144 = pygame.image.load('gui_images/144_fps_button.png')  # 144 fps button
fps_144_rect = fps_30.get_rect(center=(info_object.current_w // 2 + 350, (info_object.current_h // 2) + 100))
fps_144_pressed = pygame.image.load('gui_images/144_fps_pressed.png')

backbutton = pygame.image.load('gui_images/backbutton.png')
backbutton_rect1 = backbutton.get_rect(center=(info_object.current_w // 2 - 550, (info_object.current_h // 2 - 325)))
backbutton_rect2 = backbutton.get_rect(center=(info_object.current_w // 2 - 850, (info_object.current_h // 2 - 450)))
backbutton_rect3 = backbutton.get_rect(center=(info_object.current_w // 2 - 550, (info_object.current_h // 2 - 325)))
backbutton_pressed = pygame.image.load('gui_images/backbutton_hover.png')

menu_button = pygame.image.load('gui_images/menu.png')
menu_button_rect = menu_button.get_rect(center=(info_object.current_w // 2 - 800, (info_object.current_h // 2 - 450)))
menu_button_pressed = pygame.image.load('gui_images/pressed_menu.png')

exit_button = pygame.image.load('gui_images/exit.png')
exit_button_rect = menu_button.get_rect(center=(info_object.current_w // 2 + 650, (info_object.current_h // 2 - 325)))
exit_button_pressed = pygame.image.load('gui_images/exit_pressed.png')

quit_button = pygame.image.load('gui_images/quit.png')
quit_button_rect = quit_button.get_rect(center=(info_object.current_w // 2 + 900, (info_object.current_h // 2 - 475)))
quit_button_pressed = pygame.image.load('gui_images/quit_pressed.png')

# images
fps_text = pygame.image.load('gui_images/fps_display.png')
fps_text_rect = fps_text.get_rect(center=(info_object.current_w // 2 - 400, (info_object.current_h // 2) + 100))

master_vol = pygame.image.load('gui_images/master_vol.png')
master_vol_rect = master_vol.get_rect(center=(info_object.current_w // 2, (info_object.current_h // 2) - 250))

volume_bar = pygame.image.load('gui_images/volume_bar.png')
volume_bar_rect = volume_bar.get_rect(center=(info_object.current_w // 2, (info_object.current_h // 2) - 100))

volume_slider = pygame.image.load('gui_images/vol_slider.png')
volume_x, volume_y = info_object.current_w // 2, (info_object.current_h // 2) - 100
volume_slider_rect = volume_slider.get_rect(center=(volume_x, volume_y))

menu_background = pygame.image.load('gui_images/main_menu_background.png')
menu_background_rect = menu_background.get_rect(center=(info_object.current_w // 2, (info_object.current_h // 2)))

credits = pygame.image.load('gui_images/credits.png')
credits_rect = credits.get_rect(center=(info_object.current_w // 2, (info_object.current_h // 2)))

image = pygame.image.load('images2/main_character.png')
image_rect = image.get_rect()
image_rect.center = (400, 725)
random_enemy = pygame.image.load('images2/boss_one_defend.png')
random_enemy = pygame.transform.scale(random_enemy, (400, 400))
random_enemy_rect = random_enemy.get_rect()
random_enemy_rect.center = (200, 505)
capybara_enemy = pygame.image.load('images2/capybara.png')
capybara_enemy = pygame.transform.scale(capybara_enemy, (600, 600))
capybara_enemy_rect = capybara_enemy.get_rect()
capybara_enemy_rect.center = (200, 505)

background = pygame.image.load('images2/battle_background.png')
background = pygame.transform.scale(background, (width, height))
world_one_background = pygame.image.load('images2/world_one_background.jpg') 
world_one_background = pygame.transform.scale(world_one_background, (width, height))
world_two_background = pygame.image.load('images2/world_two_background.png')
world_two_background = pygame.transform.scale(world_two_background, (width, height))
city_one_background = pygame.image.load('images2/city_one_background.png')
city_one_background = pygame.transform.scale(city_one_background, (width, height))
selecting_moves_background = pygame.image.load('images2/selecting_moves_background.png')
selecting_moves_background = pygame.transform.scale(selecting_moves_background, (width, height))
store_background = pygame.image.load('images2/store_background.jpg')
store_background = pygame.transform.scale(store_background, (width, height))

# colours

Red = (255, 0, 0)
Darker_Red = (115, 10, 24)
Orange = (209, 113, 40)
Yellow = (255, 255, 0)
Green = (0, 255, 0)
Light_Green = (59, 138, 55)
Baby_Green = (178, 255, 102)
Blue = (0, 0, 255)
Darker_Blue = (78, 96, 204)
Purple = (255, 0, 255)

Black = (0, 0, 0)
White = (255, 255, 255)

Grey = (169, 169, 169)
Dark_Grey = (56, 56, 56)
Darker_Grey = (139, 139, 139)

gold = (255, 215, 0)
dark_brown = (101, 67, 33)
Brown = (139, 69, 19)
chest_width = 100
chest_height = 100
chest_rect = pygame.Rect(960 - chest_width // 2, 540 - chest_height // 2, chest_width, chest_height)

lid_width = 200
lid_height = 50
lid_rect = pygame.Rect(960 - lid_width // 2, 540 - chest_height // 2 - lid_height, lid_width, lid_height)

lock_width = 20
lock_height = 40
lock_rect = pygame.Rect(960 - chest_width // 2 + 40, 540 - chest_height // 2 + 30, lock_width, lock_height)



items = ["Side Block", "Roundhouse Kick", "Back Fist", "Slap", "Tackle", "1 inch punch", "Double Punch", "Side Kick", "Low Block", "Middle Block", "High Block", "Cross Punch", "Hook Punch", "Karate Chop", "Head Butt", "Jab", "Knife Hand Strike", "Tornado Kick", "540 Kick", "Force Palm Block", "Uppercut", "Flying Slide Kick", "Spear Hand Strike", "Tiger Elbow Strike"]
rarity = [60,60,60,60,60,45,45,45,45,45,45,35,35,35,35,35,10,10,10,1,1,1,1,1]
chest_content = None

# settings page
settings_page = pygame.image.load('gui_images/settings_page.png')
settings_page_rect = settings_page.get_rect(center=(info_object.current_w // 2, (info_object.current_h // 2)))

# gui variables
current_screen = 'main menu'
playing_screen = ''
running = True
slider_dragging = False  # track if the slider is being dragged
open_settings = False

# player variables

player_name = "Geoffrey" 
player_level = 5
player_attack_stat = 1 + player_level*.05
player_defense_stat = 1 + player_level*.05
player_total_health = int(100 + 5*player_level)
player_health = player_total_health
player_health_percent = 100
total_xp_needed = player_level * 20
current_xp = 0
money = 0

# movement/action variables

walking = True
slot = ""
slot_number = ""
slot_occupied = [False, False, False, False]
question = ""
damage_dealt = 0
damage_recieved = 0
block_defense = 1
enemy_block_defense = 1
large_font = pygame.font.SysFont(None, 80)
font = pygame.font.SysFont(None, 50)
small_font = pygame.font.SysFont(None, 30)
large_times = pygame.font.SysFont('Times New Roman', 80, bold=True)
times = pygame.font.SysFont('Times New Roman', 50, bold=True)
small_times = pygame.font.SysFont('Times New Roman', 30, bold=True)
speed = 1
current_time_1 = 0
current_time_2 = 0
current_time_3 = 0
current_time_4 = 0
new_time_1 = 0
new_time_2 = 0
new_time_3 = 0
new_time_4 = 0
move_one = ""
move_two = ""
move_three = ""
move_four = ""
move_one_color = Grey
move_two_color = Grey
move_three_color = Grey
move_four_color = Grey
attack_one_cooldown = True
attack_two_cooldown = True
attack_three_cooldown = True
attack_four_cooldown = True

Punch = True
Jab = False
Kick = False
Block = False

Fight = True
selecting_moves = True
Fighting = False
dead = False

jumping = False
up = 0
down = 0

# sound

background_music = pygame.mixer.music.load('sound/background_music.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
button_click = pygame.mixer.Sound('sound/button_sound.mp3')
button_click = pygame.mixer.Sound('sound/button_sound.mp3')
heal_sound = pygame.mixer.Sound('sound/heal_sound.mp3')


# action functions

def punch(slot):
    global move_one, move_two, move_three, move_four
    global move_one_speed, move_two_speed, move_three_speed, move_four_speed
    global move_one_damage, move_two_damage, move_three_damage, move_four_damage
    global move_one_color, move_two_color, move_three_color, move_four_color
    global move_one_cooldown, move_two_cooldown, move_three_cooldown, move_four_cooldown
    global move_one_defense, move_two_defense, move_three_defense, move_four_defense
    global move_one_type, move_two_type, move_three_type, move_four_type
    if slot == "1" and not slot_occupied[0]:
        move_one = "Punch"
        move_one_color = Darker_Blue
        move_one_speed = 1
        move_one_damage = 20
        move_one_cooldown = 2000
        move_one_defense = 1
        move_one_type = "Attack"
        slot_occupied[0] = True
        return True
    elif slot == "2" and not slot_occupied[1]:
        move_two = "Punch"
        move_two_color = Darker_Blue
        move_two_speed = 1
        move_two_damage = 20
        move_two_cooldown = 2000
        move_two_defense = 1
        move_two_type = "Attack"
        slot_occupied[1] = True
        return True
    elif slot == "3" and not slot_occupied[2]:
        move_three = "Punch"
        move_three_color = Darker_Blue
        move_three_speed = 1
        move_three_damage = 20
        move_three_cooldown = 2000
        move_three_defense = 1
        move_three_type = "Attack"
        slot_occupied[2] = True
        return True
    elif slot == "4" and not slot_occupied[3]:
        move_four = "Punch"
        move_four_color = Darker_Blue
        move_four_speed = 1
        move_four_damage = 20
        move_four_cooldown = 2000
        move_four_defense = 1
        move_four_type = "Attack"
        slot_occupied[3] = True
        return True
    else:
        return False
def jab(slot):
    global move_one, move_two, move_three, move_four
    global move_one_speed, move_two_speed, move_three_speed, move_four_speed
    global move_one_damage, move_two_damage, move_three_damage, move_four_damage
    global move_one_color, move_two_color, move_three_color, move_four_color
    global move_one_cooldown, move_two_cooldown, move_three_cooldown, move_four_cooldown
    global move_one_defense, move_two_defense, move_three_defense, move_four_defense
    global move_one_type, move_two_type, move_three_type, move_four_type
    if slot == "1" and not slot_occupied[0]:
        move_one = "Jab"
        move_one_color = Darker_Red
        move_one_speed = 2
        move_one_damage = 5
        move_one_cooldown = 200
        move_one_defense = 1
        move_one_type = "Attack"
        slot_occupied[0] = True
        return True
    elif slot == "2" and not slot_occupied[1]:
        move_two = "Jab"
        move_two_color = Darker_Red
        move_two_speed = 2
        move_two_damage = 5
        move_two_cooldown = 200
        move_two_defense = 1
        move_two_type = "Attack"
        slot_occupied[1] = True
        return True
    elif slot == "3" and not slot_occupied[2]:
        move_three = "Jab"
        move_three_color = Darker_Red
        move_three_speed = 2
        move_three_damage = 5
        move_three_cooldown = 200
        move_three_defense = 1
        move_three_type = "Attack"
        slot_occupied[2] = True
        return True
    elif slot == "4" and not slot_occupied[3]:
        move_four = "Jab"
        move_four_color = Darker_Red
        move_four_speed = 2
        move_four_damage = 5
        move_four_cooldown = 200
        move_four_defense = 1
        move_four_type = "Attack"
        slot_occupied[3] = True
        return True
    else:
        return False
def kick(slot):
    global move_one, move_two, move_three, move_four
    global move_one_speed, move_two_speed, move_three_speed, move_four_speed
    global move_one_damage, move_two_damage, move_three_damage, move_four_damage
    global move_one_color, move_two_color, move_three_color, move_four_color
    global move_one_cooldown, move_two_cooldown, move_three_cooldown, move_four_cooldown
    global move_one_defense, move_two_defense, move_three_defense, move_four_defense
    global move_one_type, move_two_type, move_three_type, move_four_type
    if slot == "1" and not slot_occupied[0]:
        move_one = "Kick"
        move_one_color = Orange
        move_one_speed = 1
        move_one_damage = 35
        move_one_cooldown = 3000
        move_one_defense = 1
        move_one_type = "Attack"
        slot_occupied[0] = True
        return True
    elif slot == "2" and not slot_occupied[1]:
        move_two = "Kick"
        move_two_color = Orange
        move_two_speed = 1
        move_two_damage = 35
        move_two_cooldown = 3000
        move_two_defense = 1
        move_two_type = "Attack"
        slot_occupied[1] = True
        return True
    elif slot == "3" and not slot_occupied[2]:
        move_three = "Kick"
        move_three_color = Orange
        move_three_speed = 1
        move_three_damage = 35
        move_three_cooldown = 3000
        move_three_defense = 1
        move_three_type = "Attack"
        slot_occupied[2] = True
        return True
    elif slot == "4" and not slot_occupied[3]:
        move_four = "Kick"
        move_four_color = Orange
        move_four_speed = 1
        move_four_damage = 35
        move_four_cooldown = 3000
        move_four_defense = 1
        move_four_type = "Attack"
        slot_occupied[3] = True
        return True
    else:
        return False
def block(slot):
    global move_one, move_two, move_three, move_four
    global move_one_speed, move_two_speed, move_three_speed, move_four_speed
    global move_one_damage, move_two_damage, move_three_damage, move_four_damage
    global move_one_color, move_two_color, move_three_color, move_four_color
    global move_one_cooldown, move_two_cooldown, move_three_cooldown, move_four_cooldown
    global move_one_defense, move_two_defense, move_three_defense, move_four_defense
    global move_one_type, move_two_type, move_three_type, move_four_type
    if slot == "1" and not slot_occupied[0]:
        move_one = "Block"
        move_one_color = Light_Green
        move_one_speed = 1
        move_one_damage = 10
        move_one_cooldown = 1000
        move_one_defense = 0.6
        move_one_type = "Defend"
        slot_occupied[0] = True
        return True
    elif slot == "2" and not slot_occupied[1]:
        move_two = "Block"
        move_two_color = Light_Green
        move_two_speed = 1
        move_two_damage = 10
        move_two_cooldown = 1000
        move_two_defense = 0.6
        move_two_type = "Defend"
        slot_occupied[1] = True
        return True
    elif slot == "3" and not slot_occupied[2]:
        move_three = "Block"
        move_three_color = Light_Green
        move_three_speed = 1
        move_three_damage = 10
        move_three_cooldown = 1000
        move_three_defense = 0.6
        move_three_type = "Defend"
        slot_occupied[2] = True
        return True
    elif slot == "4" and not slot_occupied[3]:
        move_four = "Block"
        move_four_color = Light_Green
        move_four_speed = 1
        move_four_damage = 10
        move_four_cooldown = 1000
        move_four_defense = 0.6
        move_four_type = "Defend"
        slot_occupied[3] = True
        return True
    else:
        return False
def side_block(slot):
    global move_one, move_two, move_three, move_four
    global move_one_speed, move_two_speed, move_three_speed, move_four_speed
    global move_one_damage, move_two_damage, move_three_damage, move_four_damage
    global move_one_color, move_two_color, move_three_color, move_four_color
    global move_one_cooldown, move_two_cooldown, move_three_cooldown, move_four_cooldown
    global move_one_defense, move_two_defense, move_three_defense, move_four_defense
    global move_one_type, move_two_type, move_three_type, move_four_type
    if slot == "1"  :
        move_one = "Side Block"
        move_one_color = Green
        move_one_speed = 1
        move_one_damage = 15
        move_one_cooldown = 3000
        move_one_defense = 0.5
        move_one_type = "Defend"
         
        return True
    elif slot == "2"  :
        move_two = "Side Block"
        move_two_color = Green
        move_two_speed = 1
        move_two_damage = 15
        move_two_cooldown = 3000
        move_two_defense = 0.5
        move_two_type = "Defend"
         
        return True
    elif slot == "3"  :
        move_three = "Side Block"
        move_three_color = Green
        move_three_speed = 1
        move_three_damage = 15
        move_three_cooldown = 3000
        move_three_defense = 0.5
        move_three_type = "Defend"
         
        return True
    elif slot == "4"  :
        move_four = "Side Block"
        move_four_color = Green
        move_four_speed = 1
        move_four_damage = 15
        move_four_cooldown = 3000
        move_four_defense = 0.5
        move_four_type = "Defend"
         
        return True
    else:
        return False

def round_house_kick(slot):
    global move_one, move_two, move_three, move_four
    global move_one_speed, move_two_speed, move_three_speed, move_four_speed
    global move_one_damage, move_two_damage, move_three_damage, move_four_damage
    global move_one_color, move_two_color, move_three_color, move_four_color
    global move_one_cooldown, move_two_cooldown, move_three_cooldown, move_four_cooldown
    global move_one_defense, move_two_defense, move_three_defense, move_four_defense
    global move_one_type, move_two_type, move_three_type, move_four_type
    if slot == "1"  :
       move_one = "Roundhouse Kick"
       move_one_color = Orange
       move_one_speed = 1
       move_one_damage = 40
       move_one_cooldown = 4000
       move_one_defense = 1
       move_one_type = "Attack"
        
       return True
    elif slot == "2"  :
       move_two = "Roundhouse Kick"
       move_two_color = Orange
       move_two_speed = 1
       move_two_damage = 40
       move_two_cooldown = 4000
       move_two_defense = 1
       move_two_type = "Attack"
   
       return True
    elif slot == "3"  :
       move_three = "Roundhouse Kick"
       move_three_color = Orange
       move_three_speed = 1
       move_three_damage = 40
       move_three_cooldown = 4000
       move_three_defense = 1
       move_three_type = "Attack"
      
       return True
    elif slot == "4"  :
       move_four = "Roundhouse Kick"
       move_four_color = Orange
       move_four_speed = 1
       move_four_damage = 40
       move_four_cooldown = 4000
       move_four_defense = 1
       move_four_type = "Attack"
   
       return True
    else:
       return False

def back_fist(slot):
    global move_one, move_two, move_three, move_four
    global move_one_speed, move_two_speed, move_three_speed, move_four_speed
    global move_one_damage, move_two_damage, move_three_damage, move_four_damage
    global move_one_color, move_two_color, move_three_color, move_four_color
    global move_one_cooldown, move_two_cooldown, move_three_cooldown, move_four_cooldown
    global move_one_defense, move_two_defense, move_three_defense, move_four_defense
    global move_one_type, move_two_type, move_three_type, move_four_type
    if slot == "1"  :
       move_one = "Back Fist"
       move_one_color = Darker_Blue
       move_one_speed = 1
       move_one_damage = 35
       move_one_cooldown = 3500
       move_one_defense = 1
       move_one_type = "Attack"
       
       return True
    elif slot == "2"  :
       move_two = "Back Fist"
       move_two_color = Darker_Blue
       move_two_speed = 1
       move_two_damage = 35
       move_two_cooldown = 3500
       move_two_defense = 1
       move_two_type = "Attack"
       
       return True
    elif slot == "3" :
       move_three = "Back Fist"
       move_three_color = Darker_Blue
       move_three_speed = 1
       move_three_damage = 35
       move_three_cooldown = 3500
       move_three_defense = 1
       move_three_type = "Attack"
       
       return True
    elif slot == "4" : 
       move_four = "Back Fist"
       move_four_color = Darker_Blue
       move_four_speed = 1
       move_four_damage = 35
       move_four_cooldown = 3500
       move_four_defense = 1
       move_four_type = "Attack"
       
       return True
    else:
       return False

def slap(slot):
    global move_one, move_two, move_three, move_four
    global move_one_speed, move_two_speed, move_three_speed, move_four_speed
    global move_one_damage, move_two_damage, move_three_damage, move_four_damage
    global move_one_color, move_two_color, move_three_color, move_four_color
    global move_one_cooldown, move_two_cooldown, move_three_cooldown, move_four_cooldown
    global move_one_defense, move_two_defense, move_three_defense, move_four_defense
    global move_one_type, move_two_type, move_three_type, move_four_type
    if slot == "1"  :
       move_one = "Slap"
       move_one_color = Darker_Red
       move_one_speed = 1
       move_one_damage = 15
       move_one_cooldown = 1500
       move_one_defense = 1
       move_one_type = "Attack"
       
       return True
    elif slot == "2"  :
       move_two = "Slap"
       move_two_color = Darker_Red
       move_two_speed = 1
       move_two_damage = 15
       move_two_cooldown = 1500
       move_two_defense = 1
       move_two_type = "Attack"
       
       return True
    elif slot == "3"  :
       move_three = "Slap"
       move_three_color = Darker_Red
       move_three_speed = 1
       move_three_damage = 15
       move_three_cooldown = 1500
       move_three_defense = 1
       move_three_type = "Attack"
       
       return True
    elif slot == "4"  :
       move_four = "Slap"
       move_four_color = Darker_Red
       move_four_speed = 1
       move_four_damage = 15
       move_four_cooldown = 1500
       move_four_defense = 1
       move_four_type = "Attack"
       
       return True
    else:
       return False
def tackle(slot):
    global move_one, move_two, move_three, move_four
    global move_one_speed, move_two_speed, move_three_speed, move_four_speed
    global move_one_damage, move_two_damage, move_three_damage, move_four_damage
    global move_one_color, move_two_color, move_three_color, move_four_color
    global move_one_cooldown, move_two_cooldown, move_three_cooldown, move_four_cooldown
    global move_one_defense, move_two_defense, move_three_defense, move_four_defense
    global move_one_type, move_two_type, move_three_type, move_four_type
    if slot == "1"  :
       move_one = "Tackle"
       move_one_color = Orange
       move_one_speed = 1
       move_one_damage = 50
       move_one_cooldown = 4000
       move_one_defense = 1
       move_one_type = "Attack"
       
       return True
    elif slot == "2"  :
       move_two = "Tackle"
       move_two_color = Orange
       move_two_speed = 1
       move_two_damage = 50
       move_two_cooldown = 4000
       move_two_defense = 1
       move_two_type = "Attack"
       
       return True
    elif slot == "3"  :
       move_three = "Tackle"
       move_three_color = Orange
       move_three_speed = 1
       move_three_damage = 50
       move_three_cooldown = 4000
       move_three_defense = 1
       move_three_type = "Attack"
       
       return True
    elif slot == "4" : 
       move_four = "Tackle"
       move_four_color = Orange
       move_four_speed = 1
       move_four_damage = 50
       move_four_cooldown = 4000
       move_four_defense = 1
       move_four_type = "Attack"
       
       return True
    else:
       return False
    
def one_inch_punch(slot):
    global move_one, move_two, move_three, move_four
    global move_one_speed, move_two_speed, move_three_speed, move_four_speed
    global move_one_damage, move_two_damage, move_three_damage, move_four_damage
    global move_one_color, move_two_color, move_three_color, move_four_color
    global move_one_cooldown, move_two_cooldown, move_three_cooldown, move_four_cooldown
    global move_one_defense, move_two_defense, move_three_defense, move_four_defense
    global move_one_type, move_two_type, move_three_type, move_four_type
    if slot == "1"  :
       move_one = "1 Inch Punch"
       move_one_color = Darker_Blue
       move_one_speed = 1
       move_one_damage = 60
       move_one_cooldown = 2500
       move_one_defense = 1
       move_one_type = "Attack"
       
       return True
    elif slot == "2":
       move_two = "1 Inch Punch"
       move_two_color = Darker_Blue 
       move_two_speed = 1
       move_two_damage = 60
       move_two_cooldown = 2500
       move_two_defense = 1
       move_two_type = "Attack"
       
       return True
    elif slot == "3":
       move_three = "1 Inch Punch"
       move_three_color = Darker_Blue 
       move_three_speed = 1
       move_three_damage = 60
       move_three_cooldown = 2500
       move_three_defense = 1
       move_three_type = "Attack"
       
       return True
    elif slot == "4" : 
       move_four = "1 Inch Punch "
       move_four_color = Darker_Blue
       move_four_speed = 1
       move_four_damage = 60
       move_four_cooldown = 2500
       move_four_defense = 1
       move_four_type = "Attack"
       
       return True
    else:
       return False
def double_punch(slot):
    global move_one, move_two, move_three, move_four
    global move_one_speed, move_two_speed, move_three_speed, move_four_speed
    global move_one_damage, move_two_damage, move_three_damage, move_four_damage
    global move_one_color, move_two_color, move_three_color, move_four_color
    global move_one_cooldown, move_two_cooldown, move_three_cooldown, move_four_cooldown
    global move_one_defense, move_two_defense, move_three_defense, move_four_defense
    global move_one_type, move_two_type, move_three_type, move_four_type
    if slot == "1"  :
       move_one = "Double Punch"
       move_one_color = Darker_Blue
       move_one_speed = 1
       move_one_damage = 60
       move_one_cooldown = 3000
       move_one_defense = 1
       move_one_type = "Attack"
       
       return True
    elif slot == "2"  :
       move_two = "Double Punch"
       move_two_color = Darker_Blue
       move_two_speed = 1
       move_two_damage = 60
       move_two_cooldown = 3000
       move_two_defense = 1
       move_two_type = "Attack"
       
       return True
    elif slot == "3"  :
       move_three = "Double Punch"
       move_three_color = Darker_Blue
       move_three_speed = 1
       move_three_damage = 60
       move_three_cooldown = 3000
       move_three_defense = 1
       move_three_type = "Attack"
       
       return True
    elif slot == "4"  :
       move_four = "Double Punch"
       move_four_color = Darker_Blue
       move_four_speed = 1
       move_four_damage = 60
       move_four_cooldown = 3000
       move_four_defense = 1
       move_four_type = "Attack"
       
       return True
    else:
       return False

def side_kick(slot):
    global move_one, move_two, move_three, move_four
    global move_one_speed, move_two_speed, move_three_speed, move_four_speed
    global move_one_damage, move_two_damage, move_three_damage, move_four_damage
    global move_one_color, move_two_color, move_three_color, move_four_color
    global move_one_cooldown, move_two_cooldown, move_three_cooldown, move_four_cooldown
    global move_one_defense, move_two_defense, move_three_defense, move_four_defense
    global move_one_type, move_two_type, move_three_type, move_four_type
    if slot == "1"  :
       move_one = "Side Kick"
       move_one_color = Orange
       move_one_speed = 1
       move_one_damage = 45
       move_one_cooldown = 2000
       move_one_defense = 1
       move_one_type = "Attack"
       
       return True
    elif slot == "2"  :
       move_two = "Side Kick"
       move_two_color = Orange
       move_two_speed = 1
       move_two_damage = 45
       move_two_cooldown = 2000
       move_two_defense = 1
       move_two_type = "Attack"
       
       return True
    elif slot == "3"  :
       move_three = "Side Kick"
       move_three_color = Orange
       move_three_speed = 1
       move_three_damage = 45
       move_three_cooldown = 2000
       move_three_defense = 1
       move_three_type = "Attack"
       
       return True
    elif slot == "4"  :
       move_four = "Side Kick"
       move_four_color = Orange
       move_four_speed = 1
       move_four_damage = 45
       move_four_cooldown = 2000
       move_four_defense = 1
       move_four_type = "Attack"
       
       return True
    else:
       return False

def low_block(slot):
    global move_one, move_two, move_three, move_four
    global move_one_speed, move_two_speed, move_three_speed, move_four_speed
    global move_one_damage, move_two_damage, move_three_damage, move_four_damage
    global move_one_color, move_two_color, move_three_color, move_four_color
    global move_one_cooldown, move_two_cooldown, move_three_cooldown, move_four_cooldown
    global move_one_defense, move_two_defense, move_three_defense, move_four_defense
    global move_one_type, move_two_type, move_three_type, move_four_type
    if slot == "1"  :
       move_one = "Low Block"
       move_one_color = Green
       move_one_speed = 1
       move_one_damage = 30
       move_one_cooldown = 2000
       move_one_defense = 0.6
       move_one_type = "Defend"
       
       return True
    elif slot == "2"  :
       move_two = "Low Block"
       move_two_color = Green
       move_two_speed = 1
       move_two_damage = 30
       move_two_cooldown = 2000
       move_two_defense = 0.6
       move_two_type = "Defend"
       
       return True
    elif slot == "3"  :
       move_three = "Low Block"
       move_three_color = Green
       move_three_speed = 1
       move_three_damage = 30
       move_three_cooldown = 2000
       move_three_defense = 0.6
       move_three_type = "Defend"
       
       return True
    elif slot == "4"  :
       move_four = "Low Block"
       move_four_color = Green
       move_four_speed = 1
       move_four_damage = 30
       move_four_cooldown = 2000
       move_four_defense = 0.6
       move_four_type = "Defend"
       
       return True
    else:
       return False

def middle_block(slot):
    global move_one, move_two, move_three, move_four
    global move_one_speed, move_two_speed, move_three_speed, move_four_speed
    global move_one_damage, move_two_damage, move_three_damage, move_four_damage
    global move_one_color, move_two_color, move_three_color, move_four_color
    global move_one_cooldown, move_two_cooldown, move_three_cooldown, move_four_cooldown
    global move_one_defense, move_two_defense, move_three_defense, move_four_defense
    global move_one_type, move_two_type, move_three_type, move_four_type
    if slot == "1"  :
       move_one = "Middle Block"
       move_one_color = Green
       move_one_speed = 1
       move_one_damage = 25
       move_one_cooldown = 2500
       move_one_defense = 0.7
       move_one_type = "Defend"
       
       return True
    elif slot == "2"  :
       move_two = "Middle Block"
       move_two_color = Green
       move_two_speed = 1
       move_two_damage = 25
       move_two_cooldown = 2500
       move_two_defense = 0.7
       move_two_type = "Defend"
       
       return True
    elif slot == "3"  :
       move_three = "Middle Block"
       move_three_color = Green
       move_three_speed = 1
       move_three_damage = 25
       move_three_cooldown = 2500
       move_three_defense = 0.7
       move_three_type = "Defend"
       
       return True
    elif slot == "4"  :
       move_four = "Middle Block"
       move_four_color = Green
       move_four_speed = 1
       move_four_damage = 25
       move_four_cooldown = 2500
       move_four_defense = 0.7
       move_four_type = "Defend"
       
       return True
    else:
       return False

def high_block(slot):
    global move_one, move_two, move_three, move_four
    global move_one_speed, move_two_speed, move_three_speed, move_four_speed
    global move_one_damage, move_two_damage, move_three_damage, move_four_damage
    global move_one_color, move_two_color, move_three_color, move_four_color
    global move_one_cooldown, move_two_cooldown, move_three_cooldown, move_four_cooldown
    global move_one_defense, move_two_defense, move_three_defense, move_four_defense
    global move_one_type, move_two_type, move_three_type, move_four_type
    if slot == "1"  :
       move_one = "High Block"
       move_one_color = Green
       move_one_speed = 1
       move_one_damage = 25
       move_one_cooldown = 3000
       move_one_defense = 0.8
       move_one_type = "Defend"
       
       return True
    elif slot == "2"  :
       move_two = "High Block"
       move_two_color = Green
       move_two_speed = 1
       move_two_damage = 25
       move_two_cooldown = 3000
       move_two_defense = 0.8
       move_two_type = "Defend"
       
       return True
    elif slot == "3"  :
       move_three = "Low Block"
       move_three_color = Green
       move_three_speed = 1
       move_three_damage = 25
       move_three_cooldown = 3000
       move_three_defense = 0.8
       move_three_type = "Defend"
       
       return True
    elif slot == "4"  :
       move_four = "Low Block"
       move_four_color = Green
       move_four_speed = 1
       move_four_damage = 25
       move_four_cooldown = 3000
       move_four_defense = 0.8
       move_four_type = "Defend"
       
       return True
    else:
       return False

def cross_punch(slot):
    global move_one, move_two, move_three, move_four
    global move_one_speed, move_two_speed, move_three_speed, move_four_speed
    global move_one_damage, move_two_damage, move_three_damage, move_four_damage
    global move_one_color, move_two_color, move_three_color, move_four_color
    global move_one_cooldown, move_two_cooldown, move_three_cooldown, move_four_cooldown
    global move_one_defense, move_two_defense, move_three_defense, move_four_defense
    global move_one_type, move_two_type, move_three_type, move_four_type
    if slot == "1"  :
       move_one = "Cross Punch"
       move_one_color = Darker_Blue
       move_one_speed = 1
       move_one_damage = 60
       move_one_cooldown = 2500
       move_one_defense = 1
       move_one_type = "Attack"
       
       return True
    elif slot == "2"  :
       move_two = "Cross Punch"
       move_two_color = Darker_Blue
       move_two_speed = 1
       move_two_damage = 60
       move_two_cooldown = 2500
       move_two_defense = 1
       move_two_type = "Attack"
       
       return True
    elif slot == "3"  :
       move_three = "Cross Punch"
       move_three_color = Darker_Blue
       move_three_speed = 1
       move_three_damage = 60
       move_three_cooldown = 2500
       move_three_defense = 1
       move_three_type = "Attack"
       
       return True
    elif slot == "4"  :
       move_four = "Cross Punch"
       move_four_color = Darker_Blue
       move_four_speed = 1
       move_four_damage = 60
       move_four_cooldown = 2500
       move_four_defense = 1
       move_four_type = "Attack"
       
       return True
    else:
       return False

def hook_punch(slot):
    global move_one, move_two, move_three, move_four
    global move_one_speed, move_two_speed, move_three_speed, move_four_speed
    global move_one_damage, move_two_damage, move_three_damage, move_four_damage
    global move_one_color, move_two_color, move_three_color, move_four_color
    global move_one_cooldown, move_two_cooldown, move_three_cooldown, move_four_cooldown
    global move_one_defense, move_two_defense, move_three_defense, move_four_defense
    global move_one_type, move_two_type, move_three_type, move_four_type
    if slot == "1"  :
       move_one = "Hook Punch"
       move_one_color = Darker_Blue
       move_one_speed = 1
       move_one_damage = 90
       move_one_cooldown = 2500
       move_one_defense = 1
       move_one_type = "Attack"
       
       return True
    elif slot == "2"  :
       move_two = "Hook Punch"
       move_two_color = Darker_Blue
       move_two_speed = 1
       move_two_damage = 90
       move_two_cooldown = 2500
       move_two_defense = 1
       move_two_type = "Attack"
       
       return True
    elif slot == "3"  :
       move_three = "Hook Punch"
       move_three_color = Darker_Blue
       move_three_speed = 1
       move_three_damage = 90
       move_three_cooldown = 2500
       move_three_defense = 1
       move_three_type = "Attack"
       
       return True
    elif slot == "4"  :
       move_four = "Hook Punch"
       move_four_color = Darker_Blue
       move_four_speed = 1
       move_four_damage = 90
       move_four_cooldown = 2500
       move_four_defense = 1
       move_four_type = "Attack"
       
       return True
    else:
       return False

def karate_chop(slot):
    global move_one, move_two, move_three, move_four
    global move_one_speed, move_two_speed, move_three_speed, move_four_speed
    global move_one_damage, move_two_damage, move_three_damage, move_four_damage
    global move_one_color, move_two_color, move_three_color, move_four_color
    global move_one_cooldown, move_two_cooldown, move_three_cooldown, move_four_cooldown
    global move_one_defense, move_two_defense, move_three_defense, move_four_defense
    global move_one_type, move_two_type, move_three_type, move_four_type
    if slot == "1"  :
       move_one = "Karate Chop"
       move_one_color = Darker_Blue
       move_one_speed = 1
       move_one_damage = 80
       move_one_cooldown = 2000
       move_one_defense = 1
       move_one_type = "Attack"
       
       return True
    elif slot == "2"  :
       move_two = "Karate Chop"
       move_two_color = Darker_Blue
       move_two_speed = 1
       move_two_damage = 80
       move_two_cooldown = 2000
       move_two_defense = 1
       move_two_type = "Attack"
       
       return True
    elif slot == "3"  :
       move_three = "Karate Chop"
       move_three_color = Darker_Blue
       move_three_speed = 1
       move_three_damage = 80
       move_three_cooldown = 2000
       move_three_defense = 1
       move_three_type = "Attack"
       
       return True
    elif slot == "4"  :
       move_four = "Karate Chop"
       move_four_color = Darker_Blue
       move_four_speed = 1
       move_four_damage = 80
       move_four_cooldown = 2000
       move_four_defense = 1
       move_four_type = "Attack"
       
       return True
    else:
       return False

def head_butt(slot):
    global move_one, move_two, move_three, move_four
    global move_one_speed, move_two_speed, move_three_speed, move_four_speed
    global move_one_damage, move_two_damage, move_three_damage, move_four_damage
    global move_one_color, move_two_color, move_three_color, move_four_color
    global move_one_cooldown, move_two_cooldown, move_three_cooldown, move_four_cooldown
    global move_one_defense, move_two_defense, move_three_defense, move_four_defense
    global move_one_type, move_two_type, move_three_type, move_four_type
    if slot == "1"  :
       move_one = "Head Butt"
       move_one_color = Orange
       move_one_speed = 1
       move_one_damage = 120
       move_one_cooldown = 3000
       move_one_defense = 1
       move_one_type = "Attack"
       
       return True
    elif slot == "2"  :
       move_two = "Head Butt"
       move_two_color = Orange
       move_two_speed = 1
       move_two_damage = 120
       move_two_cooldown = 2000
       move_two_defense = 1
       move_two_type = "Attack"
       return True
    elif slot == "3"  :
       move_three = "Head Butt"
       move_three_color = Orange
       move_three_speed = 1
       move_three_damage = 120
       move_three_cooldown = 2000
       move_three_defense = 1
       move_three_type = "Attack"
       
       return True
    elif slot == "4"  :
       move_four = "Head Butt"
       move_four_color = Orange
       move_four_speed = 1
       move_four_damage = 120
       move_four_cooldown = 2000
       move_four_defense = 1
       move_four_type = "Attack"
       return True
    else:
       return False

def knife_hand_strike(slot):
    global move_one, move_two, move_three, move_four
    global move_one_speed, move_two_speed, move_three_speed, move_four_speed
    global move_one_damage, move_two_damage, move_three_damage, move_four_damage
    global move_one_color, move_two_color, move_three_color, move_four_color
    global move_one_cooldown, move_two_cooldown, move_three_cooldown, move_four_cooldown
    global move_one_defense, move_two_defense, move_three_defense, move_four_defense
    global move_one_type, move_two_type, move_three_type, move_four_type
    if slot == "1"  :
       move_one = "Knife Hand Strike"
       move_one_color = Darker_Blue
       move_one_speed = 1
       move_one_damage = 95
       move_one_cooldown = 1000
       move_one_defense = 1
       move_one_type = "Attack"
       
       return True
    elif slot == "2"  :
       move_two = "Knife Hand Strike"
       move_two_color = Darker_Blue
       move_two_speed = 1
       move_two_damage = 95
       move_two_cooldown = 1000
       move_two_defense = 1
       move_two_type = "Attack"
       
       return True
    elif slot == "3"  :
       move_three = "Knife Hand Strike"
       move_three_color = Darker_Blue
       move_three_speed = 1
       move_three_damage = 95
       move_three_cooldown = 1000
       move_three_defense = 1
       move_three_type = "Attack"
       
       return True
    elif slot == "4"  :
       move_four = "Knife Hand Strike"
       move_four_color = Darker_Blue
       move_four_speed = 1
       move_four_damage = 95
       move_four_cooldown = 1000
       move_four_defense = 1
       move_four_type = "Attack"
       
       return True
    else:
       return False

def tornado_kick(slot):
    global move_one, move_two, move_three, move_four
    global move_one_speed, move_two_speed, move_three_speed, move_four_speed
    global move_one_damage, move_two_damage, move_three_damage, move_four_damage
    global move_one_color, move_two_color, move_three_color, move_four_color
    global move_one_cooldown, move_two_cooldown, move_three_cooldown, move_four_cooldown
    global move_one_defense, move_two_defense, move_three_defense, move_four_defense
    global move_one_type, move_two_type, move_three_type, move_four_type
    if slot == "1"  :
       move_one = "Tornado Kick"
       move_one_color = Darker_Red
       move_one_speed = 1
       move_one_damage = 110
       move_one_cooldown = 1
       move_one_defense = 1
       move_one_type = "Attack"
       
       return True
    elif slot == "2"  :
       move_two = "Tornado Kick"
       move_two_color = Darker_Red
       move_two_speed = 1
       move_two_damage = 110
       move_two_cooldown = 1000
       move_two_defense = 1
       move_two_type = "Attack"
       
       return True
    elif slot == "3"  :
       move_three = "Tornado Kick"
       move_three_color = Darker_Red
       move_three_speed = 1
       move_three_damage = 110
       move_three_cooldown = 1000
       move_three_defense = 1
       move_three_type = "Attack"
       
       return True
    elif slot == "4"  :
       move_four = "Tornado Kick"
       move_four_color = Darker_Red
       move_four_speed = 1
       move_four_damage = 110
       move_four_cooldown = 1000
       move_four_defense = 1
       move_four_type = "Attack"
       
       return True
    else:
       return False
    
def five_hundred_forty_kick(slot):
    global move_one, move_two, move_three, move_four
    global move_one_speed, move_two_speed, move_three_speed, move_four_speed
    global move_one_damage, move_two_damage, move_three_damage, move_four_damage
    global move_one_color, move_two_color, move_three_color, move_four_color
    global move_one_cooldown, move_two_cooldown, move_three_cooldown, move_four_cooldown
    global move_one_defense, move_two_defense, move_three_defense, move_four_defense
    global move_one_type, move_two_type, move_three_type, move_four_type
    if slot == "1"  :
       move_one = "540 Kick"
       move_one_color = Darker_Red
       move_one_speed = 1
       move_one_damage = 150
       move_one_cooldown = 1500
       move_one_defense = 1
       move_one_type = "Attack"
       
       return True
    elif slot == "2"  :
       move_two = "540 Kick"
       move_two_color = Darker_Red
       move_two_speed = 1
       move_two_damage = 150
       move_two_cooldown = 1500
       move_two_defense = 1
       move_two_type = "Attack"
       
       return True
    elif slot == "3"  :
       move_three = "540 Kick"
       move_three_color = Darker_Red
       move_three_speed = 1
       move_three_damage = 150
       move_three_cooldown = 1500
       move_three_defense = 1
       move_three_type = "Attack"
       
       return True
    elif slot == "4"  :
       move_four = "540 Kick"
       move_four_color = Darker_Red
       move_four_speed = 1
       move_four_damage = 150
       move_four_cooldown = 1500
       move_four_defense = 1
       move_four_type = "Attack"
       
       return True
    else:
       return False

def ult_force_palm_block_def(slot):
    global move_one, move_two, move_three, move_four
    global move_one_speed, move_two_speed, move_three_speed, move_four_speed
    global move_one_damage, move_two_damage, move_three_damage, move_four_damage
    global move_one_color, move_two_color, move_three_color, move_four_color
    global move_one_cooldown, move_two_cooldown, move_three_cooldown, move_four_cooldown
    global move_one_defense, move_two_defense, move_three_defense, move_four_defense
    global move_one_type, move_two_type, move_three_type, move_four_type
    if slot == "1"  :
       move_one = "Force Palm Block"
       move_one_color = Green
       move_one_speed = 1
       move_one_damage = 60
       move_one_cooldown = 1000
       move_one_defense = 0.8
       move_one_type = "Defend"
       
       return True
    elif slot == "2"  :
       move_two = "Force Palm Block"
       move_two_color = Green
       move_two_speed = 1
       move_two_damage = 60
       move_two_cooldown = 1000
       move_two_defense = 0.8
       move_two_type = "Defend"
       
       return True
    elif slot == "3"  :
       move_three = "Force Palm Block"
       move_three_color = Green
       move_three_speed = 1
       move_three_damage = 60
       move_three_cooldown = 1000
       move_three_defense = 0.8
       move_three_type = "Defend"
       
       return True
    elif slot == "4"  :
       move_four = "Force Palm Block"
       move_four_color = Green
       move_four_speed = 1
       move_four_damage = 60
       move_four_cooldown = 1000
       move_four_defense = 0.8
       move_four_type = "Defend"
       
       return True
    else:
       return False

def ult_uppercut_off(slot):
    global move_one, move_two, move_three, move_four
    global move_one_speed, move_two_speed, move_three_speed, move_four_speed
    global move_one_damage, move_two_damage, move_three_damage, move_four_damage
    global move_one_color, move_two_color, move_three_color, move_four_color
    global move_one_cooldown, move_two_cooldown, move_three_cooldown, move_four_cooldown
    global move_one_defense, move_two_defense, move_three_defense, move_four_defense
    global move_one_type, move_two_type, move_three_type, move_four_type
    if slot == "1"  :
       move_one = "Uppercut"
       move_one_color = Darker_Red
       move_one_speed = 1
       move_one_damage = 120
       move_one_cooldown = 1000
       move_one_defense = 1
       move_one_type = "Attack"
       
       return True
    elif slot == "2" : 
       move_two = "Uppercut"
       move_two_color = Darker_Red
       move_two_speed = 1
       move_two_damage = 120
       move_two_cooldown = 1000
       move_two_defense = 1
       move_two_type = "Attack"
       
       return True
    elif slot == "3"  :
       move_three = "Uppercut"
       move_three_color = Darker_Red
       move_three_speed = 1
       move_three_damage = 120
       move_three_cooldown = 1000
       move_three_defense = 1
       move_three_type = "Attack"
       
       return True
    elif slot == "4"  :
       move_four = "Uppercut"
       move_four_color = Darker_Red
       move_four_speed = 1
       move_four_damage = 120
       move_four_cooldown = 1000
       move_four_defense = 1
       move_four_type = "Attack"
        
       return True
    else:
       return False

def ult_flying_slide_kick_sp(slot):
    global move_one, move_two, move_three, move_four
    global move_one_speed, move_two_speed, move_three_speed, move_four_speed
    global move_one_damage, move_two_damage, move_three_damage, move_four_damage
    global move_one_color, move_two_color, move_three_color, move_four_color
    global move_one_cooldown, move_two_cooldown, move_three_cooldown, move_four_cooldown
    global move_one_defense, move_two_defense, move_three_defense, move_four_defense
    global move_one_type, move_two_type, move_three_type, move_four_type
    if slot == "1":
       move_one = "Flying Slide Kick"
       move_one_color = Darker_Blue
       move_one_speed = 1
       move_one_damage = 80
       move_one_cooldown = 500
       move_one_defense = 1
       move_one_type = "Attack"
        
       return True
    elif slot == "2"  :
       move_two = "Flying Slide Kick"
       move_two_color = Darker_Blue
       move_two_speed = 1
       move_two_damage = 80
       move_two_cooldown = 500
       move_two_defense = 1
       move_two_type = "Attack"
        
       return True
    elif slot == "3"  :
       move_three = "Flying Slide Kick"
       move_three_color = Darker_Blue
       move_three_speed = 1
       move_three_damage = 80
       move_three_cooldown = 500
       move_three_defense = 1
       move_three_type = "Attack"
        
       return True
    elif slot == "4"  :
       move_four = "Flying Slide Kick"
       move_four_color = Darker_Blue
       move_four_speed = 1
       move_four_damage = 80
       move_four_cooldown = 500
       move_four_defense = 1
       move_four_type = "Attack"
        
       return True
    else:
       return False

def ult_spear_hand_strike_sr(slot):
    global move_one, move_two, move_three, move_four
    global move_one_speed, move_two_speed, move_three_speed, move_four_speed
    global move_one_damage, move_two_damage, move_three_damage, move_four_damage
    global move_one_color, move_two_color, move_three_color, move_four_color
    global move_one_cooldown, move_two_cooldown, move_three_cooldown, move_four_cooldown
    global move_one_defense, move_two_defense, move_three_defense, move_four_defense
    global move_one_type, move_two_type, move_three_type, move_four_type
    if slot == "1":
       move_one = "Spear Hand Strike"
       move_one_color = Darker_Blue
       move_one_speed = 1
       move_one_damage = 60
       move_one_cooldown = 5000
       move_one_defense = 1
       move_one_type = "Attack"
        
       return True
    elif slot == "2"  :
       move_two = "Spear Hand Strike"
       move_two_color = Darker_Blue
       move_two_speed = 1
       move_two_damage = 60
       move_two_cooldown = 500
       move_two_defense = 1
       move_two_type = "Attack"
        
       return True
    elif slot == "3"  :
       move_three = "Spear Hand Strike"
       move_three_color = Darker_Blue
       move_three_speed = 1
       move_three_damage = 60
       move_three_cooldown = 500
       move_three_defense = 1
       move_three_type = "Attack"
        
       return True
    elif slot == "4"  :
       move_four = "Spear Hand Strike"
       move_four_color = Darker_Blue
       move_four_speed = 1
       move_four_damage = 60
       move_four_cooldown = 500
       move_four_defense = 1
       move_four_type = "Attack"
        
       return True
    else:
       return False

def ult_tiger_elbow_Strike(slot):
    global move_one, move_two, move_three, move_four
    global move_one_speed, move_two_speed, move_three_speed, move_four_speed
    global move_one_damage, move_two_damage, move_three_damage, move_four_damage
    global move_one_color, move_two_color, move_three_color, move_four_color
    global move_one_cooldown, move_two_cooldown, move_three_cooldown, move_four_cooldown
    global move_one_defense, move_two_defense, move_three_defense, move_four_defense
    global move_one_type, move_two_type, move_three_type, move_four_type
    if slot == "1":
       move_one = "Tiger Elbow Strike"
       move_one_color = Orange
       move_one_speed = 1
       move_one_damage = 300
       move_one_cooldown = 1000
       move_one_defense = 1
       move_one_type = "Attack"
        
       return True
    elif slot == "2"  :
       move_two = "Tiger Elbow Strike"
       move_two_color = Orange
       move_two_speed = 1
       move_two_damage = 300
       move_two_cooldown = 1000
       move_two_defense = 1
       move_two_type = "Attack"
        
       return True
    elif slot == "3"  :
       move_three = "Tiger Elbow Strike"
       move_three_color = Orange
       move_three_speed = 1
       move_three_damage = 300
       move_three_cooldown = 1000
       move_three_defense = 1
       move_three_type = "Attack"
        
       return True
    elif slot == "4"  :
       move_four = "Tiger Elbow Strike"
       move_four_color = Orange
       move_four_speed = 1
       move_four_damage = 300
       move_four_cooldown = 1000
       move_four_defense = 1
       move_four_type = "Attack"
        
       return True
    else:
       return False
# keybind selection
def selecting_moves_menu():
    global selecting_moves, question, Punch, slot_number, fps, running
    while selecting_moves:
        button = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        screen.blit(selecting_moves_background, (0, 0))
        where_text = large_times.render(question, True, White)
        where_text_rect = where_text.get_rect()
        where_text_rect.topleft=((1920 - where_text_rect.width)/2, 200)
        screen.blit(where_text, where_text_rect)
        if button[pygame.K_1]:
            slot_number = "1"
        elif button[pygame.K_2]:
            slot_number = "2"
        elif button[pygame.K_3]:
            slot_number = "3"
        elif button[pygame.K_4]:
            slot_number = "4"
        if Punch: 
            question = "Where would you like to place Punch?"
            move_name = "Punch"
            move_type = "Medium Attack"
            move_color = Darker_Blue
            description = "A medium attack dealing 20 damage, with a 2 second cooldown"
            if punch(str(slot_number)):
                button_click.play()
                Punch = False
                Jab = True
                slot_number = ""
        elif Jab:
            question = "Where would you like to place Jab?" 
            move_name = "Jab"
            move_type = "Fast Attack"
            move_color = Darker_Red
            description = "A super fast attack dealing 5 damage, with a 0.2 second cooldown"
            if jab(str(slot_number)):
                button_click.play()
                Jab = False
                Kick = True
                slot_number = ""
        elif Kick: 
            question = "Where would you like to place Kick?"
            move_name = "Kick"
            move_type = "Powerful Attack"
            move_color = Orange 
            description = "A powerful kick dealing 35 damage on impact, with a 3 second cooldown"
            if kick(str(slot_number)):
                button_click.play()
                Kick = False
                Block = True
                slot_number = ""
        elif Block: 
            question = "Where would you like to place Block?" 
            move_name = "Block"
            move_type = "Medium Defense"
            move_color = Light_Green
            description = "Blocks 40% of damage dealt by enemy, hold to keep activated, 10 dps"
            if block(str(slot_number)):
                button_click.play()
                Block = False
                selecting_moves= False
                slot_number = ""

        pygame.draw.rect(screen, move_color , (540, 700, 920, 300))
        pygame.draw.rect(screen, Dark_Grey, (540, 700, 920, 300), width = 20)
        move_text = large_times.render(move_name, True, Black)
        move_text_rect = move_text.get_rect()
        move_text_rect.topleft= ((920-move_text_rect.width)/2 + 540, 750)
        screen.blit(move_text, move_text_rect)
        move_type_text = times.render(move_type, True, Dark_Grey)
        move_type_text_rect = move_type_text.get_rect()
        move_type_text_rect.topleft=((920-move_type_text_rect.width)/2 + 540, 825)
        screen.blit(move_type_text, move_type_text_rect)
        move_desc_text = small_times.render(description, True, Dark_Grey)
        move_desc_text_rect = move_desc_text.get_rect()
        move_desc_text_rect.topleft=((920-move_desc_text_rect.width)/2 + 540, 875)
        screen.blit(move_desc_text, move_desc_text_rect)

        pygame.draw.rect(screen, move_one_color , (250, 385, 300, 300))
        pygame.draw.rect(screen, Dark_Grey, (250, 385, 300, 300), width = 10)
        move_one_text = large_times.render(str(move_one), True, Black)
        move_one_text_rect = move_one_text.get_rect()
        move_one_text_rect.topleft=((300-move_one_text_rect.width)/2 + 250, 460)
        screen.blit(move_one_text, move_one_text_rect)
        num_one_text = large_times.render("1", True, Dark_Grey)
        num_one_text_rect = num_one_text.get_rect()
        num_one_text_rect.topleft=(265, 400)
        screen.blit(num_one_text, num_one_text_rect)

        pygame.draw.rect(screen, move_two_color , (650, 385, 300, 300))
        pygame.draw.rect(screen, Dark_Grey, (650, 385, 300, 300), width = 10)
        move_two_text = large_times.render(move_two, True, Black)
        move_two_text_rect = move_two_text.get_rect()
        move_two_text_rect.topleft=((300-move_two_text_rect.width)/2 + 650, 460)
        screen.blit(move_two_text, move_two_text_rect)
        num_two_text = large_times.render("2", True, Dark_Grey)
        num_two_text_rect = num_two_text.get_rect()
        num_two_text_rect.topleft=(665, 400)
        screen.blit(num_two_text, num_two_text_rect)

        pygame.draw.rect(screen, move_three_color, (1050, 385, 300, 300))
        pygame.draw.rect(screen, Dark_Grey, (1050, 385, 300, 300), width = 10)
        move_three_text = large_times.render(move_three, True, Black)
        move_three_text_rect = move_three_text.get_rect()
        move_three_text_rect.topleft=((300-move_three_text_rect.width)/2 + 1050, 460)
        screen.blit(move_three_text, move_three_text_rect)
        num_three_text = large_times.render("3", True, Dark_Grey)
        num_three_text_rect = num_three_text.get_rect()
        num_three_text_rect.topleft=(1065, 400)
        screen.blit(num_three_text, num_three_text_rect)

        pygame.draw.rect(screen, move_four_color, (1450, 385, 300, 300))
        pygame.draw.rect(screen, Dark_Grey, (1450, 385, 300, 300), width = 10)
        move_four_text = large_times.render(move_four, True, Black)
        move_four_text_rect = move_four_text.get_rect()
        move_four_text_rect.topleft=((300-move_four_text_rect.width)/2 + 1450, 460)
        screen.blit(move_four_text, move_four_text_rect)
        num_four_text = large_times.render("4", True, Dark_Grey)
        num_four_text_rect = num_four_text.get_rect()
        num_four_text_rect.topleft=(1465, 400)
        screen.blit(num_four_text, num_four_text_rect)
        clock.tick(fps)
        pygame.display.flip()

# worlds/cities
def world_one(x=100, y=900):
    global image, jumping, up, down, player_health, player_total_health, walk_speed, money, running, slider_dragging, open_settings, current_cursor, fps, current_screen, mouse_position, walking
    if walking == False:
        pass
    encounter_loading()
    screen.blit(world_one_background, (0, 0))
    image_rect = image.get_rect()
    image_rect.center = (x, y)
    image = pygame.transform.scale(image, (80, 144))
    walking = True
    jumping = False
    walk_speed = 10
    while walking:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                current_cursor = cursor_down  
                if current_screen == 'play' and volume_slider_rect.collidepoint(mouse_position):
                    slider_dragging = True  
            elif event.type == pygame.MOUSEBUTTONUP:
                slider_dragging = False  
                current_cursor = cursor_up  
                
                if current_screen == 'play':
                    if exit_button_rect.collidepoint(mouse_position):
                        button_click.play()
                        current_screen = 'main menu'
                        open_settings = False
                        walking = False
                    if menu_button_rect.collidepoint(mouse_position):
                        button_click.play()
                        open_settings = True  
                    if open_settings:  
                        if backbutton_rect1.collidepoint(mouse_position):
                            button_click.play()
                            open_settings = False
                        elif fps_30_rect.collidepoint(mouse_position):  
                            button_click.play()
                            fps = 30
                        elif fps_60_rect.collidepoint(mouse_position):
                            button_click.play()
                            fps = 60
                        elif fps_144_rect.collidepoint(mouse_position):
                            button_click.play()
                            fps = 144

            elif event.type == pygame.MOUSEMOTION:
                if slider_dragging:  # if dragging, update the slider position
                    volume_x = mouse_position[0]
                    volume_x = max(316, min(mouse_position[0], 1597))
                    volume_slider_rect.centerx = volume_x  # update slider rect position
                    volume_level = (volume_x - 316) / (1597 - 316)  # calculates the volume of the music based on position of the slider
                    pygame.mixer.music.set_volume(volume_level) # sets music volume
                    
        keys = pygame.key.get_pressed()
        screen.blit(world_one_background, (0, 0))
        screen.blit(image, image_rect)
        money_text = large_font.render("$ " + str(money), True, Green)
        money_text_rect = money_text.get_rect()
        money_text_rect.topleft=(1740, 40)
        screen.blit(money_text, money_text_rect)

        if keys[K_p]:
            if keys[K_1]:
                world_two()
            elif keys[K_2]:
                city_one()

        if keys[K_LSHIFT]:
            walk_speed = 20
        else:
            walk_speed = 10

        if image_rect.x >= 1880:
            enemy_one_stats()
            background_music = pygame.mixer.music.load('sound/battle_music.mp3')
            pygame.mixer.music.play(-1)
            encounter_loading()
            if fighting():
                background_music = pygame.mixer.music.load('sound/background_music.mp3')
                pygame.mixer.music.play(-1)
                world_two()
            else: 
                player_health = player_total_health
                background_music = pygame.mixer.music.load('sound/background_music.mp3')
                pygame.mixer.music.play(-1)
                world_one()
            jumping = False
            walking = False
        if image_rect.x <= 0:
            if keys[K_d]:
                image_rect.x += walk_speed
        else: 
            if keys[K_d]:
                image_rect.x += walk_speed
            if keys[K_a]:
                image_rect.x -= walk_speed

        if keys[K_SPACE]:
            jumping = True
        
        if jumping:
            if up <= 10:
                image_rect.y -= 10
                up += 1
            else:
                image_rect.y += 10
                down += 1
                if down >= 11:
                    down = 0
                    up = 0
                    jumping = False
        
        screen.blit(menu_button, menu_button_rect)
        if menu_button_rect.collidepoint(mouse_position):
            screen.blit(menu_button_pressed, menu_button_rect)
        if open_settings:   
            screen.blit(settings_page, settings_page_rect)  
            screen.blit(fps_30, fps_30_rect)  
            screen.blit(fps_60, fps_60_rect)
            screen.blit(fps_144, fps_144_rect)
            screen.blit(fps_text, fps_text_rect)  
            screen.blit(master_vol, master_vol_rect)    
            screen.blit(volume_bar, volume_bar_rect)
            screen.blit(volume_slider, volume_slider_rect)  
            screen.blit(backbutton, backbutton_rect1)
            screen.blit(exit_button, exit_button_rect)  

            if fps_30_rect.collidepoint(mouse_position):  
                screen.blit(fps_30_pressed, fps_30_rect)
            if fps_60_rect.collidepoint(mouse_position):
                screen.blit(fps_60_pressed, fps_60_rect)
            if fps_144_rect.collidepoint(mouse_position):
                screen.blit(fps_144_pressed, fps_144_rect)
            if backbutton_rect3.collidepoint(mouse_position):
                screen.blit(backbutton_pressed, backbutton_rect3)
            if exit_button_rect.collidepoint(mouse_position):
                screen.blit(exit_button_pressed, exit_button_rect)

        mouse_position = pygame.mouse.get_pos()
        screen.blit(current_cursor, mouse_position)
        pygame.display.flip()
        clock.tick(fps)
def world_two(x=100, y=940):
    global image
    global jumping
    global up
    global down
    global player_health
    global player_total_health
    global dead
    global heal
    global running, slider_dragging, open_settings, current_cursor, fps, current_screen, mouse_position, walking
    if walking == False:
        pass
    image = pygame.image.load('images2/main_character.png')
    image_rect = image.get_rect()
    image_rect.center = (x, y)
    image = pygame.transform.scale(image, (80, 144))
    walking = True
    jumping = False
    encounter_loading()
    if dead:
        heal()
        dead = False
    while walking:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                current_cursor = cursor_down  
                if current_screen == 'play' and volume_slider_rect.collidepoint(mouse_position):
                    slider_dragging = True  
            elif event.type == pygame.MOUSEBUTTONUP:
                slider_dragging = False  
                current_cursor = cursor_up  
                
                if current_screen == 'play':
                    if exit_button_rect.collidepoint(mouse_position):
                        button_click.play()
                        current_screen = 'main menu'
                        open_settings = False
                        walking = False
                    if menu_button_rect.collidepoint(mouse_position):
                        button_click.play()
                        open_settings = True  
                    if open_settings:  
                        if backbutton_rect1.collidepoint(mouse_position):
                            button_click.play()
                            open_settings = False
                        elif fps_30_rect.collidepoint(mouse_position):  
                            button_click.play()
                            fps = 30
                        elif fps_60_rect.collidepoint(mouse_position):
                            button_click.play()
                            fps = 60
                        elif fps_144_rect.collidepoint(mouse_position):
                            button_click.play()
                            fps = 144

            elif event.type == pygame.MOUSEMOTION:
                if slider_dragging:  # if dragging, update the slider position
                    volume_x = mouse_position[0]
                    volume_x = max(316, min(mouse_position[0], 1597))
                    volume_slider_rect.centerx = volume_x  # update slider rect position
                    volume_level = (volume_x - 316) / (1597 - 316)  # calculates the volume of the music based on position of the slider
                    pygame.mixer.music.set_volume(volume_level) # sets music volume
        keys = pygame.key.get_pressed()
        screen.blit(world_two_background, (0, 0))
        screen.blit(capybara_enemy, (550, 400))
        screen.blit(image, image_rect)
        money_text = large_font.render("$ " + str(money), True, Green)
        money_text_rect = money_text.get_rect()
        money_text_rect.topleft=(1740, 40)
        screen.blit(money_text, money_text_rect)
        if keys[K_p]:
            if keys[K_0]:
                world_one()
            elif keys[K_2]:
                city_one()
        if image_rect.x >= 1880:
            city_one()
            jumping = False
            walking = False
        if image_rect.x <= 0:
            enemy_one_stats()
            background_music = pygame.mixer.music.load('sound/battle_music.mp3')
            pygame.mixer.music.play(-1)
            encounter_loading()
            if fighting():
                background_music = pygame.mixer.music.load('sound/background_music.mp3')
                pygame.mixer.music.play(-1)
                world_one(1880, 900)
            else:
                background_music = pygame.mixer.music.load('sound/background_music.mp3')
                pygame.mixer.music.play(-1)
                player_health = player_total_health
                world_one(100, 900)
            jumping = False
            walking = False
        else: 
            if keys[K_d]:
                image_rect.x += 10
            if keys[K_a]:
                image_rect.x -= 10

        if keys[K_SPACE]:
            jumping = True
        
        if jumping:
            if up <= 10:
                image_rect.y -= 10
                up += 1
            else:
                image_rect.y += 10
                down += 1
            if down >= 11:
                down = 0
                up = 0
                jumping = False
        if 200 <= image_rect.x <= 390:  
            pygame.draw.rect(screen, Dark_Grey, (150, 600, 300, 150))  
            pygame.draw.rect(screen, Darker_Grey, (150, 600, 300, 150), width=10)  
            enter_text = small_font.render("Press E to", True, Black)
            enter_text_rect = enter_text.get_rect()
            enter_text_rect.topleft = ((300 - enter_text.get_width()) // 2 + 150, 650)  #
            screen.blit(enter_text, enter_text_rect)
            store_text = small_font.render("Enter Moves store", True, Black)
            store_text_rect = store_text.get_rect()
            store_text_rect.topleft = ((300 - store_text_rect.width) // 2 + 150, 675)  
            screen.blit(store_text, store_text_rect)
            if keys[K_e]:
                store()
        if image_rect.x >= 1150 and image_rect.x <= 1350:
            pygame.draw.rect(screen, Dark_Grey, (950, 600, 300, 150))
            pygame.draw.rect(screen, Darker_Grey, (950, 600, 300, 150), width = 10)
            enter_text = small_font.render("Press E to ", True, Black)
            enter_text_rect = enter_text.get_rect()
            enter_text_rect.topleft=((300-enter_text_rect.width)/2 + 950, 650)
            screen.blit(enter_text, enter_text_rect)
            hospital_text = small_font.render("Enter Healing Center", True, Black)
            hospital_text_rect = hospital_text.get_rect()
            hospital_text_rect.topleft=((300-hospital_text_rect.width)/2 + 950, 675)
            screen.blit(hospital_text, hospital_text_rect)
            if keys[K_e]:
                heal()
        if image_rect.x >= 600 and image_rect.x <= 900:
            enemy_two_stats()
            background_music = pygame.mixer.music.load('sound/battle_music.mp3')
            pygame.mixer.music.play(-1)
            encounter_loading()
            if fighting():
                background_music = pygame.mixer.music.load('sound/background_music.mp3')
                pygame.mixer.music.play(-1)
                world_two(1050, 940)
            else:
                background_music = pygame.mixer.music.load('sound/background_music.mp3')
                pygame.mixer.music.play(-1)
                player_health = player_total_health
                world_one(100, 900)
        
                screen.blit(menu_button, menu_button_rect)
        
        screen.blit(menu_button, menu_button_rect)
        if menu_button_rect.collidepoint(mouse_position):
            screen.blit(menu_button_pressed, menu_button_rect)
        if open_settings:   
            screen.blit(settings_page, settings_page_rect)  
            screen.blit(fps_30, fps_30_rect)  
            screen.blit(fps_60, fps_60_rect)
            screen.blit(fps_144, fps_144_rect)
            screen.blit(fps_text, fps_text_rect)  
            screen.blit(master_vol, master_vol_rect)    
            screen.blit(volume_bar, volume_bar_rect)
            screen.blit(volume_slider, volume_slider_rect)  
            screen.blit(backbutton, backbutton_rect1)
            screen.blit(exit_button, exit_button_rect)  

            if fps_30_rect.collidepoint(mouse_position):  
                screen.blit(fps_30_pressed, fps_30_rect)
            if fps_60_rect.collidepoint(mouse_position):
                screen.blit(fps_60_pressed, fps_60_rect)
            if fps_144_rect.collidepoint(mouse_position):
                screen.blit(fps_144_pressed, fps_144_rect)
            if backbutton_rect3.collidepoint(mouse_position):
                screen.blit(backbutton_pressed, backbutton_rect3)
            if exit_button_rect.collidepoint(mouse_position):
                screen.blit(exit_button_pressed, exit_button_rect)

        mouse_position = pygame.mouse.get_pos()
        screen.blit(current_cursor, mouse_position)
        pygame.display.flip()
        clock.tick(fps)
def city_one(x=100, y=940):
    global image
    global jumping
    global up
    global down
    global heal
    global dead
    global background_music
    global running, slider_dragging, open_settings, current_cursor, fps, current_screen, mouse_position, walking
    image = pygame.image.load('images2/main_character.png')
    image_rect = image.get_rect()
    image_rect.center = (x, y)
    image = pygame.transform.scale(image, (80, 144))
    walking = True
    jumping = False
    encounter_loading()
    while walking:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                current_cursor = cursor_down  
                if current_screen == 'play' and volume_slider_rect.collidepoint(mouse_position):
                    slider_dragging = True  
            elif event.type == pygame.MOUSEBUTTONUP:
                slider_dragging = False  
                current_cursor = cursor_up  
                
                if current_screen == 'play':
                    if exit_button_rect.collidepoint(mouse_position):
                        button_click.play()
                        current_screen = 'main menu'
                        open_settings = False
                        walking = False
                    if menu_button_rect.collidepoint(mouse_position):
                        button_click.play()
                        open_settings = True  
                    if open_settings:  
                        if backbutton_rect1.collidepoint(mouse_position):
                            button_click.play()
                            open_settings = False
                        elif fps_30_rect.collidepoint(mouse_position):  
                            button_click.play()
                            fps = 30
                        elif fps_60_rect.collidepoint(mouse_position):
                            button_click.play()
                            fps = 60
                        elif fps_144_rect.collidepoint(mouse_position):
                            button_click.play()
                            fps = 144
            elif event.type == pygame.MOUSEMOTION:
                if slider_dragging:  # if dragging, update the slider position
                    volume_x = mouse_position[0]
                    volume_x = max(316, min(mouse_position[0], 1597))
                    volume_slider_rect.centerx = volume_x  # update slider rect position
                    volume_level = (volume_x - 316) / (1597 - 316)  # calculates the volume of the music based on position of the slider
                    pygame.mixer.music.set_volume(volume_level) # sets music volume
        keys = pygame.key.get_pressed()
        screen.blit(city_one_background, (0, 0))
        screen.blit(image, image_rect)
        money_text = large_font.render("$ " + str(money), True, Green)
        money_text_rect = money_text.get_rect()
        money_text_rect.topleft=(1740, 40)
        screen.blit(money_text, money_text_rect)
        if keys[K_p]:
            if keys[K_0]:
                world_one()
            elif keys[K_1]:
                world_two()
        if image_rect.x >= 1840:
            if keys[K_a]:
                image_rect.x -= 10
        elif image_rect.x <= 0:
            world_two(1880, 940)
            jumping = False
            walking = False
        else: 
            if keys[K_d]:
                image_rect.x += 10
            if keys[K_a]:
                image_rect.x -= 10

        if keys[K_SPACE]:
            jumping = True
        
        if jumping:
            if up <= 10:
                image_rect.y -= 10
                up += 1
            else:
                image_rect.y += 10
                down += 1
                if down >= 11:
                    down = 0
                    up = 0
                    jumping = False
        if image_rect.x >= 1150 and image_rect.x <= 1350:
            pygame.draw.rect(screen, Dark_Grey, (950, 600, 300, 150))
            pygame.draw.rect(screen, Darker_Grey, (950, 600, 300, 150), width = 10)
            enter_text = small_font.render("Press E to ", True, Black)
            enter_text_rect = enter_text.get_rect()
            enter_text_rect.topleft=((300-enter_text_rect.width)/2 + 950, 650)
            screen.blit(enter_text, enter_text_rect)
            hospital_text = small_font.render("Enter Healing Center", True, Black)
            hospital_text_rect = hospital_text.get_rect()
            hospital_text_rect.topleft=((300-hospital_text_rect.width)/2 + 950, 675)
            screen.blit(hospital_text, hospital_text_rect)
            if keys[K_e]:
                heal()
        if image_rect.x >= 600 and image_rect.x <= 850:
            screen.blit(random_enemy, (550, 600))
            pygame.display.flip()
            time.sleep(1)
            enemy_three_stats()
            background_music = pygame.mixer.music.load('sound/battle_music.mp3')
            pygame.mixer.music.play(-1)
            encounter_loading()
            if fighting():
                background_music = pygame.mixer.music.load('sound/background_music.mp3')
                pygame.mixer.music.play(-1)
                city_one(950, 940)
            else:
                background_music = pygame.mixer.music.load('sound/background_music.mp3')
                pygame.mixer.music.play(-1)
                dead = True
                world_two(1275, 940)
        if image_rect.x >= 1025 and image_rect.x <= 1100:
            time.sleep(1)
            boss_one_stats()
            background_music = pygame.mixer.music.load('sound/battle_music.mp3')
            pygame.mixer.music.play(-1)
            encounter_loading()
            if fighting():
                background_music = pygame.mixer.music.load('sound/background_music.mp3')
                pygame.mixer.music.play(-1)
                city_one(1200, 940)
            else:
                background_music = pygame.mixer.music.load('sound/background_music.mp3')
                pygame.mixer.music.play(-1)
                dead = True
                world_two(1275, 940)
       
                screen.blit(menu_button, menu_button_rect)
        
        screen.blit(menu_button, menu_button_rect)
        if menu_button_rect.collidepoint(mouse_position):
            screen.blit(menu_button_pressed, menu_button_rect)
        if open_settings:   
            screen.blit(settings_page, settings_page_rect)  
            screen.blit(fps_30, fps_30_rect)  
            screen.blit(fps_60, fps_60_rect)
            screen.blit(fps_144, fps_144_rect)
            screen.blit(fps_text, fps_text_rect)  
            screen.blit(master_vol, master_vol_rect)    
            screen.blit(volume_bar, volume_bar_rect)
            screen.blit(volume_slider, volume_slider_rect)  
            screen.blit(backbutton, backbutton_rect1)
            screen.blit(exit_button, exit_button_rect)  

            if fps_30_rect.collidepoint(mouse_position):  
                screen.blit(fps_30_pressed, fps_30_rect)
            if fps_60_rect.collidepoint(mouse_position):
                screen.blit(fps_60_pressed, fps_60_rect)
            if fps_144_rect.collidepoint(mouse_position):
                screen.blit(fps_144_pressed, fps_144_rect)
            if backbutton_rect3.collidepoint(mouse_position):
                screen.blit(backbutton_pressed, backbutton_rect3)
            if exit_button_rect.collidepoint(mouse_position):
                screen.blit(exit_button_pressed, exit_button_rect)

        mouse_position = pygame.mouse.get_pos()
        screen.blit(current_cursor, mouse_position)
        pygame.display.flip()
        clock.tick(fps)

# enemy stats
def enemy_one_stats():
    global enemy_attack_one, enemy_attack_two, enemy_attack_three, enemy_attack_four
    global enemy_damage_one, enemy_damage_two, enemy_damage_three, enemy_damage_four
    global enemy_cooldown_one, enemy_cooldown_two, enemy_cooldown_three, enemy_cooldown_four
    global enemy_defense_one, enemy_defense_two, enemy_defense_three, enemy_defense_four
    global enemy_xp
    global enemy
    global enemy_rect
    global enemy_name
    global enemy_level
    global enemy_attack_stat, enemy_defense_stat, enemy_health, enemy_total_health
    global enemy_turn
    global money_drop

    enemy_turn = True
    enemy_level = 5
    enemy_name = "Squishy"

    # Stats for enemy
    enemy_attack_stat = 1 + enemy_level*.05
    enemy_defense_stat = 1 + enemy_level*.05
    enemy_total_health = int(100 + 5*enemy_level)
    enemy_health = enemy_total_health

    # Image for enemy
    enemy = pygame.image.load('images2/squishy.png')
    enemy = pygame.transform.scale(enemy, (261, 239))
    enemy_rect = image.get_rect()
    enemy_rect.center = (1400, 300)

    enemy_xp = 60
    money_drop = 10

    # enemy's techniques and moves
    enemy_attack_one = False
    enemy_attack_two = False
    enemy_attack_three = False
    enemy_attack_four = False

    enemy_damage_one = 40
    enemy_cooldown_one = 2000
    enemy_defense_one = 1

    enemy_damage_two = 20
    enemy_cooldown_two = 2000
    enemy_defense_two = 1

    enemy_damage_three = 5
    enemy_cooldown_three = 200
    enemy_defense_three = 1

    enemy_damage_four = 10
    enemy_cooldown_four = 1000
    enemy_defense_four = 0.6
def enemy_two_stats():
    global enemy_attack_one, enemy_attack_two, enemy_attack_three, enemy_attack_four
    global enemy_damage_one, enemy_damage_two, enemy_damage_three, enemy_damage_four
    global enemy_cooldown_one, enemy_cooldown_two, enemy_cooldown_three, enemy_cooldown_four
    global enemy_defense_one, enemy_defense_two, enemy_defense_three, enemy_defense_four
    global enemy_xp
    global enemy
    global enemy_rect
    global enemy_name
    global enemy_level
    global enemy_attack_stat, enemy_defense_stat, enemy_health, enemy_total_health
    global enemy_turn
    global money_drop

    enemy_turn = True

    enemy_level = 10
    enemy_name = "Capybara"

    # Stats for enemy
    enemy_attack_stat = 1 + enemy_level*.05
    enemy_defense_stat = 1 + enemy_level*.05
    enemy_total_health = int(100 + 5*enemy_level)
    enemy_health = enemy_total_health

    # Image of Enemy
    enemy = pygame.image.load('images2/capybara.png')
    enemy_rect = image.get_rect()
    enemy_rect.center = (1350, 250)

    enemy_xp = 100
    money_drop = 15

    # Enemy's techniques
    enemy_attack_one = False
    enemy_attack_two = False
    enemy_attack_three = False
    enemy_attack_four = False

    enemy_damage_one = 60
    enemy_cooldown_one = 2000
    enemy_defense_one = 1

    enemy_damage_two = 40
    enemy_cooldown_two = 2000
    enemy_defense_two = 1

    enemy_damage_three = 10
    enemy_cooldown_three = 200
    enemy_defense_three = 1

    enemy_damage_four = 20
    enemy_cooldown_four = 1000
    enemy_defense_four = 0.6
def enemy_three_stats():
    global enemy_attack_one, enemy_attack_two, enemy_attack_three, enemy_attack_four
    global enemy_damage_one, enemy_damage_two, enemy_damage_three, enemy_damage_four
    global enemy_cooldown_one, enemy_cooldown_two, enemy_cooldown_three, enemy_cooldown_four
    global enemy_defense_one, enemy_defense_two, enemy_defense_three, enemy_defense_four
    global enemy_xp
    global enemy
    global enemy_rect
    global enemy_name
    global enemy_level
    global enemy_attack_stat, enemy_defense_stat, enemy_health, enemy_total_health
    global enemy_turn
    global money_drop

    enemy_turn = True

    enemy_level = 12
    enemy_name = "Morvak's Goon"

    enemy_attack_stat = 1 + enemy_level*.05
    enemy_defense_stat = 1 + enemy_level*.05
    enemy_total_health = int(100 + 5*enemy_level)
    enemy_health = enemy_total_health

    enemy = random_enemy
    enemy_rect = image.get_rect()
    enemy_rect.center = (1400, 300)

    enemy_xp = 140
    money_drop = 15

    enemy_attack_one = False
    enemy_attack_two = False
    enemy_attack_three = False
    enemy_attack_four = False

    enemy_damage_one = 40
    enemy_cooldown_one = 500
    enemy_defense_one = 1

    enemy_damage_two = 20
    enemy_cooldown_two = 600
    enemy_defense_two = 1

    enemy_damage_three = 5
    enemy_cooldown_three = 200
    enemy_defense_three = 1

    enemy_damage_four = 10
    enemy_cooldown_four = 500
    enemy_defense_four = 0.6
def boss_one_stats():
    global enemy_attack_one, enemy_attack_two, enemy_attack_three, enemy_attack_four
    global enemy_damage_one, enemy_damage_two, enemy_damage_three, enemy_damage_four
    global enemy_cooldown_one, enemy_cooldown_two, enemy_cooldown_three, enemy_cooldown_four
    global enemy_defense_one, enemy_defense_two, enemy_defense_three, enemy_defense_four
    global enemy_xp
    global enemy
    global enemy_rect
    global enemy_name
    global enemy_level
    global enemy_attack_stat, enemy_defense_stat, enemy_health, enemy_total_health
    global enemy_turn
    global money_drop

    enemy_turn = True

    enemy_level = 20
    enemy_name = "Morvak"

    enemy_attack_stat = 1 + enemy_level*.05
    enemy_defense_stat = 1 + enemy_level*.05
    enemy_total_health = int(100 + 5*enemy_level)
    enemy_health = enemy_total_health

    enemy = pygame.image.load('images2/boss_one.png')
    enemy = pygame.transform.scale(enemy, (400, 400))
    enemy_rect = image.get_rect()
    enemy_rect.center = (1400, 300)

    enemy_xp = 200
    money_drop = 20

    enemy_attack_one = False
    enemy_attack_two = False
    enemy_attack_three = False
    enemy_attack_four = False

    enemy_damage_one = 60
    enemy_cooldown_one = 1000
    enemy_defense_one = 1

    enemy_damage_two = 30
    enemy_cooldown_two = 1000
    enemy_defense_two = 1

    enemy_damage_three = 10
    enemy_cooldown_three = 200
    enemy_defense_three = 1

    enemy_damage_four = 15
    enemy_cooldown_four = 1000
    enemy_defense_four = 0.6

# level bar and tracker
def level_track():
    global player_level
    global player_attack_stat
    global player_defense_stat
    global player_total_health
    global player_health
    global current_xp
    global total_xp_needed
    if current_xp >= total_xp_needed:
        current_xp = current_xp - total_xp_needed
        player_level += 1
        player_bars()
        xp_bar = int((current_xp/total_xp_needed)*400)
        player_attack_stat = 1 + player_level*.05
        player_defense_stat = 1 + player_level*.05
        player_total_health = int(100 + 5*player_level)
        total_xp_needed = player_level * 20
        pygame.draw.rect(screen, Baby_Green, (275, 525, xp_bar, 10))
        pygame.draw.rect(screen, Black, (275, 525, 400, 10), width = 2)

    else:
        xp_bar = int((current_xp/total_xp_needed)*400)
        pygame.draw.rect(screen, Baby_Green, (275, 525, xp_bar, 10))
        pygame.draw.rect(screen, Black, (275, 525, 400, 10), width = 2)

# battle platforms
def draw_ecllipse():
    pygame.draw.ellipse(screen, Grey, (150, 650, 500, 300))
    pygame.draw.ellipse(screen, Dark_Grey, (150, 650, 500, 300), width = 10)
    pygame.draw.ellipse(screen, Grey, (1300, 300, 500, 300))
    pygame.draw.ellipse(screen, Dark_Grey, (1300, 300, 500, 300), width = 10)

# transition screen
def encounter_loading():
    box_x = 1880
    box_x_2 = 0
    for i in range(47):
        pygame.draw.rect(screen, Black , (box_x, 0, 80, 1080))
        pygame.draw.rect(screen, Black , (box_x_2, 0, 80, 1080))
        clock.tick(60)
        pygame.display.flip()
        box_x -= 40
        box_x_2 += 40

# death animations
def enemy_death():
    global damage_dealt
    global damage_recieved
    global enemy
    global enemy_rect
    global image
    tick = 0
    damage_dealt = 0
    damage_recieved = 0
    while tick <= 60:
        enemy_rect.y += 10
        screen.blit(background, (0, 0))
        draw_ecllipse()
        player_bars()
        screen.blit(enemy, enemy_rect)
        player_techniques()
        level_track()
        screen.blit(image, image_rect)
        pygame.display.flip()
        tick += 5
        clock.tick(60)
    screen.blit(background, (0, 0))
    draw_ecllipse()
    player_bars()
    player_techniques()
    level_track()
    screen.blit(image, image_rect)
    pygame.display.flip()
def death():
    global damage_dealt
    global damage_recieved
    global enemy
    global enemy_rect
    global image
    tick = 0
    damage_dealt = 0
    damage_recieved = 0
    while tick <= 60:
        image_rect.y += 10
        screen.blit(background, (0, 0))
        draw_ecllipse()
        player_bars()
        player_techniques()
        level_track()
        screen.blit(enemy, enemy_rect)
        screen.blit(image, image_rect)
        pygame.display.flip()
        tick += 5
        clock.tick(60)
    screen.blit(background, (0, 0))
    draw_ecllipse()
    player_bars()
    player_techniques()
    level_track()
    screen.blit(enemy, enemy_rect)
    pygame.draw.rect(screen, Black, (540, 460, 920, 300))
    pygame.draw.rect(screen, Dark_Grey, (540, 460, 920, 300), width = 20)
    death_text = large_times.render("You have been defeated!", True, Red)
    death_text_rect = death_text.get_rect()
    death_text_rect.topleft= ((920-death_text_rect.width)/2 + 540, 510)
    screen.blit(death_text, death_text_rect)
    pygame.display.flip()

# attack animations
def attack_animation():
    global image
    image = pygame.image.load('images2/main_character.png')
    tick = 0
    while tick <= 60:
        image_rect.x += 85 * speed
        image_rect.y -= 34 * speed
        screen.blit(background, (0, 0))
        draw_ecllipse()
        player_bars()
        player_techniques()
        level_track()
        screen.blit(enemy, enemy_rect)
        screen.blit(image, image_rect)
        pygame.display.flip()
        tick += 5*speed
        clock.tick(60)
    tick = 0
    while tick <= 60:
        image_rect.x -= 85 * speed
        image_rect.y += 34 * speed
        screen.blit(background, (0, 0))
        draw_ecllipse()
        player_bars()
        player_techniques()
        level_track()
        screen.blit(enemy, enemy_rect)
        screen.blit(image, image_rect)
        pygame.display.flip()
        tick += 5*speed
        clock.tick(120)
    return
def enemy_attack():
    global image
    tick = 0
    while tick <= 60:
        enemy_rect.x -= 170
        enemy_rect.y += 68
        screen.blit(background, (0, 0))
        draw_ecllipse()
        player_bars()
        player_techniques()
        level_track()
        screen.blit(image, image_rect)
        screen.blit(enemy, enemy_rect)
        pygame.display.flip()
        tick += 10
        clock.tick(60)
    tick = 0
    while tick <= 60:
        enemy_rect.x += 170
        enemy_rect.y -= 68
        screen.blit(background, (0, 0))
        draw_ecllipse()
        player_bars()
        player_techniques()
        level_track()
        screen.blit(image, image_rect)
        screen.blit(enemy, enemy_rect)
        pygame.display.flip()
        tick += 10
        clock.tick(120)
    return

# info bars
def player_bars():
    global enemy_health
    global damage_dealt
    global player_health
    global player_health_percent
    global damage_recieved
    global enemy_name
    player_health = player_health - (damage_recieved*enemy_attack_stat*block_defense/player_defense_stat)
    player_health = int(player_health)
    enemy_health = enemy_health - (damage_dealt*player_attack_stat*enemy_block_defense/enemy_defense_stat)
    enemy_health = int(enemy_health)
    player_health_percent = int(player_health/player_total_health*100)
    enemy_health_percent = int(enemy_health/enemy_total_health*100)
    pygame.draw.rect(screen, Darker_Grey, (250, 350, 500, 200))
    pygame.draw.rect(screen, Darker_Grey, (1050, 50, 500, 200))
    pygame.draw.rect(screen, Dark_Grey, (250, 350, 500, 200), width = 10)
    pygame.draw.rect(screen, Dark_Grey, (1050, 50, 500, 200), width = 10)
    if player_health_percent >= 50:
        pygame.draw.rect(screen, Green, (275, 500, (player_health_percent*4), 20))
    elif player_health_percent >= 25:
        pygame.draw.rect(screen, Yellow, (275, 500, (player_health_percent*4), 20))
    else:
        pygame.draw.rect(screen, Red, (275, 500, (player_health_percent*4), 20))
    
    if enemy_health_percent >= 50:
        pygame.draw.rect(screen, Green, (1075, 200, (enemy_health_percent*4), 20))
    elif enemy_health_percent >= 25:
        pygame.draw.rect(screen, Yellow, (1075, 200, (enemy_health_percent*4), 20))
    else:
        pygame.draw.rect(screen, Red, (1075, 200, (enemy_health_percent*4), 20))

    pygame.draw.rect(screen, Black, (275, 500, 400, 20), width = 5)
    pygame.draw.rect(screen, Black, (1075, 200, 400, 20), width = 5)
    player_text = font.render(player_name, True, Green)
    player_text_rect = player_text.get_rect()
    player_text_rect.topleft=(275, 375)
    screen.blit(player_text, player_text_rect)
    player_lvl_text = font.render("level " + str(player_level), True, Green)
    player_lvl_text_rect = player_text.get_rect()
    player_lvl_text_rect.topleft=(575, 375)
    screen.blit(player_lvl_text, player_lvl_text_rect)
    if player_health <= 0:
        player_hp = font.render("0 /" + str(player_total_health), True, White)
    else: 
        player_hp = font.render(str(player_health) + " /" + str(player_total_health), True, White)
    player_hp_rect = player_hp.get_rect()
    player_hp_rect.topleft=(275, 450)
    screen.blit(player_hp, player_hp_rect)

    enemy_text = font.render(enemy_name, True, Red)
    enemy_text_rect = enemy_text.get_rect()
    enemy_text_rect.topleft=(1075, 75)
    screen.blit(enemy_text, enemy_text_rect)
    enemy_lvl_text = font.render("level " + str(enemy_level), True, Red)
    enemy_lvl_text_rect = enemy_text.get_rect()
    enemy_lvl_text_rect.topleft=(1375, 75)
    screen.blit(enemy_lvl_text, enemy_lvl_text_rect)
    if enemy_health <= 0:
        enemy_hp = font.render("0 /" + str(enemy_total_health), True, White)
    else:
        enemy_hp = font.render(str(enemy_health) + " /" + str(enemy_total_health), True, White)
    enemy_hp_rect = enemy_hp.get_rect()
    enemy_hp_rect.topleft=(1075, 150)
    screen.blit(enemy_hp, enemy_hp_rect)

# techniques
def player_techniques():
    global move_one, move_two, move_three, move_four
    global move_one_speed, move_two_speed, move_three_speed, move_four_speed
    global move_one_damage, move_two_damage, move_three_damage, move_four_damage
    global move_one_color, move_two_color, move_three_color, move_four_color
    global move_one_cooldown, move_two_cooldown, move_three_cooldown, move_four_cooldown
    global new_time_1, current_time_1, new_time_2, current_time_2, new_time_3, current_time_3, new_time_4, current_time_4
    pygame.draw.rect(screen, move_one_color , (900, 750, 200, 200))
    if not attack_one_cooldown:
        pygame.draw.rect(screen, Grey, (900, 750, 200, ((new_time_1-current_time_1)/move_one_cooldown*200)))
    pygame.draw.rect(screen, Dark_Grey, (900, 750, 200, 200), width = 10)
    move_one_text = times.render(str(move_one), True, Black)
    move_one_text_rect = move_one_text.get_rect()
    move_one_text_rect.topleft=((200-move_one_text_rect.width)/2 + 900, 800)
    screen.blit(move_one_text, move_one_text_rect)
    num_one_text = times.render("1", True, Dark_Grey)
    num_one_text_rect = num_one_text.get_rect()
    num_one_text_rect.topleft=(915, 765)
    screen.blit(num_one_text, num_one_text_rect)

    pygame.draw.rect(screen, move_two_color , (1150, 750, 200, 200))
    if not attack_two_cooldown:
        pygame.draw.rect(screen, Grey, (1150, 750, 200, ((new_time_2-current_time_2)/move_two_cooldown*200)))
    pygame.draw.rect(screen, Dark_Grey, (1150, 750, 200, 200), width = 10)
    move_two_text = times.render(move_two, True, Black)
    move_two_text_rect = move_two_text.get_rect()
    move_two_text_rect.topleft=((200-move_two_text_rect.width)/2 + 1150, 800)
    screen.blit(move_two_text, move_two_text_rect)
    num_two_text = times.render("2", True, Dark_Grey)
    num_two_text_rect = num_two_text.get_rect()
    num_two_text_rect.topleft=(1165, 765)
    screen.blit(num_two_text, num_two_text_rect)

    pygame.draw.rect(screen, move_three_color, (1400, 750, 200, 200))
    if not attack_three_cooldown:
        pygame.draw.rect(screen, Grey, (1400, 750, 200, ((new_time_3-current_time_3)/move_three_cooldown*200)))
    pygame.draw.rect(screen, Dark_Grey, (1400, 750, 200, 200), width = 10)
    move_three_text = times.render(move_three, True, Black)
    move_three_text_rect = move_three_text.get_rect()
    move_three_text_rect.topleft=((200-move_three_text_rect.width)/2 + 1400, 800)
    screen.blit(move_three_text, move_three_text_rect)
    num_three_text = times.render("3", True, Dark_Grey)
    num_three_text_rect = num_three_text.get_rect()
    num_three_text_rect.topleft=(1415, 765)
    screen.blit(num_three_text, num_three_text_rect)

    pygame.draw.rect(screen, move_four_color, (1650, 750, 200, 200))
    if not attack_four_cooldown:
        pygame.draw.rect(screen, Grey, (1650, 750, 200, ((new_time_4-current_time_4)/move_four_cooldown*200)))
    pygame.draw.rect(screen, Dark_Grey, (1650, 750, 200, 200), width = 10)
    move_four_text = times.render(move_four, True, Black)
    move_four_text_rect = move_four_text.get_rect()
    move_four_text_rect.topleft=((200-move_four_text_rect.width)/2 + 1650, 800)
    screen.blit(move_four_text, move_four_text_rect)
    num_four_text = times.render("4", True, Dark_Grey)
    num_four_text_rect = num_four_text.get_rect()
    num_four_text_rect.topleft=(1665, 765)
    screen.blit(num_four_text, num_four_text_rect)

# actions
def fighting(): 
    global enemy_attack_one, enemy_attack_two, enemy_attack_three, enemy_attack_four
    global enemy_damage_one, enemy_damage_two, enemy_damage_three, enemy_damage_four
    global enemy_cooldown_one, enemy_cooldown_two, enemy_cooldown_three, enemy_cooldown_four
    global enemy_defense_one, enemy_defense_two, enemy_defense_three, enemy_defense_four
    global enemy_xp
    global enemy, enemy_rect
    global Fight
    global block_defense
    global move_one, move_two, move_three, move_four
    global move_one_speed, move_two_speed, move_three_speed, move_four_speed
    global move_one_damage, move_two_damage, move_three_damage, move_four_damage
    global move_one_color, move_two_color, move_three_color, move_four_color
    global move_one_cooldown, move_two_cooldown, move_three_cooldown, move_four_cooldown
    global move_one_defense, move_two_defense, move_three_defense, move_four_defense
    global move_one_type, move_two_type, move_three_type, move_four_type
    global attack_one_cooldown, attack_two_cooldown, attack_three_cooldown, attack_four_cooldown
    global enemy_turn
    global player_health, enemy_health
    global damage_dealt, damage_recieved
    global new_time_1, current_time_1, new_time_2, current_time_2, new_time_3, current_time_3, new_time_4, current_time_4
    global current_xp
    global image
    global money, money_drop
    block_defense = 1
    enemy_health = enemy_total_health # Ensures enemy is full hp
    damage_dealt = 0 
    damage_recieved = 0
    Fight = True
    image_rect.center = (400, 725)
    level_track()
    while Fight:
        keys = pygame.key.get_pressed()
        if keys[K_p]:
            enemy_health = 0
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Fight = False

        # Checks to see if player is using a block, if so the character will be using a shield
        if block_defense != 1:
            image = pygame.image.load('images2/main_character_block.png')
            image = pygame.transform.scale(image, (224, 282.8))
        else:
            image = pygame.image.load('images2/main_character.png')

        # Allows users to select which attack they would like to use, each move has a unique cooldown based on what moves the user chose
        if attack_one_cooldown:
            if player_health <= 0:
                pass
            elif enemy_health > 0:
                if keys[pygame.K_1]:
                    speed = move_one_speed # Applies stats from move one
                    block_defense = move_one_defense
                    if move_one_type == "Attack":
                        attack_animation() # attacking animation
                        damage_dealt = move_one_damage # applies damage from move one
                    elif move_one_type == "Defend":
                        damage_dealt = move_one_damage
                    attack_one_cooldown = False # resets cooldown time
                    current_time_1 = pygame.time.get_ticks()
        else:
                new_time_1 = pygame.time.get_ticks()
                if new_time_1 - current_time_1 >= move_one_cooldown:
                    attack_one_cooldown = True
        if attack_two_cooldown:
            if player_health <= 0:
                pass
            elif enemy_health > 0:
                if keys[pygame.K_2]:
                    speed = move_two_speed
                    block_defense = move_two_defense
                    if move_two_type == "Attack":
                        attack_animation()
                        damage_dealt = move_two_damage
                    elif move_two_type == "Defend":
                        damage_dealt = move_two_damage
                    attack_two_cooldown = False
                    current_time_2 = pygame.time.get_ticks()
        else:
                new_time_2 = pygame.time.get_ticks()
                if new_time_2 - current_time_2 >= move_two_cooldown:
                    attack_two_cooldown = True
        if attack_three_cooldown:
            if player_health <= 0:
                pass
            elif enemy_health > 0:
                if keys[pygame.K_3]:
                    speed = move_three_speed
                    block_defense = move_three_defense
                    if move_three_type == "Attack":
                        attack_animation()
                        damage_dealt = move_three_damage
                    elif move_three_type == "Defend":
                        damage_dealt = move_three_damage
                    attack_three_cooldown = False
                    current_time_3 = pygame.time.get_ticks()
        else:
                new_time_3 = pygame.time.get_ticks()
                if new_time_3 - current_time_3 >= move_three_cooldown:
                    attack_three_cooldown = True
        if attack_four_cooldown:
            if player_health <= 0:
                pass
            elif enemy_health > 0:
                if keys[pygame.K_4]:
                    speed = move_four_speed
                    block_defense = move_four_defense
                    if move_four_type == "Attack":
                        attack_animation()
                        damage_dealt = move_four_damage
                    elif move_four_type == "Defend":
                        damage_dealt = move_four_damage  
                    attack_four_cooldown = False
                    current_time_4 = pygame.time.get_ticks()
        else:
                new_time_4 = pygame.time.get_ticks()
                if new_time_4 - current_time_4 >= move_four_cooldown:
                    attack_four_cooldown = True

        draw_ecllipse()
        player_bars()
        player_techniques()
        level_track()
        damage_recieved = 0
        damage_dealt = 0
        # Randomly generates a number to see what attack the enemy will be using, all attacks are taken directly from the stats of that enemy
        if enemy_turn:
            enemy_fight = random.randint(1,100)
            if enemy_fight <= 25:
                enemy_current_time = pygame.time.get_ticks()
                enemy_turn = False
                enemy_attack_one = True
            elif enemy_fight <= 50:
                enemy_current_time = pygame.time.get_ticks()
                enemy_turn = False
                enemy_attack_two = True
            elif enemy_fight <= 75:
                enemy_current_time = pygame.time.get_ticks()
                enemy_turn = False
                enemy_attack_three = True
            elif enemy_fight <= 100:
                enemy_current_time = pygame.time.get_ticks()
                enemy_turn = False
                enemy_attack_four = True
        if enemy_attack_one:
            if enemy_health <= 0:
                pass
            elif player_health > 0:
                new_enemy_time = pygame.time.get_ticks()
                if new_enemy_time - enemy_current_time >= enemy_cooldown_one:
                    enemy_attack()
                    damage_recieved = enemy_damage_one
                    enemy_block_defense = enemy_defense_one
                    enemy_attack_one = False
                    enemy_turn = True
        elif enemy_attack_two:
            if enemy_health <= 0:
                pass
            elif player_health > 0:
                new_enemy_time = pygame.time.get_ticks()
                if new_enemy_time - enemy_current_time >= enemy_cooldown_two:
                    enemy_attack()
                    damage_recieved = enemy_damage_two
                    enemy_block_defense = enemy_defense_two
                    enemy_attack_two = False
                    enemy_turn = True
        elif enemy_attack_three:
            if enemy_health <= 0:
                pass
            elif player_health > 0:
                new_enemy_time = pygame.time.get_ticks()
                if new_enemy_time - enemy_current_time >= enemy_cooldown_three:
                    enemy_attack()
                    damage_recieved = enemy_damage_three
                    enemy_block_defense = enemy_defense_three
                    enemy_attack_three = False
                    enemy_turn = True
        elif enemy_attack_four:
            if enemy_health <= 0:
                pass
            elif player_health > 0:
                new_enemy_time = pygame.time.get_ticks()
                if new_enemy_time - enemy_current_time >= enemy_cooldown_four:
                    enemy_attack()
                    damage_recieved = enemy_damage_four
                    enemy_block_defense = enemy_defense_four
                    enemy_attack_four = False
                    enemy_turn = True
        
        draw_ecllipse()
        player_bars()
        player_techniques()
        level_track()
        damage_recieved = 0
        damage_dealt = 0
        # Checks if enemy or player has died, if they have died the death animation will occur
        if enemy_health > 0:
            screen.blit(enemy, enemy_rect)
        else: 
            enemy_turn = False
            enemy_death()
            current_xp = current_xp + enemy_xp
            player_bars()
            level_track()
            pygame.display.flip()
            level_track()
            money = money + money_drop
            pygame.display.flip()
            time.sleep(2)
            return True
        if player_health > 0:
            screen.blit(image, image_rect)
        else:
            enemy_turn = False
            death()
            time.sleep(2)
            return False
        damage_recieved = 0
        damage_dealt = 0
        clock.tick(60)
        pygame.display.flip()
def heal():
    global player_health 
    global player_total_health
    global player_health_percent
    heal_sound.play()
    while player_health_percent < 100:
        player_health += 1
        player_health_percent = int(player_health/player_total_health*100)
        pygame.draw.rect(screen, Darker_Grey, (560, 250, 800, 200))
        pygame.draw.rect(screen, Dark_Grey, (560, 250, 800, 200), width = 10)
        if player_health_percent >= 50:
            pygame.draw.rect(screen, Green, (585, 400, (player_health_percent*7), 20))
        elif player_health_percent >= 25:
            pygame.draw.rect(screen, Yellow, (585, 400, (player_health_percent*7), 20))
        else:
            pygame.draw.rect(screen, Red, (585, 400, (player_health_percent*7), 20))
        pygame.draw.rect(screen, Black, (585, 400, 700, 20), width = 5)
        player_text = font.render(player_name, True, Green)
        player_text_rect = player_text.get_rect()
        player_text_rect.topleft=(585, 275)
        screen.blit(player_text, player_text_rect)
        player_lvl_text = font.render("level " + str(player_level), True, Green)
        player_lvl_text_rect = player_text.get_rect()
        player_lvl_text_rect.topleft=(1075, 275)
        screen.blit(player_lvl_text, player_lvl_text_rect)
        if player_health <= 0:
            player_hp = font.render("0 /" + str(player_total_health), True, White)
        else: 
            player_hp = font.render(str(player_health) + " /" + str(player_total_health), True, White)
        player_hp_rect = player_hp.get_rect()
        player_hp_rect.topleft=(585, 350)
        screen.blit(player_hp, player_hp_rect)
        if player_health_percent == 100:
            pygame.draw.rect(screen, Darker_Grey, (560, 250, 800, 200))
            pygame.draw.rect(screen, Dark_Grey, (560, 250, 800, 200), width = 10)
            full_health_text = font.render("You have been healed to Full Health", True, Black)
            full_health_text_rect = full_health_text.get_rect()
            full_health_text_rect.topleft=(650, 325)
            screen.blit(full_health_text, full_health_text_rect)
            pygame.display.flip()
            time.sleep(2)
        pygame.display.flip()
        clock.tick(60)

def store(x=100, y=940):
    global image
    shopping = True
    exit_button_rect = pygame.Rect(x, y, 200, 80)  
    exit_button_color = (200, 0, 0)  
    exit_button_hover_color = (255, 50, 50)  
    font = pygame.font.Font(None, 48)  
    button_text = font.render("Exit", True, (255, 255, 255))
    chest_content = None

    pygame.mouse.set_visible(True)  

    while shopping:
        screen.blit(store_background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                shopping = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if chest_rect.collidepoint(event.pos):
                    chest_content = random.choices(items, weights=rarity, k=1)[0]
                    print(f"Chest contains: {chest_content}")
                elif exit_button_rect.collidepoint(event.pos):
                    shopping = False

        pygame.draw.rect(screen, dark_brown, lid_rect)
        pygame.draw.rect(screen, Brown, chest_rect)
        pygame.draw.rect(screen, gold, lock_rect)

        if chest_content is not None:
            content_text = font.render(f"You got: {chest_content}", True, Black)
            content_text_rect = content_text.get_rect(center=(960, 540))
            screen.blit(content_text, content_text_rect)

        mouse_pos = pygame.mouse.get_pos()
        if exit_button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, exit_button_hover_color, exit_button_rect)
        else:
            pygame.draw.rect(screen, exit_button_color, exit_button_rect)

     
        text_rect = button_text.get_rect(center=exit_button_rect.center)
        screen.blit(button_text, text_rect)
        pygame.display.flip()
        clock.tick(60)
# main code
while running:
    clock.tick(fps)
    screen.fill('white')

    # mouse positioning and click detection
    mouse_position = pygame.mouse.get_pos()
    button = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            current_cursor = cursor_down  # changes click sprite
            if current_screen == 'settings' and volume_slider_rect.collidepoint(mouse_position):
                slider_dragging = True  # start dragging the slider
            elif current_screen == 'play' and volume_slider_rect.collidepoint(mouse_position):
                slider_dragging = True  
        elif event.type == pygame.MOUSEBUTTONUP:
            slider_dragging = False  # stop dragging the slider
            current_cursor = cursor_up  # revert to default cursor
            
            if current_screen == 'main menu':
                if play_button_rect.collidepoint(mouse_position):  # button click detection
                    button_click.play()
                    current_screen = 'play'
                elif settings_button_rect.collidepoint(mouse_position):
                    button_click.play()
                    current_screen = 'settings'
                elif credits_button_rect.collidepoint(mouse_position):
                    button_click.play()
                    current_screen = 'credits'
                elif quit_button_rect.collidepoint(mouse_position):
                    running = False
            elif current_screen == 'settings':
                if backbutton_rect1.collidepoint(mouse_position):  # back button
                    button_click.play()
                    current_screen = 'main menu'
                elif fps_30_rect.collidepoint(mouse_position):  # change FPS
                    button_click.play()
                    fps = 30
                elif fps_60_rect.collidepoint(mouse_position):
                    button_click.play()
                    fps = 60
                elif fps_144_rect.collidepoint(mouse_position):
                    button_click.play()
                    fps = 144

            elif current_screen == 'credits':
                if backbutton_rect2.collidepoint(mouse_position):
                    button_click.play()
                    current_screen = 'main menu'

            elif current_screen == 'play':
                if exit_button_rect.collidepoint(mouse_position):
                    button_click.play()
                    current_screen = 'main menu'
                    open_settings = False
                if menu_button_rect.collidepoint(mouse_position):
                    button_click.play()
                    open_settings = True    # opens up settings menu
                if backbutton_rect3.collidepoint(mouse_position):
                    button_click.play()
                    open_settings = False
                elif fps_30_rect.collidepoint(mouse_position):  # change FPS
                    button_click.play()
                    fps = 30
                elif fps_60_rect.collidepoint(mouse_position):
                    button_click.play()
                    fps = 60
                elif fps_144_rect.collidepoint(mouse_position):
                    button_click.play()
                    fps = 144

        elif event.type == pygame.MOUSEMOTION:
            if slider_dragging:  # if dragging, update the slider position
                volume_x = mouse_position[0]
                volume_x = max(316, min(mouse_position[0], 1597))
                volume_slider_rect.centerx = volume_x  # update slider rect position
                volume_level = (volume_x - 316) / (1597 - 316)  # calculates the volume of the music based on position of the slider
                pygame.mixer.music.set_volume(volume_level) # sets music volume

    # menu pages
    if current_screen == 'main menu':
        screen.blit(menu_background, menu_background_rect)   # main menu image
        screen.blit(play_button, play_button_rect)  # main menu buttons
        screen.blit(settings_button, settings_button_rect)
        screen.blit(credits_button, credits_button_rect)
        screen.blit(quit_button, quit_button_rect)

        if play_button_rect.collidepoint(mouse_position):  # hover feature for play button
            screen.blit(pressed_play_button, play_button_rect)
        if settings_button_rect.collidepoint(mouse_position):  # hover feature for settings button
            screen.blit(pressed_settings_button, settings_button_rect)
        if credits_button_rect.collidepoint(mouse_position):  # hover feature for credits button
            screen.blit(pressed_credits_button, credits_button_rect)
        if quit_button_rect.collidepoint(mouse_position):
            screen.blit(quit_button_pressed, quit_button_rect)

    elif current_screen == 'settings':
        screen.blit(menu_background, menu_background_rect) # main menu image
        screen.blit(settings_page, settings_page_rect)  # settings image page
        screen.blit(fps_30, fps_30_rect)  # FPS buttons
        screen.blit(fps_60, fps_60_rect)
        screen.blit(fps_144, fps_144_rect)
        screen.blit(fps_text, fps_text_rect)  # settings text
        screen.blit(master_vol, master_vol_rect)    # audio text
        screen.blit(volume_bar, volume_bar_rect)
        screen.blit(volume_slider, volume_slider_rect)  # audio slider
        screen.blit(backbutton, backbutton_rect1)

        if fps_30_rect.collidepoint(mouse_position):  # hover feature for FPS buttons
            screen.blit(fps_30_pressed, fps_30_rect)
        if fps_60_rect.collidepoint(mouse_position):
            screen.blit(fps_60_pressed, fps_60_rect)
        if fps_144_rect.collidepoint(mouse_position):
            screen.blit(fps_144_pressed, fps_144_rect)
        if backbutton_rect1.collidepoint(mouse_position):
            screen.blit(backbutton_pressed, backbutton_rect1)
    
    elif current_screen == 'credits':
        screen.blit(credits, credits_rect)
        screen.blit(backbutton, backbutton_rect2)

        if backbutton_rect2.collidepoint(mouse_position):
            screen.blit(backbutton_pressed, backbutton_rect2)

    elif current_screen == 'play':
        selecting_moves_menu()
        world_one()
        
    # mouse position updates
    screen.blit(current_cursor, mouse_position)
    # update display
    pygame.display.flip()
