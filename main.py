import random

#smile = [
#  [3,0,0,1,0],
#  [0,0,0,0,0],
#  [0,0,0,1,0],
#  [0,1,1,0,1],
#  [0,0,0,0,2]
#  ]

#Map 1:
#smile = [[3,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,1,0,2]]

#Map 2:
#smile = [[3,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,1],[0,0,0,0,2]]

#Map 3:
#smile = [[3,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,1],[0,0,1,0,2]]

#Map 4:
#smile = [[3,0,0,0,0],[0,0,0,1,0],[1,0,0,0,0],[0,0,0,0,1],[0,0,0,0,2]]

#Map 5:
#smile = [[3,1,0,0,0],[0,0,0,0,0],[1,0,1,0,0],[0,0,0,0,1],[0,0,1,0,2]]

#Map 6:
#smile = [[3,0,0,0,0],[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,2]]

#Map 7:
#smile = [[3,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,1,1],[0,1,0,0,2]]

#Map 8:
#smile = [[3,0,1,0,0],[1,0,0,0,0],[0,0,1,1,1],[0,0,0,0,0],[0,0,0,1,2]]

#Map 9:
smile = [[3,0,0,0,0],[1,1,1,0,0],[0,0,0,0,0],[0,0,0,1,1],[0,1,0,0,2]]

i = 0
j = 0
scx = 0
scy = 0

coords_y = 0
coords_x = 0

l = 0
m = 0
ecx = 0
ecy = 0

recent = ""
recent_memory1 = ""
recent_memory2 = ""

n = 0
p = 0

path = []

moves = 0

def Find_Start():
    global l, m, ecx, ecy, smile, i, j, scx, scy, coords_y, coords_x, path, moves
    foundS = 0
    for x in smile:
        j = 0
        for y in x:
            if y == 3:
                scx = i
                scy = j
                foundS = 1
            j=j+1
        i=i+1
    if foundS == 0:
        print("Start not found, Aborted")
    else:
        print("Start found: coords " + str(scx) + ", " + str(scy))
    print()

def Find_End():
    global l, m, ecx, ecy, smile, i, j, scx, scy, coords_y, coords_x, path, moves
    foundE = 0
    for z in smile:
        l = 0
        for w in z:
            if w == 2:
                ecx = m
                ecy = l
                foundE = 1
            l=l+1
        m=m+1
    if foundE == 0:
        print("End not found, Aborted")
    else:
        print("End found: coords " +str(ecx) + ", " + str(ecy))
    print()

def Path_Up():
  global l, m, ecx, ecy, smile, i, j, scx, scy, coords_y, coords_x, path, moves, n
  while coords_x - 1 > -1 and coords_x - 1 < 5 and n == 0:
    if smile [coords_x - 1][coords_y] != 1:
      path.append([coords_x, coords_y])
      coords_x = coords_x - 1
      print("up")
      print(str(coords_x) + " " + str(coords_y))
      moves = moves + 1
    else:
      n = 1
  n = 0

def Path_Left():
  global l, m, ecx, ecy, smile, i, j, scx, scy, coords_y, coords_x, path, moves, n
  while coords_y - 1 > -1 and coords_y - 1 < 5 and n == 0:
    if smile [coords_x][coords_y - 1] != 1:
      path.append([coords_x, coords_y])
      coords_y = coords_y - 1
      print("left")
      print(str(coords_x) + " " + str(coords_y))
      moves = moves + 1 
    else:
      n = 1
  n = 0

def Path_Down():
  global l, m, ecx, ecy, smile, i, j, scx, scy, coords_y, coords_x, path, moves, n
  while coords_x + 1 > -1 and coords_x + 1 < 5 and n == 0:
    if smile [coords_x + 1][coords_y] != 1:
      path.append([coords_x, coords_y])
      coords_x = coords_x + 1
      print("down")
      print(str(coords_x) + " " + str(coords_y))
      moves = moves + 1
    else:
      n = 1
  n = 0

def Path_Right():
  global l, m, ecx, ecy, smile, i, j, scx, scy, coords_y, coords_x, path, moves, n
  while coords_y + 1 > -1 and coords_y + 1 < 5 and n == 0:
    if smile [coords_x][coords_y + 1] != 1:
      path.append([coords_x, coords_y])
      coords_y = coords_y + 1
      print("right")
      print(str(coords_x) + " " + str(coords_y))
      moves = moves + 1
    else:
      n = 1
  n = 0


def Path_Up1():
  global l, m, ecx, ecy, smile, i, j, scx, scy, coords_y, coords_x, path, moves, n
  if coords_x - 1 > -1 and coords_x - 1 < 5 and n == 0:
    if smile [coords_x - 1][coords_y] != 1:
      path.append([coords_x, coords_y])
      coords_x = coords_x - 1
      print("up")
      print(str(coords_x) + " " + str(coords_y))
      moves = moves + 1
    else:
      n = 1
  n = 0

def Path_Left1():
  global l, m, ecx, ecy, smile, i, j, scx, scy, coords_y, coords_x, path, moves, n
  if coords_y - 1 > -1 and coords_y - 1 < 5 and n == 0:
    if smile [coords_x][coords_y - 1] != 1:
      path.append([coords_x, coords_y])
      coords_y = coords_y - 1
      print("left")
      print(str(coords_x) + " " + str(coords_y))
      moves = moves + 1 
    else:
      n = 1
  n = 0

def Path_Down1():
  global l, m, ecx, ecy, smile, i, j, scx, scy, coords_y, coords_x, path, moves, n
  if coords_x + 1 > -1 and coords_x + 1 < 5 and n == 0:
    if smile [coords_x + 1][coords_y] != 1:
      path.append([coords_x, coords_y])
      coords_x = coords_x + 1
      print("down")
      print(str(coords_x) + " " + str(coords_y))
      moves = moves + 1
    else:
      n = 1
  n = 0

def Path_Right1():
  global l, m, ecx, ecy, smile, i, j, scx, scy, coords_y, coords_x, path, moves, n
  if coords_y + 1 > -1 and coords_y + 1 < 5 and n == 0:
    if smile [coords_x][coords_y + 1] != 1:
      path.append([coords_x, coords_y])
      coords_y = coords_y + 1
      print("right")
      print(str(coords_x) + " " + str(coords_y))
      moves = moves + 1
    else:
      n = 1
  n = 0

def opposite(direction):
  if direction == "R":
    answer = "L"
  elif direction == "D":
    answer = "U"
  elif direction == "L":
    answer = "R"
  elif direction == "U":
    answer = "D"
  return answer

def Find_Path():
  global l, m, ecx, ecy, smile, i, j, scx, scy, coords_y, coords_x, path, moves, n, recent_memory2, recent_memory1, recent, p
  coords_x = scx
  coords_y = scy
  recent_memory4 = ""
  recent_memory3 = ""
  n = 0
  print(moves)
  print(ecx)
  while coords_x != ecx or coords_y != ecy:
    print("*")
    if scy < ecy:
      if p == 0:
        if coords_y + 1 > -1 and coords_y + 1 < 5 and recent_memory1 != "Rl":
          if smile [coords_x][coords_y + 1] != 1:
            
            recent = "R"
            Path_Right()
        random.randint(0, 3)
      elif p == 1:
        if coords_y - 1 > -1 and coords_y - 1 < 5 and recent_memory1 != "Ll":
          if smile [coords_x][coords_y - 1] != 1:
            
            recent = "L"
            Path_Left1()
        random.randint(0, 3)
      elif p == 2:
        if coords_x + 1 > -1 and coords_x + 1 < 5 and recent_memory1 != "Dl":
          if smile [coords_x + 1][coords_y] != 1:
            
            recent = "D"
            Path_Down()
        random.randint(0, 3)
      elif p == 3:
        if coords_x - 1 > -1 and coords_x - 1 < 5 and recent_memory1 != "Ul":
          if smile [coords_x - 1][coords_y] != 1:
            
            recent = "U"
            Path_Up1()
      p = random.randint(0, 3)
      recent_memory4 = recent_memory3
      recent_memory3 = recent_memory2
      recent_memory2 = recent_memory1
      recent_memory1 = recent
      #moves = moves + 1
      #if recent_memory2 == recent and recent_memory4 == recent:
      #  recent = ""
      #elif recent_memory4 == recent:
      #  recent = recent_memory1
      if  moves > 500:
        break
  path.append([coords_x, coords_y])

def Simplify_Path():
  global l, m, ecx, ecy, smile, i, j, scx, scy, coords_y, coords_x, path, moves, n, recent_memory2, recent_memory1, recent, p
  start = 1
  dup = [0, 0]
  while len(dup) > 0:
    start = 0
    dup.clear()
    for x in path:
      q = 0
      for i in range(len(path)):
        if path[i] == x:
          q = q + 1
          
      if q > 1:
        dup = [r for r,y in enumerate(path) if y==x]
        print(dup)
        print(dup[0])
        del path[dup[0]: dup[1]]
        print(path)
        print(len(dup))

def Simplify_Path_Again():
  print()
  global l, m, ecx, ecy, smile, i, j, scx, scy, coords_y, coords_x, path, moves, n, recent_memory2, recent_memory1, recent, p
  for x in range(len(path)):
    q = 0
    brk = 0
    for i in range(len(path)):
      if path[i][0] == path[x][0]:
        if path[i][1] == path[x][1] - 1 or path[i][1] == path[x][1] + 1:
          print('Two')
          if x != i + 1 and x != i - 1:
            del path[x + 1: i]
            brk = 1
            print(path)
            break
      elif path[i][1] == path[x][1]:
        if path[i][0] == path[x][0] - 1 or path[i][0] == path[x][0] + 1:
          print('Four')
          if x != i + 1 and x != i - 1:
            del path[x + 1: i]
            print(path)
            brk = 1
            break
        if brk == 1:
          break
      if brk == 1:
        break
    if brk == 1:
        break

def Robot_Path():
  global l, m, ecx, ecy, smile, i, j, scx, scy, coords_y, coords_x, path, moves, n, recent_memory2, recent_memory1, recent, p
  facing = 1
  face = 1
  for i in range(len(path)-1):
    if  path[i][0] == path[i + 1][0] - 1 and path[i][1] == path[i + 1][1]:
      face = 2
    elif  path[i][0] == path[i + 1][0] and path[i][1] == path[i + 1][1] + 1:
      face = 1
    elif  path[i][0] == path[i + 1][0] + 1 and path[i][1] == path[i + 1][1]:
      face = 0
    elif  path[i][0] == path[i + 1][0] and path[i][1] == path[i + 1][1] - 1:
      face = 3
    if facing != face:
      if facing - face < 0:
        facing = abs(facing - face)
        print('turn left ' + str(facing))
        facing = face
      else:
        facing = facing - face
        print('turn right ' + str(facing))
        facing = face
    print("move forward")
    
Find_Start()
Find_End()
Find_Path()
print(path)
Simplify_Path()
Simplify_Path_Again()
print(path)
Robot_Path()