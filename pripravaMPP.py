from Program import pripravaPROGRAM
from tkinter import *
import webbrowser

# dober tutorial za tkinter:
#     https://likegeeks.com/python-gui-examples-tkinter-tutorial/

window = Tk()
window.title("Priprava na sveto mašo (MPP)")
window.geometry('500x150')

upFrame = Frame(window)
upFrame.grid(column=0, row=0)
frame = Frame(upFrame)   # to okno je znotraj zgornjega
frame.grid(column=1, row=3)
downFrame = Frame(window)
downFrame.grid(column=0, row=2)

txt = Label(upFrame, text="Vpiši datum oblike DD.MM.LLLL:", font=("Arial Bold", 10))
txt.grid(column=0, row=0)
datum = Entry(upFrame, width=10)  # lahko onemogočiš: state='disabled'
datum.grid(column=1, row=0)

txt2 = Label(upFrame, text="Vpiši naslov razmišljanja:", font=("Arial Bold", 10))
txt2.grid(column=0, row=1)
naslov = Entry(upFrame, width=10)  # lahko onemogočiš: state='disabled'
naslov.grid(column=1, row=1)

txt3 = Label(upFrame, text="Vpiši razmišljanje (v HTML5):", font=("Arial Bold", 10))
txt3.grid(column=0, row=2)
razmisljanje = Entry(upFrame, width=50)  # lahko onemogočiš: state='disabled'
razmisljanje.grid(column=1, row=2)

sporocilo = Label(downFrame, text="", font=("Arial Bold", 12))
sporocilo.grid(column=0, row=0)


def pripravi():
    dan = datum.get()   # niz podan v okencu ob pritisku na gumb
    title = naslov.get()
    text = razmisljanje.get()
    sporocilo.configure(text="Uspešno ste ustvarili stran\ns pripravo za datum: "+dan)
    return pripravaPROGRAM.pripravi_html(dan, title, text)


def pripravi_in_odpri():
    webbrowser.open(pripravi())


prip = Button(frame, text="Pripravi stran", bg="orange", fg="blue", command=pripravi)
prip.grid(column=0, row=0)
odpr = Button(frame, text="Pripravi in odpri", bg="orange", fg="red", command=pripravi_in_odpri)
odpr.grid(column=1, row=0)

window.mainloop()
