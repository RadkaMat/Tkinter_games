# -*- coding: UTF-8 -*-
from random import choice
from tkinter import *
from random_words import random_words1

okno = Tk()
okno.title('Hra šibenice')
okno.geometry('608x342')
okno.iconphoto(False, PhotoImage(file='..\\pictures\\icon.png'))

obrazek_na_pozadi = PhotoImage(file='..\\pictures\\bg_meadow.png')
pozadi = Label(okno, image=obrazek_na_pozadi)
pozadi.place(x=0, y=0, relwidth=1, relheight=1)


def vytisknout_tlacitko(tlacitko):
    vytisknout['text'] = tlacitko
    return tlacitko


def hra():
    hadani = vytisknout['text']

    if hadani.lower() in tajne_slovo\
    or hadani.upper() in tajne_slovo:
        for index, pismeno in enumerate(tajne_slovo):

            if hadani.lower() == pismeno:
                tajenka[index] = hadani.lower() + ' '
                cedulka_tajenka['text'] = ''.join(list(tajenka))

            if hadani.upper() == pismeno:
                tajenka[index] = hadani.upper() + ' '
                cedulka_tajenka['text'] = ''.join(list(tajenka))

            if '_ ' not in tajenka:
                konec_hry_cedulka = Label(master=okno, text='Vyhrál jsi!', font='Arial 16', bg='#5bdddd', height=1,
                                          width=15)
                konec_hry_cedulka.place(x=355, y=120)

    else:
        zivoty_pocet['text'] -= 1
        zivoty_emoji['text'] = '\U00002764' * zivoty_pocet['text']
        global obrazek
        obrazek = PhotoImage(file=f"..\\pictures\\hang_{7 - int(zivoty_pocet['text'])}.png")
        postava_obrazek['image'] = obrazek

        if zivoty_pocet['text'] < 1:
            konec_hry_cedulka = Label(master=okno, text='Prohrál jsi!', font='Arial 16', bg='#5bdddd', height=1, width=15)
            konec_hry_cedulka.place(x=355, y=120)
            zivoty_emoji.config(text=tajne_slovo, anchor='center')


tajne_slovo = choice(random_words1)
tajenka = ['_ '] * len(tajne_slovo)

obrazek_tlacitko = PhotoImage(file='..\\pictures\\button.png')
tlacitko_modre = Label(master=okno, borderwidth=0, image=obrazek_tlacitko)
tlacitko_modre.place(x=195, y=6)

cedulka_zivoty = Label(master=okno, text='Životy:', font='Arial 18', bg='#4dcfdc', height=1, width=11)
cedulka_zivoty.place(x=30, y=75)

zivoty_pocet = Label(master=okno, text=7, font='Arial 18', bg='#4dcfdc', height=1, width=2)
zivoty_pocet.place(x=160, y=75)

zivoty_emoji = Label(master=okno, text='\U00002764' * zivoty_pocet['text'], fg='red', font='Arial 16',
                     bg='#5bdddd', height=1, width=13, anchor='w')
zivoty_emoji.place(x=30, y=115)

vytisknout = Label(master=okno, text='', font='Arial 16', height=1, width=4, bg='#5bdddd')
vytisknout.place(x=285, y=120)

nadpis = Label(master=okno, text='Hra šibenice', font='Arial 20', bg='#7de6f0')
nadpis.place(x=225, y=10)

cedulka_tajenka = Label(master=okno, text=''.join(list(tajenka)), font='Arial 16', bg='#4dcfdc', height=1, width=20)
cedulka_tajenka.place(x=295, y=75)

vyhodnotit = Button(master=okno, text='Vyhodnotit', font='Arial 16', command=hra, bg='#5bdddd', height=1, width=16)
vyhodnotit.place(x=350, y=115)

obrazek = PhotoImage(file='..\\pictures\\hang_0.png')
postava_obrazek = Label(master=okno, borderwidth=0, image=obrazek)
postava_obrazek.place(x=50, y=152)

# tlačítko abecedy
tlacitko_A = Button(master=okno, text='A', font='Arial 16', bg='#b7ffeb', command=lambda tlacitko='A': vytisknout_tlacitko(tlacitko))
tlacitko_A.place(x=230, y=180)

tlacitko_B = Button(master=okno, text='B', font='Arial 16', bg='#b7ffeb', command=lambda tlacitko='B': vytisknout_tlacitko(tlacitko))
tlacitko_B.place(x=270, y=180)

tlacitko_C = Button(master=okno, text='C', font='Arial 16', bg='#b7ffeb', command=lambda tlacitko='C': vytisknout_tlacitko(tlacitko))
tlacitko_C.place(x=310, y=180)

tlacitko_D = Button(master=okno, text='D', font='Arial 16', bg='#b7ffeb', command=lambda tlacitko='D': vytisknout_tlacitko(tlacitko))
tlacitko_D.place(x=350, y=180)

tlacitko_E = Button(master=okno, text='E', font='Arial 16', bg='#b7ffeb', command=lambda tlacitko='E': vytisknout_tlacitko(tlacitko))
tlacitko_E.place(x=390, y=180)

tlacitko_F = Button(master=okno, text='F', font='Arial 16', bg='#b7ffeb', command=lambda tlacitko='F': vytisknout_tlacitko(tlacitko))
tlacitko_F.place(x=430, y=180)

tlacitko_G = Button(master=okno, text='G', font='Arial 16', bg='#b7ffeb', command=lambda tlacitko='G': vytisknout_tlacitko(tlacitko))
tlacitko_G.place(x=470, y=180)

tlacitko_H = Button(master=okno, text='H', font='Arial 16', bg='#b7ffeb', command=lambda tlacitko='H': vytisknout_tlacitko(tlacitko))
tlacitko_H.place(x=510, y=180)

tlacitko_I = Button(master=okno, text='I', font='Arial 16', bg='#b7ffeb', command=lambda tlacitko='I': vytisknout_tlacitko(tlacitko))
tlacitko_I.place(x=550, y=180)

tlacitko_J = Button(master=okno, text='J', font='Arial 16', bg='#b7ffeb', command=lambda tlacitko='J': vytisknout_tlacitko(tlacitko))
tlacitko_J.place(x=230, y=230)

tlacitko_K = Button(master=okno, text='K', font='Arial 16', bg='#b7ffeb', command=lambda tlacitko='K': vytisknout_tlacitko(tlacitko))
tlacitko_K.place(x=270, y=230)

tlacitko_L = Button(master=okno, text='L', font='Arial 16', bg='#b7ffeb', command=lambda tlacitko='L': vytisknout_tlacitko(tlacitko))
tlacitko_L.place(x=310, y=230)

tlacitko_M = Button(master=okno, text='M', font='Arial 16', bg='#b7ffeb', command=lambda tlacitko='M': vytisknout_tlacitko(tlacitko))
tlacitko_M.place(x=350, y=230)

tlacitko_N = Button(master=okno, text='N', font='Arial 16', bg='#b7ffeb', command=lambda tlacitko='N': vytisknout_tlacitko(tlacitko))
tlacitko_N.place(x=390, y=230)

tlacitko_O = Button(master=okno, text='O', font='Arial 16', bg='#b7ffeb', command=lambda tlacitko='O': vytisknout_tlacitko(tlacitko))
tlacitko_O.place(x=430, y=230)

tlacitko_P = Button(master=okno, text='P', font='Arial 16', bg='#b7ffeb', command=lambda tlacitko='P': vytisknout_tlacitko(tlacitko))
tlacitko_P.place(x=470, y=230)

tlacitko_Q = Button(master=okno, text='Q', font='Arial 16', bg='#b7ffeb', command=lambda tlacitko='Q': vytisknout_tlacitko(tlacitko))
tlacitko_Q.place(x=510, y=230)

tlacitko_R = Button(master=okno, text='R', font='Arial 16', bg='#b7ffeb', command=lambda tlacitko='R': vytisknout_tlacitko(tlacitko))
tlacitko_R.place(x=550, y=230)

tlacitko_S = Button(master=okno, text='S', font='Arial 16', bg='#b7ffeb', command=lambda tlacitko='S': vytisknout_tlacitko(tlacitko))
tlacitko_S.place(x=240, y=280)

tlacitko_T = Button(master=okno, text='T', font='Arial 16', bg='#b7ffeb', command=lambda tlacitko='T': vytisknout_tlacitko(tlacitko))
tlacitko_T.place(x=280, y=280)

tlacitko_U = Button(master=okno, text='U', font='Arial 16', bg='#b7ffeb', command=lambda tlacitko='U': vytisknout_tlacitko(tlacitko))
tlacitko_U.place(x=320, y=280)

tlacitko_V = Button(master=okno, text='V', font='Arial 16', bg='#b7ffeb', command=lambda tlacitko='V': vytisknout_tlacitko(tlacitko))
tlacitko_V.place(x=360, y=280)

tlacitko_W = Button(master=okno, text='W', font='Arial 16', bg='#b7ffeb', command=lambda tlacitko='W': vytisknout_tlacitko(tlacitko))
tlacitko_W.place(x=395, y=280)

tlacitko_X = Button(master=okno, text='X', font='Arial 16', bg='#b7ffeb', command=lambda tlacitko='X': vytisknout_tlacitko(tlacitko))
tlacitko_X.place(x=440, y=280)

tlacitko_Y = Button(master=okno, text='Y', font='Arial 16', bg='#b7ffeb', command=lambda tlacitko='Y': vytisknout_tlacitko(tlacitko))
tlacitko_Y.place(x=480, y=280)

tlacitko_Z = Button(master=okno, text='Z', font='Arial 16', bg='#b7ffeb', command=lambda tlacitko='Z': vytisknout_tlacitko(tlacitko))
tlacitko_Z.place(x=520, y=280)

okno.mainloop()