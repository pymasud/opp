from turtle import Turtle,Screen ## import the class Turtle from the module turtle

timmy = Turtle()
print(timmy)
timmy.shape("turtle")  ## attibutes method
timmy.color("coral")    ## attibutes method
timmy.forward(100)    ## methods
timmy.backward(200)   ## methods

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()