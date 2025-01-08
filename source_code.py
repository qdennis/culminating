import pygame
from pygame import *
from pygame.font import *

# display
pygame.init()
info_object = pygame.display.Info()

width, height = info_object.current_w, info_object.current_h

screen = pygame.display.set_mode((width, height))
fps = 60
pygame.display.set_caption('Mastering Balance')
clock = pygame.time.Clock()

# custom cursor
cursor_up = pygame.image.load('cursorUp.png')
cursor_down = pygame.image.load('cursorDown.png')
current_cursor = cursor_up
cursor_rect = cursor_up.get_rect()
pygame.mouse.set_visible(False)

# buttons
play_button = pygame.image.load('play_button4x.png')  # play button
play_button_rect = play_button.get_rect(center=(info_object.current_w // 2, info_object.current_h // 2))
pressed_play_button = pygame.image.load('pressed_play.png')

settings_button = pygame.image.load('settings_button.png')  # settings button
settings_button_rect = settings_button.get_rect(center=(info_object.current_w // 2, (info_object.current_h // 2) + 150))
pressed_settings_button = pygame.image.load('pressed_settings.png')

credits_button = pygame.image.load('credits_button.png')  # credits button
credits_button_rect = credits_button.get_rect(center=(info_object.current_w // 2, (info_object.current_h // 2) + 300))
pressed_credits_button = pygame.image.load('pressed_credits.png')

fps_30 = pygame.image.load('30_fps_button.png') # 30 fps button
fps_30_rect = fps_30.get_rect(center=(info_object.current_w // 2 - 150, (info_object.current_h // 2) + 100))
fps_30_pressed = pygame.image.load('30_fps_pressed.png')

fps_60 = pygame.image.load('60_fps_button.png') # 60 fps button
fps_60_rect = fps_30.get_rect(center=(info_object.current_w // 2 + 100 , (info_object.current_h // 2) + 100))
fps_60_pressed = pygame.image.load('60_fps_pressed.png')

fps_144 = pygame.image.load('144_fps_button.png') # 144 fps button
fps_144_rect = fps_30.get_rect(center=(info_object.current_w // 2 + 350, (info_object.current_h // 2) + 100))
fps_144_pressed = pygame.image.load('144_fps_pressed.png')

# images

fps_text = pygame.image.load('fps_display.png')
fps_text_rect = fps_text.get_rect(center=(info_object.current_w // 2 - 400, (info_object.current_h // 2) + 100))

master_vol = pygame.image.load('master_vol.png')
master_vol_rect = master_vol.get_rect(center=(info_object.current_w // 2, (info_object.current_h // 2) - 250))

volume_bar = pygame.image.load('volume_bar.png')
volume_bar_rect = volume_bar.get_rect(center=(info_object.current_w // 2, (info_object.current_h // 2) - 100))

volume_slider = pygame.image.load('vol_slider.png')
volume_slider_rect = volume_slider.get_rect(center=(info_object.current_w // 2, (info_object.current_h // 2) - 100))

# settings page
settings_page = pygame.image.load('settings_page.png')
settings_page_rect = settings_page.get_rect(center=(info_object.current_w // 2, (info_object.current_h // 2)))

# variables
current_screen = 'main menu'
running = True

# main code
while running:
    clock.tick(fps)
    screen.fill('white')

    # mouse positioning and click detection
    mouse_position = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            current_cursor = cursor_down  # click detection
        elif event.type == pygame.MOUSEBUTTONUP:
            current_cursor = cursor_up  # revert to default cursor
            if current_screen == 'main menu':
                if play_button_rect.collidepoint(mouse_position):  # button click detection
                    current_screen = 'play'
                elif settings_button_rect.collidepoint(mouse_position):
                    current_screen = 'settings' 
                elif credits_button_rect.collidepoint(mouse_position):
                    current_screen = 'credits'
            elif current_screen == 'settings':
                if not settings_page_rect.collidepoint(mouse_position):  # click outside settings page
                    current_screen = 'main menu'
                elif fps_30_rect.collidepoint(mouse_position):  # changes fps when user clicks on the button
                    fps = 30
                elif fps_60_rect.collidepoint(mouse_position):
                    fps = 60
                elif fps_144_rect.collidepoint(mouse_position):
                    fps = 144

    # add movement binds as well as character image
    #
    #

    # menu pages
    if current_screen == 'main menu':
        screen.blit(play_button, play_button_rect)  # main menu buttons
        screen.blit(settings_button, settings_button_rect)
        screen.blit(credits_button, credits_button_rect)

        if play_button_rect.collidepoint(mouse_position):  # hover feature for play button
            screen.blit(pressed_play_button, play_button_rect)
        if settings_button_rect.collidepoint(mouse_position):  # hover feature for settings button
            screen.blit(pressed_settings_button, settings_button_rect)
        if credits_button_rect.collidepoint(mouse_position):  # hover feature for credits button
            screen.blit(pressed_credits_button, credits_button_rect)

    elif current_screen == 'settings':
        screen.blit(settings_page, settings_page_rect)  # settings image page
        screen.blit(fps_30, fps_30_rect)    # fps buttons
        screen.blit(fps_60, fps_60_rect)
        screen.blit(fps_144, fps_144_rect)
        screen.blit(fps_text, fps_text_rect)    # settings text
        screen.blit(master_vol, master_vol_rect)
        screen.blit(volume_bar, volume_bar_rect)
        screen.blit(volume_slider, volume_slider_rect)
        
        if fps_30_rect.collidepoint(mouse_position):  # hover feature for fps buttons
            screen.blit(fps_30_pressed, fps_30_rect)
        if fps_60_rect.collidepoint(mouse_position):  
            screen.blit(fps_60_pressed, fps_60_rect)
        if fps_144_rect.collidepoint(mouse_position): 
            screen.blit(fps_144_pressed, fps_144_rect)
        

    elif current_screen == 'play':
        pass
        ####################
        # INSERT GAME HERE #
        ####################

    # mouse position updates
    screen.blit(current_cursor, mouse_position)
    # update display
    pygame.display.flip()
