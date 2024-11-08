def add_book(library, title, author, year, copies_available):
    """Add a new book to the library."""
    book = {
        'title': title,
        'author': author,
        'year': year,
        'copies_available': copies_available
    }
    library.append(book)
    print(f"Book '{title}' added to the library.")
def borrow_book(library, title):
    """Borrow a book from the library."""
    for book in library:
        if book['title'].lower() == title.lower():
            if book['copies_available'] > 0:
                book['copies_available'] -= 1
                print(f"You have borrowed '{title}'.")
                return
            else:
                print(f"Sorry, '{title}' is not available for borrowing.")
                return
    print(f"Book '{title}' not found in the library.")
def search_books(library, search_term):
    """Search for books by title or author."""
    results = [book for book in library if search_term.lower() in book['title'].lower() or search_term.lower() in book['author'].lower()]
    return results
def list_available_books(library):
    """List all available books sorted by the year of publication."""
    available_books = [book for book in library if book['copies_available'] > 0]
    sorted_books = sorted(available_books, key=lambda x: x['year'])
    print("\nAvailable Books:")
    for book in sorted_books:
        print(f"{book['title']} by {book['author']} ({book['year']}) - Copies Available: {book['copies_available']}")
def main():
    library = []
    while True:
        print("Library Management System")
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. Search Books")
        print("4. List Available Books")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            year = int(input("Enter year of publication: "))
            copies_available = int(input("Enter number of copies available: "))
            add_book(library, title, author, year, copies_available)
        elif choice == '2':
            title = input("Enter the title of the book you want to borrow: ")
            borrow_book(library, title)
        elif choice == '3':
            search_term = input("Enter title or author to search: ")
            results = search_books(library, search_term)
            if results:
                print("\nSearch Results:")
                for book in results:
                    print(f"{book['title']} by {book['author']} ({book['year']}) - Copies Available: {book['copies_available']}")
            else:
                print("No books found.")
        elif choice == '4':
            list_available_books(library)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
if __name__ == "__main__":
    main()
