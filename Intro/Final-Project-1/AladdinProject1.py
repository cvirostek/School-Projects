# Codeskulptor link: http://www.codeskulptor.org/#user28_OODGyXHHfn_1.py

##### INSTRUCTIONS #####
# Use the arrow keys to control Aladdin's movement.
# Press the space bar to fire a lazer.
# The object of the game is to get as far as you can.
# Monkeys will fly from the right of the screen and try to shoot you.
# You will lose a life if a monkey escapes or hits you with a bullet.


import simplegui
import random

#set variables
WIDTH = 1000
HEIGHT = 500
background_pos = [WIDTH/2, HEIGHT/2+100/2]
bullet_pos = [-100, -100]
bullet_hurts = True
explosion_frame = [0, 0]
explosion_frame_number = 0
kill_counter = 0
lazer_fire = 1
lazer_stop = False
lives = 5
player_size = (409/3, 478/3)
player_pos = [WIDTH/4, HEIGHT/2]
player_frame = 409/2
player_frame_number = 0
player_speed = 10
player_rotation = 0
player_exploded = 0
gameOn = False
gameover = False
gameover_setup = True
monkey_dead = 0
monkey_pos = [1161, random.randint(360/6, HEIGHT-360/6)]
monkey_speed = 10
score = 0
score_high = 0
spinwheel = 0
title_movement = [-0.75, 1] #[rotation (radians), size multiplier]
title_spin = 0.05
title_pulse = 0.1
velocity_down = 0
velocity_up = 0
velocity_left = 0
velocity_right = 0
wub = False

#load images
image_background = simplegui.load_image('https://www.dropbox.com/s/kfiam5shvir3vri/background.jpg?dl=1')
image_monkey = simplegui.load_image('https://www.dropbox.com/s/blll39j2x7hxpo8/Aladdin%20monkey.png?dl=1')
image_player = simplegui.load_image('https://www.dropbox.com/s/3htfpwknmwi9gc9/player.png?dl=1')
image_lazer = simplegui.load_image('https://www.dropbox.com/s/yvdm7fsr1w7pyim/LAZEHR.png?dl=1')
image_bullet = simplegui.load_image('https://www.dropbox.com/s/0b7ngj06liw0q66/bulletbill.png?dl=1')
image_menu = simplegui.load_image('https://www.dropbox.com/s/4e7tfibjnxnkp58/menu_background.png?dl=1')
image_pinwheel = simplegui.load_image('https://www.dropbox.com/s/iyv6xitsawqvmxk/sunburst.jpg?dl=1')
image_title = simplegui.load_image('https://www.dropbox.com/s/8pc8v10t6y6z1zj/title.png?dl=1')
image_explosion = simplegui.load_image('https://www.dropbox.com/s/q0oy2m0nkmnvnth/explosion.png?dl=1')
image_gameover = simplegui.load_image('https://www.dropbox.com/s/nn0tbjavf3o2hty/gameover.jpg?dl=1')

#load sounds
sound_regular = simplegui.load_sound('https://www.dropbox.com/s/cz72vwkpc4lezmp/Regular%20theme.mp3?dl=1')
sound_wub = simplegui.load_sound('https://www.dropbox.com/s/chtr9j8ob1l8y8y/Freak%20It%20by%20Spag%20Heddy.mp3?dl=1')
sound_home = simplegui.load_sound('https://www.dropbox.com/s/qjo3kh53z03nq5r/Home%20screen%20music.mp3?dl=1')
sound_explosion = simplegui.load_sound('https://www.dropbox.com/s/m5edgvjy3y3d3hw/Bomb%203-SoundBible.com-1260663209.mp3?dl=1')
sound_lazer = simplegui.load_sound('https://www.dropbox.com/s/r76v1fncomi09a4/lazersound.wav?dl=1')
sound_gameover = simplegui.load_sound('https://www.dropbox.com/s/nkgcpm7u396il7z/Super-Mario-Bros-Game-Over-sound-effect-Super-Mario-Bros-Game-Over-sound-effect.mp3?dl=1')
sound_hurt = simplegui.load_sound('https://www.dropbox.com/s/tpccg5e0v9klyin/WilhelmScream_vbr.mp3?dl=1')
sound_monkey_escape = simplegui.load_sound('https://www.dropbox.com/s/rbw897zhjh4dhki/Goatscream.wav?dl=1')
sound_bullet = simplegui.load_sound('https://www.dropbox.com/s/dzqilg0hgln58xd/bulletsound.mp3?dl=1')

#set sound volumes
sound_regular.set_volume(0.4)
sound_wub.set_volume(0)
sound_explosion.set_volume(0.6)
sound_hurt.set_volume(0.5)
sound_monkey_escape.set_volume(0.4)
sound_gameover.set_volume(0.9)

#sets button to give unlimited lives on first click, and end game on second
def click():
    global lives
    if lives>0:
        lives = -1
    else:
        lives = 0

#toggles between two different songs for the in-game music
def click2():
    global wub
    if not wub:
        wub = True
        sound_wub.set_volume(0.4)
        sound_regular.set_volume(0)
    elif wub:
        wub = False
        sound_regular.set_volume(0.4)
        sound_wub.set_volume(0)

#resets the necessary variables when a new game is started
def reset_variables():
    global monkey_dead, monkey_pos, bullet_pos, lives, bullet_hurts, monkey_speed, explosion_frame, explosion_frame_number, velocity_up, velocity_down, velocity_left, velocity_right, player_rotation, player_pos, gameover_setup, player_exploded, score, kill_counter
    gameover_setup = True
    player_exploded = 0
    score = 0
    monkey_dead = 0
    monkey_pos = [1161, random.randint(360/6, HEIGHT-360/6)]
    bullet_pos = [-100, -100]
    lives = 5
    bullet_hurts = True
    monkey_speed = 10
    explosion_frame = [0, 0]
    explosion_frame_number = 20
    velocity_down = 0
    velocity_up = 0
    velocity_left = 0
    velocity_right = 0
    player_rotation = 0
    player_pos = [WIDTH/2, HEIGHT/2]
    kill_counter = 0

#draw handler
def draw(canvas):
    global image_player, player_frame, player_pos, monkey_pos, bullet_pos, explosion_frame_number, monkey_dead, lives, bullet_hurts, gameOn, monkey_speed, spinwheel, title_movement, title_spin, title_pulse, gameover, kill_counter
    if not gameOn:
        #plays music
        if not gameover:
            sound_home.play()
        sound_wub.pause()
        sound_wub.rewind()
        sound_regular.pause()
        sound_regular.rewind()
        #title screen animations
        spinwheel += 0.05
        title_movement[0]+=title_spin
        title_movement[1]+=title_pulse
        if title_movement[0]<-0.5:
            title_spin=0.05
        elif title_movement[0]>0.5:
            title_spin=-0.05
        if title_movement[1]>1.6:
            title_pulse=-0.05
        elif title_movement[1]<1:
            title_pulse=0.05
        #draw title screen images
        canvas.draw_image(image_pinwheel, (1500 / 2, 1500 / 2), (1500, 1500), (WIDTH/2, HEIGHT/2), (1500, 1500), spinwheel)
        canvas.draw_image(image_menu, (1000 / 2, 500 / 2), (1000, 500), (WIDTH/2, HEIGHT/2+HEIGHT/8), (1000, 500))
        canvas.draw_image(image_player, (player_frame, 478 / 2), (409, 478), (WIDTH/8, HEIGHT*0.575), (409/2, 478/2), title_movement[0]*-0.5)
        canvas.draw_image(image_monkey, (504 / 2, 360 / 2 + monkey_dead), (504, 360), (WIDTH*(7.0/8), HEIGHT*0.62+title_movement[0]*30), (504/2, 360/2))
        canvas.draw_image(image_title, (734 / 2, 275 / 2), (734, 275), (WIDTH/2, HEIGHT/2.5), (734/2*title_movement[1], 275/2*title_movement[1]), title_movement[0])
    if gameOn:
        #stop home music, play game music
        sound_home.pause()
        sound_home.rewind()
        sound_regular.play()
        sound_wub.play()
        #lose a life when hit
        if bullet_hurts:
            if bullet_pos[0]<player_pos[0]+player_size[0]/4 and bullet_pos[0]>player_pos[0]-player_size[0]/4:
                if bullet_pos[1]<player_pos[1]+player_size[1]/2+206/20 and bullet_pos[1]>player_pos[1]-player_size[1]/2-206/20:
                    lives -= 1
                    bullet_hurts = False
                    sound_hurt.play()
                    timer_hurt_sound.start()
        #draws moving background
        canvas.draw_image(image_background, (3000 / 2, 600 / 2), (3000, 600), background_pos, (3000, 600))
        background_pos[0] -= monkey_speed-5
        if background_pos[0] < 0:
            background_pos[0] = 3000/2
        #draws lives
        canvas.draw_text('Lives: '+str(lives), (10, 30), 36, 'Red')
        #draws score
        canvas.draw_text('Distance: '+str(score)+"m", (775, 30), 36, 'Red')
        #draws kills
        canvas.draw_text('Kills: '+str(kill_counter), (375, 30), 36, 'Red')
        #draws player
        canvas.draw_image(image_player, (player_frame, 478 / 2), (409, 478), player_pos, player_size, player_rotation)
        #moves player
        player_pos[0] += velocity_right
        player_pos[0] -= velocity_left
        player_pos[1] -= velocity_up
        player_pos[1] += velocity_down
        #keeps player on screen
        if player_pos[0] < player_size[0]/2:
            player_pos[0] = player_size[0]/2
        if player_pos[0] > WIDTH - player_size[0]/2:
            player_pos[0] = WIDTH - player_size[0]/2
        if player_pos[1] < player_size[1]/2:
            player_pos[1] = player_size[1]/2
        if player_pos[1] > HEIGHT:
            player_pos[1] = HEIGHT
        #draws/moves monkeys
        canvas.draw_image(image_monkey, (504 / 2, 360 / 2 + monkey_dead), (504, 360), monkey_pos, (504/3, 360/3))
        monkey_pos[0] -= monkey_speed
        #resets monkey/bullet/explosion
        if monkey_pos[0]<-160:
            explosion_frame_number = 20
            if monkey_dead == 0:
                lives -= 1
                sound_monkey_escape.play()
                timer_monkey_sound.start()
            monkey_pos[1]=random.randint(360/6, HEIGHT-360/6)
            monkey_pos[0]=WIDTH+160
            monkey_dead = 0
            bullet_hurts = True
            monkey_speed += 0.2
        #draws lazer
        canvas.draw_image(image_lazer, (1000 / 2, 40 / 2), (1000, 40+lazer_fire), (player_pos[0]+525, player_pos[1]-75), (1000, 30))
        #draws/moves bullet
        if monkey_pos[0] > 800 and monkey_pos[0] < 800 + monkey_speed + 16:
            if monkey_dead == 0:
                bullet_pos[0] = monkey_pos[0]-55
                bullet_pos[1] = monkey_pos[1]-40
                sound_bullet.play()
                timer_bullet_sound.start()
        canvas.draw_image(image_bullet, (333 / 2, 206 / 2 + 1 - int(bullet_hurts)), (333, 206), (bullet_pos[0], bullet_pos[1]), (333/10, 206/10))
        bullet_pos[0] -= monkey_speed + 15
        #draws explosion
        canvas.draw_image(image_explosion, explosion_frame, (320, 240), monkey_pos, (1280/2, 1200/2))
        #makes monkey explode
        if not lazer_stop and lazer_fire == 0:
            if monkey_pos[0] > player_pos[0] + 25 and monkey_dead == 0:
                if monkey_pos[1] > player_pos[1] - 135 and monkey_pos[1] < player_pos[1] - 15:
                    timer_animation_explosion.start()
                    explosion_frame_number = 0
                    monkey_dead = 1
                    sound_explosion.play()
                    timer_boom_sound.start()
                    kill_counter += 1
        #ends game at 0 lives
        if lives == 0:
            gameOn = False
            gameover = True
            canvas.draw_image(image_menu, (1000 / 2, 500 / 2), (1000, 500), (WIDTH/2, HEIGHT/2), (1000, 500))
            timer_gameover.start()
    #game over sequence
    if gameover:
        #draws game over screen and final score
        timer_distance.stop()
        canvas.draw_image(image_gameover, (1000 / 2, 500 / 2), (1000, 500), (WIDTH/2, HEIGHT/2), (1000, 500))
        canvas.draw_text("High Score: "+str(score_high), (WIDTH/2-100, HEIGHT/3-100), 36, 'White')
        canvas.draw_text("Score: "+str(score), (WIDTH/2-60, HEIGHT/3-60), 36, 'White')
        canvas.draw_text("Kills: "+str(kill_counter), (WIDTH/2-40, HEIGHT/3-20), 36, 'White')
        canvas.draw_image(image_player, (player_frame, 478 / 2), (409, 478 + player_exploded), player_pos, player_size, player_rotation)
        canvas.draw_image(image_explosion, explosion_frame, (320, 240), player_pos, (1280/2, 1200/2))
        sound_gameover.play()
        gameover_scene()
    elif not gameover and not gameOn:
        #stops and rewinds gameover sound
        sound_gameover.pause()
        sound_gameover.rewind()

#shows Aladdin crash-landing and exploding after all lives are lost
def gameover_scene():
    global player_pos, player_rotation, monkey_pos, gameover_setup, explosion_frame_number, player_exploded
    if gameover_setup:
        player_rotation = 0.75
        player_pos = [-150, -75]
        gameover_setup = False
    if player_pos[0] > WIDTH - 50:
        if player_exploded == 0:
            timer_animation_explosion.start()
            explosion_frame_number = 0
            sound_explosion.play()
            timer_boom_sound.start()
            player_exploded = 1
    else:
        player_pos[0] += 5
        player_pos[1] += 2
        
#changes the player sprite's frame every 100 milliseconds
def timer_handler_animation_player():
    global player_frame, player_frame_number
    player_frame_number+=1
    if player_frame_number==3:
        player_frame_number=0
    player_frame = 409/2 + 409*player_frame_number

#changes the explosion sprite's frame every 40 milliseconds
def timer_handler_animation_explosion():
    global explosion_frame, explosion_frame_number
    if gameOn or gameover:
        explosion_frame_number += 1
        if explosion_frame_number == 20:
            timer_animation_explosion.stop()
        explosion_frame[0] = 320/2 + 320*(explosion_frame_number % 4)
        explosion_frame[1] = 240/2 + 240*(explosion_frame_number/4)
        
#turns the lazer back off after 100 milliseconds
def timer_handler_lazer():
    global lazer_fire, lazer_stop
    if gameOn:
        if lazer_stop:
            lazer_stop = False
            timer_lazer.stop()
        else:
            lazer_stop = True
            lazer_fire = 1
            
#shows the game over screen for 5 seconds
def timer_handler_gameover():
    global gameover, gameOn
    gameover = False
    timer_gameover.stop()

#stops and rewinds the explosion sound after it has played for 1 second
def timer_handler_boom_sound():
    sound_explosion.pause()
    sound_explosion.rewind()
    timer_boom_sound.stop()

#stops and rewinds the lazer sound after it has played for 0.5 seconds
def timer_handler_pew_sound():
    sound_lazer.pause()
    sound_lazer.rewind()
    timer_pew_sound.stop()

#stops and rewinds the hurt sound after it has played for 1 second
def timer_handler_hurt_sound():
    sound_hurt.pause()
    sound_hurt.rewind()
    timer_hurt_sound.stop()

#stops and rewinds the monkey escaping sound after it has played for 1 second
def timer_handler_monkey_sound():
    sound_monkey_escape.pause()
    sound_monkey_escape.rewind()
    timer_monkey_sound.stop()
    
#stops and rewinds the bullet sound after it has played for 250 milliseconds
def timer_handler_bullet_sound():
    sound_bullet.pause()
    sound_bullet.rewind()
    timer_bullet_sound.stop()

#increases the player score by 1 every 0.5 seconds
def timer_handler_distance():
    global score, score_high
    if score < score_high:
        score += 1
    else:
        score += 1
        score_high += 1
        
def keydown(key):
    global velocity_up, velocity_down, velocity_left, velocity_right, lazer_fire, gameOn
    if key and not gameOn:
        #allows you to start a new game by pressing any button at the title screen
        if not gameover:
            gameOn = True
            reset_variables()
            timer_distance.start()
    if gameOn:
        #controls player movement
        if key == simplegui.KEY_MAP['down']:
            velocity_down = player_speed
        elif key == simplegui.KEY_MAP['up']:
            velocity_up = player_speed
        elif key == simplegui.KEY_MAP['left']:
            velocity_left = player_speed
        elif key == simplegui.KEY_MAP['right']:
            velocity_right = player_speed
            
        #fires the lazer when you press space
        elif key == simplegui.KEY_MAP['space'] and not lazer_stop:
            timer_pew_sound.stop()
            lazer_fire = 0
            sound_lazer.pause()
            sound_lazer.rewind()
            timer_lazer.start()
            sound_lazer.play()
            timer_pew_sound.start()
    
def keyup(key):    
    global velocity_up, velocity_down, velocity_left, velocity_right, lazer_fire
    if gameOn:
        #controls player movement
        if key == simplegui.KEY_MAP['down']:
            velocity_down = 0
        elif key == simplegui.KEY_MAP['up']:
            velocity_up = 0
        elif key == simplegui.KEY_MAP['left']:
            velocity_left = 0
        elif key == simplegui.KEY_MAP['right']:
            velocity_right = 0
    
#create frame/handlers
frame = simplegui.create_frame("Aladdin: The Movie: The Game", WIDTH, HEIGHT)
frame.add_button("Cheat", click)
frame.add_button("Wub", click2)
frame.set_draw_handler(draw)
timer_animation_player = simplegui.create_timer(100, timer_handler_animation_player)
timer_lazer = simplegui.create_timer(100, timer_handler_lazer)
timer_animation_explosion = simplegui.create_timer(40, timer_handler_animation_explosion)
timer_gameover = simplegui.create_timer(5000, timer_handler_gameover)
timer_boom_sound = simplegui.create_timer(1000, timer_handler_boom_sound)
timer_pew_sound = simplegui.create_timer(500, timer_handler_pew_sound)
timer_hurt_sound = simplegui.create_timer(1000, timer_handler_hurt_sound)
timer_distance = simplegui.create_timer(500, timer_handler_distance)
timer_monkey_sound = simplegui.create_timer(1000, timer_handler_monkey_sound)
timer_bullet_sound = simplegui.create_timer(250, timer_handler_bullet_sound)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

#start frame/animations
timer_animation_player.start()
frame.start()

