from random import *
from tkinter import *

finestra=Tk()

finestra.title("Tris - LEO CAF")
finestra.geometry("400x400")
#inestra.resizable(False, False)
finestra.wm_iconbitmap("tris.ico")
finestra.configure(bg="blue")

tris=Label(finestra, text="""
<immagine_tris>

By LEO_CAF""", bg="blue", fg="white")
tris.grid(column=0, row=0)

"""
████████╗██████╗░██╗░██████╗
╚══██╔══╝██╔══██╗██║██╔════╝
░░░██║░░░██████╔╝██║╚█████╗░
░░░██║░░░██╔══██╗██║░╚═══██╗
░░░██║░░░██║░░██║██║██████╔╝
░░░╚═╝░░░╚═╝░░╚═╝╚═╝╚═════╝░
"""

bg="white"
font="Arial 15"
c=10
r=10

def click():
    pass

"""
print("Premere:")
print(1,2,3)
print(4,5,6)
print(7,8,9)
"""
global a,b,xop,mossa,partita,run,giocatore,player,p

def gioco():


    start()

    while True:
        player=input("\nPlayer [x][o]: ")

        if player=="x":
            giocatore=3
        elif player=="o":
            giocatore=3

        if player=="x" or player=="o":
            break
        else:
            print("\nInserire solo [x] oppure [o]")

    while run:
        turno()
        disegno()
        controllo()

        if partita==False:
            if xop=="x":
                print("\nVittoria X")
            elif xop=="o":
                print("\nVittoria O")
            elif xop=="p":
                print("\nPareggio")

            fine=input("\nESCI [y]: ")
            if fine=="y":
                run=False
            else:
                gioco()

def start():
    a=["elemento_0",1,1,1,1,1,1,1,1,1]
    b=["elemento_0","","","","","","","","",""]
    p=[0,"r1","r2","r3","c1","c2","c3","d1","d2"]

    xop=""
    mossa=0

    partita=True
    run=True

    giocatore=0
    player=""

    t_1=StringVar()
    t_2=StringVar()
    t_3=StringVar()
    t_4=StringVar()
    t_5=StringVar()
    t_6=StringVar()
    t_7=StringVar()
    t_8=StringVar()
    t_9=StringVar()

    t_1.set(" - ")
    t_2.set(" - ")
    t_3.set(" - ")
    t_4.set(" - ")
    t_5.set(" - ")
    t_6.set(" - ")
    t_7.set(" - ")
    t_8.set(" - ")
    t_9.set(" - ")

    b_1=Button(finestra, textvariable=t_1, bg=bg, font=font, command=click).grid(column=c+1, row=r+1)
    b_2=Button(finestra, textvariable=t_2, bg=bg, font=font, command=click).grid(column=c+2, row=r+1)
    b_3=Button(finestra, textvariable=t_3, bg=bg, font=font, command=click).grid(column=c+3, row=r+1)
    b_4=Button(finestra, textvariable=t_4, bg=bg, font=font, command=click).grid(column=c+1, row=r+2)
    b_5=Button(finestra, textvariable=t_5, bg=bg, font=font, command=click).grid(column=c+2, row=r+2)
    b_6=Button(finestra, textvariable=t_6, bg=bg, font=font, command=click).grid(column=c+3, row=r+2)
    b_7=Button(finestra, textvariable=t_7, bg=bg, font=font, command=click).grid(column=c+1, row=r+3)
    b_8=Button(finestra, textvariable=t_8, bg=bg, font=font, command=click).grid(column=c+2, row=r+3)
    b_9=Button(finestra, textvariable=t_9, bg=bg, font=font, command=click).grid(column=c+3, row=r+3)

def verifica():
    global a,b,xop,mossa,partita,run,giocatore,player,p

    p[1]=a[1]*a[2]*a[3]
    p[2]=a[4]*a[5]*a[6]
    p[3]=a[7]*a[8]*a[9]
    p[4]=a[1]*a[4]*a[7]
    p[5]=a[2]*a[5]*a[8]
    p[6]=a[3]*a[6]*a[9]
    p[7]=a[1]*a[5]*a[9]
    p[8]=a[3]*a[5]*a[7]

def turno():
    global a,b,xop,mossa,partita,run,giocatore,player,p

    if player=="x":
        if giocatore==3:
            while True:
                mossa=input("\nGiocatore: x Mossa: ")

                if mossa.isdigit():
                    mossa=int(mossa)
                    if mossa>0 and mossa<10:
                        break
                    else:
                        print("\nInserire solo [1][2][3][3][4][5][6][7][8][9]")
                else:
                    print("\nInserire solo [1][2][3][3][4][5][6][7][8][9]")
        else:
            ragionamento()
            print("\nGiocatore: o Mossa: "+str(mossa))
    else:
        if giocatore==5:
            while True:
                mossa=input("\nGiocatore: o Mossa: ")

                if mossa.isdigit():
                    mossa=int(mossa)
                    if mossa>0 and mossa<10:
                        break
                    else:
                        print("\nInserire solo [1][2][3][3][4][5][6][7][8][9]")
                else:
                    print("\nInserire solo [1][2][3][3][4][5][6][7][8][9]")
        else:
            ragionamento()
            print("\nGiocatore: x Mossa: "+str(mossa))

    if a[mossa]==1:
        a[mossa]=giocatore
        if giocatore==3:
            giocatore=5
        else:
            giocatore=3
    else:
        print("\nCasella Occupata\n")

def disegno():
    global a,b,xop,mossa,partita,run,giocatore,player,p
    global bottone_1,bottone_2,bottone_3,bottone_4,bottone_5,bottone_6,bottone_7,bottone_8,bottone_9

    for i in range(1,10,1):
        if a[i]==3:
            b[i]=" x "

        if a[i]==5:
            b[i]=" o "

        if a[i]==1:
            b[i]=" - "

    t_1.set(b[1])
    t_2.set(b[2])
    t_3.set(b[3])
    t_4.set(b[4])
    t_5.set(b[5])
    t_6.set(b[6])
    t_7.set(b[7])
    t_8.set(b[8])
    t_9.set(b[9])

    print(b[1],b[2],b[3])
    print(b[4],b[5],b[6])
    print(b[7],b[8],b[9])

def controllo():
    global a,b,xop,mossa,partita,run,giocatore,player,p

    verifica()

    if p[1]==27 or p[2]==27 or p[3]==27 or p[4]==27 or p[5]==27 or p[6]==27 or p[7]==27 or p[8]==27:
        partita=False
        xop="x"
    elif p[1]==125 or p[2]==125 or p[3]==125 or p[4]==125 or p[5]==125 or p[6]==125 or p[7]==125 or p[8]==125:
        partita=False
        xop="o"
    else:
        if a[1]!=1 and a[2]!=1 and a[3]!=1 and a[4]!=1 and a[5]!=1 and a[6]!=1 and a[7]!=1 and a[8]!=1 and a[9]!=1:
            partita=False
            xop="p"

def ragionamento():
    global a,b,xop,mossa,partita,run,giocatore,player,p

    verifica()

    u=[]
    c_tre=0
    c_mossa=0

    if player=="x":
        for i in range(1,9,1):
            if p[i]==25:
                u.append(i)
        if len(u)==0:
            for i in range(1,9,1):
                if p[i]==9:
                    u.append(i)
            if len(u)==0:
                for i in range(1,9,1):
                    if p[i]==5:
                        u.append(i)
                if len(u)==0:
                    for i in range(1,9,1):
                        if p[i]==3:
                            u.append(i)
                    if len(u)==0:
                        u.append(0)
    else:
        for i in range(1,9,1):
            if p[i]==9:
                u.append(i)
        if len(u)==0:
            for i in range(1,9,1):
                if p[i]==25:
                    u.append(i)
            if len(u)==0:
                for i in range(1,9,1):
                    if p[i]==3:
                        u.append(i)
                if len(u)==0:
                    for i in range(1,9,1):
                        if p[i]==5:
                            u.append(i)
                    if len(u)==0:
                        u.append(0)

    if u[0]==0:
        c_tre=9
    else:
        c_tre=choice(u)

    if c_tre==1:
        if a[1]==1 and a[2]!=1 and a[3]!=1:
            c_mossa=1
        if a[1]!=1 and a[2]==1 and a[3]!=1:
            c_mossa=2
        if a[1]!=1 and a[2]!=1 and a[3]==1:
            c_mossa=3

        if a[1]==1 and a[2]==1 and a[3]!=1:
            c_mossa=choice((1,2))
        if a[1]==1 and a[2]!=1 and a[3]==1:
            c_mossa=choice((1,3))
        if a[1]!=1 and a[2]==1 and a[3]==1:
            c_mossa=choice((2,3))

    if c_tre==2:
        if a[4]==1 and a[5]!=1 and a[6]!=1:
            c_mossa=4
        if a[4]!=1 and a[5]==1 and a[6]!=1:
            c_mossa=5
        if a[4]!=1 and a[5]!=1 and a[6]==1:
            c_mossa=6

        if a[4]==1 and a[5]==1 and a[6]!=1:
            c_mossa=choice((4,5))
        if a[4]==1 and a[5]!=1 and a[6]==1:
            c_mossa=choice((4,6))
        if a[4]!=1 and a[5]==1 and a[6]==1:
            c_mossa=choice((5,6))

    if c_tre==3:
        if a[7]==1 and a[8]!=1 and a[9]!=1:
            c_mossa=7
        if a[7]!=1 and a[8]==1 and a[9]!=1:
            c_mossa=8
        if a[7]!=1 and a[8]!=1 and a[9]==1:
            c_mossa=9

        if a[7]==1 and a[8]==1 and a[9]!=1:
            c_mossa=choice((7,8))
        if a[7]==1 and a[8]!=1 and a[9]==1:
            c_mossa=choice((7,9))
        if a[7]!=1 and a[8]==1 and a[9]==1:
            c_mossa=choice((8,9))

    if c_tre==4:
        if a[1]==1 and a[4]!=1 and a[7]!=1:
            c_mossa=1
        if a[1]!=1 and a[4]==1 and a[7]!=1:
            c_mossa=4
        if a[1]!=1 and a[4]!=1 and a[7]==1:
            c_mossa=7

        if a[1]==1 and a[4]==1 and a[7]!=1:
            c_mossa=choice((1,4))
        if a[1]==1 and a[4]!=1 and a[7]==1:
            c_mossa=choice((1,7))
        if a[1]!=1 and a[4]==1 and a[7]==1:
            c_mossa=choice((4,7))

    if c_tre==5:
        if a[2]==1 and a[5]!=1 and a[8]!=1:
            c_mossa=2
        if a[2]!=1 and a[5]==1 and a[8]!=1:
            c_mossa=5
        if a[2]!=1 and a[5]!=1 and a[8]==1:
            c_mossa=8

        if a[2]==1 and a[5]==1 and a[8]!=1:
            c_mossa=choice((2,5))
        if a[2]==1 and a[5]!=1 and a[8]==1:
            c_mossa=choice((2,8))
        if a[2]!=1 and a[5]==1 and a[8]==1:
            c_mossa=choice((5,8))

    if c_tre==6:
        if a[3]==1 and a[6]!=1 and a[9]!=1:
            c_mossa=3
        if a[3]!=1 and a[6]==1 and a[9]!=1:
            c_mossa=6
        if a[3]!=1 and a[6]!=1 and a[9]==1:
            c_mossa=9

        if a[3]==1 and a[6]==1 and a[9]!=1:
            c_mossa=choice((3,6))
        if a[3]==1 and a[6]!=1 and a[9]==1:
            c_mossa=choice((3,9))
        if a[3]!=1 and a[6]==1 and a[9]==1:
            c_mossa=choice((6,9))

    if c_tre==7:
        if a[1]==1 and a[5]!=1 and a[9]!=1:
            c_mossa=1
        if a[1]!=1 and a[5]==1 and a[9]!=1:
            c_mossa=5
        if a[1]!=1 and a[5]!=1 and a[9]==1:
            c_mossa=9

        if a[1]==1 and a[5]==1 and a[9]!=1:
            c_mossa=choice((1,5))
        if a[1]==1 and a[5]!=1 and a[9]==1:
            c_mossa=choice((1,9))
        if a[1]!=1 and a[5]==1 and a[9]==1:
            c_mossa=choice((5,9))

    if c_tre==8:
        if a[3]==1 and a[5]!=1 and a[7]!=1:
            c_mossa=3
        if a[3]!=1 and a[5]==1 and a[7]!=1:
            c_mossa=5
        if a[3]!=1 and a[5]!=1 and a[7]==1:
            c_mossa=7

        if a[3]==1 and a[5]==1 and a[7]!=1:
            c_mossa=choice((3,5))
        if a[3]==1 and a[5]!=1 and a[7]==1:
            c_mossa=choice((3,7))
        if a[3]!=1 and a[5]==1 and a[7]==1:
            c_mossa=choice((5,7))

    if c_tre==9:
        c_mossa=randint(1,9)

    mossa=c_mossa

gioco()

finestra.mainloop()
