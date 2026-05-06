import turtle

letur = turtle.Turtle()
letur.width(1)

#start = [-900, 510]
start = [-50, 510]
color = 'white'
letur.fillcolor(color)
letur.color(color)
turtle.Screen().bgcolor('black')
turtle.Screen().tracer(0, 0)
#letur.fillcolor('blue')
#letur.color("blue")

y = start[0] * -2
gps = 20

letur.penup()
letur.goto(start)
lines = 0
end = 0
letur.speed(0)


def makleen(t : turtle, value : any, end : int, gps : int, leenlen : float | None = gps) -> float:
    t.penup()
    oc = [t.xcor(), t.ycor()]
    t.goto(start[0] - 5, start[1] + (end - gps) - (gps / 2))
    t.setheading(0)
    t.write(f"{int(1 - (end / gps))}  |{value}>", align="right", font=("Arial", int(gps / 2), "normal"))
    t.goto(start[0], start[1] + (end - gps))
    t.pendown()
    x = t.ycor() - start[1]
    t.forward(leenlen)
    t.back(leenlen - gps)
    t.penup()
    t.goto(oc)
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

    t.penup()
    t.setheading(0)
    t.goto(t.xcor(), (start[1] - (pos1 * gps)))
    blipi(t, gps / 2)
    t.pendown()
    t.goto(t.xcor(), (start[1] - (pos2 * gps)))
    blipi(t, gps / 2)
    t.pendown()
    t.goto(t.xcor(), start[1] + end)
    whynot(t, gps / 2)
    t.forward(gps)

    t.goto(t.xcor(), (start[1] - (pos2 * gps)))
    blipi(t, gps / 2)
    t.pendown()
    t.goto(t.xcor(), start[1] + end)
    whynot(t, gps / 2)

    return end

def fadder(t : turtle, pos1 : int, pos2 : int, end : int, gps : int, start, leenlen : float | None = gps, cin : int | None = -1) -> float:
    if bool(cin != -1):
        end = exclugat(t, pos1, pos2, end, gps, start, 0, leenlen)
        end = andgat(t, pos1, pos2, end, gps, start, 0, leenlen)

        end = exclugat(t, (-(end) / gps) - 1, cin, end, gps, start, 0, leenlen)
        end = andgat(t, (-(end) / gps) - 2, cin, end, gps, start, 0, leenlen)

        end = tobegat(t, (-(end) / gps) - 2, (-(end) / gps), end, gps, start, 0, leenlen)
    else:
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

        for q in range(x - 2):
            end = fadder(letur, pos1[q + 1], pos2[q + 1], end, gps, start, leenlen)
        
        end = exclugat(letur, pos1[x - 1], pos2[x - 1], end, gps, start, 0, leenlen)
        end = andgat(letur, pos1[x - 1], pos2[x - 1], end, gps, start, 0, leenlen)

        end = exclugat(letur, (-(end) / gps) - 1, cof, end, gps, start, 0, leenlen)
        end = andgat(letur, (-(end) / gps) - 2, cof, end, gps, start, 0, leenlen)

        end = tobegat(letur, (-(end) / gps) - 2, (-(end) / gps), end, gps, start, 0, leenlen)

        return end
    
    else:
        end = hadder(letur, pos1[0], pos2[0], end, gps, start, leenlen)

        for q in range(x - 1):
            end = fadder(letur, pos1[q + 1], pos2[q + 1], end, gps, start, leenlen)

        return end

def retriv(letur : turtle, fact : int, gps : int, invert : int):
    letur.penup()
    if bool(invert == 0) : letur.goto(letur.xcor() - (gps * fact), letur.ycor())
    elif bool(invert == 1) : letur.goto(letur.xcor() + (gps * fact), letur.ycor())
    letur.pendown()


#This is where I inserted commands to be run
#'''
end = makleen(letur, 'A1', end, gps, y)
end = makleen(letur, 'B1', end, gps, y)
end = andgat(letur, 1, 2, end, gps, start, 0, y)
retriv(letur, 1, gps, 0)
end = andgat(letur, 5, 6, end, gps, start, 0, y)
end = makleen(letur, 'A2', end, gps, y)
end = makleen(letur, 'B2', end, gps, y)
meas(letur, 3, y, end, gps, start)
meas(letur, 4, y, end, gps, start)
#'''

letur.setheading(0)
letur.goto(start[0] - 30, start[1] + 10)
turtle.update()

if (input("sav ") == "yes") : turtle.getcanvas().postscript(file="welp.eps")
    
