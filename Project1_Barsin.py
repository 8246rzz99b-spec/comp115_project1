import turtle

t = turtle.Turtle()
t.speed(0)
t.shape("blank")

wn = turtle.Screen()
wn.bgcolor("black")
  # We use colormode(255) so we can define colors using RGB values from 0 to 255 instead of the default 0.0 to 1.0 range.
  # And this code makes it easier to manually create smooth gradient colors.
turtle.colormode(255)

r, g, b = 255, 0, 0   # start at red

for i in range(1000):
    t.pencolor(r, g, b)

    # our pattern
    t.forward(i)
    t.right(90)
    t.left(45)
    t.right(87)
    t.backward(25)
    t.right(100)
    t.left(120)

    # The color transition
    if r == 255 and g < 255 and b == 0:
        g += 1      # Red --> Yellow
    elif g == 255 and r > 0:
        r -= 1      # Yellow --> Green
    elif g == 255 and b < 255:
        b += 1      # Green --> Cyan
    elif b == 255 and g > 0:
        g -= 1      # Cyan --> Blue
    elif b == 255 and r < 255:
        r += 1      # Blue --> Magenta
    elif r == 255 and b > 0:
        b -= 1      # Magenta --> Red

wn.mainloop()