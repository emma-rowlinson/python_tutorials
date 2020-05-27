class Bank:

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
        },
        "9999": {
            "account_num": "9999",
            "balance": float(1000000),
            "pin": "1994",
            "name": "Mr Monopoly"
        }
    }

    def getAccount(self, account_num):
        return self.accounts.get(account_num, "Invalid")

    def getBalance(self, account_num):
        return self.getAccount(account_num)['balance']

    def performWithdrawal(self, account_num, amount):
        account = self.getAccount(account_num)
        account['balance'] -= amount

    def performDeposit(self, account_num, amount):
        account = self.getAccount(account_num)
        account['balance'] += amount 

    def updatePin(self, account_num, newPin):
        account = self.getAccount(account_num)
        account['pin'] = newPin

    def performTransfer(self, from_acc_num, to_acc_num, amount): 
        # Add to destination account
        to_acc = self.getAccount(to_acc_num)
        to_acc['balance'] += amount
        # Subtract from current account
        from_acc = self.getAccount(from_acc_num)
        from_acc['balance'] -= amount