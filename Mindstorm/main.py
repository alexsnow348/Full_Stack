import turtle

def draw_square(brad):

    for i in range(4):
        brad.forward(100)
        brad.right(90)


def draw_circle():
    angie = turtle.Turtle()
    angie.shape('arrow')
    angie.color('blue')
    angie.circle(100)

def draw_triangle():
    tom = turtle.Turtle()
    tom.shape('turtle')
    tom.color('red')
    tom.forward(100)
    tom.left(120)
    tom.forward(100)
    tom.left(120)
    tom.forward(100)


if __name__ == '__main__':
        window = turtle.Screen()
        window.bgcolor('gray')
        # draw_square()
        # draw_circle()
        # draw_triangle()

        brad = turtle.Turtle()
        brad.shape('turtle')
        brad.color('purple')
        brad.speed(2)
        for i in range(3):
            draw_square(brad)
            brad.right(10)
        window.exitonclick()
