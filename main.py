#GUI CLOCK
#Ver 2.0
#Amlan Saha Kundu
#=================================

import time, turtle, datetime
from turtle import *
#=================================

bgcolor("black")

#=================================
x = datetime.datetime.now()
h = x.strftime("%I")
m = x.strftime("%M")
s = x.strftime("%S")
z = x.strftime("%p")

day = x.strftime("%d")
mon = x.strftime("%b")
wday = x.strftime("%a")
wda = str(wday)+","

name = "amlan's beast"
#=================================
th = Turtle()
tm = Turtle()
ts = Turtle()
tz = Turtle()

m1 = Turtle()
m2 = Turtle()
m3 = Turtle()
m4 = Turtle()
m5 = Turtle()
m6 = Turtle()

p = Turtle()
q = Turtle()
r = Turtle()

da = Turtle()
mo = Turtle()
wd = Turtle()

nm = Turtle()

#===========================
m1.pensize(3)
m2.pensize(3)
m3.pensize(3)
m4.pensize(3)
m5.pensize(3)
m6.pensize(3)

#===========================

m1.goto(-200,0)
m1.pencolor("#ff00ff")
m1.fd(70)
m1.left(90)
m1.fd(10)
m1.pencolor("black")


m2.goto(-200,0)
m2.pencolor("blue")
m2.fd(140)
m2.left(90)
m2.fd(10)
m2.pencolor("black")

m3.goto(-200,0)
m3.pencolor("green")
m3.fd(210)
m3.left(90)
m3.fd(10)
m3.pencolor("black")

m4.goto(-200,0)
m4.pencolor("yellow")
m4.fd(280)
m4.left(90)
m4.fd(10)
m4.pencolor("black")

m5.goto(-200,0)
m5.pencolor("orange")
m5.fd(350)
m5.left(90)
m5.fd(10)
m5.pencolor("black")

m6.goto(-200,0)
m6.pencolor("#25ffff")
m6.fd(420)
m6.left(90)
m6.fd(10)
m6.pencolor("black")

m1.pencolor("black")
m2.pencolor("black")
m3.pencolor("black")
m4.pencolor("black")
m5.pencolor("black")
m6.pencolor("black")

#===========================

th.goto(-150,10)
tm.goto(20,100)
ts.goto(20,40)
tz.goto(100,40)

p.goto(-200,-20)
q.goto(-200,-40)
r.goto(-200,-60)

wd.goto(-150,-150)
mo.goto(-30,-150)
da.goto(80,-150)

nm.goto(-150,-220)

#============================
th.pencolor("#bbfbbb")
tm.pencolor("#aafaaa")
ts.pencolor("#99f999")
tz.pencolor("#bbbbbb")

wd.pencolor("#bbbbbb")
mo.pencolor("#ffbbff")
da.pencolor("#ffbbff")

nm.pencolor("orange")
#=============================
th.ht()
tm.ht()
ts.ht()
tz.ht()

wd.ht()
da.ht()
mo.ht()
nm.ht()
#===========================

wd.write(wda, font=("Nasalization Rg",40))
mo.write(mon, font=("Nasalization Rg",40))
da.write(day, font=("Nasalization Rg",40))
nm.write(name, font=("Nasalization Rg",32))


i=int(s)+9
j=int(m)
k=int(h)


p.pensize(10)
q.pensize(10)
r.pensize(10)
p.color("#ff0000")
q.color("#ffff00")
r.color("#00ff00")

tempp = i*7
p.fd(tempp)
tempq = j*7
q.fd(tempq)
tempr = k*35
r.fd(tempr)
colormode = 1
while i<61:
    
    if i<10:
        i1 = "0"+str(i)
    else:
        i1 = str(i)
    if j<10:
        j1 = "0"+str(j)
    else:
        j1 = str(j)
    k1 = k
    if k <10:
        th.goto(-100,10)
    else:
        th.goto(-150,10)
    th.write(str(k1), font=("Nasalization Rg",120))
    tm.write(str(j1), font=("Nasalization Rg",50))
    ts.write(str(i1), font=("Nasalization Rg",40))
    tz.write(str(z), font=("Nasalization Rg",30))
    #==================================
    p.pensize(10)
    q.pensize(10)
    r.pensize(10)
    p.color("#ff0000")
    q.color("#ffff00")
    r.color("#00ff00")

    #========================================================

    if i >= 10:
        m1.pencolor("white")
        
    if i >= 20:
        m2.pencolor("white")

    if i >= 30:
        m3.pencolor("white")

    if i >= 40:
        m4.pencolor("white")
        
    if i >= 50:
        m5.pencolor("white")
        
    
    #========================================================
    if colormode%3 == 1:
        th.pencolor("#bbfbbb")
        tm.pencolor("#aafaaa")
        ts.pencolor("#99f999")
    elif colormode%3 == 2:
        th.pencolor("#fbbbbb")
        tm.pencolor("#faaaaa")
        ts.pencolor("#f99999")
    elif colormode%3 == 0:
        th.pencolor("#bbbbfb")
        tm.pencolor("#aaaafa")
        ts.pencolor("#9999f9")
    time.sleep(0.745)
    i+=1
    p.fd(7)
    if i ==60:
        i = 0
        j += 1
        p.clear()
        p.color("black")
        p.goto(-200,-20)
        q.fd(7)
        m1.pencolor("black")
        m2.pencolor("black")
        m3.pencolor("black")
        m4.pencolor("black")
        m5.pencolor("black")
        m6.pencolor("black")
        
        
    if j == 60:
        k += 1
        j = 0
        q.clear()
        q.color("black")
        q.goto(-200,-40)
        r.fd(35)
        
    if k > 12:
        k = 1
        r.clear()
        r.color("black")
        r.goto(-200,-60)
    elif k == 11 and j==59 and i==59:
        if z == "AM":
            z = "PM"
        elif z == "PM":
            z = "AM"
        
    ts.clear()
    tm.clear()
    th.clear()
    tz.clear()
    colormode += 1
    
    
