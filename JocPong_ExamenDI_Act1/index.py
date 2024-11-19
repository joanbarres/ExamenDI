import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((BOLA_AMPLADA, BOLA_ALTURA))
        self.surf.fill(BLANC)
        self.rect = self.surf.get_rect(topleft=(400, 400))
        self.speed_x = 10
        self.speed_y = 10

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.top <= 0: 
            self.speed_y *= -1
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.speed_y *= -1
        if self.rect.left <= 0:
            return True
        if self.rect.right >= SCREEN_WIDTH:
            return True
        return False

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.surf = pygame.Surface((RAQUETA_AMPLADA, RAQUETA_ALTURA))
        self.surf.fill(BLANC)
        self.rect = self.surf.get_rect(topleft=(x, y))
        self.speed = 0

    def update(self):
        self.rect.y += self.speed
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
RAQUETA_AMPLADA = 10
RAQUETA_ALTURA = 150
BOLA_AMPLADA = 20
BOLA_ALTURA = 10
BLANC = (255, 255, 255)
NEGRE = (0, 0, 0)
VELOCITAT_RAQUETA = 5


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

jugador_esquerra = Player(20, (SCREEN_HEIGHT - RAQUETA_ALTURA) // 2)
jugador_dreta = Player(SCREEN_WIDTH - 20 - RAQUETA_AMPLADA, (SCREEN_HEIGHT - RAQUETA_ALTURA) // 2)


bola = Ball()
raquetes = pygame.sprite.Group()
raquetes.add(jugador_esquerra, jugador_dreta)
bola_group = pygame.sprite.GroupSingle(bola)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                jugador_esquerra.speed = -VELOCITAT_RAQUETA
            if event.key == pygame.K_s:
                jugador_esquerra.speed = VELOCITAT_RAQUETA
            if event.key == pygame.K_UP:
                jugador_dreta.speed = -VELOCITAT_RAQUETA
            if event.key == pygame.K_DOWN:
                jugador_dreta.speed = VELOCITAT_RAQUETA

        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_w, pygame.K_s):
                jugador_esquerra.speed = 0
            if event.key in (pygame.K_UP, pygame.K_DOWN):
                jugador_dreta.speed = 0

    raquetes.update()
    bola.update()
    bola_out = bola_group.update()

    if pygame.sprite.spritecollide(bola, raquetes, False):
        bola.speed_x *= -1
    if bola_out:
        bola.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        bola.speed_x *= -1  

    screen.fill(NEGRE)

    screen.blit(bola.surf, bola.rect)
    screen.blit(jugador_esquerra.surf, jugador_esquerra.rect)
    screen.blit(jugador_dreta.surf, jugador_dreta.rect)

    pygame.display.flip()

pygame.quit()  
