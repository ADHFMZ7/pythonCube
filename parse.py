import numpy as np

def parseOBJ(filename):

  with open(filename, 'r') as f:
    lines = f.readlines()

  vectors = [] 

  for i in lines:
    l = i.split()
    if l[0] == 'v':
      vectors.append(np.array([l[1], l[2], l[3]], dtype=float))


  return vectors

#class vec3:
#
#  def __init__(self, x=0, y=0, z=0)
#    self.elem = [x, y, z]
#
#  def __add__(self, v2):
#   
#  def __get__(self, index):
#    if index not in range(0, 3):
#      print("index not found")
#      return False
#    return self.elem[index]
#
#
#class Cube:
#
#  def __init__(self):

class Mesh:
  pass    


