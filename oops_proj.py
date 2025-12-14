class ChatBook:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.logged_in = False
        self.menu()
    
    def menu(self):
        user_input = input("""Welcome to chatbot, how would yoy like to proceed?
                           1. Press 1 to signup
                           2. Press 2 to signin
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press any other key to exit \n""")
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()

    def signup(self):
        email = input("Enter your email here : ")
        password = input("Setup your password here : ")
        self.username = email
        self.password = password
        print("You have signedup successfully")
        print("\n")
        self.menu()

    def signin(self):
        if self.username == '' and self.password == '':
            print("please signup fro menu")
        else:
            email = input("Enter your email here : ")
            password = input("Enter your password here : ")
            if self.username == email and self.password == password:
                print("You have signed in")
                self.logged_in = True
            else:
                print("please enter correct credentials")

obj = ChatBook()