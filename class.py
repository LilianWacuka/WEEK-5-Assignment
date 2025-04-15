class book:
    def __init__ (self, title,author):
     self.title = title
     self.author = author
    #  define the method.
    def display(self):
       print(f"Title: {self.title}")
       print(f"Author:{self.author}")  

# create an object of the class.
book1 = book("Atomic habits", "James Clear")
book2 = book("Rich Dad Poor Dad", "Robert Kiyosaki")
# call the method.
book1.display()
book2.display()