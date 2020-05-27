# Bank < -- REST API(HTTP Server) --> Website / App / Frontend
from flask import Flask
from flask import request

from bank import Bank

app = Flask(__name__) # sets name of server

bank = Bank()

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/account')
def account():
    return bank.getAccount("")

@app.route('/balance') # route is a function in the app module
def balance():
    balance = bank.getBalance("")
    return f"Your balance is £{balance}"

@app.route('/post', methods=["POST"]) ## This is a decorator, it gives our function(post) some extra information
# methods=["POST"] means it can take post requests, default is get requests
def post(): 
    # request is provided by the decorator - https://flask.palletsprojects.com/en/1.1.x/api/?highlight=request#flask.request
    json = request.get_json()

    account_num = json['account_num']

    balance = bank.getBalance(account_num)
    return f"Your balance is £{balance}"




# HTTP METHODS: (HTTP IS NOT AN OBJECT) - https://www.w3schools.com/whatis/whatis_http.asp
#   - GET  
#       - http://www.google.co.uk -> When we go to this in the browser, it fires a Get request
#       - The response is the HTML, CSS and Javascript ( i.e the webpage )
#   - POST
#       - Body (request information)
#       - Headers (authorization)
#       - Example: Fill in a register form, POST request to API with a body(name, password, email etc.) (sent to the API), Response could be a webpage, or anything you want. Generally JSON
# There are others too