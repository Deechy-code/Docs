import sys
import getpass
import string
import os

users=['user','user2','user3']
pins=['1234','2222','3333']
amounts=[1000,2000,3000]
count=0
while True:
    user=raw_input('\nEnter the username:',)
    user=user.lower()
    if user in users:
        if user == users[0]:
            n = 0
        elif user== users[1]:
            n = 1
        else:
            n = 2
        break
    else:
        print("******************")
        print("INVALID USERNAME")
        print("******************")



while count<3:
    print("***************")
    pin=str(getpass.getpass("Enter the pin:"))
    print("***************")
    if pin.isdigit():
        if user=='user':
            if pin==pins[0]:
                break
            else:
                count +=1
                print("************")
                print("Invalid pin number")
                print("************")
                print()
                
        if user=='user2':
            if pin==pins[1]:
                break
            else:
                count +=1
                print("************")
                print("Invalid pin number")
                print("************")
                print()

        if user=='user3':
            if pin==pins[2]:
                break
            else:
                count +=1
                print("************")
                print("Invalid pin number")
                print("************")
                print()
    else:
        print("**************")
        print("Pin Consist of 4 digit")
        print("**************")
        count +=1
if count==3:
    print("*************")
    print("****Unsuccessful attempt and your account is locked****")
    print("**************")
    exit()

print("***************")
print("Login Successful")
print("****************")
print()
print("*****************")
print(str.capitalize(users[n]),'Welcome to  HDFC Atm')
print("******************")
print("This is your ATM machine")


while True:
    print("**********************")
    response=raw_input("SELECT FROM FOLLOWING OPTIONS: \nStatement__(S) \nWithdraw___(W) \nLodgement__(L)  \nChange PIN_(P)  \nQuit_______(Q) \n: ").lower()
    print("**********************")
    valid_responses=['s','w','l','p','q']
    response==response.lower()
    if response=='s':
        print("*************")
        print('You have',amounts[n],"in indian rupees in our account")
        print("*************")
        
        
    elif response=='w':
        print("***************")
        cash_out=int(raw_input('Enter the Withdraw amount:'))
        print("***************");
        
        if cash_out%10 !=0:
            print("***********")
            print("Amount u want to withdraw must to match 10 indian note")
            print("************")
        elif cash_out>amounts[n]:
            print("*************")
            print("Insuffficient balance")
            print("*************")
        else:
            amounts[n]=amounts[n]-cash_out
            print("****************")
            print("Your new balance is:",amounts[n],"RUPEES")
            print("***************")
                     
                     
                     
    elif response=='l':
        print()
        print("***************")
        cash_in=int(raw_input("Enter amount you like to lodge"))
        print("***************")
        print()
        if cash_in%10 !=0:
            print("***********")
            print("Amount u want to lodge must to match 10 indian note")
            print("************")
       
        else:
            amounts[n]=amounts[n]+cash_in
            print("****************")
            print("Your new balance is:",amounts[n],"RUPEES")
            print("***************")
                     
    elif response=='p':
            print("**********")
            new_pin=str(getpass.getpass("enter a new pin:"))
            print("**********")
            if new_pin.isdigit() and new_pin!=pins[n] and len(new_pin)==4:
                     print("*********")
                     new_ppin=str(getpass.getpass("Confirm New Pin:"))
                     print("**********")
                     if new_ppin !=new_pin:
                            print("***********")
                            print("Mismatch")
                            print("**********")
                     else:
                          pins[n]=new_pin
                          print("New Pin Saved")
            else:
                     
                     print("*********")
                     print("New pin consist of 4 digit and must be different from previous one")
                     print("********")
                     
    elif response=='q':
        exit()
    else:
        print('------------------')
        print('Response not valid')
        print('------------------')
                     
                     
                    
                     
                     
                     
                     
                     
        
