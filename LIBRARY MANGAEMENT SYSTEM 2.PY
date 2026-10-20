
class User:

    def __init__(self, user_id, name, email, password):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password

    def login(self, password):
        if self.password == password:
            return True
        return False

    def logout(self):
        print(self.name, "has logged out.")

    def show_profile(self):
        print("\n--- Profile ---")
        print("ID:", self.user_id)
        print("Name:", self.name)
        print("Email:", self.email)



class Student(User):

    def __init__(self, user_id, name, email, password, course):
        super().__init__(user_id, name, email, password)

        self.course = course
        self.issued_books = []

    def search_book(self, library, title):
        library.search_book(title)

    def issue_book(self, library, book_id):

        book = library.find_book(book_id)

        if book is None:
            print("Book not found.")
            return

        if book.available:
            book.issue_book()
            self.issued_books.append(book)

            print("Book issued successfully.")
        else:
            print("Sorry, this book is already issued.")

    def return_book(self, library, book_id):

        for book in self.issued_books:

            if book.book_id == book_id:

                book.return_book()
                self.issued_books.remove(book)

                print("Book returned successfully.")
                return

        print("You have not issued this book.")

    def show_issued_books(self):

        print("\n--- My Books ---")

        if len(self.issued_books) == 0:
            print("You have no issued books.")
            return

        for book in self.issued_books:
            print(book.book_id, "-", book.title)



class Librarian(User):

    def __init__(self, user_id, name, email, password, employee_id):
        super().__init__(user_id, name, email, password)

        self.employee_id = employee_id

    def add_book(self, library, book):
        library.add_book(book)

    def remove_book(self, library, book_id):
        library.remove_book(book_id)

    def update_book(self, library, book_id, new_title):
        library.update_book(book_id, new_title)

    def show_students(self, library):
        library.show_students()



class Author:

    def __init__(self, author_id, name):
        self.author_id = author_id
        self.name = name

    def show_author(self):
        print("Author ID:", self.author_id)
        print("Author Name:", self.name)



class Book:

    def __init__(self, book_id, title, author, category, price):

        self.book_id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.price = price

        self.available = True

    def show_book(self):

        if self.available:
            status = "Available"
        else:
            status = "Issued"

        print(
            self.book_id,
            "|", self.title,
            "|", self.author.name,
            "|", self.category,
            "|", status
        )

    def issue_book(self):
        self.available = False

    def return_book(self):
        self.available = True

    def change_title(self, new_title):
        self.title = new_title




class Library:

    def __init__(self, name):

        self.name = name
        self.books = []
        self.students = []

    def add_book(self, book):

        self.books.append(book)
        print("Book added successfully.")

    def remove_book(self, book_id):

        book = self.find_book(book_id)

        if book:
            self.books.remove(book)
            print("Book removed successfully.")
        else:
            print("Book not found.")

    def find_book(self, book_id):

        for book in self.books:

            if book.book_id == book_id:
                return book

        return None

    def search_book(self, title):

        found = False

        for book in self.books:

            if title.lower() in book.title.lower():
                book.show_book()
                found = True

        if not found:
            print("No book found.")

    def update_book(self, book_id, new_title):

        book = self.find_book(book_id)

        if book:
            book.change_title(new_title)
            print("Book updated successfully.")
        else:
            print("Book not found.")

    def add_student(self, student):

        self.students.append(student)

    def show_students(self):

        print("\n--- Students ---")

        for student in self.students:
            print(student.user_id, "-", student.name)

    def show_all_books(self):

        print("\n--- All Books ---")

        for book in self.books:
            book.show_book()



class Login:

    def check_login(self, user, password):

        if user.login(password):
            print("Login successful!")
            return True

        print("Wrong password.")
        return False



library = Library("College Library")




author1 = Author(1, "R.K. Narayan")
author2 = Author(2, "A.P.J. Abdul Kalam")




book1 = Book(
    101,
    "Malgudi Days",
    author1,
    "Fiction",
    250
)

book2 = Book(
    102,
    "Wings of Fire",
    author2,
    "Biography",
    300
)




library.add_book(book1)
library.add_book(book2)




student = Student(
    1,
    "Bikash",
    "bikash@gmail.com",
    "1234",
    "Computer Science"
)

library.add_student(student)



login = Login()

print("\n===== LIBRARY LOGIN =====")

if login.check_login(student, "1234"):

    while True:

        print("\n===== MENU =====")
        print("1. Show all books")
        print("2. Search book")
        print("3. Issue book")
        print("4. Return book")
        print("5. Show my books")
        print("6. Show profile")
        print("7. Logout")

        choice = input("Enter your choice: ")


        if choice == "1":

            library.show_all_books()


        elif choice == "2":

            title = input("Enter book name: ")

            student.search_book(
                library,
                title
            )


        elif choice == "3":

            book_id = int(
                input("Enter book ID: ")
            )

            student.issue_book(
                library,
                book_id
            )


        elif choice == "4":

            book_id = int(
                input("Enter book ID: ")
            )

            student.return_book(
                library,
                book_id
            )


        elif choice == "5":

            student.show_issued_books()


        elif choice == "6":

            student.show_profile()


        elif choice == "7":

            student.logout()
            break


        else:

            print("Please enter a valid option.")