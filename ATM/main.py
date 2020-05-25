import os
import time

class ATM:

    account_pin = "1234"
    account_balance = float(250.00)
    account_num = ""
    def clear(self):
        os.system('clear') # Mac # clears terminal
        # os.system('cls') # Windows

    def balance(self):
        self.clear()
        print(f"Current balance: {self.account_balance}")
        input("Press any key to return to main menu:")
        #Go back to menu
        self.mainMenu()

    def withdraw(self):
        self.clear()
        print(f"Account balance: {self.account_balance}")
        withdrawal_amount = abs(float(input("Amount to withdraw: ")))
        remaining_bal = self.account_balance - withdrawal_amount
        if remaining_bal < 0:
            print("Insufficient funds, soz mate")
            input("Press any key to try again you broke bastard!")
            self.withdraw()
        print(f"Remaining account balance: {remaining_bal}")

        print(""" 
    'Y' to confirm withdrawal
    'N' to change withdrawal amount
    'X' to cancel withdrawal """)

        confirm = input("").upper()
        if confirm == "Y":
            self.account_balance = remaining_bal
            print(f"Please take your £{withdrawal_amount}!")
        elif confirm == "N":
            self.withdraw()
        elif confirm == "X":
            print("Withdrawal cancelled")
            

        input("Press any key to return to main menu:")
        #Go back to menu
        self.mainMenu()

    def deposit(self):
        self.clear()
        print(f"Account balance: {self.account_balance}")
        deposit_amount = abs(float(input("Amount to deposit: ")))
        new_bal = self.account_balance + deposit_amount
        print(f"New account balance: {new_bal}")

        print(""" 
    'Y' to confirm deposit
    'N' to change deposit amount
    'X' to cancel deposit """)

        confirm = input("").upper()
        if confirm == "Y":
            self.account_balance = new_bal
            print(f"Please insert your £{deposit_amount}!")
        elif confirm == "N":
            self.withdraw()
        elif confirm == "X":
            print("Deposit cancelled")
            

        input("Press any key to return to main menu:")
        #Go back to menu
        self.mainMenu()

    def transfer(self):
        print("Transfer")

        #Go back to menu
        self.mainMenu()

    def changePin(self):
        self.clear()
        # Check old pin first
        
        counter = 0
        while counter < 3:
            old_pin = input("Please enter current PIN:")
            if old_pin == self.account_pin:
                print("PIN entered successfully")
                break
            else:
                counter += 1
                print("Incorrect PIN, try again")
                if counter == 3:
                    print("BYEEEEE")
                    time.sleep(2)
                    self.mainMenu()
                continue

        # Update to new pin
        new_pin = input("Please enter new PIN:")
        confirm_pin = input("Re-enter new PIN:")
  
        if new_pin == confirm_pin:
            self.account_pin = new_pin
        else:
            print("PIN numbers don't match!")
            input("Press any key to continue")
            self.changePin()
        #Go back to menu
        self.mainMenu()

    def menuAction(self, action_num):
        switch = {
            "1": self.balance,
            "2": self.withdraw,
            "3": self.deposit,
            "4": self.transfer,
            "5": self.changePin
        }
        func = switch.get(action_num, lambda : self.menuAction(input('Invalid Selection, Try Again: '))) ## Recursion
        return func()

    def mainMenu(self):
        self.clear()
        print(f"Welcome, account number {self.account_num}")
        print("\n")
        print("Select an option: ")
        print("1. View Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Transfer")
        print("5. Change PIN")

        action_num = input()
        self.menuAction(action_num)

    def run(self):
        self.account_num = input("Enter your account number: ")
        counter = 0
        while counter < 3:
            pin = input("Enter your pin: ")
            if pin == self.account_pin:
                print("PIN entered successfully")
                self.mainMenu()
                break
            else:
                counter += 1
                print("Incorrect PIN, try again")
                if counter == 3:
                    print("BYEEEEE")
                    exit()
                continue

atm = ATM()
atm.run()