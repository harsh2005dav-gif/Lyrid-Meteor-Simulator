import pygame
import random
import math
pygame.mixer.init()
whoosh_sound = pygame.mixer.Sound("whoosh.mp3.mp3")

# 1. Initialize the Environment
pygame.init()
WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lyrid Meteor Shower - Project #12")

# 2. Define the 'Radiant (Where Lyrids come from)
RADIANT = (WIDTH - 100, 100) # Top right corner

class Meteor:
    def __init__(self):
        self.x, self.y = RADIANT
        # Lyrids move fast (~48km/s), we simulate with high speed
        self.angle = random.uniform(math.pi / 2, math.pi)
        self.speed = random.uniform(10, 20)
        self.length = random.randint(30, 60)
        self.brightness = 255 # Start bright
        whoosh_sound.play()

    def update(self):
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed
        self.brightness -= 2 # Fade out as it moves

    def draw(self):
        # Draw the bright streak against the black sky
        end_x = self.x - math.cos(self.angle) * self.length
        end_y = self.y - math.sin(self.angle) * self.length
        color = (self.brightness, self.brightness, self.brightness)
        if self.brightness > 0:
            pygame.draw.line(screen, color, (self.x, self.y), (end_x, end_y), 2)

# 3. Main Mission Loop
running = True
meteors = []
clock = pygame.time.Clock()

while running:
    screen.fill((0, 0, 0)) # Pitch Black Background

    # Spawn a meteor roughly every 2-3 seconds
    if random.random()< 0.02:
        meteors.append(Meteor())

    for m in meteors[:]:
        m.update()
        m.draw()
        if m.brightness <= 0 or m.x < 0 or m.y > HEIGHT:
            meteors.remove(m) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60) # 60 FPS for smooth motion

pygame.quit()