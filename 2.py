for x in 0,1:
  for y in 0,1:
    for z in 0,1:
      for w in 0,1:
        F = ((x <= y) == (z or w)) or (x <= z)
        if F == 1:
          print(y,z,x,w)