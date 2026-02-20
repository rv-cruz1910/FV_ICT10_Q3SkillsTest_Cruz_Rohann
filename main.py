from pyscript import display, document

def SIGNUP(e):
    document.getElementById('output').innerHTML = ''

    username = document.getElementById('name').value
    password = document.getElementById('pass').value
    #counts amount of characcters in a username, if less than 7, it is invalid
    if len(username) < 7:
        display(f"Your username is too short. Add at least {7 - len(username)} more character/s to proceed.",
            target="output")
   #counts amount of characcters in a password, if less than 10, it is invalid
    if len(password) < 10:
        display(f"Your password is too short. Add at least {10 - len(password)} more character/s to proceed.",
            target="output")
    #looks for atleast one letter in the password because it is part of the conditions
    if not any(char.isalpha() for char in password):
        display("Password must contain at least one letter.", target="output")
    #looks for atleast one number in the password because it is part of the conditions
    if not any(char.isdigit() for char in password):
        display("Password must contain at least one number.", target="output")

    else:
        display("Your account has been created!", target="output")