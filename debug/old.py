import pygame as pg, os, re

def get_image_dir() -> str:
    dir = os.path.dirname(os.path.abspath(__file__))
    r = re.compile(r'^F.*-.*g$')
    l = list(filter(r.match, os.listdir(dir)))
    return dir + '\\' + l[0]

def get_file(dir, exp) -> str:
    r = re.compile(exp)
    l = list(filter(r.match, os.listdir(dir)))
    return dir + '\\' + l[0]

def redraw_game_window():
    #Update
    player_sprites.update()
    #Draw and Render
    score_label = pg.font.SysFont("comicsans", 50).render(f"{SCORE}", 1, BLACK)
    screen.blit(bg, (0,0))
    player.update()
    screen.blit(score_label, (WIDTH/2-15, 10))
    #Flip/Update display after drawing
    pg.display.update()

class Player(pg.sprite.Sprite):
    def __init__(self, fish_img):
        pg.sprite.Sprite.__init__(self)
        self.vx = 0
        self.vy = 0
        self.fish_img = pg.image.load(fish_img)
        self.rect = self.fish_img.get_rect()
        self.mask = pg.mask.from_surface(self.fish_img)
        self.fish_img = pg.transform.scale(self.fish_img, (50, 30))

    def update(self):
        self.vx = 0
        self.vy = 0
        
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE]:
            self.vy -= 5

        self.rect.y += self.vy

RESOLUTION = WIDTH, HEIGHT = 495, 880
FPS = 30
SCORE = 0

#Movement
player_vel = 20

#Color Space
WHITE = (255, 255, 255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

#Image Directory
IMG_DIR = get_image_dir()

#Background
bg = pg.transform.scale(pg.image.load(get_file(IMG_DIR, r'^bg.*$')), (RESOLUTION))

#Game Initialization
pg.init()
screen = pg.display.set_mode(RESOLUTION)
pg.display.set_caption("Flappy Fish")
clock = pg.time.Clock()

#Player
player_sprites = pg.sprite.Group()
player = Player(get_file(IMG_DIR, r'^fish.*$'))
player_sprites.add(player)

#Game Loop
running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    keys = pg.key.get_pressed()
    if keys[pg.K_ESCAPE]:
        pg.quit()

    redraw_game_window()