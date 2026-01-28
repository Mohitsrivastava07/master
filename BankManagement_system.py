import random
import time
import qrcode
import sys

records = {
    "Name" : ["Mohit", "Naitik", "Ayush"],
    "Pass" : ["123@", "1234@", "12345@"],
    "acc" : [10242, 21457, 45876],
    "bal" : [1024.45, 1028.46, 1030.48]
}

while True:
    print()
    print("." * 100)
    print("*" * 100)
    print("Bank Management System". center(100))
    print("*" * 100)
    print("." * 100)
    print()

    while True:
        print()
        print(f"""
                1. Account Creation
                2. Deposits
                3. Withdrawals
                4. Balance Inquiry 
                5. QR-Code 
                6. Exits """)

        try:
            choice = int(input("\nChoice any option to go to next process --> "))
            print(f"You choice is {choice}")
        except ValueError:
           print("Enter only number!")
           continue

        # for Account Creation
        if (choice == 1):
            print()
            print("*" * 100)
            print("1. Account Creation". center(100))
            print("*" * 100)
            print()
            
            name = input("Enter your name --> ")     
            pin = input("Enter your pin --> ")
            
            # if pin and name both are not in pass and name of record.
            if pin not in records["Pass"] and name not in records["Name"]:

                text1 = "Your account number is generated!!"
                for word in text1.split():
                    print(word, end=" ", flush=True)
                    time.sleep(0.6)

                # random number to generate randomly as 5-digits
                acc = random.randint(10000, 99999)
                print(f"\nAccount number --> {acc}")
                
                # appending the new user into particular list of records
                records["Name"].append(name)
                records["Pass"].append(pin)
                records["acc"].append(acc)
                records["bal"].append(0.0)
                
                print(f"""
                        Username --> {name}
                        Password --> {pin}
                        Account --> {acc}
                        Balance --> 0.0""")        
            else:
                print("This name or pin both are available")
                print("Please! create the other name and pin")
        
        # for deposits  
        elif (choice == 2):
            print()
            print("*" * 100)
            print("2. Deposits Option". center(100))
            print("*" * 100)
            print()
            
            name = input("Enter your name --> ")
            acc = int(input("Enter your account --> "))
            pin = input("Enter your pin --> ")
            
            if name in records["Name"]:
                i = records["Name"].index(name)
                
                if records["Pass"][i] == pin and records["acc"][i] == acc:
                    amount = float(input("Enter the amount --> "))
                    
                    if amount >= 0:
                        records["bal"][i] += amount
                        
                        text2 = "Your amount will deposited!!"
                        for word in text2.split():
                            print(word, end=" ", flush=True)
                            time.sleep(0.6)
                        print(f"\nUpdate balance --> {records['bal'][i]}")
                        
                    else:
                        print("Invalid amount deposits")    
                else:
                    print("Invalid Password and Account number")
            else:
                print("Account not found!!")   
        
        # for withdrawals
        elif (choice == 3):
            print()
            print("*" * 100)
            print("3. Withdrawal Option". center(100))
            print("*" * 100)
            print()
            
            name = input("Enter your name --> ")
            acc = int(input("Enter your account --> "))
            pin = input("Enter your pin --> ")
            
            if name in records["Name"]:
                i = records["Name"].index(name)
                
                if records["Pass"][i] == pin and records["acc"][i] == acc:
                    w_amount = float(input("Enter the withdrawals amounts --> "))
                    
                    if (w_amount <= records["bal"][i]):
                        records["bal"][i] -= w_amount
                        print("Your amount will withdrawaled!")
                        print(f"Update balance --> {records['bal'][i]}")
                    else:
                        print("Invalid withdrawal amount!")
                else:
                    print("Invalid Password and Account number!")
            else:
                print("Invalid username!")
        
        # for balance inquiry
        elif (choice == 4):
            print()
            print("*" * 100)
            print("4. Balance Inquiry".center(100))
            print("*" * 100)
            print()
            
            name = input("Enter your name --> ")
            acc = int(input("Enter your account --> "))
            pin = input("Enter your pin --> ")
            
            if name in records["Name"]:
                i = records["Name"].index(name)
                
                if records["Pass"][i] == pin and records["acc"][i] == acc:
                    print(f"Your total balance --> {records['bal'][i]}")
                else:
                    print("Invalid Password and Account!")
            else:
                print(f"Invalid username!")
        
        # for generated the qrcode of particular list of records
        elif (choice == 5):
            print()
            print("*" * 100)
            print("5. QR-Code Generation".center(100))
            print("*" * 100)
            print()
            
            # Ask for the username
            name = input("Enter the username to generate QR --> ").strip()
            
            if name in records["Name"]:
                # get the index of the user
                i = records["Name"].index(name)
                
                # prepare the user data
                user_data = f"""
                Username: {records['Name'][i]}
                Account: {records['acc'][i]}
                Password: {records['Pass'][i]}
                Balance: {records['bal'][i]}
                """
                # generate the QR code
                img = qrcode.make(user_data)
                
                # save the QR code as an image
                img.save(f"{name}_QR.png")
                
                # show the QR code
                # img.show()
                
                print(f"QR code generated for {name} and saved as {name}_QR.png")
            else:
                print("Username not found!")
        
        # for exits       
        elif (choice == 6):
            print()
            print("*" * 100)
            print("6. Exits".center(100))
            print("*" * 100)
            print()
            
            ans = input("Do you want to exits (y/n) --> ")
            if ans == "y":
                sys.exit("Thank you for using Bank Management System")
        else:
            print("Invalid option! Please choose between 1–6.")
                