from BirdBrain import Finch
from time import sleep
bird = Finch()

print("exercise 1")
print("Distance: ", bird.getDistance())
if (bird.getDistance() > 50):
   bird.setMove("B",15,100)

print("exercise 2")
bird.setBeak(100,0,100)
bird.setBeak(0,0,0)

