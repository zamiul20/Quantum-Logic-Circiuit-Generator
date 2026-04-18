import turtle

letur = turtle.Turtle()
letur.width(1)

start = [-920, 500]
color = 'white'
letur.fillcolor(color)
letur.color(color)
turtle.Screen().bgcolor('black')
turtle.Screen().tracer(0, 0)
#letur.fillcolor('blue')
#letur.color("blue")

y = 1850
gps = 8

letur.penup()
letur.goto(start)
lines = 0
end = 0
letur.speed(0)


def makleen(t : turtle, value : any, end : int, gps : int, leenlen : float | None = gps) -> float:
    t.penup()
    t.goto(start[0] - 5, start[1] + (end - gps))
    t.setheading(0)
    t.write(f"|{value}>", align="right", font=("Arial", int(gps / 2), "normal"))
    t.forward(5)
    t.pendown()
    x = t.ycor() - start[1]
    t.forward(leenlen)
    t.back(leenlen - gps)
    t.penup()

    return x

def blipi(t : turtle, gps : int):
    x = gps / 2
    t.pendown()
    t.back(x) ; t.setheading(270)
    t.begin_fill()
    t.circle(x) ; t.end_fill()
    t.setheading(0) ; t.forward(x)
    t.penup()

def whynot(t : turtle, gps : int):
    x = gps / 2
    t.pendown()
    t.width(1)
    t.back(x) ; t.setheading(270)
    t.circle(x)
    t.setheading(0) ; t.forward(gps) ; t.back(x)
    t.setheading(270) ; t.forward(x) ; t.back(gps)
    t.forward(x) ; t.setheading(0)
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
    if bool(inver == 1):
        end = andgat(t, (-(end / gps) - 1), -(end / gps), end, gps, start, 0, leenlen)
    if bool(inver == 0):
        end = andgat(t, (-(end / gps) - 1), -(end / gps), end, gps, start, 1, leenlen)

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

def widder(letur : turtle, pos1 : list, pos2 : list, follow : int, x : int, end : int, gps : int, start, leenlen : float | None = gps):
    if bool(follow == 1):
        cof = -(end / gps)
        end = hadder(letur, pos1[0], pos2[0], end, gps, start, leenlen)
        ste = -(end / gps) - 1

        for q in range(x - 2):
            end = fadder(letur, pos1[q + 1], pos2[q + 1], end, gps, start, leenlen)
        
        end = exclugat(letur, pos1[x - 1], pos2[x - 1], end, gps, start, 0, leenlen)
        end = andgat(letur, pos1[x - 1], pos2[x - 1], end, gps, start, 0, leenlen)

        end = exclugat(letur, (-(end) / gps) - 1, cof, end, gps, start, 0, leenlen)
        end = andgat(letur, (-(end) / gps) - 2, cof, end, gps, start, 0, leenlen)

        end = tobegat(letur, (-(end) / gps) - 2, (-(end) / gps), end, gps, start, 0, leenlen)

        end = andgat(letur, 2, ste, end, gps, start, 0, leenlen)
        for z in range(x - 1):
            end = andgat(letur, 2, ste + (7 * (z + 1)) - 3, end, gps, start, 0, leenlen)

        return end
    
    else:
        end = hadder(letur, pos1[0], pos2[0], end, gps, start, leenlen)
        ste = -(end / gps) - 1

        for q in range(x - 1):
            end = fadder(letur, pos1[q + 1], pos2[q + 1], end, gps, start, leenlen)

        end = andgat(letur, 2, ste, end, gps, start, 0, leenlen)
        for z in range(x - 1):
            end = andgat(letur, 2, ste + (7 * (z + 1)) - 3, end, gps, start, 0, leenlen)

        return end

#This is where I inserted commands to be run
#'''
end = makleen(letur, 1, end, gps, y)
end = makleen(letur, 0, end, gps, y)

end = tobegat(letur, 1, 2, end, gps, start, 0, y)
#'''


letur.setheading(0)
letur.goto(start[0] - 30, start[1] + 10)
turtle.update()

if (input("sav ") == "yes") : turtle.getcanvas().postscript(file="welp.eps")
