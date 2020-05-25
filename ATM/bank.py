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
        }
    }

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