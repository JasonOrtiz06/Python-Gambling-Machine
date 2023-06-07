from tkinter import *
import random
from meinmodul import Jackpotpool as JP
from Jackpot_ändern import Jackpot_änderung as JÄ

### Fenster
root = Tk()
root.geometry("400x600")
root.resizable(width=FALSE, height=FALSE)

### Hintergrund vom Fenster

bg = PhotoImage(file = "C:\\APlocal\\77J44670\\DataNow\\HomeShare\\windows\\Desktop\\Neuer Ordner\\Files for Programming\\02 Images\\wallpaper_for_gambling.png")

  
canvas1 = Canvas( root, width = 400, 
                 height = 400) 
  
canvas1.pack(fill = "both", expand = True) 
  
canvas1.create_image( 0, 0, image = bg,  
                     anchor = "nw") 

### Variablen für das Geld
Cash = 2000
Bank = 10000
gesetzt = 0
Jackpot = JP
multiplikator = 0

### funktionen für buttons
def farbeändern0():
    Button25.configure(background="white")
    Button50.configure(background="white")
    Button100.configure(background="white")
    Button1.configure(background="white")
    Label1.configure(background="white")
    Label2.configure(background="white")
    Label3.configure(background="white")

def farbeändern25():
    Button25.configure(background="light green")
    Button50.configure(background="white")
    Button100.configure(background="white")

def farbeändern50():
    Button25.configure(background="white")
    Button50.configure(background="light green")
    Button100.configure(background="white")

def farbeändern100():
    Button25.configure(background="white")
    Button50.configure(background="white")
    Button100.configure(background="light green")

def farbeändern_gewonnen():
    Button1.configure(background="gold")
    Button25.configure(background="gold")
    Button50.configure(background="gold")
    Button100.configure(background="light green")
    Label1.configure(background="gold")
    Label2.configure(background="gold")
    Label3.configure(background="gold")

### funktionen fürs Setzen von Cash
def setze0():
    global gesetzt
    gesetzt = 0
    Label_Geldänderung.configure(text=f"...", fg="black")

def setze25():
    global gesetzt
    gesetzt = 25
    Label_Geldänderung.configure(text=f"...", fg="black")
    

def setze50():
    global gesetzt
    gesetzt = 50
    Label_Geldänderung.configure(text=f"...", fg="black")
    

def setze100():
    global gesetzt
    gesetzt = 100
    Label_Geldänderung.configure(text=f"...", fg="black")

def deaktiviere_einzahlen():
    Button_Geld_einzahlen["state"] = "disabled"

def aktiviere_start():
    Button1["state"] = "active"

def cheat_sicherung_an():
    Button25["state"] = "disabled"
    Button50["state"] = "disabled"
    Button100["state"] = "disabled"

def cheat_sicherung_aus():
    Button25["state"] = "normal"
    Button50["state"] = "normal"
    Button100["state"] = "normal"

def setze_multiplikator_0():
    global multiplikator
    multiplikator = 0
    Label_Jackpot_multiplikator.configure(text=f"Mult.: x[-]")
    



### Funktionen
def geld_einzahlen():
    global Cash
    global Bank
    einzuzahlen = int(Entry_Cash.get())
    if einzuzahlen <= Cash:
        Cash = Cash - einzuzahlen
        Bank = Bank + einzuzahlen
        Label_Cash.configure(text=Cash)
        Label_Purse.configure(text=f"Purse: {Cash}$")
        Label_Bank.configure(text=f"Bank: {Bank}$")

        if Cash <= 24:
            print("fehler zu wenig cash")
            Button1["state"] = "disabled"
            Button25["state"] ="disabled"
            Button50["state"] ="disabled"
            Button100["state"] ="disabled"

        elif Cash <= 49:
            print("fehler zu wenig cash")
            Button1["state"] = "disabled"
            Button25["state"] ="active"
            Button50["state"] ="disabled"
            Button100["state"] ="disabled"

        elif Cash <= 99:
            print("fehler zu wenig cash")
            Button1["state"] = "disabled"
            Button25["state"] ="active"
            Button50["state"] ="active"
            Button100["state"] ="disabled"

        else:
            print("alles gut beim einzahlen")

    else:
        print("FEHLER! beim einzahlen")

def geld_auszahlen():
    global Cash
    global Bank
    auszuzahlen = int(Entry_Cash.get())
    if auszuzahlen <= Bank:
        Cash = Cash + auszuzahlen
        Bank = Bank - auszuzahlen
        Label_Cash.configure(text=f"Cash: {Cash}$")
        Label_Purse.configure(text=f"Purse:{Cash}$")
        Label_Bank.configure(text=f"Bank:{Bank}$")
        
        if Cash >= 100:
           Button100["state"] = "active"
           Button50["state"] = "active"
           Button25["state"] = "active"

        elif Cash >= 50:
            Button50["state"] = "active"
            Button25["state"] = "active"

        elif Cash >= 25:
            Button25["state"] = "active"
            
            
    else:
        print("FEHLER!")
    

def start():
    global Cash, gesetzt, Jackpot

    Zahl1 = random.randint(1,3)
    Zahl2 = random.randint(1,3)
    Zahl3 = random.randint(1,3)


    Label1.configure(text=Zahl1)
    Label2.configure(text=Zahl2)
    Label3.configure(text=Zahl3)


    if Zahl1 == Zahl2 == Zahl3:
        Label_Spielausgang.configure(text="Gewonnen!", fg="green")
        Label_Geldänderung.configure(text=f"[...]", fg="black")
        Label_Cash.configure(text=f"Cash: {Cash}$")
        Jackpot = Jackpot + gesetzt 
        farbeändern_gewonnen()
        cheat_sicherung_an()
        Button1["state"] = "disabled"
        Label_Jackpot.configure(text=f"Jackpot: {Jackpot}$")
        
        ### Button vervielfachen
        def vervielfachen():
            global Cash, Jackpot, multiplikator

            ### Multipliziere den Jackpot bevor man ihn auszahlt
            multiplikator = random.randint(0, 2)
            Label_Jackpot_multiplikator.configure(text=f"Mult.: x{multiplikator}")
            Jackpot = Jackpot * multiplikator
            Cash = Cash + Jackpot
            Label_Geldänderung.configure(text=f"[+{Jackpot}]$", fg="green" )
            setze0()
            farbeändern0()
            
            

            Button_vervielfach["state"] = "disabled"
            Button1 ["state"] = "normal"
            Jackpot = 0
            Label_Jackpot.configure(text=f"Jackpot: {Jackpot}$")
            Label_Cash.configure(text=f"Cash: {Cash}$")
            Label_Purse.configure(text=f"Purse:{Cash}$")
        
        ### Button für vervielfachen
        Button_vervielfach = Button(root, text="%", command=lambda: [vervielfachen(), cheat_sicherung_aus()])
        Button_vervielfach.place(x=15, y=260)


        print("Gewonnenes Geld:",Jackpot)


        

    else:
        Label_Spielausgang.configure(text="Verloren!", fg="red")
        Cash = Cash - gesetzt
        Jackpot = Jackpot + gesetzt
        # Jackpot soll hier für die csv geändert werden
        Label_Geldänderung.configure(text=f"[-{gesetzt}]$", fg="red")
        Label_Cash.configure(text=f"Cash: {Cash}$")
        Label_Purse.configure(text=f"Purse: {Cash}$")
        Label_Jackpot.configure(text=f"Jackpot: {Jackpot}$")
        print("Verlorenes Geld:",Cash)
        
        if Cash <= 24:
            print("fehler zu wenig cash")
            Button1["state"] = "disabled"
            Button25["state"] ="disabled"
            Button50["state"] ="disabled"
            Button100["state"] ="disabled"
            setze0()
            farbeändern0()
            Button1["state"] = "disabled"
            

        elif Cash <= 49:
            print("fehler zu wenig cash")
            Button1["state"] = "disabled"
            Button25["state"] ="active"
            Button50["state"] ="disabled"
            Button100["state"] ="disabled"
            setze0()
            farbeändern0()
            Button1["state"] = "disabled"

        elif Cash <= 99:
            print("fehler zu wenig cash")
            Button1["state"] = "active"
            Button25["state"] ="active"
            Button50["state"] ="active"
            Button100["state"] ="disabled"
            setze0()
            farbeändern0()
            Button1["state"] = "disabled"

        else:
            print("alles gut")



        


### Buttons

Button25 = Button(root, text="[25]", font="Arial 18", background="white", width=8, command=lambda: [setze25(), farbeändern25(), aktiviere_start(), setze_multiplikator_0()])
Button25.place(x=10, y=10)

Button50 = Button(root, text="[50]", font="Arial 18", background="white", width=8, command=lambda: [setze50(), farbeändern50(), aktiviere_start(), setze_multiplikator_0()])
Button50.place(x=150, y=10)

Button100 = Button(root, text="[100]", font="Arial 18", background="white", width=8, command=lambda: [setze100(), farbeändern100(), aktiviere_start(), setze_multiplikator_0()])
Button100.place(x=290, y=10)

Button1 = Button(root, text=" - [START] - ", font="Arial 18", width=10, state="disabled", command=start)
Button1.place(x=122, y=250)


### Labels

Label1 = Label(root, text="[]", font="Arial 30")
Label1.place(x=50, y=80)

Label2 = Label(root, text="[]", font="Arial 30")
Label2.place(x=180, y=80)

Label3 = Label(root, text="[]", font="Arial 30")
Label3.place(x=310, y=80)

Label_Spielausgang = Label(root, text="[-]")
Label_Spielausgang.place(x=270, y=215)

Label_Geldänderung = Label(root, text="[   ]")
Label_Geldänderung.place(x=80, y=215)

Label_Cash = Label(root, text=f"Cash: {Cash}$")
Label_Cash.place(x=156, y=200)

Label_Bank = Label(root, text=f"Bank:{Bank}$")
Label_Bank.place(x=10, y=350)

Label_Purse = Label(root, text=f"Purse:{Cash}$")
Label_Purse.place(x=10, y=325)

Label_Jackpot = Label(root, text=f"Jackpot: {Jackpot}")
Label_Jackpot.place(x=155, y=222)

Label_Jackpot_multiplikator = Label(root, text=f"Mult.: x[-]")
Label_Jackpot_multiplikator.place(x=40, y=260)

### Entrywidgets

Button_Geld_abheben = Button(root, width=2, height=1, text="+", command=geld_auszahlen)
Button_Geld_abheben.place(x=73, y=225)

Button_Geld_einzahlen = Button(root, width=2, height=1, text="+", command=geld_einzahlen)
Button_Geld_einzahlen.place(x=73, y=250)

Entry_Cash = Entry(root, width=7 ,text="")
Entry_Cash.place(x=150, y=337)

### CANVAS Anpassungen
  
Button25_canvas = canvas1.create_window( 10, 10, 
                                       anchor = "nw", 
                                       window = Button25) 
  
Button50_canvas = canvas1.create_window(  140, 10, anchor = "nw", 
                                       window = Button50) 

Button100_canvas = canvas1.create_window( 270, 10, anchor = "nw", 
                                       window = Button100)

Button_Geld_einzahlen_canvas = canvas1.create_window( 120, 350, anchor = "nw", 
                                       window = Button_Geld_einzahlen)

Button_Geld_abheben_canvas = canvas1.create_window( 120, 325, anchor = "nw", 
                                       window = Button_Geld_abheben)


root.mainloop()

JÄ = Jackpot


###### Es soll einen Button geben um mehr Geld einzahlen zu können und mit Geld rauszu gehen.
###### Wenn das Geld 0 erreicht soll der + Button rot werden und man muss Geld einzahlen
###### Das Geld das man rausholt soll man auf einem "Bankaccount speichern können um es dann wieder einzu zahlen XD"
###### evtl. eine Datei die Das Geld und den jeweiligen Nutzer speichert.
###### vielleicht mit Entry am Anfang den Username mit einem Password abfragen.
###### Man soll dann das Cash von Sitzung zu Sitzung mitnehmen können. 
###### Das mit Accountdaten kann man mit einem Plugin (wie Tkinter lösen)
###### vielleicht kann man sich auch stuff in form von dateien kaufen, für das Chash in nem seperaten programm
###### wäre sick glaub ich!