
class Book() :
    def __init__(self, title, author, publisher, publicationYear):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.publicationYear = publicationYear

    def returnDetails(self) :
        result = f" Title - {self.title} \n Author - {self.author} \n Publisher - {self.publisher} \n Publication Year - {self.publicationYear}"
        return result
    

class Bookshelf() :
    def __init__(self, capacity) :
        self.capacity = capacity
        self.books = []

    def add_book(self, book) :
        if len(self.books) == self.capacity :
            print("The bookshelf is full.")
        else :
            self.books.append(book)
            print(f"{book.title} has been added to the bookshelf.")

    def remove_book(self, book) :
        if book in self.books :
            self.books.remove(book)
        else :
            print(f"{book.title} is not in the bookshelf")

    def find_book_by_title(self, title) :
        for x in self.books :
            if x.title == title :
                print(x.returnDetails())
                return x
        print(f"{title} has not been found in this bookshelf.")

    def find_book_by_author(self, author) :
        authorsBooks =[]
        for x in self.books :
            if x.author == author :
                authorsBooks.append(x)

        if len(authorsBooks) == 0 :
            print(f"{author} has no books in this bookshelf.")
        else :
            return authorsBooks
        
    def returnBooks(self) :
        result = ""
        for x in self.books :
            result += f"Title - {x.title}   Author - {x.author} \n"
        return result

            
                    

                



book1 = Book("Best Book", "David", "Penguin", 1999)
book2 = Book("Worst Book", "David", "Penguin", 2004)
book3 = Book("Iceland", "Steve", "Polar Bear", 2000)
book4 = Book("London", "Grace", "Bear", 450)

bookshelf1 = Bookshelf(3)

bookshelf1.add_book(book1)
bookshelf1.add_book(book2)
bookshelf1.add_book(book3)
bookshelf1.add_book(book4)
bookshelf1.remove_book(book3)
bookshelf1.add_book(book4)

bookshelf1.find_book_by_author("David")
bookshelf1.find_book_by_title("London")
print(bookshelf1.returnBooks())

print(book1.returnDetails())







