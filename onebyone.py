from tree import RGBXmasTree
from time import sleep
from colorzero import Color
import datetime


tree = RGBXmasTree()


def one_by_one( finsish ): 
    colors = [
            Color('green'),
            Color('pink'), 
            Color('orange'),
            Color('blue'), 
            Color('yellow'),
            Color('red')  ] # add more if you like

    color_count = len(colors)

    try:
        while datetime.datetime.now() < finish:
            for color in colors:
                for pixel in tree:
                    pixel.color = color
                    #sleep(0.05)
    
                next_color =  colors[ (colors.index(color) + 1 ) % color_count ]         
                for pixel in tree:  
                    pixel.blink( next_color )

                for pixel in reversed(tree):  
                    pixel.blink( next_color )

                old = color

    except KeyboardInterrupt:
        tree.close()





finish =  datetime.datetime.now() + datetime.timedelta(0,3) 
one_by_one( finish )


