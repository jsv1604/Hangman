from tkinter import *
from tkinter import messagebox
from  string import ascii_uppercase


window= Tk()
window.title("Hangman")



photos = [PhotoImage(file="a.png"),PhotoImage(file="b.png"),PhotoImage(file="c.png"),PhotoImage(file="d.png"),
          PhotoImage(file="e.png"),PhotoImage(file="f.png"),PhotoImage(file="g.png"),PhotoImage(file="h.png")]

def newGame():
        print("SCREEN FOR PLAYER 1: ")
        print()
        word=input("Enter a word: ")
        global clue
        clue=input("Enter the clue: ")
        global the_word_withSpaces
        global numberOfGuesses
        numberOfGuesses = 0
        imgLabel.config(image=photos[0])
        the_word=word.upper()
        the_word_withSpaces=" ".join(the_word)
        lblWord.set(" ".join("_"*len(the_word)))

                        

def guess(letter):
    global numberOfGuesses
    if numberOfGuesses<7:
        txt=list(the_word_withSpaces)
        guessed=list(lblWord.get())
        if the_word_withSpaces.count(letter)>0:
            for c in range(len(txt)):
                if txt[c]==letter:
                    guessed[c]=letter
                lblWord.set("".join(guessed))
                if lblWord.get()==the_word_withSpaces:
                    messagebox.showinfo("Hangman","WE HAVE A WINNER")
                    
        else:
            numberOfGuesses+=1
            imgLabel.config(image=photos[numberOfGuesses])
            if numberOfGuesses==7:
                messagebox.showwarning("Hangman","Game Over")
                
Label(text="Do you want a hint?").grid(row=0,column=2)
b=Button(text="Yes",command=lambda: hint())
b.grid(row=0,column=3)
def hint():
        l=Label(text="Clue: \n"+clue)
        l.grid(row=0,column=4)
        
    

imgLabel=Label(window)
imgLabel.grid(row=0,column=0,padx=10,pady=40)
imgLabel.config(image=photos[0])

lblWord=StringVar()
Label(window, textvariable =lblWord).grid(row=0,column=3,columnspan=9,padx=10)

n=0
for c in ascii_uppercase:
    Button(window,text=c,command=lambda c=c:guess(c),width=10).grid(row=1+n//9,column=((n)%9)+1)
    n+=1

Button(window,text="New\nGame",command=lambda:newGame()).grid(row=3,column=9,sticky="NSWE")
Label(text="SCREEN FOR PLAYER 2", fg="red").grid(row=1,column=0)
newGame()
window.mainloop()
