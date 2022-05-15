
import pygame

# import libraries


# initialise pygame
from pygame import K_a

pygame.init()

# game window dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jump Man")


# set frame rate
clock = pygame.time.Clock()
FPS = 60

# game variables
GRAVITY = 1

# define colors
WHITE = (255, 255, 255)

# load images
jumpy_image = pygame.image.load("assets/jump.png.").convert_alpha()
background_image = pygame.image.load("assets/background.png").convert_alpha()


# player class
class Player():
    def __init__(self, x, y):
        self.image = pygame.transform.scale(jumpy_image, (45, 45))
        self.width = 25
        self.height = 40
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)
        self.vel_y = 0
        self.flip = False

    # process key presses
    def move(self):
        # reset variables
        dx = 0
        dy = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            dx = -10
            self.flip = True
        if key[pygame.K_d]:
            dx = 10
            self.flip = False

        # gravity
        self.vel_y += GRAVITY
        dy += self.vel_y


        # ENSURE PLAYER DOESN'T GO OFF THE EDGE
        if self.rect.left + dx < 0:
            dx = 0 - self.rect.left
        if self.rect.right + dx > SCREEN_WIDTH:
            dx = SCREEN_WIDTH -self.rect.right


        # CHECK COLLIONS
        if self.rect.bottom + dy > SCREEN_HEIGHT:
            dy = 0
            self.vel_y = -20

        # update rectangle position
        self.rect.x += dx
        self.rect.y += dy

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), (self.rect.x - 12, self.rect.y - 5))
        pygame.draw.rect(screen, WHITE, self.rect, 2)


jumpy = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)

# game loop
run = True
while run:

    clock.tick(FPS)

    jumpy.move()

    # draw background
    screen.blit(background_image, (0, 0))

    # draw sprites
    jumpy.draw()

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # update display window
    pygame.display.update()

pygame.quit()
