from tree import RGBXmasTree
from time import sleep
from colorzero import Color, Hue
from datetime import date, datetime, time, timedelta
from random import choice, randint, random, shuffle


colors = [
        Color('green'),
        Color('orange'),
        Color('blue'), 
        Color('yellow'),
        Color('red'),  ] 

color_count = len(colors)

combos = [
  [ 0,  7 ], 
  [ 5, 12 ], 
  [ 2,  8 ],
  [ 3, 10 ],
  [ 4, 11 ],
  [ 1,  8 ],
  [ 6, 13],
]

counter = {  }
for j in range (0,100):
   i = randint( 0, len( combos ) - 1 )
   combo = combos[i]

   if i in counter.keys():
     counter[i] += 1
   else:
      counter[i] = 1

   print( combo, '-', counter[i] )
  
  





'''
tree = RGBXmasTree()
tree.off


for color in colors:
    tree.color = color
    for i in range( 0, 5 ):
      for twinkel in colors:
        tree[3].blink(twinkel)
        tree[10].blink(twinkel)
'''