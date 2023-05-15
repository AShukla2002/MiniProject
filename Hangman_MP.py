from tkinter import *
from tkinter import messagebox as mssg
from string import ascii_uppercase as upp
import random

root = Tk()
root.title("Hangman")
root.resizable(0,0)
root.counter=0

wList = ["UMBRELLA","WINDOW","DESKTOP","MIRROR",'LEOPARD','PHOTOGRAPH','MICROWAVE','ABYSS','BLIZZARD','WHICHCRAFT','ZOMBIE','FISHHOOK','OXYGEN']

img = [PhotoImage(file='images/hang0.png'),PhotoImage(file='images/hang1.png'),PhotoImage(file='images/hang2.png'),PhotoImage(file='images/hang3.png'),
       PhotoImage(file='images/hang4.png'),PhotoImage(file='images/hang5.png'),PhotoImage(file='images/hang6.png'),PhotoImage(file='images/hang7.png')]

def nGame():
    global word_s
    global nguess
    nguess = 0
    l1.config(image = img[0])
    wrd = random.choice(wList)
    word_s = " ".join(wrd)
    lblwrd.set(" ".join("_"*len(wrd)))

def guess(letter):
    global nguess
    if nguess < 7:
        txt = list(word_s)
        guessed = list(lblwrd.get())
        if (word_s.count(letter) > 0):
            for ch in range(len(txt)):
                if txt[ch] == letter:
                    guessed[ch] = letter
                lblwrd.set("".join(guessed))
                if lblwrd.get() == word_s:
                    mssg.showinfo('Hangman','You Guessed it!')
        else:
            nguess+=1
            l1.config(image = img[nguess])
    if nguess == 7:
        mssg.showwarning('Hangman','Game Over!!!')

l1 = Label(root)
l1.grid(row = 0,column = 0,columnspan = 3,padx = 10,pady = 40)
l1.config(image = img[0])

lblwrd = StringVar()
Label(root,textvariable = lblwrd,font = ('Consolas 20 bold')).grid(row = 0,column = 3,columnspan = 6,padx = 10)

n=0
for a in upp:
    Button(root,text = a,bg = 'black', command = lambda a=a:guess(a),fg='yellow',width = 4,relief = 'groove',font = ('Consolas 18')).grid(row = 1+n//9,column=n%9)
    n+=1

menu = Menu(root)
root.config(menu=menu)
opt = Menu(menu)
menu.add_cascade(label = 'Options',menu = opt)
opt.add_command(label="New Game",command=nGame())
opt.add_separator()
opt.add_command(label="Close Game",command=root.destroy)

Button(root,text = 'New\nGame',bg = 'yellow',fg = 'black',command = lambda:nGame(), font = ('Consolas 10')).grid(row = 3,column = 8,sticky = 'NSWE')

nGame()
root.mainloop()
