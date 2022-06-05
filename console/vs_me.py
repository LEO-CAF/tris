print("Tris!\n")

print("Premere:")
print(1,2,3)
print(4,5,6)
print(7,8,9)

def turno():
    global giocatore,a,xo,mossa,partita,run

    if a[mossa-1]=="-":
        a[mossa-1]=giocatore
        if giocatore=="x":
            giocatore="o"
        else:
            giocatore="x"
    else:
        print("\nCasella Occupata\n")

def gioco():
    global giocatore,a,xo,mossa,partita,run

    giocatore="x"
    a=["-","-","-","-","-","-","-","-","-"]
    xo=""
    mossa=0
    partita=True
    run=True

    while run:
        mossa=input("\nGiocatore: "+giocatore+" Mossa: ")
        mossa=int(mossa)

        turno()
        disegno()
        controllo()
    	
        if partita==False:
            if xo=="x":
                print("\nVittoria X")
            elif xo=="o":
                print("\nVittoria O")
            elif xo=="p":
                print("\nPareggio")

            fine=input("\nESCI [y]: ")
            if fine=="y":
                run=False
            else:
                gioco()

def controllo():
    global giocatore,a,xo,mossa,partita,run
	      
    if a[0]=="x" and a[1]=="x" and a[2]=="x":
        partita=False
        xo="x"
    elif a[3]=="x" and a[4]=="x" and a[5]=="x":
        partita=False
        xo="x"
    elif a[6]=="x" and a[7]=="x" and a[8]=="x":
        partita=False
        xo="x"
    elif a[0]=="x" and a[3]=="x" and a[6]=="x":
        partita=False
        xo="x"
    elif a[1]=="x" and a[4]=="x" and a[7]=="x":
        partita=False
        xo="x"
    elif a[2]=="x" and a[5]=="x" and a[8]=="x":
        partita=False
        xo="x"
    elif a[0]=="x" and a[4]=="x" and a[8]=="x":
        partita=False
        xo="x"
    elif a[2]=="x" and a[4]=="x" and a[6]=="x":
        partita=False
        xo="x"
	      
    if a[0]=="o" and a[1]=="o" and a[2]=="o":
        partita=False
        xo="o"
    elif a[3]=="o" and a[4]=="o" and a[5]=="o":
        partita=False
        xo="o"
    elif a[6]=="o" and a[7]=="o" and a[8]=="o":
        partita=False
        xo="o"
    elif a[0]=="o" and a[3]=="o" and a[6]=="o":
        partita=False
        xo="o"
    elif a[1]=="o" and a[4]=="o" and a[7]=="o":
        partita=False
        xo="o"
    elif a[2]=="o" and a[5]=="o" and a[8]=="o":
        partita=False
        xo="o"
    elif a[0]=="o" and a[4]=="o" and a[8]=="o":
        partita=False
        xo="o"
    elif a[2]=="o" and a[4]=="o" and a[6]=="o":
        partita=False
        xo="o"
    
    if a[0]!="-" and a[1]!="-" and a[2]!="-" and a[3]!="-" and a[4]!="-" and a[5]!="-" and a[6]!="-" and a[7]!="-" and a[8]!="-":
        partita=False
        xo="p"
  
def disegno():
    global giocatore,a,xo,mossa,partita,run

    print(a[0],a[1],a[2])
    print(a[3],a[4],a[5])
    print(a[6],a[7],a[8])

gioco()
