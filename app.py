from login import login

print("=== Git Workflow Simulator ===")

username = input("Enter username: ")
password = input("Enter password: ")

if login(username, password):
    print("Login Successful!")
else:
    print("Invalid Credentials!")
