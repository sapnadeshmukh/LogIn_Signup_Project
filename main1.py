import re
import json

def checkUserName(dataInDic, userName):
    index = 0
    while (index < len(dataInDic['user'])):
        if(dataInDic['user'][index]['userName'] == userName):
            return True
        index = index + 1
    else:
        return "No"

def readJsonFile(fileName):
    try:
        openedJsonFile = open(fileName)
        readJsonFile = json.load(openedJsonFile)
        openedJsonFile.close()
        return readJsonFile
    except:
        return "noData"

def writeJsonFile(fileName, data):
    jsonData = json.dumps(data, indent = 4)
    jsonFile = open(fileName, 'w')
    jsonFile.write(jsonData)
    jsonFile.close()
    return jsonFile

def passwordValidation(pswrd):
    check = 0
    index = 0 
    while (index<len(pswrd)):
        if(pswrd[index] == "@" or pswrd[index] == "#"):
            check = check + 1
            break
        index = index + 1
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    index = 0
    while (index < 10):
        numInStr = str(digits[index])
        if(numInStr in pswrd):
            check = check + 1
            break
        index = index + 1
    return check

def userProfile():
    description = input("Please describe yourself -\n")
    DOB = input("Date of birth -\n")
    hobbies = input("Your hobbies -\n")
    gender = input("Gender -\n")
    profile = {
        "description": description,
        "dob": DOB,
        "hobbies": hobbies,
        "gender": gender,
    }
    return profile


signInSignUp = input("Sign-up(SU) or Sign-in(SI) :- ")
if (signInSignUp == "SU"):
    userName = input("User Name :- ")
    pswd1 = input("Password 1 :- ")
    pswd2 = input("Password 2 :- ")
    if(pswd1 != pswd2):
        print ("Both password are not same.")
    elif(True):
        validation = passwordValidation(pswd1)
        if(validation == 2):
            dataInDic = readJsonFile('userDetails.json')
            if(dataInDic == "noData"):
                data = {
                    "user": [{
                        "userName": userName,
                        "password": pswd1
                    }]
                }
                print ("Congrats " + userName + "! You are Signed Up Successfully." )
                userProfile = userProfile()
                data['user'][0]["profile"] = userProfile
                writeJsonFile('userDetails.json', data)
                print("")
                print("")
                print("")
                print(" *** ")
                print("Profile")
                print("Username :", end=" ")
                print(userName)
                print("Gender :", end=" ")
                print(userProfile["gender"])
                print("Bio :", end=" ")
                print(userProfile["description"])
                print("Hobbies :", end=" ")
                print(userProfile["hobbies"])
                print("Dob :", end=" ")
                print(userProfile['dob'])

            else:
                checked = checkUserName(dataInDic, userName)
                if(checked == "No"):
                    print ("Congrats " + userName + "! You are Signed Up Successfully." )
                    userProfile = userProfile()
                    newUser = {
                        "userName": userName,
                        "password": pswd1,
                        "profile": userProfile
                    }
                    dataInDic['user'].append(newUser)
                    writeJsonFile('userDetails.json', dataInDic)
                    print("")
                    print("")
                    print("")
                    print(" *** ")
                    print("Profile")
                    print("Username :", end=" ")
                    print(userName)
                    print("Gender :", end=" ")
                    print(userProfile["gender"])
                    print("Bio :", end=" ")
                    print(userProfile["description"])
                    print("Hobbies :", end=" ")
                    print(userProfile["hobbies"])
                    print("Dob :", end=" ")
                    print(userProfile['dob'])

                if(checked == True):
                    print("User Name already Exist.")
        else:
            print ("Atleast password should contain one spacial character and one number.")
if(signInSignUp == "SI"):
    userName = input("User Name :- ")
    pswd1 = input("Password 1 :- ")
    dataInDic = readJsonFile('userDetails.json')
    if(dataInDic == "noData"):
        print ("Invalid User Name and Password.")
    else:
        checked = checkUserName(dataInDic, userName)
        if(checked == "No"):
            print ("Invalid User Name and Password.")
        if(checked == True):
            print(userName, + "you are logged in successfully.")