from sense_hat import SenseHat
from time import sleep
from random import randint
from random import uniform
from random import choice
sense = SenseHat()

num=randint(0,255)
num1=uniform(0,255)
deck=['Ace','King','Queen','Jack']
card=choice(deck)

# define the colours
r = 255
g = 180
b = 20

red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)
purple = (180,0,180)

# Generate a random colour
def pick_random_colour():
  random_red = randint(0, 255)
  random_green = randint(0, 255)
  random_blue = randint(0, 255)
  return (random_red, random_green, random_blue)
  
  

#print a letter with a one secound timer
sense.show_letter("D", pick_random_colour())
sleep(1)
sense.show_letter("e", pick_random_colour())
sleep(1)
sense.show_letter("n", pick_random_colour())
sleep(1)
sense.show_letter("n", pick_random_colour())
sleep(1)
sense.show_letter("i", pick_random_colour())
sleep(1)
sense.show_letter("s", pick_random_colour())
sleep(1)



sense.clear()

# clear r,g og b farve pallenten
sense.clear((r,g,b))





#while True:
  #takes reading from all 3 sensors
  #t = sense.get_temperature()
  #p = sense.get_pressure()
  #h = sense.get_humidity()
  
  
  # round the values to one dicimal place
  #t = round(t,1)
  #p = round(p,1)
  #h = round(h,1)
  
  
  # creates the massage
  # sense.show_message("It Snowing", scroll_speed=0.1, text_colour=yellow, back_colour=blue)
  
  #printer din besked
  #print ("hallo world it is snowing")

  
grid = [
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r
]
i 8x8

sense.set_pixels(grid)
