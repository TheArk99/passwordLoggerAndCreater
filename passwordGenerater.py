request = int(input("What do you want to do?\n\
Do you want to log a password or create on?\n\
Do you want to exit?\n\
Press 1. to Log a password or press 2. \
for creating one or press 3. to exit... "))
if request == 1:
    emailSite = input("Type your email or Site... ")
    emailSitePassword = input("Type your password... ")
    passwords = open("Passwords.txt", "a")
    passwords.write("\n     " + emailSite + ":") 
    passwords.write("\n     " + emailSitePassword + "\n")
    passwords.close()

    passwords = open("Passwords.txt", "r") 
    print("\nWhat is in Passwords.txt after appending...") 
    print(passwords.read()) 
    print() 
    passwords.close() 

elif request == 2:
    import random, string
    emailSite = input("\nWhat Email or site are you using this password for?... ")
    passwordLength = int(input("\nHow long should the password be? \
    Please tell me in numbers... "))
    passwordCharacters = string.ascii_letters + string.digits
    password = []
    for x in range(passwordLength):
        password.append(random.choice(passwordCharacters))

    truePassword = "".join(password)
    print(truePassword)

    passwords = open("Passwords.txt", "a")
    passwords.write("\n     " + emailSite + ":") 
    passwords.write("\n     " + truePassword + "\n")
    passwords.close()

    passwords = open("Passwords.txt", "r") 
    print("\nWhat is in Passwords.txt after appending...") 
    print(passwords.read()) 
    print() 
    passwords.close() 

elif request == 3:
    print("Thank you for using this little program, hope it was useful!")

else:
    print("Error you typed a(n) wrong input, \
    please try again with the correct input.")

