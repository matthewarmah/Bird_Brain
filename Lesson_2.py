from BirdBrain import Finch
from time import sleep
bird = Finch()

print("exercise 1")
print("Distance: ", bird.getDistance())
if (bird.getDistance() > 50):
   bird.setMove("B",15,100)

print("excercise 2")
bird.getLight("R")

print("light",bird.getLight("R"))
