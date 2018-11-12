from Program import pripravaPROGRAM
from tkinter import *
import webbrowser
import os
from tkinter.filedialog import askopenfilename

# dober tutorial za tkinter:
#     https://likegeeks.com/python-gui-examples-tkinter-tutorial/

window = Tk()
window.title("Priprava na sveto mašo (MPP)")
window.geometry('500x200')

upFrame = Frame(window)
upFrame.grid(column=0, row=0)
frame = Frame(upFrame)   # to okno je znotraj zgornjega
frame.grid(column=1, row=4)
downFrame = Frame(window)
downFrame.grid(column=0, row=2)

txt = Label(upFrame, text="Vpiši datum oblike DD.MM.LLLL:", font=("Arial Bold", 10))
txt.grid(column=0, row=0)
datum = Entry(upFrame, width=10)
datum.grid(column=1, row=0)

txt2 = Label(upFrame, text="Naslov razmišljanja:", font=("Arial Bold", 10))
txt2.grid(column=0, row=1)
naslov = Entry(upFrame, width=10)
naslov.grid(column=1, row=1)

txt3 = Label(upFrame, text="Razmišljanje (v HTML5):", font=("Arial Bold", 10))
txt3.grid(column=0, row=2)
razmisljanje = Entry(upFrame, width=50)
razmisljanje.grid(column=1, row=2)

txt4 = Label(upFrame, text="Avtor razmišljanja:", font=("Arial Bold", 10))
txt4.grid(column=0, row=3)
avtor = Entry(upFrame, width=10)
avtor.grid(column=1, row=3)

sporocilo = Label(downFrame, text="", font=("Arial Bold", 12))
sporocilo.grid(column=0, row=0)


def odpri(filename=""):
    if filename == "":
        Tk().withdraw()
        filename = askopenfilename(initialdir="{}/izdelanePriprave".format(os.getcwd()))
    webbrowser.open(filename)


def pripravi():
    dan = datum.get()   # niz podan v okencu ob pritisku na gumb
    title = naslov.get()
    text = razmisljanje.get()
    author = avtor.get()
    imedatoteke = "{}-{}-{}.html".format(dan[8:10], dan[3:5], dan[0:2])
    if imedatoteke not in os.listdir("izdelanePriprave"):
        html = pripravaPROGRAM.pripravi_html(dan, title, text, author)
        sporocilo.configure(text="Uspešno ste ustvarili stran\ns pripravo za datum: "+dan)
        return html
    else:
        # tu odpre okno z opozorilom, da ta datoteka že obstaja
        # ce "naredi novo" naredi novo, sicer ne naredi nic oz. vrni ze narejeno stran
        return ""


def pripravi_in_odpri():
    webbrowser.open(pripravi())


prip = Button(frame, text="Pripravi stran", bg="orange", fg="blue", command=pripravi)
prip.grid(column=0, row=0)
odpr = Button(frame, text="Pripravi in odpri", bg="orange", fg="red", command=pripravi_in_odpri)
odpr.grid(column=1, row=0)
staro = Button(upFrame, text="Odpri že pripravljeno", bg="orange", fg="black", command=odpri)
staro.grid(column=1, row=5)

window.mainloop()
