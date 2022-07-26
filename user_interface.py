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

def profile():
    print("")
    print("1. Edit my profile")
    print("2. Add a friend")
    print("3. View all my friends")
    print("4. View all my messages")
    print("5. <- Go back ")
     


while True:
    mainMenu()  
    response1 = input("Please Choose a number: ") 

    if response1 == "1":
        print("You are now in the create account menu")

        new_username=input("Please select your username:")
        new_password=input("Please select your password:")
        new_age=input("Plese select age:")

        new_user1=classes.Person(new_username, new_password, new_age)
        network1.user_list1.append(new_user1)
        continue

    elif response1 =="2":
        print("You are now in a log-in menu")

        login_username=input("Please enter your username:")
        login_password=input("Please enter your password:")

        for x in network1.user_list1:
            if x.id == login_username and x.password== login_password :
                user=x
    while True:
        profile()
        response2 = input("Please Choose a number: ") 
        
        if response2 == "1":
            print("You are now in the edit profile menu")
            user.id=input("Please reset a username:")
            user.password=input("Please reset a password:")
            user.age=input("Please reset an age:")
            print("Bravo you have reseted your account")

            user.user_information()


        elif x.id != login_username or x.password != login_password :
            print("this username does not match with the password")
            mainMenu()


    


        elif response2 == "2":
            
            uptated_friends=input("Please select the username of the friend you wanna add:")
            friends = classes.Person(uptated_friends)
            network1.friend_list.append(uptated_friends)
            for y in network1.friend_list:
                if y.friends == uptated_friends :
                    friends = y
        elif response2 == "5":
                print("Goodbyee")
                mainMenu()
                        

            
            #variable yap= input (add who as friend?)
            #set the variable to that
            #user.friendlist.append(var)


    # new_user1=classes.Person(login_username, login_password, "No matching username or password")

    # Invalid response
        elif response1=="3":
                mainMenu()

  



    
           

    
