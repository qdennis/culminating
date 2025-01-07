import pygame
from pygame import *
from pygame.font import *

# display
pygame.init()
info_object = pygame.display.Info()
screen = pygame.display.set_mode((info_object.current_w, info_object.current_h - 60))
fps = 144
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

# settings page
settings_page = pygame.image.load('settings_page.png')
settings_page_rect = settings_page.get_rect(center=(info_object.current_w // 2, (info_object.current_h // 2)))

# variables
open_settings = 0
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
        screen.blit(settings_page, settings_page_rect)

    elif current_screen == 'play':
        pass
        ####################
        # INSERT GAME HERE #
        ####################

    # mouse position updates
    screen.blit(current_cursor, mouse_position)

    # update display
    pygame.display.flip()
