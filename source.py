from distutils import command
from tkinter import *
window =Tk()
window.attributes("-fullscreen",TRUE)
window.title("MathLearn.exe")
window.configure(bg='#7FC1F9')
def language(lang='en'):
  #window.configure(width=500,height=300)
  menu=Menu(window)
  window.config(menu=menu)
  languagemenu=Menu(menu,font="Arial 15", background='#2E64FE',
  foreground='white',activebackground='aqua',
  activeforeground='black',relief=GROOVE,tearoff=0)
  filemenu=Menu(menu,font="Arial 15", background='#2E64FE',
  foreground='white',activebackground='aqua',
  activeforeground='black',relief=GROOVE,tearoff=0)
  if(lang=='ro'):
    menu.selection_clear
    menu.add_cascade(label="Fișier",menu=filemenu)
    filemenu.add_command(label="Închidere",command=window.destroy)
    menu.add_cascade(label="Limbă",menu=languagemenu)
    languagemenu.add_command(label="Română",command=lambda: language("ro"))
    languagemenu.add_command(label="English",command=lambda: language('en'))
    languagemenu.add_command(label="中国人",command=lambda: language('ch'))
  if(lang=='en'):
    menu.add_cascade(label="File",menu=filemenu)
    filemenu.add_command(label="Exit",command=window.destroy)
    menu.add_cascade(label="Language",menu=languagemenu)
    languagemenu.add_command(label="English",command=lambda: language('en'))
    languagemenu.add_command(label="Română",command=lambda: language("ro"))
    languagemenu.add_command(label="中国人",command=lambda: language('ch'))
  if(lang=='ch'):
    menu.add_cascade(label="文件",menu=filemenu)
    filemenu.add_command(label="出口",command=window.destroy)
    menu.add_cascade(label="语言",menu=languagemenu)
    languagemenu.add_command(label="中国人",command=lambda: language('ch')) 
    languagemenu.add_command(label="English",command=lambda: language('en'))
    languagemenu.add_command(label="Română",command=lambda: language("ro"))   
  window.mainloop()


language()



  
