import pygame
from pygame import *
from pygame.font import *

# display
pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
info_object = pygame.display.Info()

width, height = info_object.current_w, info_object.current_h

screen = pygame.display.set_mode((width, height))
fps = 144
pygame.display.set_caption('Mastering Balance')
clock = pygame.time.Clock()

# custom cursor
cursor_up = pygame.image.load('images/cursorUp.png')
cursor_down = pygame.image.load('images/cursorDown.png')
current_cursor = cursor_up
cursor_rect = cursor_up.get_rect()
pygame.mouse.set_visible(False)

# buttons
play_button = pygame.image.load('images/play_button4x.png')  # play button
play_button_rect = play_button.get_rect(center=(info_object.current_w // 2, info_object.current_h // 2 + 150))
pressed_play_button = pygame.image.load('images/pressed_play.png')

settings_button = pygame.image.load('images/settings_button.png')  # settings button
settings_button_rect = settings_button.get_rect(center=(info_object.current_w // 2, (info_object.current_h // 2) + 300))
pressed_settings_button = pygame.image.load('images/pressed_settings.png')

credits_button = pygame.image.load('images/credits_button.png')  # credits button
credits_button_rect = credits_button.get_rect(center=(info_object.current_w // 2, (info_object.current_h // 2) + 450))
pressed_credits_button = pygame.image.load('images/pressed_credits.png')

fps_30 = pygame.image.load('images/30_fps_button.png')  # 30 fps button
fps_30_rect = fps_30.get_rect(center=(info_object.current_w // 2 - 150, (info_object.current_h // 2) + 100))
fps_30_pressed = pygame.image.load('images/30_fps_pressed.png')

fps_60 = pygame.image.load('images/60_fps_button.png')  # 60 fps button
fps_60_rect = fps_30.get_rect(center=(info_object.current_w // 2 + 100, (info_object.current_h // 2) + 100))
fps_60_pressed = pygame.image.load('images/60_fps_pressed.png')

fps_144 = pygame.image.load('images/144_fps_button.png')  # 144 fps button
fps_144_rect = fps_30.get_rect(center=(info_object.current_w // 2 + 350, (info_object.current_h // 2) + 100))
fps_144_pressed = pygame.image.load('images/144_fps_pressed.png')

backbutton = pygame.image.load('images/backbutton.png')
backbutton_rect1 = backbutton.get_rect(center=(info_object.current_w // 2 - 550, (info_object.current_h // 2 - 325)))
backbutton_rect2 = backbutton.get_rect(center=(info_object.current_w // 2 - 850, (info_object.current_h // 2 - 450)))
backbutton_rect3 = backbutton.get_rect(center=(info_object.current_w // 2 - 550, (info_object.current_h // 2 - 325)))
backbutton_pressed = pygame.image.load('images/backbutton_hover.png')

menu_button = pygame.image.load('images/menu.png')
menu_button_rect = menu_button.get_rect(center=(info_object.current_w // 2 - 800, (info_object.current_h // 2 - 450)))
menu_button_pressed = pygame.image.load('images/pressed_menu.png')

exit_button = pygame.image.load('images/exit.png')
exit_button_rect = menu_button.get_rect(center=(info_object.current_w // 2 + 650, (info_object.current_h // 2 - 325)))
exit_button_pressed = pygame.image.load('images/exit_pressed.png')

quit_button = pygame.image.load('images/quit.png')
quit_button_rect = quit_button.get_rect(center=(info_object.current_w // 2 + 900, (info_object.current_h // 2 - 475)))
quit_button_pressed = pygame.image.load('images/quit_pressed.png')

# images
fps_text = pygame.image.load('images/fps_display.png')
fps_text_rect = fps_text.get_rect(center=(info_object.current_w // 2 - 400, (info_object.current_h // 2) + 100))

master_vol = pygame.image.load('images/master_vol.png')
master_vol_rect = master_vol.get_rect(center=(info_object.current_w // 2, (info_object.current_h // 2) - 250))

volume_bar = pygame.image.load('images/volume_bar.png')
volume_bar_rect = volume_bar.get_rect(center=(info_object.current_w // 2, (info_object.current_h // 2) - 100))

volume_slider = pygame.image.load('images/vol_slider.png')
volume_x, volume_y = info_object.current_w // 2, (info_object.current_h // 2) - 100
volume_slider_rect = volume_slider.get_rect(center=(volume_x, volume_y))

menu_background = pygame.image.load('images/main_menu_background.png')
menu_background_rect = menu_background.get_rect(center=(info_object.current_w // 2, (info_object.current_h // 2)))

credits = pygame.image.load('images/credits.png')
credits_rect = credits.get_rect(center=(info_object.current_w // 2, (info_object.current_h // 2)))


# settings page
settings_page = pygame.image.load('images/settings_page.png')
settings_page_rect = settings_page.get_rect(center=(info_object.current_w // 2, (info_object.current_h // 2)))

# variables
current_screen = 'main menu'
running = True
slider_dragging = False  # track if the slider is being dragged
open_settings = False

# sound

background_music = pygame.mixer.music.load('sound/background_music.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
button_click = pygame.mixer.Sound('sound/button_sound.mp3')

# main code
while running:
    clock.tick(fps)
    screen.fill('white')

    # mouse positioning and click detection
    mouse_position = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            current_cursor = cursor_down  # click detection
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
        screen.blit(menu_button, menu_button_rect)

        if menu_button_rect.collidepoint(mouse_position):
            screen.blit(menu_button_pressed, menu_button_rect)
        if open_settings:   # same buttons as settings page
            screen.blit(settings_page, settings_page_rect)  
            screen.blit(fps_30, fps_30_rect)  
            screen.blit(fps_60, fps_60_rect)
            screen.blit(fps_144, fps_144_rect)
            screen.blit(fps_text, fps_text_rect)  
            screen.blit(master_vol, master_vol_rect)    
            screen.blit(volume_bar, volume_bar_rect)
            screen.blit(volume_slider, volume_slider_rect)  
            screen.blit(backbutton, backbutton_rect1)
            screen.blit(exit_button, exit_button_rect)  # exit button

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

    # mouse position updates
    screen.blit(current_cursor, mouse_position)
    # update display
    pygame.display.flip()
