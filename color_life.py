#!/usr/bin/env python

import time

from sense_hat import SenseHat

sense = SenseHat()

# Define some colours
w = (255, 255, 255) # White
b = (0, 0, 0) # Black
ye = (190, 190, 0) 
t = (180, 255, 0) 
g = (0, 255, 0) 


number_of_columns = 8
number_of_rows = 8
surrounding_cell_number = 8
# Set up where each colour will display

screen_pixels = [
    b, t, b, b, b, b, b, b,
    b, t, b, b, b, w, b, b,
    b, t, b, b, b, w, b, b,
    b, b, w, b, w, w, b, b, 
    b, b, ye, ye, ye, b, b, b,
    b, ye, b, w, b, w, b, b,
    b, b, b, w, g, w, b, b,
    b, b, b, b, g, b, b, b
]   


screen_pixels_back = [
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b
]

def getPixel(x, y):
    if x < 0 or x >= number_of_rows:
        return None
    if y < 0 or y >= number_of_columns:
        return None
    return screen_pixels[x * number_of_columns + y]

def setPixel(x, y, value):
    color = b
    if value == 1:
        color = w
    elif value == 2:
        color = ye
    elif value == 3:
        color = t
    elif value == 4:
        color = g
    screen_pixels_back[x * number_of_columns + y] = color

# game of life algorithm
# Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any live cell with more than three live neighbours dies, as if by overpopulation.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
def game_of_life(cells, currently_living): # surronding cells 8 cells, return True survives, False dies
    number_of_surronding_living = 0
    number_of_surronding_died = 0
    for i in range(surrounding_cell_number):
        if cells[i] == w:  # live
            number_of_surronding_living += 1
        if cells[i] == ye:  # live
            number_of_surronding_living += 2
        if cells[i] == t:  # live
            number_of_surronding_living += 3
        if cells[i] == g:  # live
            number_of_surronding_living += 4
        if cells[i] == b:  # live
            number_of_surronding_died += 1
    if currently_living == True:
        if number_of_surronding_living < 2:
            return 0
        if number_of_surronding_living == 2:
            return 1
        if number_of_surronding_living == 3:
            return 2
        if number_of_surronding_living == 4:
            return 3
        if number_of_surronding_living > 2:
            return 0
    elif number_of_surronding_living == 3:
             return 1
    elif number_of_surronding_living == 4:
             return 2
    return currently_living  # In any other case, live the cell the way it is

cells = [0, 0, 0, 0, 0, 0, 0, 0]
while True:
    for y in range(number_of_columns):
        for x in range(number_of_rows):
            cells[0] = getPixel(x-1,y-1)
            cells[1] = getPixel(x-1,y)
            cells[2] = getPixel(x-1,y+1)
            cells[3] = getPixel(x,y-1)
            cells[4] = getPixel(x,y+1)
            cells[5] = getPixel(x+1,y-1)
            cells[6] = getPixel(x+1,y)
            cells[7] = getPixel(x+1,y+1)
            p = getPixel(x,y)
            setPixel(x,y,game_of_life(cells, p == w))
    screen_pixels = list(screen_pixels_back)
    # Display these colours on the LED matrix
    sense.set_pixels(screen_pixels)
    time.sleep(0.8)

