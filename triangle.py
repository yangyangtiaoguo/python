import turtle

def triangle():
        turtle.fd(180)
        turtle.seth(120)
        turtle.fd(180)
        turtle.seth(240)
        turtle.fd(180)

def main():
    turtle.setup(1300,800,80,80)
    pythonsize = 10
    turtle.pensize(pythonsize)
    turtle.pencolor("blue")
    turtle.seth(0)
    triangle()

main()
    
