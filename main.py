import os
from subprocess import call
from colorama import Fore

print("Welcome To the Airport")
print("This Airport Management App Is Made As The Final Project For the Python Fundamentals (Ms. Shokri) By "+Fore.GREEN+"Alireza Abedini"+Fore.RESET)
usernames = ["Admin"]
passwords = ["Admin"]
roleIsAdmin =[True]

flights = [
        {
           "From" : "Shiraz",
            "To" : "Tehran",
            "Price": 1000000
        },
        {
           "From" : "Tehran",
            "To" : "NewYork",
            "Price": 90000000
        },
]

global isinaccount
isinaccount = False
name = ""
isadmin = False

def clear():
    if os.name == 'nt':
        call('cls', shell=True)
    elif os.name == 'posix':
        call('clear', shell=True)

def addFlight(From, To, Price):
    newFlight = {
                    "From": From,
                    "To": To,
                    "Price": Price
                }
    flights.append(newFlight)
    print("[*] Flight Added Successfully")
    input()
# def delFlight(id):
#     try:
#         flights.remove(flights[id - 1])
#     except Exception:
#         print("Somthing Went Wrong!!")

def adminMenu():
    print("[ Wellcome Admin ]")
    print("Choose By Number")
    print("1) List Flights")
    print("2) Add Flight")
    print("3) Delete Flight")
    print("4) Go Back")
    while True:
        try:
            choice = int(input(">>> "))
        except KeyboardInterrupt:
            exit()
        except Exception:
            continue
        if choice == 1:
            listAllFlights()
        elif choice == 2:
            clear()
            From = input("From: ")
            To = input("To: ")
            Price = int(input("Price: "))
            addFlight(From, To, Price)
        elif choice == 3:
            # listAllFlights()
            # delFlight(input("Enter The Id To Delete The Flight: "))
            print("[X] Yet Still Under Construction")
        elif choice == 4:
            clear()
            break
        else:
            print("[X] Invalid Choice")
def login(): #
    print("Login ( Warning: This Operation is Case Sensitive )")
    while True:
        try:
            username = input("Username: ")
            password = input("Password: ")
            userid = usernames.index(username)
            passid = passwords.index(password)
            if userid != passid:
                if input("There Is No Account With These Information Do You Need To Go Back??(y/n)") == 'y':
                    break
                else:
                    print("\n____________________\n")
                    continue
        except KeyboardInterrupt:
            exit()
        except Exception:
            if input("There Is No Account With These Information Do You Need To Go Back??(y/n)") == 'y':
                break
            else:
                print("\n____________________\n")
                continue
        global isinaccount
        isinaccount = True
        global isadmin
        isadmin = roleIsAdmin[userid]
        break

def signup(): #
    print("So If You Don't Have an Account We'll Create One For You!! ( Warning: This Operation is Case Sensitive )")
    while True:
        username = input("Enter Your Preferred Username: ")
        if username in usernames:
            if input("A User With This Username Already Exists, Do You Need To Go Back??(y/n): ").lower() == 'y':
                clear()
                break
            else:
                continue
        password = input("Enter Your Preferred Password: ")
        usernames.append(username)
        passwords.append(password)
        roleIsAdmin.append(False)
        global isinaccount
        isinaccount = True
        break

def listAllFlights():
    if len(flights) == 0:
        print("There is no Flights Registered")
    else:
        # print(flights)
        for i in range(len(flights)):
            print(f"id = {i+1}\t From {flights[i]['From']} To {flights[i]['To']} \t Price = {str(flights[i]['Price'])} Toman per sit")
def BookAFlight():
    if len(flights) == 0:
        print("There is no Flights Registered")
    else:
        andis = 0
        for i in flights:
            andis += 1
            print(f"id = {andis}\t From {i['From']} To {i['To']} \t Price = {str(i['Price'])} Toman per sit")
    while True:
        try:
            choice = int(input("Enter the Id To Book The Flight: "))
            countOfSits = int(input("How Many Sits Do You Wanna Book? "))
            break
        except Exception:
            print("Something Went Wrong")
            continue

    clear()
    print("_"*50)
    print("[ Your Bill ]")
    print(f"The Trip Will Be Started From {flights[choice - 1]['From']} To {flights[choice - 1]['To']} Price = {flights[choice - 1]['Price']} per sit")
    print(f"You Have Purchased {countOfSits} Sits")
    print(f"[$] Total Price is "+ Fore.GREEN +f"{flights[choice - 1]['Price'] * countOfSits}"+Fore.RESET)
    print("_"*50)
    input()

while True:
    while isinaccount == False:
        try:
            haveAccount = input("Do You Have an Account(y/n) ( Ctrl + C To Exit ): ").lower()
        except KeyboardInterrupt:
            print(Fore.RED+"\nGoodBye"+Fore.RESET)
            exit()
        except Exception:
            continue
        if haveAccount == 'y':
            clear()
            login()
        elif haveAccount == 'n':
            clear()
            signup()
        else:
            print("invalid Choice Try Again!")
            continue
    clear()
    while isinaccount:
        print("Main Menu")
        print("(Choose By Number)")
        print("1) list Of Flights")
        print("2) Book A Flight")
        print("3) Clear The Console")
        print("4) Logout")
        print("5) Exit")
        if isadmin:
            print("6) Admin Menu")
        while True:
            try:
                choice = int(input(">>> "))
                break
            except KeyboardInterrupt:
                print(Fore.RED+"\nGoodBye"+Fore.RESET)
                exit()
            except Exception:
                continue
        if choice == 1:
            listAllFlights()
        if choice == 2:
            BookAFlight()
        elif choice == 3:
            clear()
            break
        elif choice == 4:
            clear()
            isadmin = False
            isinaccount = False
        elif choice == 5:
            exit()
        elif choice == 6:
            if not isadmin:
                print("[X] You Are Not Authorized To Access The Menu!!")
            clear()
            adminMenu()
        else:
            print("[X] Invalid Choice")