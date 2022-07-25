import social_network_classes1 as classes

network1 = classes.SocialNetwork()

def mainMenu():
    print("########################################################")
    print("########################################################")
    print("Welcome to My Social Network")
    print("########################################################")
    print("########################################################")
    print("")
    print("1. Create a new account")
    print("2. Manage my account")
    print("3. Quit")
    print("********************************************************")
     


while True:
    mainMenu()  
    response1 = input("Please Choose a number: ") 

    if response1 == "1":
        print("You are now in the create account menu")

        new_username=input("Please select a username:")
        new_password=input("Please select a password:")

        new_user1=classes.Person(new_username, new_password, "Unknown")
        network1.user_list1.append(new_user1)
        continue

    elif response1 =="2":
        print("You are now in a log-in menu")

        login_username=input("Please enter your username:")
        login_password=input("Please enter your password:")

        for x in network1.user_list1:
            if x.id == login_username and x.password== login_password :
                user=x
     
                def profile():
                    print("")
                    print("1. Edit my profile")
                    print("2. Add a friend")
                    print("3. View all my friends")
                    print("4. View all my messages")
                    print("5. <- Go back ")

                profile()

    while True:
        response2 = input("Please Choose a number: ") 
        if response2 == "1":
                print("You are now in the edit profile menu")
                user.login_username=input("Please select a username:")
                user.login_password=input("Please select a password:")



 


    # new_user1=classes.Person(login_username, login_password, "No matching username or password")

    
    # Invalid response
        elif response1=="3":
            mainMenu()

  



    
           

    
