import turtle

letur = turtle.Turtle()
letur.width(1)
letur.color("white")

start = [-735, 390]

turtle.Screen().bgcolor('black')
y = 800
gps = 15

letur.penup()
letur.goto(start)
lines = 0
end = 0
letur.speed(0)


def makleen(t : turtle, value : any, end : int, gps : int, leenlen : float | None = gps) -> float:
    t.penup()
    t.goto(start[0] - 5, start[1] + (end - gps))
    t.setheading(0)
    t.write(f"|{value}>", align="right")
    t.forward(5)
    t.pendown()
    x = t.ycor() - start[1]
    t.forward(leenlen)
    t.back(leenlen - gps)
    t.penup()

    return x

def blipi(t : turtle, gps : int):    
    t.pendown()
    t.back(gps / 2) ; t.setheading(270)
    t.fillcolor('blue') ; t.begin_fill()
    t.circle(gps / 2) ; t.end_fill()
    t.setheading(0) ; t.forward(gps / 2)
    t.penup()

def whynot(t : turtle, gps : int):
    t.pendown()
    t.back(gps / 2) ; t.setheading(270)
    t.circle(gps / 2)
    t.setheading(0) ; t.forward(gps) ; t.back(gps / 2)
    t.setheading(270) ; t.forward(gps / 2) ; t.back(gps)
    t.forward(gps / 2) ; t.setheading(0)
    t.penup()

def andgat(t : turtle, pos1 : int, pos2 : int, end : int, gps : int, start : list, inver : int | None = 0, leenlen : float | None = gps) -> float:
    xy = [t.xcor(), t.ycor()]
    end = makleen(t, inver, end, gps, leenlen)
    t.goto(xy)

    t.penup()
    t.setheading(0)
    t.forward(gps)
    t.goto(t.xcor(), (start[1] - (pos1 * gps)))
    blipi(t, gps / 2)
    t.pendown()

    t.goto(t.xcor(), (start[1] - (pos2 * gps)))
    blipi(t, gps / 2)
    t.pendown()

    t.goto(t.xcor(), start[1] + end)
    whynot(t, gps / 2)
    t.penup()

    return end

def exclugat(t : turtle, pos1 : int, pos2 : int, end : int, gps : int, start, inver : int | None = 0, leenlen : float | None = gps) -> float:
    xy = [t.xcor(), t.ycor()]
    end = makleen(t, inver, end, gps, leenlen)
    t.goto(xy)

    t.penup()
    t.setheading(0)
    t.forward(gps)

    t.goto(t.xcor(), (start[1] - (pos1 * gps)))
    blipi(t, gps / 2)

    t.pendown()
    t.goto(t.xcor(), start[1] + end)
    whynot(t, gps / 2)

    t.penup()
    t.forward(gps)

    t.goto(t.xcor(), (start[1] - (pos2 * gps)))
    blipi(t, gps / 2)

    t.pendown()
    t.goto(t.xcor(), start[1] + end)
    whynot(t, gps / 2)

    t.penup()
    return end

def tobegat(t : turtle, pos1 : int, pos2 : int, end : int, gps : int, start, inver : int | None = 0, leenlen : float | None = gps) -> float:
    end = andgat(t, pos1, pos2, end, gps, start, 1, leenlen)
    end = exclugat(t, pos1, pos2, end, gps, start, 1, leenlen)
    end = andgat(t, (-(end / gps) - 1), -(end / gps), end, gps, start, inver, leenlen)

    return end

def fadder(t : turtle, pos1 : int, pos2 : int, end : int, gps : int, start, leenlen : float | None = gps) -> float:
    end = exclugat(t, pos1, pos2, end, gps, start, 0, leenlen)
    end = andgat(t, pos1, pos2, end, gps, start, 0, leenlen)

    end = exclugat(t, (-(end) / gps) - 1, (-(end) / gps) - 2, end, gps, start, 0, leenlen)
    end = andgat(t, (-(end) / gps) - 2, (-(end) / gps) - 3, end, gps, start, 0, leenlen)

    end = tobegat(t, (-(end) / gps) - 2, (-(end) / gps), end, gps, start, 0, leenlen)

    return end

def hadder(t : turtle, pos1 : int, pos2 : int, end : int, gps : int, start, leenlen : float | None = gps) -> float:
    end = exclugat(t, pos1, pos2, end, gps, start, 0, leenlen)
    end = andgat(t, pos1, pos2, end, gps, start, 0, leenlen)

    return end

def meas(t : turtle, pos, y : float, end : int, gps : int, start):
    xy = [t.xcor(), t.ycor()]
    t.goto(start[0] + y, start[1] - (pos * gps))
   
    t.pendown()
    t.setheading(270) ; t.forward(gps / 2)
    t.setheading(0) ; t.forward(gps)
    t.setheading(90) ; t.forward(gps)
    t.setheading(180) ; t.forward(gps)
    t.setheading(270) ; t.forward(gps / 2)
    t.penup()
    t.goto(xy)

    return end

'''
end = makleen(letur, 'A1', end, gps)
end = makleen(letur, 'A2', end, gps)
end = makleen(letur, 'A3', end, gps)
end = makleen(letur, 'A4', end, gps)
end = makleen(letur, 'B1', end, gps)
end = makleen(letur, 'B2', end, gps)
end = makleen(letur, 'B3', end, gps)
end = makleen(letur, 'B4', end, gps)

end = andgat(letur, 2, 3, end, gps, start)
end = exclugat(letur, 5, 7, end, gps, start, 1)

end = tobegat(letur, 1, 5, end, gps, start, 0)
#'''

#'''
x = 4

end = makleen(letur, 0, end, gps, y)
end = makleen(letur, 1, end, gps, y)

for z in range(x):
    end = makleen(letur, f'A{z}', end, gps, y)

for z in range(x):
    end = makleen(letur, f"B{z}", end, gps, y)

lear = []

end = hadder(letur, 3, 7, end, gps, start, y)
lear.append(-(end / gps))

for q in range(x - 1):
    z = q + 4
    end = fadder(letur, z, x + z, end, gps, start, y)
    lear.append(-(end / gps))

tirs = []
for z in lear:
    end = andgat(letur, 2, z, end, gps, start, 0, y)
    tirs.append(-(end / gps))

meas(letur, tirs[0], y, end, gps, start)
meas(letur, tirs[1], y, end, gps, start)
meas(letur, tirs[2], y, end, gps, start)
meas(letur, tirs[3], y, end, gps, start)

#'''

'''
end = makleen(letur, "A1", end, gps, y)
end = makleen(letur, "B1", end, gps, y)

meas(letur, 1, y, end, gps, start)

#'''


letur.setheading(0)
letur.goto(start[0] - 30, start[1] + 10)

if (input("sav ") == "yes"):
    turtle.getcanvas().postscript(file="welp.eps")

start = [-200, 150]

gps = 20

letur.penup()
letur.goto(start)
lines = 0
end = 0



def makleen(t : turtle, value : any, end : int, gps : int) -> float:
    t.penup()
    t.goto(start[0] - 5, start[1] + (end - gps))
    t.setheading(0)
    t.write(f"|{value}>", align="right")
    t.forward(5)
    t.pendown()
    x = t.ycor() - start[1]
    t.forward(gps)
    t.penup()

    return x

def blipi(t : turtle, gps : int):    
    t.pendown()
    t.back(gps / 2) ; t.setheading(270)
    t.fillcolor('blue') ; t.begin_fill()
    t.circle(gps / 2) ; t.end_fill()
    t.setheading(0) ; t.forward(gps / 2)
    t.penup()

def whynot(t : turtle, gps : int):
    t.pendown()
    t.back(gps / 2) ; t.setheading(270)
    t.circle(gps / 2)
    t.setheading(0) ; t.forward(gps) ; t.back(gps / 2)
    t.setheading(270) ; t.forward(gps / 2) ; t.back(gps)
    t.forward(gps / 2) ; t.setheading(0)
    t.penup()

def andgat(t : turtle, pos1 : int, pos2 : int, end : int, gps : int, start : list, inver : int | None = 0) -> float:
    xy = [t.xcor(), t.ycor()]
    end = makleen(t, inver, end, gps)
    t.goto(xy)

    t.penup()
    t.setheading(0)
    t.forward(gps)
    t.goto(t.xcor(), (start[1] - (pos1 * gps)))
    blipi(t, gps / 2)
    t.pendown()

    t.goto(t.xcor(), (start[1] - (pos2 * gps)))
    blipi(t, gps / 2)
    t.pendown()

    t.goto(t.xcor(), end)
    whynot(t, gps / 2)
    t.penup()

    return end

def exclugat(t : turtle, pos1 : int, pos2 : int, end : int, gps : int, start, inver : int | None = 0) -> float:
    xy = [t.xcor(), t.ycor()]
    end = makleen(t, inver, end, gps)
    t.goto(xy)

    t.penup()
    t.setheading(0)
    t.forward(gps)

    t.goto(t.xcor(), (start[1] - (pos1 * gps)))
    blipi(t, gps / 2)

    t.pendown()
    t.goto(t.xcor(), end)
    whynot(t, gps / 2)

    t.penup()
    t.forward(gps)

    t.goto(t.xcor(), (start[1] - (pos2 * gps)))
    blipi(t, gps / 2)

    t.pendown()
    t.goto(t.xcor(), end)
    whynot(t, gps / 2)

    t.penup()
    return end

def tobegat(t : turtle, pos1 : int, pos2 : int, end : int, gps : int, start, inver : int | None = 0) -> float:
    end = andgat(t, pos1, pos2, end, gps, start, 1)
    end = exclugat(t, pos1, pos2, end, gps, start, 1)
    end = andgat(t, -((end / gps) + 1), -(end / gps), end, gps, start, inver)

    return end

'''
end = makleen(letur, 'A1', end, gps)
end = makleen(letur, 'A2', end, gps)
end = makleen(letur, 'A3', end, gps)
end = makleen(letur, 'A4', end, gps)
end = makleen(letur, 'B1', end, gps)
end = makleen(letur, 'B2', end, gps)
end = makleen(letur, 'B3', end, gps)
end = makleen(letur, 'B4', end, gps)

end = andgat(letur, 2, 3, end, gps, start)
end = exclugat(letur, 5, 7, end, gps, start, 1)

end = tobegat(letur, 1, 5, end, gps, start, 0)
#'''

#'''
x = 4
for z in range(x):
    end = makleen(letur, f'A{z}', end, gps)

end = exclugat(letur, 0, 1, end, gps, start)
end = andgat(letur, 0, 1, end, gps, start)

end = exclugat(letur, 2, 3, end, gps, start)
end = andgat(letur, 2, 3, end, gps, start)
end = exclugat(letur, x + 1, x + 2, end, gps, start)
end = andgat(letur, x + 1, x + 2, end, gps, start)

end = exclugat(letur, 4, 3, end, gps, start)
end = andgat(letur, 2, 3, end, gps, start)
end = exclugat(letur, x + 1, x + 2, end, gps, start)
end = andgat(letur, x + 1, x + 2, end, gps, start)

end = exclugat(letur, 2, 3, end, gps, start)
end = andgat(letur, 2, 3, end, gps, start)
end = exclugat(letur, x + 1, x + 2, end, gps, start)
end = andgat(letur, x + 1, x + 2, end, gps, start)


#'''

letur.setheading(0)
letur.goto(start[0] - 30, start[1] + 10)
input("W ")
