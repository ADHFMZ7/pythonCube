#!/opt/anaconda3/envs/game/bin/python3
import parse
import numpy as np
import pygame
from matrices import proj, rot
import sys

def drawCube(cube, angle):

  for i in range(4):
    pygame.draw.line(screen, WHITE, proj(rot(cube[i], angle)) + (SCREEN_WIDTH / 2), 
                                    proj(rot(cube[(i + 1) % 4] + (SCREEN_WIDTH / 2), angle)))


    pygame.draw.line(screen, WHITE, proj(rot(cube[i + 4], angle)) + (SCREEN_WIDTH / 2),
                                    proj(rot(cube[((i + 1) % 4) + 4] + (SCREEN_WIDTH / 2), angle)))


    pygame.draw.line(screen, WHITE, proj(rot(cube[i], angle)) + (SCREEN_WIDTH / 2), 
                                    proj(rot(cube[i + 4] + (SCREEN_WIDTH / 2), angle)))


pygame.init()
pygame.display.set_caption('py3D')

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode(SIZE)


cube = parse.parseOBJ("cube.obj")

angle = 0
while 1:

  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()

  screen.fill(BLACK)
  drawCube(cube, angle) 
  pygame.display.flip()
  angle += 0.01
  if angle > 360:
    angle = 0



