import turtle

def drawTriangle(points, color, myTurtle):
  myTurtle.fillcolor(color)
  myTurtle.up()
  myTurtle.goto(points[0][0], points[0][1])
  myTurtle.down()
  myTurtle.begin_fill()
  myTurtle.goto(points[1][0], points[1][1])
  myTurtle.goto(points[2][0], points[2][1])
  myTurtle.goto(points[0][0], points[0][1])
  myTurtle.end_fill()

def findMiddle(a,b):
  return ((a[0] + b[0] /2, a[1] + b[1] /2))

def sierpinski(points, deg, myTurtle):
  colormap = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']
  drawTriangle(points, colormap[deg], myTurtle)
  if deg > 0:
    sierpinski([points[0],
               findMiddle(points[0], points[1]),
               findMiddle(points[0], points[2])],
              deg-1, myTurtle)
    sierpinski([points[2],
               findMiddle(points[0], points[1]),
               findMiddle(points[1], points[2])],
              deg-1, myTurtle)
    sierpinski([points[2],
               findMiddle(points[2], points[1]),
               findMiddle(points[0], points[2])],
               deg-1, myTurtle)

def main():
  myTurtle = turtle.Turtle()
  myWin = turtle.Screen()
  myPoints = [[-100, -50],[0, 100], [100, -50]]
  sierpinski(myPoints, 3, myTurtle)
  myWin.exitonclick()


main()
        