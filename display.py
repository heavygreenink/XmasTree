from tree import RGBXmasTree
from time import sleep
from colorzero import Color, Hue
from datetime import date, datetime, time, timedelta
from random import choice, randint, random, shuffle


sod = time(  6, 00, 00)
eod = time( 22, 00, 00)

colors = [
        Color('green'),
        Color('orange'),
        Color('blue'), 
        Color('yellow'),
        Color('red'),
        Color('white'),
  ] 

color_count = len(colors)
#----------------------------------------------------------------------------
def displayTime( now ):
    time = now.time()
    if time >= sod and time <= eod:
        return True
    else:
        return False
#----------------------------------------------------------------------------
def restTime( tree ):
    now = datetime.now()
    if not displayTime( now ):
       tree.color = Color('black')
       sleep( 60 * 10 )

#----------------------------------------------------------------------------
def endtime():

    now = datetime.now()
    finish =  now + timedelta(0, randint( 8, 20 ) ) 
    if displayTime( now ):
        return finish
    else:
        return now

#----------------------------------------------------------------------------
def random_color():
    r = random()
    g = random()
    b = random()
    return (r, g, b)

#----------------------------------------------------------------------------
def oneByOne( tree, finish ): 
  
    try:
        while datetime.now() < finish:
            for color in colors:
                for pixel in tree:
                    pixel.color = color
    
                next_color =  colors[ (colors.index(color) + 1 ) % color_count ]         
                for pixel in tree:  
                    pixel.blink( next_color )

                for pixel in reversed(tree):  
                    pixel.blink( next_color )

                old = color

    except KeyboardInterrupt:
        tree.close()


#----------------------------------------------------------------------------
def hueCycle( tree, finish ):
    tree.color = Color('green')

    try:
        while datetime.now() < finish:
            tree.color += Hue(deg=1)
    except KeyboardInterrupt:
        tree.close()

#----------------------------------------------------------------------------
def randomCSparkles( tree, finish ):
    try:
        while datetime.now() < finish:
            pixel = choice(tree)
            pixel.color = random_color()
    except KeyboardInterrupt:
        tree.close()

#----------------------------------------------------------------------------
def build( tree, finish ):
   
    tree.off

    combos = [
    [ 0, 6, 7, 13 ],
    [ 1, 5, 8, 12 ],
    [ 2, 4, 9, 11 ],
    [ 3, 10 ],
    ]

    while datetime.now() < finish:

        forward = True
        for color in colors:
            work = combos
            if not forward:
                work = reversed( combos )

            for combo in work:
                for i in combo:
                    tree[i].color = color

                sleep(.5)
        
            forward = not forward

#----------------------------------------------------------------------------
def lineBuild(tree, finish ):
    tree.off

    while datetime.now() < finish:
        for color in colors:
            for pixel in tree:
                pixel.color = color
                sleep(.1)

#----------------------------------------------------------------------------
def zigZag(tree, finish ):
    tree.off

    combos = [
        [ 0,  7 ], 
        [ 5, 12 ], 
        [ 2,  8 ],
        [ 3 ],
        [ 4, 11 ],
        [ 1,  8 ],
        [ 6, 13]
    ]

    while datetime.now() < finish:
        for color in colors:
            next_color =  colors[ (colors.index(color) + 1 ) % color_count ]         
            for combo in combos:
                for index in combo:
                    pixel = tree[index]
                    pixel.blink( next_color ) 
                    pixel.color = color


#----------------------------------------------------------------------------
def sideToSide(tree, finish ):
   
   while datetime.now() < finish:

     for current_color in colors:
        color = current_color
        next_color =  colors[ (colors.index(color) + 1 ) % color_count ]    
        for i in range( 0, 7 ):     
            tree[i].color = color
            tree[i+7].color = color
            if i > 6:
                color = next_color

        sleep( 0.6 )


#----------------------------------------------------------------------------
def asorted(tree, finish ):
 
    color = 0
    while datetime.now() < finish:
        for index in range( 0, 7 ):
            tree[index].color = colors[color]
            tree[index+7].color = colors[color]
            color = ( color + 1 ) % color_count
            sleep( 0.1 )

#----------------------------------------------------------------------------
def twinkle( tree, finish ):

    for color in colors:
        tree.color = color
        for i in range( 0, 5 ):
            for twinkel in colors:
                tree[3].blink(twinkel)
                tree[10].blink(twinkel)

#----------------------------------------------------------------------------
def flash(tree, finish ):
   
   while datetime.now() < finish:

     for current_color in colors:
        color = current_color
        next_color =  colors[ (colors.index(color) + 1 ) % color_count ]    
        for i in range( 0, 7 ):     
            tree.color = next_color
            sleep(.2)
            tree.color = color
            sleep(.2)

#----------------------------------------------------------------------------

tree = RGBXmasTree()

functions = [
    asorted,
    build,
    flash,
    hueCycle,
    lineBuild,
    oneByOne, 
    randomCSparkles,
    sideToSide,
    twinkle,
    zigZag,
]

last_index = -1
max = len(functions) -1

counter = {}
for i in range( 0, len(functions ) ):
    counter[i] = 0

while True:
    restTime( tree )

    shuffle( colors )
    function_index = randint(0, max )
    while function_index == last_index:
        function_index = randint(0, max)

    counter[ function_index ] += 1
    print(functions[function_index], counter[ function_index ] )
    functions[function_index]( tree, endtime() )
    last_index = function_index


tree.off()
tree.close()



