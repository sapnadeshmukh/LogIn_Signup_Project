import json
import re

user = input("Do you want to login / signup = ")
details = {}
new={}
is_valid = True
if user == "signup":
    is_valid = False
    user = input("enter username = ")
    password1 = input("enter password1 =")
    password2 = input("confirm a password =")
    if password1 == password2:
        print("Both passwords are same")
        if not re.search("[~!@#$%^&*]", password1):
            print("Not valid ! It should contain at least one letter in [~!@#$%^&*]")
        if not re.search("[1-9]", password1):
            print("Not valid ! It should contain one letter between [1-9]")

        else:
            is_valid = True
    else:
        print("password does not match")
    if(is_valid):
        with open("userdetails.json") as f:
            data = json.load(f)

        for i in data["userdetails"]:
            if user in i["username"]:
                print("username already exists")
                break

       

        else:
            print("congrats" + " " + user + " " +"You are signed Up Successfull!!!.")

            
            Description=input("Wite saomething about You =")
            BirthDate=input("enter date of birth =")
            Hobbies=input("enter hobbies =")
            Gender=input("enter gender =")
            details["username"] = user
            details["password"] = password1
            new["description"]=Description
            new["dob"]=BirthDate
            new["hobbies"]=Hobbies
            new["gender"]=Gender
            details["profile"]=new
            data["userdetails"].append(details)

            with open("userdetails.json", "w") as final_file:
                json.dump(data, final_file,indent=4)



if user == "login":
    nam = input("enter username = ")
    password = input("enter password1 =")
    j_data=open("userdetails.json","r")
    a_data=json.load(j_data)
    j_data.close()
    i=0
    while i<len(a_data["userdetails"]):
        a=(a_data["userdetails"][i])
        if a["username"]==nam and a["password"]==password:
            print(nam  +" " + "You are logged in successfully!!!")
            print("****profile****")
            print("Username:" ,nam)
            print("Gender:",a["profile"]["gender"])
            print("Bio:",a["profile"]["description"])
            print("Hobbies:",a["profile"]["hobbies"])
            print("Dob:",a["profile"]["dob"])
            break
        i=i+1

    else:
        print("invalid password and username")
    
            
            
