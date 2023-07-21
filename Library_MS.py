class Library:
    def __init__(self, listofbooks):
        self.books = listofbooks
        
    def Availablebook(self):
        print( "The Available book in library are : ")
        for index, book in enumerate(self.books):
            print("\t", index+1,  book)

    def borrowBook(self, Bookname):
         if Bookname in self.books:
             print(f"You have been issued {Bookname} please keep it safe and return in 10 days")
             self.books.remove(Bookname)
             return True
         else: 
             print(f"{Bookname} is not available in Library")
             return False

    def returnBook(self,Bookname):
        self.books.append(Bookname)
        print(f"Thank you for returning {Bookname}")
            
    
class Student(Library):
    def __init__(self,listofbooks):
        super().__init__(listofbooks)
        
    def requestBook(self):
        self.book = input("Enter the Book Name: ")
        return self.book
        
        """ request_book = input("Enter the Book Name: ")
        if request_book in self.books:
            print(f" The Book {request_book} is available in Library")
            
        else:
            print("The Book is not available in library")
         """
    def returnBook(self):
        self.book = input("Enter the book which you want to return: ")
        return self.book


#Books_in_library.borrowBook("Python")
#Books_in_library.Availablebook()3


if __name__ == "__main__":
    list_of_books = ["Python","Java Script", "Science", "Maths", "Data Science", "Machine Learning", "Deep Learning"]
    Books_in_library = Library(list_of_books)
    student = Student(list_of_books)
    while True:
        WelcomeMsg = """***************** Welcome to Central Library*****************
            Please choose an option: 
            1. Listing all the books
            2. Request a book
            3. Return a book
            4. Exit the Library"""
        print(WelcomeMsg)
        
        user_input = int(input("Please choose the above option: "))
        
        if user_input == 1 :
            Books_in_library.Availablebook()
        elif user_input == 2:
            Books_in_library.borrowBook(student.requestBook())
        elif user_input == 3:
             Books_in_library.returnBook(student.returnBook()) 
        elif user_input == 4:
            print("Thank you for using the Central Library ")
            quit()
        else:
            print( "Invalid Option. Please choose the valid option ")
    