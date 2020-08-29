# Bus-Online-Ticket-Booking-System
A Bus Online Ticket Booking system, which uses GUI in python. Real time Online ticket booking system.
'''Authors:-    KAVAN DESAI
   Program:-    BUS ONILE TICKET BOOKING SYSTEM
'''
from tkinter import *
import datetime
from tkinter import Tk, mainloop,TOP
from time import time
import sys
#used tkinter for booking seat as GUI.
file=open('text3.txt','r')
#file text3.txt is only form some presentation.
print(file.read())
# mainMenu is to cancel or update the booking.
def mainMenu(i):
    print("                        *************************MainMenu***************************")
    print("                        To cancel the ticket booking press 1.\n                        To update the filled choice press 2.")
    cancel=(int(input("Enter your option:")))
    if(cancel==1):
        print("                        Thanks for visiting our system.")
        sys.exit()
    elif(cancel==2):
        Update()
    elif(cancel!=1 and cancel!=2 and cancel!=0):
        print("                        Enter valid number!!")
# Update function updates the seat or information
def update():
    From()
    foading()
    to()
    loading()
    date()
    doading()

#loding function give some attribute of loading                                        
def loading():
    import time
    print(">>>Loading", end="")
    time.sleep(0.75)
    print(".",end="")
    time.sleep(0.75)
    print(".",end="")
    time.sleep(0.75)
    print(".")

#ticket function notes the ticket data and print at the end of booking ticket
def ticket():
    x=datetime.datetime.now()
    name=str(input("                        Enter your good name:"))
    age=int(input("                        Enter your age:"))
    gender=str(input("                        Male or Female:"))
    mobile_num=int(input("                        Enter your mobile number:"))
    e_mail=str(input("                        Enter your E-mail address:"))
    city=['Bhavnagar','Ahmedabad','Rajkot','Baroda']
    fileFrom=open('From.txt','r')
    fileTo=open('To.txt', 'r')
    print("************************************************************************")
    print("**************************||YOUR BUS TICKET||***************************")
    duplicateFrom=int(fileFrom.readline())
    duplicateTo=int(fileTo.readline())
    if(duplicateFrom==1 and duplicateTo==2):
        print("      From:Bhavnagar       To:Ahmedabad")
    elif(duplicateFrom==2 and duplicateTo==1):
        print("      From:Ahmedabad       To:Bhavnagar")
    elif(duplicateFrom==1 and duplicateTo==3):
        print("      From:Bhavnagar       To:Rajkot")
    elif(duplicateFrom==3 and duplicateTo==1):
        print("      From:Rajkot       To:Bhavnagar")
    elif(duplicateFrom==1 and duplicateTo==4):
        print("      From:Bhavnagar       To:Baroda")
    elif(duplicateFrom==4 and duplicateTo==1):
        print("      From:Baroda       To:Bhavnagar")
    elif(duplicateFrom==2 and duplicateTo==3):
        print("      From:Ahmedabad       To:Rajkot")
    elif(duplicateFrom==3 and duplicateTo==2):
        print("      From:Rajkot       To:Ahmedabad")
    elif(duplicateFrom==2 and duplicateTo==4):
        print("      From:Ahmedabad       To:Baroda")
    elif(duplicateFrom==4 and duplicateTo==2):
        print("      From:Baroda       To:Ahmedabad")
    elif(duplicateFrom==3 and duplicateTo==4):
        print("      From:Rajkot       To:Baroda")
    elif(duplicateFrom==4 and duplicateTo==3):
        print("      From:Baroda       To:Rajkot")
    timeToBoard=open('TimeToBoard.txt','r')
    print("      The time to board :- ",timeToBoard.read(),":00")
    print("      Name:-",name)
    print("      Age:-",age)
    print("      Gender:-",gender)
    print("      Mobile No:-",mobile_num)
    print("      E-Mail ID:-",e_mail)
    print("      Price for booking ticket(+gst, +sgst):270")
    ticket=open('Ticket.txt', 'w+')
    ticket.write("Name:")
    ticket.write(name)
    ticket.write("\n")
    ticket.write("Age:")
    ticket.write(str(age))
    ticket.write("\nGender:")
    ticket.write(gender)
    ticket.write('\nmobile number:')
    ticket.write(str(mobile_num))
    ticket.write('\nEmail:')
    ticket.write(e_mail)
    ticket.write('\nTime of booking ticket:')
    ticket.write(str(x))
    ticket.write('\ndate of travel:',)
    date=open('date.txt','r')
    ticket.write("date.read()")
    ticket.write("\n")
    seatnum=open('seatnum.txt','r')
    ticket=open('Ticket.txt', 'w+')
    seatnum=open('seatnum.txt','r')
    print(seatnum.read())
    print("      Date of booking ticket:",x)
    print("************************************************************************")
    print("                        Thanks for visiting our site                     ")
    print("************************************************************************")
    i=input("")

#seat function conforms your seat booked 
def seat(i):
    if(i==1):
        print("                        Your seat number is: ",i)
        seat1=open('seat1.txt', 'w+')
        seat1.write(str(i))
    elif(i==2):
        print("                        Your seat number is: ",i)
        seat2=open('seat2.txt', 'w+')
        seat2.write(str(i))
    elif(i==3):
        print("                        Your seat number is: ",i)
        seat3=open('seat3.txt', 'w+')
        seat3.write(str(i))
    elif(i==4):
        print("                        Your seat number is: ",i)
        seat4=open('seat4.txt', 'w+')
        seat4.write(str(i))
    elif(i==5):
        print("                        Your seat number is: ",i)
        seat5=open('seat5.txt', 'w+')
        seat5.write(str(i))
    elif(i==6):
        print("                        Your seat number is: ",i)
        seat6=open('seat6.txt', 'w+')
        seat6.write(str(i))
    elif(i==7):
        print("                        Your seat number is: ",i)
        seat7=open('seat7.txt', 'w+')
        seat7.write(str(i))
    elif(i==8):
        print("                        Your seat number is: ",i)
        seat8=open('seat8.txt', 'w+')
        seat8.write(str(i))
    elif(i==9):
        print("                        Your seat number is: ",i)
        seat9=open('seat9.txt', 'w+')
        seat9.write(str(i))
    elif(i==10):
        print("                        Your seat number is: ",i)
        seat10=open('seat10.txt', 'w+')
        seat10.write(str(i))
    elif(i==11):
        print("                        Your seat number is: ",i)
        seat11=open('seat11.txt', 'w+')
        seat11.write(str(i))
    elif(i==12):
        print("                        Your seat number is: ",i)
        seat12=open('seat12.txt', 'w+')
        seat12.write(str(i))
    elif(i==13):
        print("                        Your seat number is: ",i)
        seat13=open('seat13.txt', 'w+')
        seat13.write(str(i))
    elif(i==14):
        print("                        Your seat number is: ",i)
        seat14=open('seat14.txt', 'w+')
        seat14.write(str(i))
    elif(i==15):
        print("                        Your seat number is: ",i)
        seat15=open('seat15.txt', 'w+')
        seat15.write(str(i))
    elif(i==16):
        print("                        Your seat number is: ",i)
        seat16=open('seat16.txt', 'w+')
        seat16.write(str(i))
    elif(i==17):
        print("                        Your seat number is: ",i)
        seat17=open('seat17.txt', 'w+')
        seat17.write(str(i))
    elif(i==18):
        print("                        Your seat number is: ",i)
        seat18=open('seat18.txt', 'w+')
        seat18.write(str(i))
    elif(i==19):
        print("                        Your seat number is: ",i)
        seat19=open('seat19.txt', 'w+')
        seat19.write(str(i))
    elif(i==20):
        print("                        Your seat number is: ",i)
        seat20=open('text20.txt.txt', 'w+')
        seat20.write(str(i))
    seatnum=open('seatnum.txt','w')
    seatnum.write("      Your seat number is: ")
    seatnum.write(str(i))
#----------------------------------------------------------------------------------
#seat2 function is alternative of seat function
def seat2(i):
    if(i==1):
        print("                        Your seat number is: ",i)
        seat1a=open('seat1.txt', 'w+')
        seat1a.write(str(i))
    elif(i==2):
        print("                        Your seat number is: ",i)
        seat2a=open('seat2.txt', 'w+')
        seat2a.write(str(i))
    elif(i==3):
        print("                        Your seat number is: ",i)
        seat3a=open('seat3.txt', 'w+')
        seat3a.write(str(i))
    elif(i==4):
        print("                        Your seat number is: ",i)
        seat4a=open('seat4.txt', 'w+')
        seat4a.write(str(i))
    elif(i==5):
        print("                        Your seat number is: ",i)
        seat5a=open('seat5.txt', 'w+')
        seat5a.write(str(i))
    elif(i==6):
        print("                        Your seat number is: ",i)
        seat6a=open('seat6.txt', 'w+')
        seat6a.write(str(i))
    elif(i==7):
        print("                        Your seat number is: ",i)
        seat7a=open('seat7.txt', 'w+')
        seat7a.write(str(i))
    elif(i==8):
        print("                        Your seat number is: ",i)
        seat8a=open('seat8.txt', 'w+')
        seat8a.write(str(i))
    elif(i==9):
        print("                        Your seat number is: ",i)
        seat9a=open('seat9.txt', 'w+')
        seat9a.write(str(i))
    elif(i==10):
        print("                        Your seat number is: ",i)
        seat10a=open('seat10.txt', 'w+')
        seat10a.write(str(i))
    elif(i==11):
        print("                        Your seat number is: ",i)
        seat11a=open('seat11.txt', 'w+')
        seat11a.write(str(i))
    elif(i==12):
        print("                        Your seat number is: ",i)
        seat12a=open('seat12.txt', 'w+')
        seat12a.write(str(i))
    elif(i==13):
        print("                        Your seat number is: ",i)
        seat13a=open('seat13.txt', 'w+')
        seat13a.write(str(i))
    elif(i==14):
        print("                        Your seat number is: ",i)
        seat14a=open('seat14.txt', 'w+')
        seat14a.write(str(i))
    elif(i==15):
        print("                        Your seat number is: ",i)
        seat15a=open('seat15.txt', 'w+')
        seat15a.write(str(i))
    elif(i==16):
        print("                        Your seat number is: ",i)
        seat16a=open('seat16.txt', 'w+')
        seat16a.write(str(i))
    elif(i==17):
        print("                        Your seat number is: ",i)
        seat17a=open('seat17.txt', 'w+')
        seat17a.write(str(i))
    elif(i==18):
        print("                        Your seat number is: ",i)
        seat18a=open('seat18.txt', 'w+')
        seat18a.write(str(i))
    elif(i==19):
        print("                        Your seat number is: ",i)
        seat19a=open('seat19.txt', 'w+')
        seat19a.write(str(i))
    elif(i==20):
        print("                        Your seat number is: ",i)
        seat20a=open('text20.txt.txt', 'w+')
        seat20a.write(str(i))
    seatnum=open('seatnum.txt','w')
    seatnum.write("      Your seat number is: ")
    seatnum.write(str(i))

    
#-----------------------------------------------------------------------------------
#timming function provides suitable timings accouding to the date entered
def timmings(a,b):
    loading()
    print("                        Available bus for selected date is:")
    if((a==1 and b==2) or (a==2 and b==1)):
        for i in range(0,4):
            print("                        ",Bhv_Ahm[i],":00  ",Bhv_Ahm[i+4],":00  ")
    elif((a==1 and b==3) or (a==3 and b==1)):
        for i in range(0,2):
            print("                        ",Bhv_Raj[i],":00  ",Bhv_Raj[i+3],":00  ")
    elif(a==1 and b==4 or (a==4 and b==1)):
        for i in range(0,2):
            print("                        ",Bhv_Bar[i],":00  ",Bhv_Bar[i+2],":00  ")
    elif(a==2 and b==4 or (a==4 and b==2)):
        for i in range(0,3):
            print("                        ",Ahm_Bar[i],":00  ",Ahm_Bar[i+4],":00  ")
    elif(a==2 and b==3 or (a==3 and b==2)):
        for i in range(0,2):
            print("                        ",Ahm_Raj[i],":00  ",Ahm_Raj[i+3],":00  ")
    elif(a==3 and b==4 or (a==4 and b==3)):
        for i in range(0,3):
            print("                        ",Raj_Bar[i],":00  ",Raj_Bar[i+2],":00  ")
    timetoboard=int(input("                        Enter time to board:"))
    if(timetoboard==0):
        mainMenu()
    print("                        Cost per seat for your selected choice is: 270")
    loading()
    print("                        Enter your seat from subsequent window.")
        
# todaysdate function provides further functionality to book seat for todays date with restrictes timmings available
def todaysdate(a,b):
    x=datetime.datetime.now()
    i=0
    loading()
    print("                        Available bus for selected date is:")
    for i in range(len(Bhv_Ahm)):
        if((x.hour<Bhv_Ahm[i] or x.hour<Ahm_Bhv[i])and ((a==1 and b==2) or (a==2 and b==1))):
            print("                        ",Bhv_Ahm[i],":00")
    for i in range(len(Bhv_Raj)):
        if((x.hour<Bhv_Raj[i] or x.hour<Raj_Bhv[i]) and((a==1 and b==3) or (a==3 and b==1))):
            print("                        ",Bhv_Raj[i],":00")
    for i in range(len(Bhv_Bar)):
        if((x.hour<Bhv_Bar[i] or x.hour<Bar_Bhv[i]) and ((a==1 and b==4) or (a==4 and b==1))):
            print("                        ",Bhv_Bar[i],":00")
    for i in range(len(Ahm_Raj)):
        if((x.hour<Ahm_Raj[i] or x.hour<Raj_Ahm[i]) and ((a==2 and b==4) or (a==4 and b==2))):
            print("                        ",Ahm_Raj[i],":00")
    for i in range(len(Ahm_Bar)):
        if((x.hour<Ahm_Bar[i] or x.hour<Bar_Ahm[i]) and((a==2 and b==3) or (a==3 and b==2))):
            print("                        ",Ahm_Bar[i],":00")
    for i in range(len(Raj_Bar)):   
        if((x.hour<Raj_Bar[i] or x.hour<Ahm_Bar[i]) and ((a==3 and b==4) or (a==4 and b==3))):
            print("                        ",Raj_Bar[i],":00")
    timetoboard=int(input("                        Enter time to board:"))
    if(timetoboard==0):
        MainMenu()
    timeToBoard=open('TimeToBoard.txt','w')
    timeToBoard.write(str(timetoboard))
    print("                        Cost per seat for your selected choice is: 270")
    loading()
    print("                        Enter your seat from subsequent window.")
print("\n")
print("                        ********************Welcome to YourBus**********************")
Bhv_Ahm=[5,7,10,13,16,19,20,22]
Bhv_Raj=[7,10,13,16,20,22]
Bhv_Bar=[7,10,16,20]
Ahm_Bhv=[5,7,10,13,16,19,20,22]
Ahm_Raj=[7,10,13,16,20,22]
Ahm_Bar=[5,7,10,13,16,19,20,22]
Raj_Bhv=[7,10,13,16,20,22]
Raj_Ahm=[7,10,13,16,20,22]
Raj_Bar=[7,10,16,20]
Bar_Bhv=[7,10,16,20]
Bar_Raj=[7,10,16,20]
Bar_Ahm=[5,7,10,13,16,19,20,22]
# from function takes input where you want to travel from starting point.
def From():
    print("                        Enter 1-Bhavnagar\n                        2-Ahmedabad\n                        3-Rajkot\n                        4-Vadodra")
    From=int(input("                        From:-"))
    fileFrom=open('From.txt', 'w')
    fromstr=str(From)
    fileFrom.write(fromstr)
    if(From>4):
        print("                        Enter valid number!!")
    elif(From==1):
        print("                        Bhavnagar")
    elif(From==2):
        print("                        Ahmedabad")
    elif(From==3):
        print("                        Rajkot")
    elif(From==4):
        print("                        Vadodra")
    elif(From==0):
        mainMenu(0)
#-----------------------------------------------------------------------------------
# from where to where you want to travel
def to():
    print("                        Enter 1-Bhavnagar\n                        2-Ahmedabad\n                        3-Rajkot\n                        4-Vadodra")
    to=int(input("                        To:-"))
    fileTo=open('To.txt', 'w')
    Tostr=str(to)
    fileTo.write(Tostr)
    if(to>4):
        print("                        Enter valid number!!")
    elif(to==1):
        print("                        Bhavnagar")
    elif(to==2):
        print("                        Ahmedabad")
    elif(to==3):
        print("                        Rajkot")
    elif(to==4):
        print("                        Vadodra")
    if(From==to):
        print("                        Enter valid location.")
    elif(to==0):
        mainMenu(0)
#--------------------------------------------------------------------------------------------
#seat1a function uses tkinter libraray which books your perffered seats and available seats.
def seat1a():
    screen = Tk()
    screen.title("##############Book your seats here###############")
    screen.geometry("500x500")
    screen.configure(background='black')
    instruction=Label(text="Instruction: Select your seat",fg="red", bg="cyan")
    instruction.pack()
    mainmenu=Button(text="Main Menu", height=3, width=12,bg='cyan',command=lambda i=1: MainMenu(i))
    mainmenu.place(x=220, y=430)
    seat1=open('seat1.txt', 'r')
    seatNo1=int(seat1.read())
    seat2=open('seat2.txt', 'r')
    seatNo2=int(seat2.read())
    seat3=open('seat3.txt', 'r')
    seatNo3=int(seat3.read())
    seat4=open('seat4.txt', 'r')
    seatNo4=int(seat4.read())
    seat5=open('seat5.txt', 'r')
    seatNo5=int(seat5.read())
    seat6=open('seat6.txt', 'r')
    seatNo6=int(seat6.read())
    seat7=open('seat7.txt', 'r')
    seatNo7=int(seat7.read())
    seat8=open('seat8.txt', 'r')
    seatNo8=int(seat8.read())
    seat9=open('seat9.txt', 'r')
    seatNo9=int(seat9.read())
    seat10=open('seat10.txt', 'r')
    seatNo10=int(seat10.read())
    seat11=open('seat11.txt', 'r')
    seatNo11=int(seat11.read())
    seat12=open('seat12.txt', 'r')
    seatNo12=int(seat12.read())
    seat13=open('seat13.txt', 'r')
    seatNo13=int(seat13.read())
    seat14=open('seat14.txt', 'r')
    seatNo14=int(seat14.read())
    seat15=open('seat15.txt', 'r')
    seatNo15=int(seat15.read())
    seat16=open('seat16.txt', 'r')
    seatNo16=int(seat16.read())
    seat17=open('seat17.txt', 'r')
    seatNo17=int(seat17.read())
    seat18=open('seat18.txt', 'r')
    seatNo18=int(seat18.read())
    seat19=open('seat19.txt', 'r')
    seatNo19=int(seat19.read())
    seat20=open('seat20.txt', 'r')
    seatNo20=int(seat20.read())

    if(seatNo1==1):
        seat1=Button(text="01", height=5, width=5, bg="red")
        seat1.place(x=10, y=20)
    else:
        seat1=Button(text="01", height=5, width=5, command=lambda i=1: seat(i))
        seat1.place(x=10, y=20)
    if(seatNo2==2):
        seat2=Button(text="02", height=5, width=5,bg="red")
        seat2.place(x=70, y=20)
    else:
        seat2=Button(text="02", height=5, width=5,command=lambda i=2: seat(i))
        seat2.place(x=70, y=20)
    if(seatNo3==3):
        seat3=Button(text="03", height=5, width=5,bg="red")
        seat3.place(x=160, y=20)
    else:
        seat3=Button(text="03", height=5, width=5,command=lambda i=3: seat(i))
        seat3.place(x=160, y=20)
    if(seatNo4==4):
        seat4=Button(text="04", height=5, width=5,bg="red")
        seat4.place(x=220, y=20)
    else:
        seat4=Button(text="04", height=5, width=5,command=lambda i=4: seat(i))
        seat4.place(x=220, y=20)
    if(seatNo5==5):
        seat5=Button(text="05", height=5, width=5,bg="red")
        seat5.place(x=10, y=120)
    else:
        seat5=Button(text="05", height=5, width=5,command=lambda i=5: seat(i))
        seat5.place(x=10, y=120)
    if(seatNo6==6):
        seat6=Button(text="06", height=5, width=5,bg="red")
        seat6.place(x=70, y=120)
    else:
        seat6=Button(text="06", height=5, width=5,command=lambda i=6: seat(i))
        seat6.place(x=70, y=120)
    if(seatNo7==7):
        seat7=Button(text="07", height=5, width=5,bg="red")
        seat7.place(x=160, y=120)
    else:
        seat7=Button(text="07", height=5, width=5,command=lambda i=7: seat(i))
        seat7.place(x=160, y=120)
    if(seatNo8==8):
        seat8=Button(text="08", height=5, width=5,bg="red")
        seat8.place(x=220, y=120)
    else:
        seat8=Button(text="08", height=5, width=5,command=lambda i=8: seat(i))
        seat8.place(x=220, y=120)
    if(seatNo9==9):
        seat9=Button(text="09", height=5, width=5,bg="red")
        seat9.place(x=10, y=220)
    else:
        seat9=Button(text="09", height=5, width=5,command=lambda i=9: seat(i))
        seat9.place(x=10, y=220)
    if(seatNo10==10):
        seat10=Button(text="10", height=5, width=5,bg="red")
        seat10.place(x=70, y=220)
    else:
        seat10=Button(text="10", height=5, width=5,command=lambda i=10: seat(i))
        seat10.place(x=70, y=220)
    if(seatNo11==11):
        seat11=Button(text="11", height=5, width=5,bg="red")
        seat11.place(x=160, y=220)
    else:
        seat11=Button(text="11", height=5, width=5,command=lambda i=11: seat(i))
        seat11.place(x=160, y=220)
    if(seatNo12==12):
        seat12=Button(text="12", height=5, width=5,bg="red")
        seat12.place(x=220, y=220)
    else:
        seat12=Button(text="12", height=5, width=5,command=lambda i=12: seat(i))
        seat12.place(x=220, y=220)
    if(seatNo13==13):
        seat13=Button(text="13", height=5, width=5,bg="red")
        seat13.place(x=10, y=320)
    else:
        seat13=Button(text="13", height=5, width=5,command=lambda i=13: seat(i))
        seat13.place(x=10, y=320)
    if(seatNo14==14):
        seat14=Button(text="14", height=5, width=5,bg="red")
        seat14.place(x=70, y=320)
    else:
        seat14=Button(text="14", height=5, width=5,command=lambda i=14: seat(i))
        seat14.place(x=70, y=320)
    if(seatNo15==15):
        seat15=Button(text="15", height=5, width=5,bg="red")
        seat15.place(x=160, y=320)
    else:
        seat15=Button(text="15", height=5, width=5,command=lambda i=15: seat(i))
        seat15.place(x=160, y=320)
    if(seatNo16==16):
        seat16=Button(text="16", height=5, width=5,bg="red")
        seat16.place(x=220, y=320)
    else:
        seat16=Button(text="16", height=5, width=5,command=lambda i=16: seat(i))
        seat16.place(x=220, y=320)
    if(seatNo17==17):
        seat17=Button(text="17", height=5, width=5,bg="red")
        seat17.place(x=10, y=320)
    else:
        seat17=Button(text="17", height=5, width=5,command=lambda i=17: seat(i))
        seat17.place(x=10, y=320)
    if(seatNo18==18):
        seat18=Button(text="18", height=5, width=5,bg="red")
        seat18.place(x=70, y=320)
    else:
        seat18=Button(text="18", height=5, width=5,command=lambda i=18: seat(i))
        seat18.place(x=70, y=320)
    if(seatNo19==19):
        seat19=Button(text="19", height=5, width=5,bg="red")
        seat19.place(x=160, y=320)
    else:
        seat19=Button(text="19", height=5, width=5,command=lambda i=19: seat(19))
        seat19.place(x=160, y=320)
    if(seatNo20==20):
        seat20=Button(text="20", height=5, width=5,bg="red")
        seat20.place(x=220, y=320)
    else:
        seat20=Button(text="20", height=5, width=5,command=lambda i=20: seat(20))
        seat20.place(x=220, y=320)
    
    start=time
    screen.after(15000, screen.destroy)
    mainloop()
    end = time()
    ticket()
#--------------------------------------------------------------------------------------------
#seat2a is alternative of above function
def seat2a():
    screen2 = Tk()
    screen2.title("##############Book your seats here###############")
    screen2.geometry("500x500")
    screen2.configure(background='black')
    instruction=Label(text="Instruction: Select your seat",fg="red", bg="cyan")
    instruction.pack()
    mainmenu=Button(text="Main Menu", height=3, width=12,bg='cyan',command=lambda i=1: MainMenu(i))
    mainmenu.place(x=220, y=430)
    seat1a=open('seat1a.txt', 'r')
    seatNo1a=int(seat1a.read())
    seat2a=open('seat2a.txt', 'r')
    seatNo2a=int(seat2a.read())
    seat3a=open('seat3a.txt', 'r')
    seatNo3a=int(seat3a.read())
    seat4a=open('seat4a.txt', 'r')
    seatNo4a=int(seat4a.read())
    seat5a=open('seat5a.txt', 'r')
    seatNo5a=int(seat5a.read())
    seat6a=open('seat6a.txt', 'r')
    seatNo6a=int(seat6a.read())
    seat7a=open('seat7a.txt', 'r')
    seatNo7a=int(seat7a.read())
    seat8a=open('seat8a.txt', 'r')
    seatNo8a=int(seat8a.read())
    seat9a=open('seat9a.txt', 'r')
    seatNo9a=int(seat9a.read())
    seat10a=open('seat10a.txt', 'r')
    seatNo10a=int(seat10a.read())
    seat11a=open('seat11a.txt', 'r')
    seatNo11a=int(seat11a.read())
    seat12a=open('seat12a.txt', 'r')
    seatNo12a=int(seat12a.read())
    seat13a=open('seat13a.txt', 'r')
    seatNo13a=int(seat13a.read())
    seat14a=open('seat14a.txt', 'r')
    seatNo14a=int(seat14a.read())
    seat15a=open('seat15a.txt', 'r')
    seatNo15a=int(seat15a.read())
    seat16a=open('seat16a.txt', 'r')
    seatNo16a=int(seat16a.read())
    seat17a=open('seat17a.txt', 'r')
    seatNo17a=int(seat17a.read())
    seat18a=open('seat18a.txt', 'r')
    seatNo18a=int(seat18a.read())
    seat19a=open('seat19a.txt', 'r')
    seatNo19a=int(seat19a.read())
    seat20a=open('seat20a.txt', 'r')
    seatNo20a=int(seat20a.read())

    if(seatNo1a==1):
        seat1a=Button(text="01", height=5, width=5, bg="red")
        seat1a.place(x=10, y=20)
    else:
        seat1a=Button(text="01", height=5, width=5, command=lambda i=1: seat2(i))
        seat1a.place(x=10, y=20)
    if(seatNo2a==2):
        seat2a=Button(text="02", height=5, width=5,bg="red")
        seat2a.place(x=70, y=20)
    else:
        seat2a=Button(text="02", height=5, width=5,command=lambda i=2: seat2(i))
        seat2a.place(x=70, y=20)
    if(seatNo3a==3):
        seat3a=Button(text="03", height=5, width=5,bg="red")
        seat3a.place(x=160, y=20)
    else:
        seat3a=Button(text="03", height=5, width=5,command=lambda i=3: seat2(i))
        seat3a.place(x=160, y=20)
    if(seatNo4a==4):
        seat4a=Button(text="04", height=5, width=5,bg="red")
        seat4a.place(x=220, y=20)
    else:
        seat4a=Button(text="04", height=5, width=5,command=lambda i=4: seat2(i))
        seat4a.place(x=220, y=20)
    if(seatNo5a==5):
        seat5a=Button(text="05", height=5, width=5,bg="red")
        seat5a.place(x=10, y=120)
    else:
        seat5a=Button(text="05", height=5, width=5,command=lambda i=5: seat2(i))
        seat5a.place(x=10, y=120)
    if(seatNo6a==6):
        seat6a=Button(text="06", height=5, width=5,bg="red")
        seat6a.place(x=70, y=120)
    else:
        seat6a=Button(text="06", height=5, width=5,command=lambda i=6: seat2(i))
        seat6a.place(x=70, y=120)
    if(seatNo7a==7):
        seat7a=Button(text="07", height=5, width=5,bg="red")
        seat7a.place(x=160, y=120)
    else:
        seat7a=Button(text="07", height=5, width=5,command=lambda i=7: seat2(i))
        seat7a.place(x=160, y=120)
    if(seatNo8a==8):
        seat8a=Button(text="08", height=5, width=5,bg="red")
        seat8a.place(x=220, y=120)
    else:
        seat8a=Button(text="08", height=5, width=5,command=lambda i=8: seat2(i))
        seat8a.place(x=220, y=120)
    if(seatNo9a==9):
        seat9a=Button(text="09", height=5, width=5,bg="red")
        seat9a.place(x=10, y=220)
    else:
        seat9a=Button(text="09", height=5, width=5,command=lambda i=9: seat2(i))
        seat9a.place(x=10, y=220)
    if(seatNo10a==10):
        seat10a=Button(text="10", height=5, width=5,bg="red")
        seat10a.place(x=70, y=220)
    else:
        seat10a=Button(text="10", height=5, width=5,command=lambda i=10: seat2(i))
        seat10a.place(x=70, y=220)
    if(seatNo11a==11):
        seat11a=Button(text="11", height=5, width=5,bg="red")
        seat11a.place(x=160, y=220)
    else:
        seat11a=Button(text="11", height=5, width=5,command=lambda i=11: seat2(i))
        seat11a.place(x=160, y=220)
    if(seatNo12a==12):
        seat12a=Button(text="12", height=5, width=5,bg="red")
        seat12a.place(x=220, y=220)
    else:
        seat12a=Button(text="12", height=5, width=5,command=lambda i=12: seat2(i))
        seat12a.place(x=220, y=220)
    if(seatNo13a==13):
        seat13a=Button(text="13", height=5, width=5,bg="red")
        seat13a.place(x=10, y=320)
    else:
        seat13a=Button(text="13", height=5, width=5,command=lambda i=13: seat2(i))
        seat13a.place(x=10, y=320)
    if(seatNo14a==14):
        seat14a=Button(text="14", height=5, width=5,bg="red")
        seat14a.place(x=70, y=320)
    else:
        seat14a=Button(text="14", height=5, width=5,command=lambda i=14: seat2(i))
        seat14a.place(x=70, y=320)
    if(seatNo15a==15):
        seat15a=Button(text="15", height=5, width=5,bg="red")
        seat15a.place(x=160, y=320)
    else:
        seat15a=Button(text="15", height=5, width=5,command=lambda i=15: seat2(i))
        seat15a.place(x=160, y=320)
    if(seatNo16a==16):
        seat16a=Button(text="16", height=5, width=5,bg="red")
        seat16a.place(x=220, y=320)
    else:
        seat16a=Button(text="16", height=5, width=5,command=lambda i=16: seat2(i))
        seat16a.place(x=220, y=320)
    if(seatNo17a==17):
        seat17a=Button(text="17", height=5, width=5,bg="red")
        seat17a.place(x=10, y=320)
    else:
        seat17a=Button(text="17", height=5, width=5,command=lambda i=17: seat2(i))
        seat17a.place(x=10, y=320)
    if(seatNo18a==18):
        seat18a=Button(text="18", height=5, width=5,bg="red")
        seat18a.place(x=70, y=320)
    else:
        seat18a=Button(text="18", height=5, width=5,command=lambda i=18: seat2(i))
        seat18a.place(x=70, y=320)
    if(seatNo19a==19):
        seat19a=Button(text="19", height=5, width=5,bg="red")
        seat19a.place(x=160, y=320)
    else:
        seat19a=Button(text="19", height=5, width=5,command=lambda i=19: seat2(19))
        seat19a.place(x=160, y=320)
    if(seatNo20a==20):
        seat20a=Button(text="20", height=5, width=5,bg="red")
        seat20a.place(x=220, y=320)
    else:
        seat20a=Button(text="20", height=5, width=5,command=lambda i=20: seat2(20))
        seat20a.place(x=220, y=320)
    
    start=time
    screen2.after(15000, screen2.destroy)
    mainloop()
    end = time()
    ticket()
#----------------------------------------------------------------------------------------------------
#input of date is done by this functions
def date():
    day=int(input("                        Enter day(dd-formate)of journey:"))
    month=int(input("                        Enter month(mm-formate) of journey:"))
    year=int(input("                        Enter year(yyyy-formate) of journey:"))
    date=open('date.txt','w+')
    date.write(str(day))
    date.write(" \ ")
    date.write(str(month))
    date.write(" \ ")
    date.write(str(year))
    
    x=datetime.datetime.now()
    if(year==x.year):
        if(month>x.month):
            if(day>0 and day<32):
                print("                        Your journey date is:", day,"/",month, "/",year)
                print("")
            elif(day==0):
                MainMenu(0)
        elif(month==x.month):
            if(day>=x.day):
               print("                        Your journey date is:",day,"/",month,"/",year)
               print("")
            else:
                print("                        Enter valid Date!!")
                print("")
                update()
    elif(year==0):
        mainMenu(0)
    else:
        print("                        Enter valid Date!!")
        print("")
        update()
    if(day==x.day):
        fileFrom=open('From.txt','r')
        fileTo=open('To.txt', 'r')
        duplicateFrom=int(fileFrom.readline())
        duplicateTo=int(fileTo.readline())
        todaysdate(duplicateFrom,duplicateTo)
        loading()
        seat1a()
    else:
        fileFrom=open('From.txt','r')
        fileTo=open('To.txt', 'r')
        duplicateFrom=int(fileFrom.readline())
        duplicateTo=int(fileTo.readline())
        timmings(duplicateFrom,duplicateTo)
        loading()
        seat2a()    
#----------------------------------------------------------------------------------
#this is not really recursive but will run the program till the ticket is booked.
From()
loading()
to()
loading()
date()
