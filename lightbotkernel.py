import numpy as np
"""all done for a terrain of (m,n), corresponding to m rows, n columns.

some critical points:
* no loops are allowed.

* path should be given as a string.

* facing direction should be given as "right, left, up, or down".

* initial terrain and colors should be given as a matrix (a numpy array).

* position should be given as (y,x).  **notice that y values increase as you go down, x values increase as you go right.**

i did not put any restrictions in the functions for these conditions.
"""
def turn_left():
  global facing_direction
  if facing_direction == "right":
    facing_direction = "up"

  elif facing_direction == "left":
    facing_direction = "down"

  elif facing_direction == "down":
    facing_direction = "right"

  elif facing_direction == "up":
    facing_direction = "left"

  return facing_direction

def turn_right():
  global facing_direction
  if facing_direction == "right":
    facing_direction = "down"

  elif facing_direction == "left":
    facing_direction= "up"

  elif facing_direction== "down":
    facing_direction= "left"

  elif facing_direction == "up":
    facing_direction= "right"

  return facing_direction

  """
  I’ve defined right as east, left as west, etc.  
  these directions are fixed and do not change based on the direction you are facing. 
  in other words, whether you are facing north, south, east, or west, 
  right will always mean east and left will always mean west according to their geographical positions.
  However, turn commands depend on your current orientation. For instance,
  if you are already facing right (east), the command "turn right" will make you turn to "your right",
  causing you to face "down" (south).
 apologies for any confusion. 
 the reason I labeled them this way is that I assumed everyone would naturally think of directions in this format, 
 regardless of their orientation.
 """

def move_forward():

  global position, facing_direction, heights
  n, m = terrain.shape  # get terrain size

  if facing_direction == "right":
    #again, here moving right means moving towards east so the limitations make sense.
    if position[1]+1 < m and heights[position[0], position[1]+1]== heights[position[0], position[1]]:
     position= (position[0], position[1]+1)
    else:
     #position stays the same.
     print(f"can't go any more right from that position: {position}")

  elif facing_direction == "left":
    if position[1]-1 >= 0 and heights[position[0], position[1]-1]== heights[position[0], position[1]]:
     position= (position[0], position[1]-1)
    else:
     print(f"can't go any more left from that position: {position}")

  elif facing_direction == "up":
    if position[0]-1 >= 0  and heights[position[0]-1, position[1]]== heights[position[0], position[1]]:
     position= (position[0]-1, position[1])
    else:
      print(f"can't go any more up from that position: {position}")

  elif facing_direction == "down":
    if position[0]+1 <n  and heights[position[0]+1, position[1]]== heights[position[0], position[1]]:
     position= (position[0]+1, position[1])
    else:
      print (f"can't go any more down from that position: {position}")

  return position

def jump():

   global position, facing_direction, heights
   n, m = terrain.shape

   if facing_direction == "right":
    if position[1]+1 < m and heights[position[0], position[1]+1]== (heights[position[0], position[1]]+1):
     position= (position[0], position[1]+1)

   elif facing_direction == "left":
    if position[1]-1 >= 0 and heights[position[0], position[1]-1]== (heights[position[0], position[1]]+1):
     position= (position[0], position[1]-1)

   elif facing_direction == "up":
    if position[0]-1 >= 0 and heights[position[0]-1, position[1]]== (heights[position[0], position[1]]+1):
     position= (position[0]-1, position[1])
  
   elif facing_direction == "down":
    if position[0]+1 < n and heights[position[0]+1, position[1]]== (heights[position[0], position[1]]+1):
     position= (position[0]+1, position[1])

   return position

"""for colors, let's define:
gray= 0
blue= 1
yellow= 2"""

def switch():
  global position, facing_direction, heights
  n, m = terrain.shape

  if colors[position[0], position[1]]== 1:
    #if blue, make yellow.
    colors[position[0], position[1]] = 2
    return colors

  elif colors[position[0], position[1]]== 2:
    colors[position[0], position[1]] = 1
    print(f"you have unswitched the light at the position: {position}")

  return colors


def kernel(path, terrain, heights, facing_direction, colors):
 for _ in range(len(path)):

  if path[_]=="^":
    move_forward()

  elif path[_]== "<":
    turn_left()

  elif path[_]== ">":
    turn_right()

  elif path[_]== "*":
    jump()

  elif path[_]== "@":
    switch()

 print (f"ending position: {position}")

 print(f"ending facing direction: {facing_direction}")

 print("colors: ")
 print(colors)

 return "-"
