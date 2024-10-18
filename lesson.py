# import turtle 
 
# t=turtle.Turtle() 
# s=turtle.Screen() 
# s.bgcolor('#000000') 
# t.speed(10) 
 
# for _ in range(36): 
#     t.pencolor("red") 
#     t.circle(100) 
#     t.left(10) 
 
# turtle.done() 
 
# import turtle 
 
# st=turtle.Screen() 
# st.setup(630, 700, startx=400, starty=0) 
# t=turtle.Turtle() 
# s=turtle.Screen() 
# s.bgcolor("black") 
# t.pencolor("red") 
# a=0 
# b=0 
# t.speed(0) 
# t.penup() 
# t.goto(0, 150) 
# t.pendown() 
 
# while(True): 
#     t.forward(a) 
#     t.right(b) 
#     a+=3 
#     b+=1 
#     if b==204: 
#         break 
#     t.hideturtle() 
# turtle.done()     
 
 
import turtle as t 
 
t.speed(0) 
t.setpos(70, 0) 
t.bgcolor("black") 
 
for i in range(126): 
    t.fd(i) 
    t.rt(250) 
    t.color("#059900") 
    for a in range(3): 
        t.fd(i) 
        t.lt(40) 
        t.circle(50,30) 
        t.hideturtle() 
 
 
t.done()




