# parent class.
class Book:
    def __init__ (self, title,author):
     self.title = title
     self.author = author
#  define the method.
    def display(self):
       print(f"Title: {self.title}")
       print(f"Author:{self.author}")  
    def status(self):
        return "Available"

# creating an (inheritance) child class.
class BoughtBook(Book):
    def __init__(self, title, author, price,year):
        super().__init__(title, author)
        self.price = price
        self.year = year
# define the method.
    def display(self):
        super().display()
        print(f"Price: {self.price}")
        print(f"year:{self.year}")
 # polymorphism for bought books.
    def display(self):
        super().display()  # Calling the parent display
        print(f"Price: {self.price}")
        print(f"Year: {self.year}")
        print(f"Status: Bought")
# Child class (inherits from Book) for borrowed books
class BorrowedBook(Book):
    def __init__(self, title, author, borrow_date):
        super().__init__(title, author)
        self.borrow_date = borrow_date
 # Polymorphism: overriding the display method for borrowed books
    def display(self):
        super().display()  # Calling the parent display
        print(f"Borrow Date: {self.borrow_date}")
        print(f"Status: Borrowed")      
# Create different book objects
book1 = BoughtBook("Atomic Habits", "James Clear", 300, 2018)
book2 = BorrowedBook("Rich Dad Poor Dad", "Robert Kiyosaki", "2025-04-10")
# call the method.
print("Displaying books with polymorphism:\n")
books = [book1, book2]

for book in books:
    book.display()

