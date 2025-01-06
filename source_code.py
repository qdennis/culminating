import pygame
from pygame import *
from pygame.font import *

# display
pygame.init()
info_object = pygame.display.Info()
screen = pygame.display.set_mode((info_object.current_w, info_object.current_h))
fps = 60
pygame.display.set_caption('Mastering Balance')
clock = pygame.time.Clock()

# custom cursor
image = pygame.image.load('cursorUp.png')
image_rect = image.get_rect()
image_rect_centre = (info_object.current_w // 2, info_object.current_h // 2 )
pygame.mouse.set_visible(True)

# buttons

play_button = pygame.image.load('play_button4x.png')    # play button
play_button_rect = play_button.get_rect(center=(info_object.current_w // 2, info_object.current_h // 2))
pressed_play_button = pygame.image.load('pressed_play.png')

settings_button = pygame.image.load('settings_button.png')    # play button
settings_button_rect = settings_button.get_rect(center=(info_object.current_w // 2, (info_object.current_h // 2 )+ 150))
pressed_settings_button = pygame.image.load('pressed_settings.png')

running = True

# main code

while running:
    clock.tick(fps)
    screen.fill('white')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            image = pygame.image.load('cursorDown.png')    # click detection
        elif event.type == pygame.MOUSEBUTTONUP:
            image = pygame.image.load('cursorUp.png')
        if event.type == pygame.MOUSEBUTTONUP:
            if play_button_rect.collidepoint(mouse_position):   # button click detection
                print('button 14r')
            if settings_button_rect.collidepoint(mouse_position):
                print('button 2')

    speed = 10

    # add movement binds as well as character image
    #
    #

    # mouse positioning and click detection
    mouse_position = pygame.mouse.get_pos()
    screen.blit(play_button, play_button_rect) # button position
    screen.blit(settings_button, settings_button_rect)

    # button hover feature

    if play_button_rect.collidepoint(mouse_position):
        screen.blit(pressed_play_button, play_button_rect)
    else:
        screen.blit(play_button, play_button_rect)
    
    if settings_button_rect.collidepoint(mouse_position):
        screen.blit(pressed_settings_button, settings_button_rect)
    else:
        screen.blit(settings_button, settings_button_rect)

    screen.blit(image, mouse_position, image_rect) # cursor position updates
    

    # title screen




    pygame.display.flip()
    
