# JSON 

{
    "name": "Kyle",
    "password": "Emma",
    "nicknames": ["", "", ""],
    "details": {
        "school": "",
        "classes": ["", ""]
    }
}

## Register Example
### Request
{
    "name": "kyle",
    "password": "iloveemma123"
}

### Response
{
    "success": true, # can be true or false
    "error": null,
    "token": "adghakcseld378eolaewysldonauwelor8"
    # can put whatever you want in response object
}

## Pseudo code 
This is the website

registerInfo = {"", ""} JSON
response = API.register(registerInfo)
if response["success"] == true:
    Do something
else:
    if error == "user_exists":
        OH no 

