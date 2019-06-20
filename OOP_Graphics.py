#   Graphical programming using tkinter from graphics.py
from graphics import *

def main():
# Introduction
#   This program plots the graph of a 20 year investment

#   Get the principal and annual rate
    principal = float(input("enter the principal amount you want to invest: "))
    apr = float(input("enter the annual interest rate : "))



    win = GraphWin("investment growth chart", 500, 500)
    win.setBackground(color_rgb(255,255,255))
#   Definig the coordinate of the graph
    win.setCoords(-2.0, -200, 22, 10400)

#   This is where your graphic program goes...
    #   creating the vertical label for the graph
    t0 = Text(Point(-1, 0), "0").draw(win)
    t1 = Text(Point(-1, 2500), "$2.5k").draw(win)
    t2 = Text(Point(-1, 5000), "$5.0k").draw(win)
    t3 = Text(Point(-1, 7500), "$7.5k").draw(win)
    t4 = Text(Point(-1, 10000), "$10.0k").draw(win)

    #   Draw initial Principal
    bar = Rectangle(Point(0, 0), Point(1, principal))
    bar.setFill("red")
    bar.setOutline("white")
    bar.setWidth(2)
    bar.draw(win)

    #   Creating the bar chart for subsequent year
    #       By looping across each year
    for year in range(1, 21):
        principal = principal * (1 + apr)
        bar = Rectangle(Point(year, 0), Point(year+1, principal))
        bar.setFill("blue")
        bar.setOutline("white")
        bar.setWidth(2)
        bar.draw(win)

#   End of graphic program

    win.getMouse()
    win.close()
main()
