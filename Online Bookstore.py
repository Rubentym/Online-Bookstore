class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

class OnlineBookstore:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

# Example usage:
bookstore = OnlineBookstore()
book1 = Book("Harry Potter", "J.K. Rowling", "Fantasy")
book2 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Classic")
bookstore.add_book(book1)
bookstore.add_book(book2)
searched_book = bookstore.search_book("Harry Potter")
if searched_book:
    print(f"Book found: {searched_book.title} by {searched_book.author}")
else:
    print("Book not found.")
