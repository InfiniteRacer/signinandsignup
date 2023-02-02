global userreal
global passreal
global keycode

userreal = ''
passreal = ''
keycode = ''

def userafter():

    userinput=input("Username? (Enter 'n' to cancel) ")
    
    if userinput == userreal:
        print("")
        passwordafter()
    elif userinput == 'n':
        print("")
        print("Canceled!")
        print("")
        start()
    else:
        print("")
        print("There is no user with that username. Try again.")
        print("")
        userafter()
        
def passwordafter():
    
    passwordinput=input("Password? (Enter 'n' to cancel) ")
    
    if passwordinput == passreal:
        print("")
        print("Loading you in...")
        print("")
        loggedinname()
    elif passwordinput == 'n':
        print("")
        print("Canceled!")
        print("")
        start()
    else:
        print("")
        print("Wrong! Try again.")
        print("")
        passwordafter()

def user():

    print("Login Portal:")
    print("")

    userinput=input("Username? (Enter 'n' to cancel) ")
    
    if userinput == userreal:
        print("")
        password()
    elif userinput == 'n':
        print("")
        print("Canceled!")
        print("")
        start()
    else:
        print("")
        print("There is no user with that username. Try again.")
        print("")
        user()
        
def password():
    
    passwordinput=input("Password? (Enter 'n' to cancel) ")
    
    if passwordinput == passreal:
        print("")
        print("Loading you in...")
        print("")
        loggedinfirst()
    elif passwordinput == 'n':
        print("")
        print("Canceled!")
        print("")
        start()
    else:
        print("")
        print("Wrong! Try again.")
        print("")
        password()
        
def userkeycode():

    userinput=input("Username? ")
    
    if userinput == userreal:
        print("")
        passwordkeycode()
    else:
        print("")
        print("There is no user with that username. Try again.")
        print("")
        userkeycode()
        
def passwordkeycode():
    
    passwordinput=input("Password? ")
    
    if passwordinput == passreal:
        print("")
        print("Loading you in...")
        print("")
        resetkeycodecontinue()()
    else:
        print("")
        print("Wrong! Try again.")
        print("")
        passwordkeycode()
        
def userpasscode():

    userinput=input("Username? ")
    
    if userinput == userreal:
        print("")
        passwordpasscode()
    else:
        print("")
        print("There is no user with that username. Try again.")
        print("")
        userpasscode()
        
def passwordpasscode():
    
    passwordinput=input("Password? ")
    
    if passwordinput == passreal:
        print("")
        print("Loading you in...")
        print("")
        resetpasscodecontinue()()
    else:
        print("")
        print("Wrong! Try again.")
        print("")
        passwordpasscode()
        
def loggedinfirst():
    
    global nameuser
    
    nameuser=input("What is your name? ")
    print("")
    loggedinname()
    
def loggedinname():
    
    print("Hello " +nameuser+ "!")
    print("")
    loggedin()
    
def loggedin():

    print("Enter '1' for settings.")
    print("Enter '2' to log out.")
    print("")
    
    loggedinmenu=input("Enter your number choice: ")
    print("")
    
    if loggedinmenu == '1':
        
        settings()
    
    elif loggedinmenu == '2':
        
        print("Logging you out...")
        print("")
        startafter()
    else:
        print("Invalid Input.")
        print("")
        loggedin()
        
def settings():

    print("Enter '1' to reset your username.")
    print("Enter '2' to reset your password.")
    print("Enter '3' to reset your keycode.")
    print("Enter '4' to delete your account.")
    print("Enter '5' to go back.")
    print("")
    
    loggedinmenu=input("Enter your number choice: ")
    print("")
    
    if loggedinmenu == '1':
        
        resetusername()
        
    elif loggedinmenu == '2':
        
        resetpassword()
        
    elif loggedinmenu == '3':
        
        resetkeycode()
        
    elif loggedinmenu == '4':
        
        deleteacc()
        
    elif loggedinmenu == '5':
        
        loggedinname()
        
    else:
        print("Invalid Input.")
        print("")
        settings()
    
def resetpassword():
    
    print("Reset password.")
    resetcontinue=input("Are you sure you want to continue? (y/n) ")
    print("")
    
    if resetcontinue == 'y':
        resetpasswordcontinue()
    elif resetcontinue == 'n':
        settings()
    else:
        print("Invalid Input. Try again...")
        print("")
        resetpassword()
        
def resetkeycode():
    
    print("Reset keycode.")
    resetcontinue=input("Are you sure you want to continue? (y/n) ")
    print("")
    
    if resetcontinue == 'y':
        resetkeycodecontinue()
    elif resetcontinue == 'n':
        settings()
    else:
        print("Invalid Input. Try again...")
        print("")
        resetkeycode()
        
def resetpasswordcontinue():
    
    global passreal
    
    passcheck=input("New password: ")
    
    if passcheck == passreal:
        
        print("")
        print("Password cannot be the same as before!")
        print("")
        
        resetpasswordcontinue()
    
    passchecktwo=input("Enter password again: ")
    
    if passcheck == passchecktwo:
        print("")
        
        passreal = passchecktwo
        
        print("Success!")
        print("")
        
        settings()
    
    else:
        print("")
        print("Passwords don't match. Try again.")
        print("")
        
        resetpasswordcontinue()
    
def resetkeycodecontinue():

    global keycode
    
    keycodecheckpoint=input("Password to continue: (Enter 'n' to go back) ")
    
    if keycodecheckpoint == passreal:
        
        print("")
        
    elif keycodecheckpoint == 'n':
        
        print("")
        print("Reset stopped.")
        print("")
        settings()
        
    else:
        
        print("")
        print("Wrong. Try again.")
        print("")
        resetkeycodecontinue()
    
    keycheck=input("New key code: ")
    
    if keycheck == keycode:
        
        print("")
        print("Keycodes cannot be the same as before!")
        print("")
        
        resetkeycodecontinue()
    
    keychecktwo=input("Enter key code again: ")
    
    if keycheck == keychecktwo:
        
        print("")
        
        keycode = keychecktwo
        
        print("Success!")
        print("")
        
        settings()
        
    else:
        print("")
        print("Key codes don't match. Try again.")
        print("")
        
        resetkeycodecontinue()
        
def start():
    
    print("Login Portal:")
    print("")
    
    starttwo()
    
def starttwo():
    
    print("Enter '1' for sign in.")
    print("Enter '2' for sign up.")
    print("")
    
    startchoice=input("Enter choice here: ")
    print("")
    
    if startchoice == '1':
        
        user()
        
    elif startchoice == '2':
    
        signup()
    
    else:
        
        print("Invalid Input. Try again.")
        print("")
        starttwo()
        
def startafter():
    
    print("Login Portal:")
    print("")
    
    starttwoafter()
    
def starttwoafter():
    
    print("Enter '1' for sign in.")
    print("Enter '2' for sign up.")
    print("")
    
    startchoice=input("Enter choice here: ")
    print("")
    
    if startchoice == '1':
        
        userafter()
        
    elif startchoice == '2':
    
        signup()
    
    else:
        
        print("Invalid Input. Try again.")
        print("")
        starttwoafter()
        
def signup():
    
    global userreal
    
    userreal=input("What would you like your username to be?: (Enter 'n' to cancel) ")
    
    if userreal == 'n':
        
        userreal = ''
        
        print("")
        print("Sign up canceled!")
        print("")
        start()
        
    else:
        
        print("")
    
    signuppass()
    
def signuppass():
    
    global userreal
    global passreal
    
    passchecksign=input("What would you like your password to be?: (Enter 'n' to cancel) ")
    
    if passchecksign == 'n':
        
        userreal = ''
        passreal = ''
        
        print("")
        print("Sign up canceled!")
        print("")
        start()
    
    passchecktwosign=input("Enter password again: (Enter 'n' to cancel) ")
    
    if passchecktwosign == 'n':
        
        userreal = ''
        passreal = ''
        
        print("")
        print("Sign up canceled!")
        print("")
        start()
    
    if passchecksign == passchecktwosign:
        print("")
        
        passreal = passchecktwosign
        
        signupkeycode()
        
    else:
        print("")
        print("Passwords don't match. Try again.")
        print("")
        
        signuppass()
        
def signupkeycode():
    
    global userreal
    global passreal
    global keycode

    keychecksign=input("What would you like your keycode to be?: (Enter 'n' to cancel) ")
    
    if keychecksign == 'n':
        
        userreal = ''
        passreal = ''
        keycode = ''
        
        print("")
        print("Sign up canceled!")
        print("")
        
        start()
    
    keychecktwosign=input("Enter keycode again: (Enter 'n' to cancel) ")
    
    if keychecktwosign == 'n':
        
        userreal = ''
        passreal = ''
        keycode = ''
        
        print("")
        print("Sign up canceled!")
        print("")
        
        start()
    
    if keychecksign == keychecktwosign:
        print("")
        
        keycode = keychecktwosign
        
        print("Success! Please login to continue setup.")
        print("")
        
        start()
        
    else:
        print("")
        print("Codes don't match. Try again.")
        print("")
        
        signupkeycode()
        
def deleteacc():
    
    print("Deleting account process.")
    print("")
    deleteacc2()
    
def deleteacc2():
    
    checkpointdel=input("Are you sure you want to delete your account? (y/n) ")
    
    if checkpointdel == 'y':
        print("")
        deleteacc3()
    elif checkpointdel == 'n':
        print("")
        print("Process stopped.")
        print("")
        loggedin()
    else:
        print("")
        print("Invalid input. Try again.")
        print("")
        deleteacc2()
        
def deleteacc3():
    
    checkpointdel=input("Agree to: login details will no longer work and you will to to sign up again: (y/n) ")
    
    if checkpointdel == 'y':
        print("")
        deleteaccfinal()
    elif checkpointdel == 'n':
        print("")
        print("Process stopped.")
        print("")
        loggedin()
    else:
        print("")
        print("Invalid input. Try again.")
        print("")
        deleteacc3()
        
def deleteaccfinal():
    
    global userreal
    global passreal
    global keycode
    
    checkdel=input("Enter password: ")
    
    if checkdel == passreal:
        print("")
        checkdelogin=input("Enter keycode: ")
        
        if checkdelogin == keycode:
            print("")
            print("Account has been deleted.")
            print("")
            
            userreal = ''
            passreal = ''
            keycode = ''
            
            start()
        else:
            print("")
            print("Incorrect keycode. Please start and try again.")
            print("")
            deleteaccfinal()
    else:
        print("")
        print("Incorrect password. Please try again.")
        print("")
        deleteaccfinal()
        
def resetusername():
    
    print("Reset username.")
    print("")
    
    resetusernamestart()
    
def resetusernamestart():
    
    checkpointuser=input("Enter your password to continue: (Enter 'n' to cancel) ")
    
    if checkpointuser == passreal:
        
        print("")
        resetusernamecon()
        
    elif checkpointuser == 'n':
    
        print("")
        print("Resetting stopped.")
        print("")
        
        settings()
    
    else:
        
        print("")
        print("Wrong password. Try again.")
        print("")
        
        resetusernamestart()
        
def resetusernamecon():
    
    global userreal
    
    passset=input("Enter new username: (Enter 'n' to cancel) ")
    
    if passset == 'n':
        
        print("")
        print("Reset stopped.")
        print("")
        
        settings()
        
    elif passset == userreal:
        
        print("")
        print("Username cannot be the same as before!")
        print("")
        
        resetusernamecon()
        
    else:
        
        print("")
    
    passsetyn=input("Are you sure you want your username to be " +passset+ "? (y/n) ")
    
    if passsetyn == 'y':
        
        print("")
        
        userreal = passset
        
        print("Sucess! Your username has been updated.")
        print("")
        
        settings()
        
    elif passsetyn == 'n':
        
        print("")
        print("Stopped. Try again.")
        print("")
        
        resetusernamecon()
    
    else:
        
        print("")
        print("Invalid Input.")
        print("")

start()