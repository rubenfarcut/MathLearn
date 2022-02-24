from distutils import command
from tkinter import *



window =Tk()
window.attributes("-fullscreen",TRUE)
window.title("MathLearn.exe")
#window.configure(width=500,height=300)
window.configure(bg='#7FC1F9')

menu=Menu(window)
window.config(menu=menu)

filemenu=Menu(menu,font="Arial 15", background='#2E64FE',
 foreground='white',activebackground='aqua',
  activeforeground='black',relief=GROOVE,tearoff=0)
menu.add_cascade(label="Fișier",menu=filemenu)

filemenu.add_command(label="Închidere",command=window.destroy)



window.mainloop()
