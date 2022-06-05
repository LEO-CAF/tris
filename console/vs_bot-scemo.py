import random

print("""
████████╗██████╗░██╗░██████╗
╚══██╔══╝██╔══██╗██║██╔════╝
░░░██║░░░██████╔╝██║╚█████╗░
░░░██║░░░██╔══██╗██║░╚═══██╗
░░░██║░░░██║░░██║██║██████╔╝
░░░╚═╝░░░╚═╝░░╚═╝╚═╝╚═════╝░

By LEO_CAF
""")

print("Premere:")
print(1,2,3)
print(4,5,6)
print(7,8,9)

def gioco():
    global a,b,xop,mossa,partita,run,giocatore,player,r1,r2,r3,c1,c2,c3,d1,d2

    a=["elemento_0",1,1,1,1,1,1,1,1,1]
    b=["elemento_0","","","","","","","","",""]

    xop=""
    mossa=0

    partita=True
    run=True

    giocatore=0
    player=""

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

def verifica():
    global a,b,xop,mossa,partita,run,giocatore,player,r1,r2,r3,c1,c2,c3,d1,d2

    r1=a[1]*a[2]*a[3]
    r2=a[4]*a[5]*a[6]
    r3=a[7]*a[8]*a[9]
    c1=a[1]*a[4]*a[7]
    c2=a[2]*a[5]*a[8]
    c3=a[3]*a[6]*a[9]
    d1=a[1]*a[5]*a[9]
    d2=a[3]*a[5]*a[7]

def turno():
    global a,b,xop,mossa,partita,run,giocatore,player,r1,r2,r3,c1,c2,c3,d1,d2

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
    global a,b,xop,mossa,partita,run,giocatore,player,r1,r2,r3,c1,c2,c3,d1,d2

    for i in range(1,10,1):
        if a[i]==3:
            b[i]="x"

        if a[i]==5:
            b[i]="o"

        if a[i]==1:
            b[i]="-"

    print(b[1],b[2],b[3])
    print(b[4],b[5],b[6])
    print(b[7],b[8],b[9])

def controllo():
    global a,b,xop,mossa,partita,run,giocatore,player,r1,r2,r3,c1,c2,c3,d1,d2

    verifica()

    if r1==27 or r2==27 or r3==27 or c1==27 or c2==27 or c3==27 or d1==27 or d2==27:
        partita=False
        xop="x"
    elif r1==125 or r2==125 or r3==125 or c1==125 or c2==125 or c3==125 or d1==125 or d2==125:
        partita=False
        xop="o"
    else:
        if a[1]!=1 and a[2]!=1 and a[3]!=1 and a[4]!=1 and a[5]!=1 and a[6]!=1 and a[7]!=1 and a[8]!=1 and a[9]!=1:
            partita=False
            xop="p"

def ragionamento():
    global a,b,xop,mossa,partita,run,giocatore,player,r1,r2,r3,c1,c2,c3,d1,d2

    mossa=random.randint(1,9)

gioco()
