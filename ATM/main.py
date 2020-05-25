import os
import time
from bank import Bank # import the Bank class


class ATM:

    accounts = {
        "5678": {
            "account_num": "5678",
            "balance": float(250.00),
            "pin": "1234",
            "name": "Kyle"
        },
        "9876": {
            "account_num": "9876",
            "balance": float(300.00),
            "pin": "1997",
            "name": "Emma"
        }
    }

    account_pin = "1234"
    account_balance = float(250.00)
    account_num = ""

    def getAccount(self):
        return self.accounts.get(self.account_num)

    def updateBalance(self, newBalance):
        account = self.getAccount()
        account['balance'] = newBalance

    def getAccountByNumber(self, account_num):
        return self.accounts.get(account_num)

    def performWithdrawal(self, account_num, amount):
        account = self.getAccountByNumber(account_num)
        account['balance'] -= amount

    def updatePin(self, newPin):
        account = self.getAccount()
        account['pin'] = newPin

    def performTransfer(self, to_acc_num, amount): 
        # Add to destination account
        to_acc = self.accounts.get(to_acc_num)
        to_acc['balance'] += amount
        # Subtract from current account
        from_acc = self.getAccount()
        from_acc['balance'] -= amount

    def clear(self):
        os.system('clear') # Mac # clears terminal
        # os.system('cls') # Windows

    def logout(self):
        self.account_num = ""
        self.login()

    def balance(self):
        self.clear()
        account = self.getAccount()
        print(f"Current balance: {account.get('balance')}")
        input("Press any key to return to main menu:")
        #Go back to menu
        self.mainMenu()

    def withdraw(self):
        self.clear()
        account = self.getAccount()
        bal = account.get('balance')
        print(f"Account balance: {bal}")
        withdrawal_amount = abs(float(input("Amount to withdraw: ")))
        remaining_bal = bal - withdrawal_amount
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
            self.updateBalance(remaining_bal)
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
        account = self.getAccount()
        bal = account.get('balance')
        print(f"Account balance: {bal}")
        deposit_amount = abs(float(input("Amount to deposit: ")))
        new_bal = bal + deposit_amount
        print(f"New account balance: {new_bal}")

        print(""" 
    'Y' to confirm deposit
    'N' to change deposit amount
    'X' to cancel deposit """)

        confirm = input("").upper()
        if confirm == "Y":
            self.updateBalance(new_bal)
            print(f"Please insert your £{deposit_amount}!")
        elif confirm == "N":
            self.withdraw()
        elif confirm == "X":
            print("Deposit cancelled")
            

        input("Press any key to return to main menu:")
        #Go back to menu
        self.mainMenu()

    def amountInput(self, bal):
        transfer_amount = float(input("Amount to transfer: "))
        remaining_bal = bal - transfer_amount
        if remaining_bal < 0:
            print("Insufficient funds!")
            time.sleep(1)
            return self.amountInput(bal)
        return (remaining_bal, transfer_amount)

    def transfer(self):
        self.clear()
        account = self.getAccount()
        bal = account.get('balance')
        print(f"Balance in current account is £{bal}")
        to_acc_num = input("Account Num to transfer money to: ")
        check = self.accounts.get(to_acc_num, "Invalid")
        if check == "Invalid":
            print("Invalid account, please try again!")
            self.transfer()
        (remaining_bal, transfer_amount) = self.amountInput(bal)

        print(f"Remaining balance after transfer is £{remaining_bal}")

        print(""" 
    'Y' to confirm transfer
    'N' to change transfer amount
    'X' to cancel transfer """)

        confirm = input("").upper()
        if confirm == "Y":
            self.performTransfer(to_acc_num, transfer_amount)
            print(f"Your transfer of £{transfer_amount} has been completed!")
        elif confirm == "N":
            self.transfer()
        elif confirm == "X":
            print("transfer cancelled")
            
        input("Press any key to return to main menu:")
        #Go back to menu
        self.mainMenu()

    def changePin(self):
        self.clear()
        # Check old pin first
        
        counter = 0
        while counter < 3:
            old_pin = input("Please enter current PIN:")
            if old_pin == self.getAccount().get('pin'):
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
            self.updatePin(new_pin)
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
            "5": self.changePin,
            "0": self.logout
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
        print("0. Logout")

        action_num = input()
        self.menuAction(action_num)

    def login(self):
        self.clear()
        self.account_num = input("Enter your account number: ")
        # Get account from dictionary
        account = self.accounts.get(self.account_num, "Invalid") # this is a dict
        # Check if account is null
        if account == "Invalid":
            print("Invalid account number, please try again")
            time.sleep(2)
            self.login()


        counter = 0
        while counter < 3:
            pin = input("Enter your pin: ")
            if pin == account.get("pin"):
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
atm.login()