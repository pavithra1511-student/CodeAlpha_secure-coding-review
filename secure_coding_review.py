import re

username = input("Enter Username: ")
password = input("Enter Password: ")

if not username.isalnum():
    print("Invalid Username")
    exit()

if len(password) < 8:
    print("Password must contain at least 8 characters")
elif not re.search(r"[A-Z]", password):
    print("Password must contain an uppercase letter")
elif not re.search(r"[a-z]", password):
    print("Password must contain a lowercase letter")
elif not re.search(r"\d", password):
    print("Password must contain a number")
else:
    print("Password is strong")
    print("Login validation completed successfully")
