import turtle
    
t = turtle.Turtle()
t.speed(100)
# taking radius of initial radius

r = 10
  
# Loop for printing spiral circle
for i in range(200):
    t.circle(r + i, 40)

turtle.done()