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
