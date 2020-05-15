import turtle as tl

def writer(text='coterie'):
    tl.setworldcoordinates(-1000.,-1000.,1000.,1000.)
    tl.shape('turtle')
    tl.color('white')
    tl.pen(pencolor = 'black', pensize = 5)
    tl.penup()
    ycrd = 0
    xcrd = -450
    text = str(text)
    text = text.lower()
    for i in text:
        if i is 'c':
            tl.goto(xcrd,ycrd)
            tl.pendown()
            tl.right(90)
            tl.forward(70)
            tl.left(90)
            tl.forward(70)
            tl.left(90)
            tl.penup()
            tl.forward(70)
            tl.pendown()
            tl.left(90)
            tl.forward(70)
            tl.penup()
            tl.right(180)
            xcrd += 120
            ycrd -= 0
        
        if i is 'o':
            tl.goto(xcrd,ycrd)
            tl.pendown()
            tl.right(90)
            tl.forward(70)
            tl.left(90)
            tl.forward(70)
            tl.left(90)
            tl.forward(70)
            tl.left(90)
            tl.forward(70)
            tl.penup()
            tl.right(180)
            xcrd += 120
            ycrd -= 0
            
        if i is 't':
            tl.goto(xcrd+70,ycrd)
            tl.pendown()
            tl.right(180)
            tl.forward(35)
            tl.left(90)
            tl.forward(70)
            tl.left(180)
            tl.forward(70)
            tl.left(90)
            tl.forward(35)
            tl.penup()
            tl.right(180)
            xcrd += 120
            ycrd -= 0
            
        if i is 'e':
            tl.goto(xcrd,ycrd)
            tl.pendown()
            tl.right(90)
            tl.forward(70)
            tl.left(90)
            tl.forward(70)
            tl.penup()
            tl.left(90)
            tl.forward(35)
            tl.pendown()
            tl.left(90)
            tl.forward(70)
            tl.right(90)
            tl.forward(35)
            tl.right(90)
            tl.forward(70)
            tl.penup()
            xcrd += 120
            ycrd -= 0
        if i is 'i':
            tl.goto(xcrd+35,ycrd)
            tl.pendown()
            tl.right(90)
            tl.forward(10)
            tl.penup()
            tl.forward(20)
            tl.pendown()
            tl.forward(40)
            tl.right(180)
            tl.penup()
            tl.forward(70)
            tl.right(90)
            xcrd += 120
            ycrd -= 0
        if i is 'r':
            tl.goto(xcrd+35,ycrd)
            tl.pendown()
            tl.right(90)
            tl.forward(70)
            tl.right(180)
            tl.forward(70)
            tl.right(90)
            tl.forward(50)
            tl.right(180)
            tl.forward(30)
            tl.right(180)
            tl.penup()
            xcrd += 120
            ycrd -= 0
        else:
            pass
    print(tl.position())