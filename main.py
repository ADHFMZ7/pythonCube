#!/opt/anaconda3/envs/game/bin/python3

import parse
import numpy as np
import pygame
import sys
import time
from math import cos, sin

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900 
SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
OFFSET = np.array([SCREEN_WIDTH/2, SCREEN_HEIGHT/2])
PM = np.array([[1, 0, 0],
               [0, 1, 0]])

def drawCube(cube, angle):

  for i in range(4):
    pygame.draw.line(screen, WHITE, proj(rot(cube[i], angle)), 
                                    proj(rot(cube[(i + 1) % 4], angle)))


    pygame.draw.line(screen, WHITE, proj(rot(cube[i + 4], angle)),
                                    proj(rot(cube[((i + 1) % 4) + 4], angle)))


    pygame.draw.line(screen, WHITE, proj(rot(cube[i], angle)), 
                                    proj(rot(cube[i + 4], angle)))


def rot(A, angle):
  rotX = np.array([[1, 0, 0],
                   [0, sin(angle), -cos(angle)],
                   [0, sin(angle), cos(angle)]])

  rotY = np.array([[cos(angle), 0, sin(angle)],
                   [0, 1, 0],
                   [-sin(angle), 0, cos(angle)]])

  rotZ = np.array([[cos(angle), -sin(angle), 0],
                   [sin(angle), cos(angle), 0],
                   [0, 0, 1]])

  return rotX @ rotY @ A


def proj(A):
  return (PM @ A) + OFFSET

if __name__ == "__main__":
  pygame.init()
  pygame.display.set_caption('py3D')

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
    time.sleep(0.01)
   
