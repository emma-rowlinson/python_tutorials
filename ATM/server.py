# Bank < -- REST API(HTTP Server) --> Website / App / Frontend
from flask import Flask
from flask import request

from bank import Bank

app = Flask(__name__) # sets name of server

bank = Bank()

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/account', methods=["POST"])
def account():
    json = request.get_json()

    account_num = json["account_num"]

    return bank.getAccount(account_num)


@app.route('/balance', methods=["POST"]) ## This is a decorator, it gives our function(balance) some extra information
# methods=["POST"] means it can take post requests, default is get requests
def balance(): 
    # request is provided by the decorator - https://flask.palletsprojects.com/en/1.1.x/api/?highlight=request#flask.request
    json = request.get_json()

    account_num = json['account_num']

    balance = bank.getBalance(account_num)
    return f"Your balance is £{balance}"


@app.route('/deposit', methods=["POST"])
def deposit():
    json = request.get_json()
    account_num = json["account_num"]
    amount = json["amount"]
    bank.performDeposit(account_num, amount)
    balance = bank.getBalance(account_num)
    return f"Your balance is £{balance}"

@app.route('/withdraw', methods=["POST"])
def withdraw():
    json = request.get_json()
    account_num = json["account_num"]
    amount = json["amount"]
    bank.performWithdrawal(account_num, amount)
    balance = bank.getBalance(account_num)
    return f"Your balance is £{balance}"

@app.route('/transfer', methods=["POST"])
def transfer():
    json = request.get_json()
    to_account_num = json["to_acc"]
    from_account_num = json["from_acc"]
    amount = json["amount"]
    bank.performTransfer(from_account_num, to_account_num, amount)
    return "Transfer Successful"

@app.route('/updatepin', methods=["POST"])
def updatepin():
    json = request.get_json()
    account_num = json["account_num"]
    new_pin = json["new_pin"]
    bank.updatePin(account_num, new_pin)
    return "PIN Updated" 





# HTTP METHODS: (HTTP IS NOT AN OBJECT) - https://www.w3schools.com/whatis/whatis_http.asp
#   - GET  
#       - http://www.google.co.uk -> When we go to this in the browser, it fires a Get request
#       - The response is the HTML, CSS and Javascript ( i.e the webpage )
#   - POST
#       - Body (request information)
#       - Headers (authorization)
#       - Example: Fill in a register form, POST request to API with a body(name, password, email etc.) (sent to the API), Response could be a webpage, or anything you want. Generally JSON
# There are others too