
# Bank Accounts
Create a command line interface that mimics a basic ATM 
## Fields
- AccountNumber
- Name
- Balance
- Pin

## Actions
- View Balance
- Withdraw
- Deposit
- Transfer
- Change Pin

# Extra
## General
- Use hashes for pin instead of plain text 
- Use a csv file for persistent storage between sessions

## DB
- Use a SQL database instead of a csv

## Http service
- Create a flask server with following endpoints to run actions
    - Balance
        - Request Body 
            - Account Number
            - Pin
        - Response
            - Account Number
            - Balance
    - Withdraw
        - Request Body 
            - Account Number
            - Pin
            - Amount
        - Response
            - Status
                - Success
                - Insufficent Funds
            - NewBalance
    - Deposit
        - Request Body 
            - Account Number
            - Pin
            - Amount
        - Response
            - Status
                - Success
                - Error
            - NewBalance
    - Transfer
        - Request Body 
            - Pin
            - Amount
            - Receiver Account Number
        - Response
            - Status
                - Success
                - InsufficientFunds
            - NewBalance
    - Change Pin
        - Request Body 
            - OldPin
            - NewPin
        - Response
            - Status
                - Success
                - Error

### Frontend
- Create a web frontend that uses the bank API service to perform the actions. This can be HTML, CSS and flask or another framework such as ReactJS
