import json
import re
user = input("Do you want to login / signup = ")
details = {}

while True:
    if user == "signup":
        is_valid = False
        user = input("enter username = ")
        password1 = input("enter password1 =")
        password2 = input("confirm a password =")
        if password1 == password2:
            print("Both passwords are same")
            if not re.search("[~!@#$%^&*]", password1):
                print("Not valid ! It should contain at least one letter in [~!@#$%^&*]")
                break
            if not re.search("[0-9]", password1):
                print("Not valid ! It should contain one letter between [1-9]")
                break
            else:
                is_valid = True
        else:
            print("password does not match")
            break
if(is_valid):
    with open("userdetails.json") as f:
        data = json.load(f)

    print("Password is valid")
    details["username"] = user
    details["password"] = password1
    data["userdetails"].append(details)

    with open("userdetails.json", "w") as final_file:
        json.dump(data, final_file)

    print("congrats" + " " + user + " " +
                    "You are signed Up Successfull!!!.")
    


else:
    print("Password is invalid")
    
            
