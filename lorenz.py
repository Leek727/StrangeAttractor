"""
dx/dt = σ (y - x)
dy/dt = x(p - z) - y
dz/dt = xy - βz

dx/dt = 10 (y - x)
dy/dt = x(28 - z) - y
dz/dt = xy - (8/3)z

x = e^(-10t) + y
y = e^(-t) + x(-z) + 28x
z = e^((-8t)/3) + (3xy)/8
???
"""

import pygame
import numpy as np
import random

pygame.init()

width, height = 1000, 1000
# Set up the drawing window
screen = pygame.display.set_mode([width, height])


def to_pygame(coords):
    """Convert coordinates into pygame coordinates (lower-left => top left)."""
    return (int(coords[0] * 15 + width/2), int(height*.75 - coords[1] * 15))


class Body:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

dt = .01

# main
bodies = []
for i in range(0):
    bodies.append(Body(random.randint(-50, 50),
                  random.randint(-50, 50), random.randint(-50, 50)))

for i in range(10000):
    bodies.append(Body(20,20,20 + i / 10000))

# trail effect - fading layer
s = pygame.Surface((width,height), pygame.SRCALPHA)   # per-pixel alpha
s.fill((0,0,0,30))                         # notice the alpha value in the color

running = True
clock = pygame.time.Clock()
while running:
    # pygame event handling for closing window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # fade out to make a trail
    screen.blit(s, (0,0))
    screen_pa = pygame.PixelArray(screen)
    for b in bodies:
        x = b.x
        y = b.y
        z = b.z

        # Lorenz system diff eqs
        dx = 10 * (y - x)
        dy = x * (28 - z) - y
        dz = x*y - (8/3) * z

        # one timestep
        b.x += dx * dt
        b.y += dy * dt
        b.z += dz * dt

        #pygame.draw.circle(screen, (255, 255, 255), to_pygame((b.x, b.z)), 1)
        x, y = to_pygame((b.x, b.z))
        screen_pa[x,y] = (255,255,255)
        """
        dx/dt = 10 (y - x)
        dy/dt = x(28 - z) - y
        dz/dt = xy - (8/3)z

        """
    screen_pa.close()
    # Flip the display
    pygame.display.flip()

pygame.quit()
