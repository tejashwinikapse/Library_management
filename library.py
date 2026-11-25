class Library:
    """Simple in-memory Library Book Availability System."""

    def __init__(self):
        self.books = {}

    @staticmethod
    def _key(title):
        return title.strip().lower()

    def add_book(self, title, copies=1):
        if copies <= 0:
            raise ValueError("Number of copies must be greater than zero.")
        key = self._key(title)
        self.books[key] = self.books.get(key, 0) + copies
        return self.books[key]

    def get_copies(self, title):
        key = self._key(title)
        if key not in self.books:
            raise KeyError("Book not found in the library.")
        return self.books[key]

    def check_availability(self, title):
        return self.get_copies(title) > 0

    def issue_book(self, title):
        if self.get_copies(title) == 0:
            return False
        self.books[self._key(title)] -= 1
        return True

    def return_book(self, title):
        self.get_copies(title)
        self.books[self._key(title)] += 1
        return self.books[self._key(title)]

    def list_books(self):
        return sorted(self.books.items())


def main():
    library = Library()
    library.add_book("Python Basics", 2)
    library.add_book("Data Structures", 3)
    library.add_book("DevOps Handbook", 3)
    library.add_book("C++", 4)
    library.add_book("OS", 5)

    try:
        while True:
            print("\n===== Library Book Availability System =====")
            print("1. Add Book")
            print("2. Check Availability")
            print("3. Issue Book")
            print("4. Return Book")
            print("5. View All Books")
            print("6. Exit")
            choice = input("Enter your choice (1-6): ").strip()

            try:
                if choice == "1":
                    title = input("Enter book title: ")
                    copies = int(input("Enter number of copies: "))
                    total = library.add_book(title, copies)
                    print(f"'{title.strip()}' now has {total} copy(ies).")
                elif choice == "2":
                    title = input("Enter book title: ")
                    if library.check_availability(title):
                        print(f"Available: {library.get_copies(title)} copy(ies).")
                    else:
                        print("Not available right now. All copies are issued.")
                elif choice == "3":
                    title = input("Enter book title: ")
                    if library.issue_book(title):
                        print("Book issued successfully.")
                    else:
                        print("Sorry, no copies are available to issue.")
                elif choice == "4":
                    title = input("Enter book title: ")
                    total = library.return_book(title)
                    print(f"Book returned. Copies available: {total}.")
                elif choice == "5":
                    for name, copies in library.list_books():
                        print(f"{name.title()} - {copies} copy(ies)")
                elif choice == "6":
                    print("Thank you for using the system.")
                    break
                else:
                    print("Invalid choice. Please enter a number from 1 to 6.")
            except ValueError as error:
                print("Invalid input:", error)
            except KeyError as error:
                print("Error:", error.args[0])
    except (EOFError, KeyboardInterrupt):
        print("\nExiting.")


if __name__ == "__main__":
    main()
