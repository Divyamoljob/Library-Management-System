class Database:
    books = []
    book_id = 1000
    users = []

class User(Database):

    def __init__(self):
        self.session = False

    def add_user(self):
        userDict = {}
        name = input('Enter your name : ')
        dob = input('Enter your date of birth : ')
        contact = int(input('Enter your contact number : '))
        email = input('Enter your email : ')
        password = input('Enter your password : ')

        userDict['name'] = name
        userDict['dob'] = dob
        userDict['contact'] = contact
        userDict['email'] = email
        userDict['password'] = password

        Database.users.append(userDict)

    def user_login(self):
        users = Database.users
        username = input('Enter username : ')
        password = input('Enter password : ')
        if len(users)>0:
            for i in range(len(users)):
                if users[i]['name']==username and users[i]['password']==password:
                    self.session = True
                    print('You are successfully logged in')
                    break
                else:
                    pass
            else:
                print('Password or username is incorrrect')
        
    def view_books(self):
        if self.session==True:
            books = Database.books
            for i in range(len(books)):
                print(books[i]['book_id'], end = "\t")  
                print(books[i]['book_title'], end = "\t")   
                print(books[i]['author_name'], end = "\t") 
                print(books[i]['total_page'], end = "\t") 
                print(books[i]['available_copy'], end = "\t") 
                print(books[i]['published_year'], end = "\t") 
                print("\n")
        else:
            print('Please Login')

    def logout(self):
        self.session=False
        print('Logged out successfully')



#***********************************************ADMIN************************************************

class Admins(Database):
    username = 'admin'
    password = 'admin'
    Session = False
    admin_users = [{'username': 'admin', 'password': 'admin'},]

    def add_books(self):
        if Admins.Session==True:
            books = {}
            book_title = input('Enter book title : ');
            author_name = input('Enter author name : ')
            total_page = int(input('Enter total pages ; '))
            available_copy = int(input('Enter no of available copies : '))
            ISBN = int(input('Enter ISBN : '))
            published_year = int(input('Enter pulished year : '))

            books['book_id'] = Database.book_id+1
            Database.book_id+=1

            books['book_title'] = book_title
            books['author_name'] = author_name
            books['total_page'] = total_page
            books['available_copy'] = available_copy
            books['ISBN'] = ISBN
            books['published_year'] = published_year

            Database.books.append(books)  
        else:
            print('Please login')

    def view_books(self):
        if Admins.Session==True:
            books = Database.books
            for i in range(len(books)):
                print(books[i]['book_id'], end = "\t")  
                print(books[i]['book_title'], end = "\t")   
                print(books[i]['author_name'], end = "\t") 
                print(books[i]['total_page'], end = "\t") 
                print(books[i]['available_copy'], end = "\t") 
                print(books[i]['published_year'], end = "\t") 
                print("\n")
        else:
            print('Please login')

    def edit_books(self):
        if Admins.Session==True:
            book_id = int(input('Enter book id : '))
            books = Database.books
            for i in range(len(books)):
                if books[i]['book_id'] == book_id:
                    change = input('Enter the field : ')
                    data = input('Enter the data : ')
                    Database.books[i][change]=data
                    print('Changed successfully')
                    break              
        else:
            print('Please login')

    def delete_books(self):
        if Admins.Session==True:
            book_id = int(input('Enter book id : '))
            books = Database.books
            for i in range(len(books)):
                if books[i]['book_id'] == book_id:
                    del Database.books[i]
                    print('Deleted successfully')
                    break              
        else:
            print('Please login')

    def create_admin(self):
        user = {}
        username = input('Enter username : ')
        password = input('Enter password : ')
        user['username'] = username
        user['password'] = password
        Admins.admin_users.append(user)

    def admin_login(self):
        username = input('Enter username : ')
        password = input('Enter password : ')
        admins = Admins.admin_users
        for i in range(len(admins)):
            if admins[i]['username']==username and admins[i]['password']==password:
                print('You are logged in')
                Admins.Session = True
            else:
                print('Username or password is incorrect')

    def logout(self):
        Admins.Session = False
        print('Logged out successfully')

