import numpy as np
from math import cos, sin



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

  return rotX @ rotY @  A


def proj(A):
  PM = np.array([[1, 0, 0],
                 [0, 1, 0]])
  return PM @ A

    
