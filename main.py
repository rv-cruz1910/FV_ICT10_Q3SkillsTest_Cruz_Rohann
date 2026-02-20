from pyscript import display, document

def SIGNUP(e):
    document.getElementById('output').innerHTML = ''

    username = document.getElementById('name').value
    password = document.getElementById('pass').value

    if len(username) < 7:
        display(
            f"Your username is too short. Add at least {7 - len(username)} more character/s to proceed.",
            target="output"
        )

    if len(password) < 10:
        display(
            f"Your password is too short. Add at least {10 - len(password)} more character/s to proceed.",
            target="output"
        )

    if not any(char.isalpha() for char in password):
        display("Password must contain at least one letter.", target="output")

    if not any(char.isdigit() for char in password):
        display("Password must contain at least one number.", target="output")

    else:
        display("Your account has been created!", target="output")