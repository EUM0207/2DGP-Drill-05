from pico2d import *

open_canvas(1280, 1024)

background = load_image('TUK_GROUND.png')
character = load_image('adv_chara.png')

running = True
x = 1280 // 2
y = 1024 // 2
dir = (0,0)
frame = 0
idle_frame = 0

def handle_events():
    global running
    global dir
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_RIGHT:
                dir = (1, 0)
            elif event.key == SDLK_LEFT:
                dir = (-1, 0)
            elif event.key == SDLK_DOWN:
                dir = (0, -1)
            elif event.key == SDLK_UP:
                dir = (0, 1)
        elif event.type == SDL_KEYUP:
            if event.key in (SDLK_RIGHT, SDLK_LEFT, SDLK_UP, SDLK_DOWN):
                dir = (0, 0)

while running:
    clear_canvas()

    sprite_y = 0
    if dir == (1, 0):
        sprite_y = 720
    elif dir == (-1, 0):
        sprite_y = 1080
    elif dir == (0, -1):
        sprite_y = 360
    elif dir == (0, 1):
        sprite_y = 0
    else: 
        sprite_y = 0

    if dir != (0, 0):
        frame = (frame + 1) % 6 + 3
    if dir == (0,0):
        frame = (frame + 1) % 3
        idle_frame = frame



    background.draw(1280 // 2, 1024 // 2)
    if dir == (0,0):
        character.clip_draw(idle_frame * 160, sprite_y, 160, 360, x, y, 160, 240)
    if dir[0] == -1 or dir[0] == 1: 
        character.clip_composite_draw(frame * 160, sprite_y, 160, 360, 0, 'h', x, y, 160, 240)
    else:
        character.clip_draw(frame * 160, sprite_y,160, 360, x, y, 160, 240)
    update_canvas()
    handle_events()

    x += dir[0] * 5
    y += dir[1] * 5

    x = clamp(0, x, 1280)
    y = clamp(0, y, 1024)

    delay(0.05)

close_canvas()