from ProgramskeDatoteke import pripraviHTML
from tkinter import *
import webbrowser
import os
from tkinter.filedialog import askopenfilename

# dober tutorial za tkinter:
#     https://likegeeks.com/python-gui-examples-tkinter-tutorial/

window = Tk()
window.title("Priprava na sveto maso (MPP)")
window.geometry('650x200')

upFrame = Frame(window)
upFrame.grid(column=0, row=0)
frame = Frame(upFrame)   # to okno je znotraj zgornjega
frame.grid(column=1, row=4)
downFrame = Frame(window)
downFrame.grid(column=0, row=2)

txt = Label(upFrame, text="Vpisi datum oblike DD.MM.LLLL:", font=("Arial Bold", 10))
txt.grid(column=0, row=0)
datum = Entry(upFrame, width=30)
datum.grid(column=1, row=0)

txt2 = Label(upFrame, text="Naslov razmisljanja:", font=("Arial Bold", 10))
txt2.grid(column=0, row=1)
naslov = Entry(upFrame, width=30)
naslov.grid(column=1, row=1)

txt3 = Label(upFrame, text="Razmisljanje (v HTML5):", font=("Arial Bold", 10))
txt3.grid(column=0, row=2)
razmisljanje = Entry(upFrame, width=70)
razmisljanje.grid(column=1, row=2)

txt4 = Label(upFrame, text="Avtor razmisljanja:", font=("Arial Bold", 10))
txt4.grid(column=0, row=3)
avtor = Entry(upFrame, width=30)
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
    if imedatoteke in os.listdir("izdelanePriprave"):
        # tu odpre okno z opozorilom, da ta datoteka ze obstaja
        # ce "naredi novo" naredi novo, sicer ne naredi nic oz. vrni ze narejeno stran
        pozor = Tk()
        pozor.title("Opozorilo")
        pozor.geometry('225x70')
        op = Label(pozor, text="Pozor, datoteka ze obstaja!\nZelis zamenjati staro datoteko z novo?",
                   font=("Arial Bold", 10))
        op.grid(column=0, row=0)
        fr = Frame(pozor)
        fr.grid(column=0, row=1)
        da = Button(fr, text="DA", bg="red", fg="orange", command=pozor.destroy)
        da.grid(column=0, row=0)
        ne = Button(fr, text="NE", bg="red", fg="orange", command=pozor.destroy)
        ne.grid(column=1, row=0)
        sporocilo.configure(text="Stran za ta datum ze obstaja,\nprogram se ne razume vase izbire.")
        return ""
    html = pripraviHTML.pripravi_html(dan, title, text, author)
    sporocilo.configure(text="Uspesno ste ustvarili stran\ns pripravo za datum: "+dan)
    return html


def pripravi_in_odpri():
    webbrowser.open(pripravi())


prip = Button(frame, text="Pripravi stran", bg="orange", fg="blue", command=pripravi)
prip.grid(column=0, row=0)
odpr = Button(frame, text="Pripravi in odpri", bg="orange", fg="red", command=pripravi_in_odpri)
odpr.grid(column=1, row=0)
staro = Button(upFrame, text="Odpri ze pripravljeno", bg="orange", fg="black", command=odpri)
staro.grid(column=1, row=5)

window.mainloop()
