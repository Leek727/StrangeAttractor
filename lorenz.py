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
    return (coords[0] * 15 + width/2, (height*.75 - coords[1] * 15))


class Body:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


# constants
dt = .005


# main
bodies = []
for i in range(0):
    bodies.append(Body(random.randint(-50, 50),
                  random.randint(-50, 50), random.randint(-50, 50)))

for i in range(10000):
    bodies.append(Body(20,20,20 + i / 10000))

running = True
clock = pygame.time.Clock()
while running:
    # Did the user click the window close button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # trail effect
    s = pygame.Surface((width,height), pygame.SRCALPHA)   # per-pixel alpha
    s.fill((0,0,0,30))                         # notice the alpha value in the color
    screen.blit(s, (0,0))
    

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

        #print(dx, dy, dz)

        pygame.draw.circle(screen, (255, 255, 255), to_pygame((b.x, b.z)), 1)
        """
        dx/dt = 10 (y - x)
        dy/dt = x(28 - z) - y
        dz/dt = xy - (8/3)z

        """

    # Flip the display
    pygame.display.flip()
    #clock.tick(60)

pygame.quit()
