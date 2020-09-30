# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 11:40:09 2020

@author: Mansi
"""



from tkinter import *

import tkinter.messagebox

tk= Tk()

tk.title("TIC TAC TOE")

click = True

def check(buttons):
    if((button1["text"]=="X" and button2["text"]=="X" and button3["text"]=="X") or
            (button4["text"]=="X" and button5["text"]=="X" and button6["text"]=="X")or
            (button7["text"]=="X" and button8["text"]=="X" and button9["text"]=="X")or
            (button1["text"]=="X" and button4["text"]=="X" and button7["text"]=="X")or
            (button8["text"]=="X" and button2["text"]=="X" and button5["text"]=="X")or
            (button9["text"]=="X" and button6["text"]=="X" and button3["text"]=="X")or
            (button1["text"]=="X" and button5["text"]=="X" and button9["text"]=="X")or
            (button7["text"]=="X" and button5["text"]=="X" and button3["text"]=="X")):
        
        tkinter.messagebox.showinfo("Winner is X","You have won this round!")
        
    
    elif((button1["text"]=="O" and button2["text"]=="O" and button3["text"]=="O") or
            (button4["text"]=="O" and button5["text"]=="O" and button6["text"]=="O")or
            (button7["text"]=="O" and button8["text"]=="O" and button9["text"]=="O")or
            (button1["text"]=="O" and button4["text"]=="O" and button7["text"]=="O")or
            (button8["text"]=="O" and button2["text"]=="O" and button5["text"]=="O")or
            (button9["text"]=="O" and button6["text"]=="O" and button3["text"]=="O")or
            (button1["text"]=="O" and button5["text"]=="O" and button9["text"]=="O")or
            (button7["text"]=="O" and button5["text"]=="O" and button3["text"]=="O")):
        
        tkinter.messagebox.showinfo("Winner is O","You have won this round!")
        
    else:
        draw(buttons)
        
def restart(buttons):
    button1["text"]=" "
    button2["text"]=" "
    button3["text"]=" "
    button4["text"]=" "
    button5["text"]=" "
    button6["text"]=" "
    button7["text"]=" "
    button8["text"]=" "
    button9["text"]=" "

def draw(buttons):
        if button1["text"]!=" " and button2["text"]!=" " and  button3["text"]!=" " and button4["text"]!=" " and  button5["text"]!=" " and  button6["text"]!=" " and  button7["text"]!=" " and button8["text"]!=" " and button9["text"]!=" " :
            tkinter.messagebox.showinfo("DRAW","IT IS A DRAW.")
    

def checker(buttons):
    
    global click
    
    if(buttons["text"]==" " and click == True ):
        buttons["text"]="X"
        click= False
        
    elif(buttons["text"]==" " and click == False ):
        buttons["text"]="O"
        click= True

    check(buttons)
       
        
        
buttons =StringVar()
checks = Button(tk,text = "RESTART ",font =' Helvetica 10 bold italic', height =3, width = 8 ,bg='#54FA9B',command =lambda:restart(buttons))
checks.grid(row= 0 ,column = 1)                

button1 = Button(tk,text=" ", font =' Helvetica 28 bold italic', height =3, width =  3,bg='#54FA9B', command =lambda:checker(button1))
button1.grid(row=1,column =0 ,sticky = S + N + E + W)


button2 = Button(tk,text=" ", font =' Helvetica 28 bold italic', height =3, width = 3 ,bg='#54FA9B', command =lambda:checker(button2))
button2.grid(row=1,column =1 ,sticky = S + N + E + W)

button3 = Button(tk,text=" ", font =' Helvetica 28 bold italic', height =3, width = 3 ,bg='#54FA9B', command =lambda:checker(button3))
button3.grid(row=1,column =2 ,sticky = S + N + E + W)

button4 = Button(tk,text=" ", font =' Helvetica 28 bold italic', height =3, width = 3 ,bg='#54FA9B', command =lambda:checker(button4))
button4.grid(row=2,column =0 ,sticky = S + N + E + W)

button5 = Button(tk,text=" ", font =' Helvetica 28 bold italic', height =3, width = 3 ,bg='#54FA9B', command =lambda:checker(button5))
button5.grid(row=2,column =1 ,sticky = S + N + E + W)

button6 = Button(tk,text=" ", font =' Helvetica 28 bold italic', height =3, width = 3 ,bg='#54FA9B', command =lambda:checker(button6))
button6.grid(row=2,column =2 ,sticky = S + N + E + W)

button7 = Button(tk,text=" ", font =' Helvetica 28 bold italic', height =3, width = 3 ,bg='#54FA9B', command =lambda:checker(button7))
button7.grid(row=3,column =0 ,sticky = S + N + E + W)

button8 = Button(tk,text=" ", font =' Helvetica 28 bold italic', height =3, width = 3 ,bg='#54FA9B', command =lambda:checker(button8))
button8.grid(row=3,column =1 ,sticky = S + N + E + W)

button9 = Button(tk,text=" ", font =' Helvetica 28 bold italic', height =3, width = 3 ,bg='#54FA9B', command =lambda:checker(button9))
button9.grid(row=3,column =2 ,sticky = S + N + E + W)


    
    
tk.mainloop()
