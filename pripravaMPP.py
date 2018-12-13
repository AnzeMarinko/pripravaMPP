from Program import pripravaPROGRAM
from tkinter import *

 # https://likegeeks.com/python-gui-examples-tkinter-tutorial/
 # https://docs.python.org/3/library/tkinter.html
window = Tk()
window.title("Priprava na sveto mašo (MPP)")
window.geometry('900x500')
lbl = Label(window, text="Vpiši datum oblike DD.MM.LLLL:", font=("Arial Bold", 12))
lbl.grid(column=0, row=0)
txt = Entry(window,width=10)  # lahko onemogočiš: state='disabled'
txt.grid(column=1, row=0)
txt.focus()
html = Label(window, text="")
html.grid(column=0, row=1)
def clicked():
    datum = txt.get() # niz podan v okencu ob pritisku na gumb
    lbl.configure(text="Vnešeni datum: "+datum+"; Vnesi nov datum oblike DD.MM.LLLL:")
    nova_stran = pripravaPROGRAM.pripraviHTML(datum)
    html.configure(text=nova_stran)
btn = Button(window, text="Click Me", bg="orange", fg="red", command=clicked)
btn.grid(column=2, row=0)
window.mainloop()
