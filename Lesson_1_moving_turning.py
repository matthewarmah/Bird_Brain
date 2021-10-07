from BirdBrain import Finch
bird = Finch()

print("exercise 1")
print("Distance: ", bird.getDistance())
if (bird.getDistance() > 50):
   bird.setMove("F",15,100)

print("exercise 2")
bird.setBeak(100,0,100)
bird.setBeak(0,0,0)

print("exercise 3")
bird.setTurn('R',360,50)

print("exercise 4 ")
bird.setMove("F",25,100)
bird.setTurn('R',90,50)
bird.setMove("F",25,100)
bird.setTurn('R',90,50)
bird.setMove("F",25,100)
bird.setTurn('R',90,50)

print("exercise 6")
#1 inch = 2.54 centimeters 
bird.setMove("F",27.94,100)
