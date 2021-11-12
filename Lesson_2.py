from BirdBrain import Finch      #use the finch class that is located in the BirdBrain.py module/library 
from time import sleep               #use the sleep class that is located in the time module
bird = Finch()

print("exercise 1")
print("Distance: ", bird.getDistance())
if (bird.getDistance() > 50):
   bird.setMove("B",15,100)

print("excercise 2")
bird.getLight("R")

print("light",bird.getLight("R"))

print("exercise 3")
print(type(bird.getDistance()))

print("exercise 4")
