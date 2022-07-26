

class SocialNetwork:
    def __init__(self):
        self.user_list1 = []
        
        


class Person:
    def __init__(self, name, password, age):
        self.id = name
        self.password = password
        self.age = age
     

    def user_information(self):
        print("name:", self.id)
        print("password:", self.password)
        print("age:",self.age)

    def add_friend(self,friends):
        self.friend_list = []
        self.friends = friends
        print("friends" , self.friends)
       
        #implement adding friend. Hint add to self.friendlist
        
    def send_message(self):
        #implement sending message to friend here
        pass

    
        