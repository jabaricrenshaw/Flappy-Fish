from settings import *
from sprites import *
import pygame as pg
import inspect
import time
import sys
import os


class Game():
    def __init__(self) -> None:
        # Initialize Game window
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode(RESOLUTION)
        pg.display.set_caption("Flappy Fish")
        self.clock = pg.time.Clock()
        self.running = True
        self.font_name = pg.font.match_font(FONT_NAME)

    def new(self) -> None:
        # Start a new game
        self.score = 0

        # Sprites and Sprite Groups
        self.all_sprites = pg.sprite.Group()
        self.player_sprites = pg.sprite.Group()
        self.pipes = pg.sprite.Group()

        # Sprite Initialization
        self.player = Player()
        self.p = [Pipe()]
        #self.p1 = Pipe(WIDTH-50, HEIGHT/2 + 10, 50, HEIGHT/2)
        #self.p2 = Pipe(WIDTH-50, 0, 50, HEIGHT/2 - 10)
 
        self.player_sprites.add(self.player)
        self.all_sprites.add(self.player)
        for object in self.p:
            self.pipes.add(object)
            self.all_sprites.add(object)

        self.run()

    def run(self) -> None:
        # Game Loop
        self.playing = True
        self.t1 = 0
        self.t2 = 0
        while self.playing:
            self.dt = self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self) -> None:
        # Game Loop - Update
        self.player_sprites.update()
        self.pipes.update()

        self.t1 += self.dt
        self.t2 += self.dt
        if self.t1 >= 3500:
            self.p.append(Pipe())
            self.pipes.add(self.p[len(self.p)-1]) 
            self.all_sprites.add(self.p[len(self.p)-1])
            self.p.pop(0)
            self.score += 1
            self.t1 = 0

        if self.t2 >= 3500*3:
            self.pipes.remove(self.pipes.sprites()[:2])
            self.t2 = 0

        if self.player.pos.y > HEIGHT + self.player.rect.height or self.player.pos.y < 0:
            self.playing = False

        hits = pg.sprite.spritecollide(
            self.player, self.pipes, False, pg.sprite.collide_mask)
        if hits:
            self.playing = False

    def events(self) -> None:
        # Game Loop - Events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    if self.playing:
                        self.playing = False
                    self.show_go_screen()

    def draw(self) -> None:
        # Game Loop - Draw
        self.screen.blit(pg.transform.scale(bg, RESOLUTION), (0, 0))

        self.draw_text(VERSION, 22, BLACK, WIDTH-70, HEIGHT-2, "version")

        self.player_sprites.draw(self.screen)
        self.pipes.draw(self.screen)

        self.draw_text(str(self.score), 50, BLACK, WIDTH/2-15, 10)
        self.draw_text(str(self.score), 50, WHITE, WIDTH/2-15-2, 10-2)

        pg.display.flip()

    def show_start_screen(self) -> None:
        # Show start screen
        self.screen.blit(pg.transform.scale(bg, RESOLUTION), (0, 0))

        self.draw_text(VERSION, 22, BLACK, WIDTH-70, HEIGHT-2, "version")

        self.draw_text(f"Welcome to {TITLE}!", 22,
                       BLACK, WIDTH/2, HEIGHT/2-22*7)
        self.draw_text(f"Welcome to {TITLE}!", 22,
                       WHITE, WIDTH/2-1, HEIGHT/2-22*7-2)

        self.draw_text("(Use the spacebar to fly!)",
                       22, BLACK, WIDTH/2, HEIGHT/2)
        self.draw_text("(Use the spacebar to fly!)",
                       22, WHITE, WIDTH/2-1, HEIGHT/2-2)

        self.draw_text("Press any key to start.", 22,
                       BLACK, WIDTH/2, HEIGHT/2-22)
        self.draw_text("Press any key to start.", 22,
                       WHITE, WIDTH/2-1, HEIGHT/2-22-2)

        pg.display.flip()
        self.wait_for_key()

    def show_go_screen(self) -> None:
        # Show game over screen
        if not self.running:
            return

        self.screen.blit(pg.transform.scale(bg, RESOLUTION), (0, 0))

        self.draw_text(VERSION, 22, BLACK, WIDTH-70, HEIGHT-2, "version")

        self.draw_text("Game Over!", 22, BLACK, WIDTH/2, HEIGHT/2-22*7)
        self.draw_text("Game Over!", 22, WHITE, WIDTH/2-1, HEIGHT/2-22*7-2)

        self.draw_text(f"Score: {self.score}", 22, BLACK, WIDTH/2, HEIGHT/2)
        self.draw_text(f"Score: {self.score}", 22,
                       WHITE, WIDTH/2-1, HEIGHT/2-2)

        self.draw_text("(Press any key to play again.)", 22,
                       BLACK, WIDTH/2, HEIGHT/2-22)
        self.draw_text("(Press any key to play again.)", 22,
                       WHITE, WIDTH/2-1, HEIGHT/2-22-2)

        pg.display.flip()
        self.wait_for_key()

    def wait_for_key(self) -> None:
        #print(inspect.getouterframes(inspect.currentframe(), 2)[1][3])
        waiting = True
        while(waiting):
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP:
                    waiting = False

    def draw_text(self, text: str, size: int, color: str, x: float, y: float, pos: str = None) -> None:
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        if pos is None:
            text_rect.midtop = (x, y)
        elif pos is "version":
            text_rect.midbottom = (x,y)
        
        self.screen.blit(text_surface, text_rect)


if __name__ == "__main__":

    RESOLUTION = WIDTH, HEIGHT = 495, 880

    g = Game()
    g.show_start_screen()

    while g.running:
        g.new()
        g.show_go_screen()
        # can add pg.QUIT here to end the game after dying

pg.quit()
