#import json
#import datetime
#def welcome():
#    print("Welcome to your dashboard")

def signin(Username=None, Password=None):

    for lattempt in range(1,4):
        Username = input("Enter your username:")
        Password = input("Enter your Password:")
        #if not len(Username or Password) < 1:
        if len(Username or Password) > 1:
            if True:
                db = open("database.txt", "r")
                d = []
                f = []
                for i in db:
                    a,b,c = i.split(",")
                    a = a.strip()
                    b = b.strip()
                    #c = c.strip()
                    #c = a,b
                    d.append(a)
                    f.append(b)
                data = dict(zip(d, f))
                #print(data)
                try:
                    if data[Username]:
                        #try:
                            if Password == data[Username]:
                                print("Login success!")
                                print("Hi", Username)
                                break
                                welcome()
                            else:
                                print("Incorrect password or username")
                        #except:
                            #print("Incorrect password or username")
                    else:
                        print("Password or username doesn't exist")
                except:
                    print("Password or username doesn't exist")
            else:
                print("Error logging into the system")
        else:
            #print("Please attempt login again")
            if lattempt == 3:
                print ("Last login attempt Unsuccessful")
            else:
                print ("Attempt : %d Unsuccessful, Enter a valid User Name & Password " % (lattempt))
            #lattempt += 1
    else:
        print("Closing after 3 failed attempts to login\n")
            #continue
            #break
            #gainAccess()
        #lattempt += 1
        # b = b.strip()
# accessDb()


    

def register(Username=None, Password1=None, Password2=None):
    Username = input("Enter a Username:")
    Password1 = input("Create Password [Minimum 8 characters] :")
    Password2 = input("Confirm Password :")
    Branch = ["Downtown Toronto", "Central Toronto", "East Toronto","Etobicoke","Scarborough", "North York", "Ajax","Markham","Whitby","Richmond Hill", "Milton", "Pickering", "Oshawa","Oakville","Burlington","Clarington","Hamilton","Aurora","Vaughan"]
    
    db = open("database.txt", "r")
    d = []
    for i in db:
        a,b,c = i.split(",")
        #b = b.strip()
        a = a.strip()
        b = b.strip()
        #c = c.strip()
        #c = a,b
        d.append(a)
        #print(len(Password1))
        #print(len(Password2))
    
    if len(Password1) >= 8:
        db = open("database.txt", "r")
        #print("INside teh if loop", len(Password1))

        if not Username ==None:
            if len(Username) <1:
                print("Please provide a username")
                register()
            elif Username in d:
                print("Username exists")
                register()

                    
            else:
                    
                if Password1 == Password2:
                    
                    for num, bra in enumerate (Branch, start=1):          
                        print(num, bra)
                    braname = input("Select a branch for the new user : ")
                    braid = (int(braname) -1)
                    #print (Branch[braname])
                    usbraname = Branch[braid]
                    #print (Branch[braid])    
                    #print(list(enumerate(Branch, start=1)))
                    db = open("database.txt", "a")
                    db.write(Username+", "+Password1+", "+usbraname+"\n")
                    print("User created successfully!")
                    print("Please login to proceed:")
                            
                else:
                    print("Passwords do not match")
                    register()

    else:
        print("Password too short")



def home(option=None):
    print("Welcome, please select an option")
    option = input("Login | Signup | Exit:")
    if option.lower() == "login":
        signin()
    elif option.lower() == "signup":
        register()
    elif option.lower() == "exit":
        exit()
    else:
        print("Please enter a valid parameter, this is case-sensitive")




# register(Username, Password1, Password2)
# gainAccess(Username, Password1)
home()