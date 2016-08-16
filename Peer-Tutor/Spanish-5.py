# Codeskulptor link: http://www.codeskulptor.org/#user41_W1e9yhZpRi_3.py

import simplegui
import random
import math

#instantiate variables/objects/constants
HEIGHT = 666;
WIDTH = 1184;

#options
show_FPS = False;
cheats = True;

#load images
img_background = simplegui.load_image("https://www.dropbox.com/s/dx0k43m88k4fbw7/background.jpg?dl=1");
img_shaw = simplegui.load_image("https://www.dropbox.com/s/dn4xh8o8yakxrai/shaw.png?dl=1");
img_can = simplegui.load_image("https://www.dropbox.com/s/9fx7ke0efstxpjh/can.png?dl=1");
img_player = simplegui.load_image("https://www.dropbox.com/s/6i9nqn5lnrv9buc/player.png?dl=1");
img_win = simplegui.load_image("https://www.dropbox.com/s/fa60nd353e9y0c1/win.jpg?dl=1");
img_lose = simplegui.load_image("https://www.dropbox.com/s/inj9bfobbuotmk7/lose.jpg?dl=1");
img_title = simplegui.load_image("https://www.dropbox.com/s/japd0kbhw97a1rq/title.png?dl=1");
img_sunburst = simplegui.load_image("https://www.dropbox.com/s/cexucsds3vs3b97/sunburst.jpg?dl=1");
img_menu = simplegui.load_image("https://www.dropbox.com/s/5yx4l8rqm4d7taz/menu.png?dl=1");
image_list = [img_background, img_shaw, img_can, img_player, img_win, img_lose, img_title, img_sunburst, img_menu];

#load sounds
snd_music = simplegui.load_sound('https://www.dropbox.com/s/13kgis0xmxk17yb/music.mp3?dl=1');
snd_unodostres = simplegui.load_sound('https://www.dropbox.com/s/idtbjjtrrqvp0ig/unodostresy.wav?dl=1');
snd_des = simplegui.load_sound('https://www.dropbox.com/s/m3n1272axco8p5j/desafortunadamente.wav?dl=1');
snd_gracias = simplegui.load_sound('https://www.dropbox.com/s/wdgaf9wls9pz86g/graciasporhablarespanol.wav?dl=1');
snd_puntos = simplegui.load_sound('https://www.dropbox.com/s/ks0h9h0j9z36ced/puntosadios.wav?dl=1');
snd_unpoco = simplegui.load_sound('https://www.dropbox.com/s/pj1dnkpx0yml5e8/unpocodiferente.wav?dl=1');
snd_esla = simplegui.load_sound('https://www.dropbox.com/s/hp4jykoato9x1wg/eslacorrecta.wav?dl=1');
snd_galletas = simplegui.load_sound('https://www.dropbox.com/s/6eepzj5cpg9la1b/galletas.wav?dl=1');
snds_bad = [snd_des, snd_gracias, snd_puntos, snd_unpoco];
snds_good = [snd_esla, snd_galletas];

snd_music.set_volume(0.2);
snd_music.play();


#image dimensions
background_size = [2000, 1000];
shaw_size = [538, 1019];
can_size = [458, 458];
player_size = [237, 454];
win_size = [670, 360];
lose_size = [1701, 957];
title_size = [911, 191];
sunburst_size = [1500, 1500];
menu_size = [1500, 750];

# variables for title screen
sunrot = 0;
title_scale = 1;
title_rot = 0;
title_dir = [1, 1];

#other variables
musicOnOff = True;

#Define classes
class FrameCounter:
    def __init__(self):
        self.frames = 0;
        self.frameRate = 0;
        if show_FPS:
            self.frameTimer = simplegui.create_timer(1000, self.timer);

    def timer(self):
        self.frameRate = self.frames;
        self.frames = 0;

    def update(self, canvas):
        self.frames += 1;
        self.draw(canvas);

    def draw(self, canvas):
        canvas.draw_text(str(self.frameRate), [WIDTH - frame.get_canvas_textwidth("60.", 36), 36], 36, "Green");

class Player:
    def __init__(self):
        self.vel = [0, 0, 0, 0] #[-x, x, -y, y]
        self.speed = 10;
        self.scale = .3;
        self.size = [player_size[0] * self.scale, player_size[1] * self.scale];
        self.pos = [WIDTH / 2, HEIGHT - self.size[1]/2]; #[x, y]
        self.hitbox = [(player_size[0] - 150) * self.scale, (player_size[1] - 35) * self.scale];
        self.death_cause = 1;

    def update(self, canvas):
        self.vel = [0, 0, 0, 0];
        if controls.up:
            self.vel[3] = self.speed;
        if controls.down:
            self.vel[2] = self.speed;
        if controls.left:
            self.vel[0] = self.speed;
        if controls.right:
            self.vel[1] = self.speed;
        self.pos[0] += self.vel[1] - self.vel[0];
        self.pos[1] += self.vel[2] - self.vel[3];
        if self.pos[1] > HEIGHT - self.size[1]/2:
            self.pos[1] = HEIGHT - self.size[1]/2;
        elif self.pos[1] < shaw.size[1]:
            self.pos[1] = shaw.size[1];
        if self.pos[0] < self.size[0]/2:
            self.pos[0] = self.size[0]/2;
        elif self.pos[0] > WIDTH - self.size[0]/2:
            self.pos[0] = WIDTH - self.size[0]/2;
        self.draw(canvas);

    def draw(self, canvas):
        canvas.draw_image(img_player, [player_size[0]/2, player_size[1]/2], player_size, [self.pos[0], self.pos[1]], self.size);

class Shaw:
    def __init__(self):
        self.pos = [WIDTH / 2, 150]; #[x, y]
        self.rotation = 0;
        self.speed = 10;
        self.rotSpeed = math.radians(10);
        self.scale = .3;
        self.size = [shaw_size[0] * self.scale, shaw_size[1] * self.scale];
        self.time = 3;
        self.frame = 1;
        self.direction = 1;
        self.level = 1;
        self.mouthTimer = simplegui.create_timer(1000, self.timer);

    def update(self, canvas):
        self.time -= 1./60;
        if self.time <= 0 and not calendar.end:
            calendar.start = True;
            cans.add();
            if self.level == 1:
                self.time = randfloat(0.2, 0.5);
            elif self.level == 2:
                self.time = randfloat(0.1, 0.25);
            elif self.level == 3:
                self.time = randfloat(0.05, 0.125);
        cans.speed = random.randint(5, 10);
        if calendar.value <= 120:
            self.level = 2
            cans.speed = random.randint(7, 14);
            self.pos[0] += self.speed*self.direction;
            if self.pos[0] > WIDTH - self.size[0]/4 or self.pos[0] < self.size[0]/4:
                self.direction *= -1;
        if calendar.value <= 60:
            self.level = 3;
            self.speed = 7;
            cans.speed = random.randint(10, 20);
            self.rotation += self.rotSpeed*self.direction;
        self.draw(canvas);

    def draw(self, canvas):
        if self.frame == 1:
            canvas.draw_image(img_shaw, [shaw_size[0]/4, shaw_size[1]/2], [shaw_size[0]/2, shaw_size[1]], self.pos, [self.size[0]/2, self.size[1]], self.rotation);
        else:
            canvas.draw_image(img_shaw, [shaw_size[0]/4*3, shaw_size[1]/2], [shaw_size[0]/2, shaw_size[1]], self.pos, [self.size[0]/2, self.size[1]], self.rotation);


    def timer(self):
        self.frame = 1;
        self.mouthTimer.stop();

class Controls:
    def __init__(self):
        self.up = False;
        self.down = False;
        self.left = False;
        self.right = False;
        self.a = False;
        self.d = False;
        self.continyoo = False;

    def keyDown(self, key):
        if key == simplegui.KEY_MAP['down']:
            self.down = True;
        elif key == simplegui.KEY_MAP['up']:
            self.up = True;
        elif key == simplegui.KEY_MAP['left']:
            self.left = True;
        elif key == simplegui.KEY_MAP['right']:
            self.right = True;
        elif key == simplegui.KEY_MAP['a']:
            self.a = True;
        elif key == simplegui.KEY_MAP['d']:
            self.d = True;
        elif key == simplegui.KEY_MAP['space']:
            self.continyoo = True;

    def keyUp(self, key):
        self.keypressed = False;
        if key == simplegui.KEY_MAP['down']:
            self.down = False;
        elif key == simplegui.KEY_MAP['up']:
            self.up = False;
        elif key == simplegui.KEY_MAP['left']:
            self.left = False;
        elif key == simplegui.KEY_MAP['right']:
            self.right = False;
        elif key == simplegui.KEY_MAP['a']:
            self.a = False;
        elif key == simplegui.KEY_MAP['d']:
            self.d = False;

class Can:
    def __init__(self, speed):
        self.scale = 0.2;
        self.radius = 229 * self.scale;
        self.pos = [shaw.pos[0], shaw.pos[1]];
        self.speed = speed;
        self.angle = math.radians(random.randint(15, 165));
        self.vel = [self.speed * math.cos(self.angle), self.speed * math.sin(self.angle)];
        self.rotVel = math.radians(random.randint(-5, 5));
        self.rotation = math.radians(random.randint(-45, 45));
        self.size = [can_size[0] * self.scale, can_size[1] * self.scale];

    def update(self):
        self.pos[0] += self.vel[0];
        self.pos[1] += self.vel[1];
        self.rotation += self.rotVel;
        if self.pos[0] < 0 - self.radius or self.pos[0] > WIDTH + self.radius or self.pos[1] > HEIGHT + self.radius:
            cans.destroy(self);
        if self.pos[1] > player.pos[1] - player.hitbox[1]/2 - self.radius:
            if self.pos[1] < player.pos[1] + player.hitbox[1]/2 + self.radius:
                if self.pos[0] > player.pos[0] - player.hitbox[0]/2 - self.radius:
                    if self.pos[0] < player.pos[0] + player.hitbox[0]/2 + self.radius:
                        self.hit();

    def hit(self):
        grade.value -= Cans.DAMAGE;
        sound.playBad();
        cans.destroy(self);
        shaw.mouthTimer.start();
        shaw.frame = 2;

    def draw(self, canvas):
        canvas.draw_image(img_can, [can_size[0]/2, can_size[1]/2], can_size, [self.pos[0], self.pos[1]], self.size, self.rotation);


class Cans:
    DAMAGE = 0.25;
    def __init__(self):
        self.cans = [];
        self.speed = random.randint(3, 6);

    def update(self, canvas):
        for can in self.cans:
            can.update();
            can.draw(canvas);

    def add(self):
        self.cans.append(Can(self.speed));

    def destroy(self, can):
        self.cans.remove(can);

class Grade:
    def __init__(self):
        self.value = 100.;
        self.death_cause = 1;
        self.letter = "";

    def update(self, canvas):
        self.draw(canvas);

    def draw(self, canvas):
        canvas.draw_polygon([(2, 2), (150, 2), (150, 150), (2, 150)], 4, 'White', 'Black');
        canvas.draw_text("Nota:", [75 - frame.get_canvas_textwidth("Nota:", 36)/2, 50], 36, "White");
        canvas.draw_text(str(self.value)+"%", [75 - frame.get_canvas_textwidth(str(self.value)+"%", 36)/2, 100], 36, "Red");
        canvas.draw_text(str(self.value)+"%", [75 - frame.get_canvas_textwidth(str(self.value)+"%", 36)/2, 100], 36, "rgba(0,255,0,"+str((self.value-60)/40.)+")");


class Calendar:
    def __init__(self):
        self.value = 180;
        self.dayTimer = simplegui.create_timer(500, self.timer);
        self.start = False;
        self.end = False;
        self.endTime = 3;

    def update(self, canvas):
        if self.end:
            calendar.endTime -= 1./60;
            if self.endTime <= 0:
                determineGrade(grade.value);
        else:
            if self.start:
                self.dayTimer.start();
            if self.value <= 0:
                self.end = True;
        self.draw(canvas);

    def draw(self, canvas):
        canvas.draw_polygon([(WIDTH - 150, 2), (WIDTH - 2, 2), (WIDTH - 2, 150), (WIDTH - 150, 150)], 4, 'White', 'Black');
        canvas.draw_text("Dias:", [WIDTH - 75 - frame.get_canvas_textwidth("Dias:", 40)/2, 50], 40, "White");
        canvas.draw_line([WIDTH - 83, 24], [WIDTH - 75, 17], 4, 'White')
        canvas.draw_text(str(self.value), [WIDTH - 75 - frame.get_canvas_textwidth(str(self.value), 30)/2, 100], 30, "White");

    def timer(self):
        if not self.end:
            self.value -= 1;

class Sound:
    def __init__(self):
        self.sound = random.choice(snds_bad);

    def playBad(self):
        self.sound.pause();
        self.sound.rewind();
        self.sound = random.choice(snds_bad);
        self.sound.play();

    def playGood(self):
        self.sound.pause();
        self.sound.rewind();
        self.sound = random.choice(snds_good);\
        self.sound.play();

    def playUnoDosTres(self):
        self.sound.pause();
        self.sound.rewind();
        self.sound = snd_unodostres;
        self.sound.play();

def randfloat(low, high):
    return random.random() * (high - low) + low;

def determineGrade(nota):
    if nota >= 97:
        grade.letter = "A+";
    elif nota >= 93:
        grade.letter = "A";
    elif nota >= 90:
        grade.letter = "A-";
    elif nota >= 87:
        grade.letter = "B+";
    elif nota >= 83:
        grade.letter = "B";
    elif nota >= 80:
        grade.letter = "B-";
    elif nota >= 77:
        grade.letter = "C+";
    elif nota >= 73:
        grade.letter = "C";
    elif nota >= 70:
        grade.letter = "C-";
    elif nota >= 67:
        grade.letter = "D+";
    elif nota >= 63:
        grade.letter = "D";
    elif nota >= 60:
        grade.letter = "D-";
    elif nota >= 57:
        grade.letter = "F+";
    elif nota >= 53:
        grade.letter = "F";
    else:
        grade.letter = "F-";
    if nota >= 70:
        player.death_cause = 2;
        sound.playGood();
    else:
        player.death_cause = 1;
        sound.playBad();
    frame.set_draw_handler(gameOver);

#Create objects
player = Player();
controls = Controls();
cans = Cans();
frameCounter = FrameCounter();
grade = Grade();
calendar = Calendar();
shaw = Shaw();
sound = Sound();

def reset():
    player.pos = [WIDTH / 2, HEIGHT - player.size[1]/2];
    grade.value = 100;
    calendar.value = 180;
    calendar.dayTimer.start();
    shaw.pos = [WIDTH / 2, 150];
    shaw.rotation = 0;
    cans.cans = [];
    shaw.time = 3;
    calendar.start = False;
    calendar.dayTimer.stop();
    shaw.level = 1;
    calendar.end = False;
    calendar.endTime = 3;
    shaw.speed = 10;

#Drawing and stuff
def game(canvas):
    canvas.draw_image(img_background, [background_size[0]/2, background_size[1]/2], background_size, [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT]);
    grade.update(canvas);
    calendar.update(canvas);
    cans.update(canvas);
    shaw.update(canvas);
    player.update(canvas);
    if show_FPS:
        frameCounter.update(canvas);

def menu(canvas):
    global sunrot, title_scale, title_rot;
    canvas.draw_image(img_sunburst, [sunburst_size[0]/2, sunburst_size[1]/2], sunburst_size, [WIDTH/2, HEIGHT/2.7], [2000, 2000], math.radians(sunrot));
    canvas.draw_image(img_menu, [menu_size[0]/2, menu_size[1]/2], menu_size, [WIDTH/2, HEIGHT/2], [WIDTH, HEIGHT]);
    canvas.draw_image(img_title, [title_size[0]/2, title_size[1]/2], title_size, [WIDTH/2, HEIGHT/2.7], [title_size[0]*title_scale, title_size[1]*title_scale], math.radians(title_rot));
    if show_FPS:
        frameCounter.update(canvas);
    sunrot += 3;
    title_rot += 1 * title_dir[1];
    title_scale += 0.02 * title_dir[0];
    if sunrot > 360:
        sunrot -= 360;
    if title_scale > 1.25 or title_scale < 0.75:
        title_dir[0] *= -1;
    if title_rot > 10 or title_rot < -10:
        title_dir[1] *= -1;
    if controls.continyoo:
        controls.continyoo = False;
        reset();
        sound.playUnoDosTres();
        frame.set_draw_handler(game);

# Small program to add up total pixels:
# http://www.codeskulptor.org/#user41_1XLpTEBwZI_0.py
def loading(canvas):
    pixels = 0;
    for img in image_list:
        pixels += img.get_width() * img.get_height();
    percent = str(int(math.ceil(100*pixels/8283642.)))+"%";
    canvas.draw_text("Cargando...", [(WIDTH - frame.get_canvas_textwidth("Cargando...", HEIGHT / 10)) / 2, HEIGHT / 2], HEIGHT / 10, "White");
    canvas.draw_text(percent, [(WIDTH - frame.get_canvas_textwidth(percent, HEIGHT / 10)) / 2, HEIGHT / 1.5], HEIGHT / 10, "White");
    if all([img.get_width()>0 for img in image_list]):
        frame.set_draw_handler(menu);

def gameOver(canvas):
    calendar.dayTimer.stop();
    if player.death_cause == 1:
        canvas.draw_image(img_lose, [lose_size[0]/2, lose_size[1]/2], lose_size, [WIDTH/2, HEIGHT/2], [WIDTH, HEIGHT]);
        canvas.draw_text("Recibiste una "+grade.letter+". Pierdes el juego.", [(WIDTH - frame.get_canvas_textwidth("Recibiste una "+grade.letter+". Pierdes el juego.", 45)) - 10, 100], 45, "Red");
    elif player.death_cause == 2:
        canvas.draw_image(img_win, [win_size[0]/2, win_size[1]/2], win_size, [WIDTH/2, HEIGHT/2], [WIDTH, HEIGHT]);
        canvas.draw_text("Recibiste una "+grade.letter+".  Felicitaciones!", [(WIDTH - frame.get_canvas_textwidth("Recibiste una "+grade.letter+".  Felicitaciones!", 50)) / 2, 220], 50, "Green");
        canvas.draw_line([630, 195], [630, 225], 4, 'Green');
        canvas.draw_line([630, 184], [630, 188], 4, 'Green');
    if controls.continyoo:
        controls.continyoo = False;
        frame.set_draw_handler(menu);
    reset();

def instawin():
    grade.value = 100;
    calendar.value = 0;

def instalose():
    grade.value = 0;
    calendar.value = 0;

def easy():
    Cans.DAMAGE = 0.25;
    dif_label.set_text("Dificultad: F"+chr(225)+"cil");

def hard():
    Cans.DAMAGE = 0.5;
    dif_label.set_text("Dificultad: Dif"+chr(237)+"cil");

def impossible():
    Cans.DAMAGE = 1.0;
    dif_label.set_text("Dificultad: Imposible");

def music():
    global musicOnOff;
    if musicOnOff:
        musicOnOff = False;
        music_label.set_text('M'+chr(250)+'sica: '+'no');
        snd_music.pause();
    else:
        musicOnOff = True;
        music_label.set_text('M'+chr(250)+'sica: '+'s'+chr(237));
        snd_music.play();

def musicTimer():
    snd_music.rewind();
    snd_music.play();

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Espanol 5: El Juego", WIDTH, HEIGHT)
frame.set_draw_handler(loading);
frame.set_keydown_handler(controls.keyDown);
frame.set_keyup_handler(controls.keyUp);
if show_FPS:
    frameCounter.frameTimer.start();
dif_label = frame.add_label('Dificultad: F'+chr(225)+'cil');
btn_easy = frame.add_button('F'+chr(225)+'cil', easy);
btn_hard = frame.add_button('Dif'+chr(237)+'cil', hard);
btn_impossible = frame.add_button('Imposible', impossible);
blank1 = frame.add_label('');
music_label = frame.add_label('M'+chr(250)+'sica: '+'s'+chr(237));
btn_music = frame.add_button('Cambiar', music);
if cheats:
    blank2 = frame.add_label('');
    cheats_label = frame.add_label('Enga'+chr(241)+'ar:');
    btn_win = frame.add_button('Ganar', instawin);
    btn_lose = frame.add_button('Perder', instalose);
music_timer = simplegui.create_timer(208000, musicTimer);
music_timer.start();

# Start the frame animation
frame.start()
