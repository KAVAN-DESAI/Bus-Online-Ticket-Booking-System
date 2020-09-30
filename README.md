# Bus-Online-Ticket-Booking-System
A Bus Online Ticket Booking system, which uses GUI in python. Real time Online ticket booking system.

### Installation: -

* Run a program that makes 20 file with required name as per sequence!
* The just Download "Bus-Online-Ticket-Booking-System.py" file. 
* Just make sure that the all files are in same folder to avoid ERROR'S.

Note: - The latest version of Python is installed (Though latest version is not required).

###  About project: -

#### Libraries: -
```python
from tkinter import *
import datetime
from tkinter import Tk, mainloop,TOP
from time import time
import sys
```
* Tkinter is used for booking seats which is GUI.
*datetime is used for real time operations and booking.
*time is used to add a extra feature to the project of loading.

#### Functions: -

##### Main function: -

```python
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
```
* Main function is build for UPDATE, CANCEL, EXIT feature.

##### Update function: -

```python
def update():
    From()
    loading()
    to()
    loading()
    date()
    loading()
```
* Update function updates all information and cancels the present wrong information

##### Loading function: -
```python
def loading():
    import time
    print(">>>Loading", end="")
    time.sleep(0.75)
    print(".",end="")
    time.sleep(0.75)
    print(".",end="")
    time.sleep(0.75)
    print(".")
```
* Loading function add the feature of loading with the use of time library.

##### Ticket function: -
```python
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
```
*Ticket function is one of the most important function.
*It deals with the information of the user/costumer.
*It uses file I/O and real time operation to book ticket will available seats.

##### Seat function: -

*Both seat function deals with booking the seats.
*It takes care the no two costumers book the same seat.
*And booked seats are not rebooked by another costumer.

##### Timming function: -

```python
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
```
*Timming function provide real time bus availability.
*According to choosen city, it provides the available bus timmings.

##### Todaysdate function: -

*It is specific to the day of booking.
*as this project deals with real time booking.

##### From and To function: -

This both function takes input of from which city to which city the costumer wants 
to travel. And the time to board of the costomer with price details.

##### Seat1a and Seat2a function: -

This functions deals with the tkinter library.
As the costumer will be shown a window which shows the available seat with cyan colour
and booked seats with red colour.
Here, costumer will not be able to select the red seats.
After few seconds the window will close and a notification will be provided
that they have booked "x numbered seat".

##### Date function: -

*Date function is prompt towards selection of correct date, i.e. it will not
accept the pass date.

#### Calling the functions: -

```python

From()
loading()
to()
loading()
date()

```

*This is not recursive, it will run till the costumer/user completely books the ticket!


#### Quick Approch: -

*This project deals with real time ticket booking.
*user/costumer has to input some basic detalis as name and gender etc.
*Then user is provide available timmings for specific date city and all.
*The tkinter library is used to book the seat number in bus(which is GUI).
*And at last the user is provide the copy of ticket with details.
