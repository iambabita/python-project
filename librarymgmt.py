class Library:
    def __init__(self, books=None):
        if books is None:
            books = []
        self.books = books
        self.no_of_books = len(books)

    def show_books(self):
        print("\nBooks in the Library:")
        for book in self.books:
            print("-", book)

    def add_book(self, book_name):
        self.books.append(book_name)
        self.no_of_books += 1
        print(f"'{book_name}' added to the Library.")

    def search_book(self, book_name):
        if book_name in self.books:
            print(f"'{book_name}' is available in the Library.")
        else:
            print(f"'{book_name}' is not found in the Library.")

    def remove_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            self.no_of_books -= 1
            print(f"'{book_name}' removed from the Library.")
        else:
            print(f"'{book_name}' is not in the Library.")

    def get_no_of_books(self):
        return self.no_of_books


 
lib = Library(["Python Basics", "Data Science", "Machine Learning"])

while True:
    print("\n Library !!!")
    print("1. Show Books:")
    print("2. Add Book:")
    print("3. Search Book:")
    print("4. Remove Book:")
    print("5. Total Books:")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        lib.show_books()

    elif choice == "2":
        book = input("Enter book name to add: ")
        lib.add_book(book)

    elif choice == "3":
        book = input("Enter book name to search: ")
        lib.search_book(book)

    elif choice == "4":
        book = input("Enter book name to remove: ")
        lib.remove_book(book)

    elif choice == "5":
        print("Total books in library:", lib.get_no_of_books())

    elif choice == "6":
        print("Exiting Library System...")
        break

    else:
        print("Invalid choice! Try again.")