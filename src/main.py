from addbook import addBook
from editbook import editBook
from removebook import removeBook
from search import searchBook
from recommend import recommendBook
from updatedb import updateDb


def main():
    print("=" * 40)
    print("  CLI Book Library")
    print("=" * 40)

    while True:
        print("\n--- Main Menu ---")
        print("  1. Add a book")
        print("  2. Edit a book")
        print("  3. Remove a book")
        print("  4. Search for a book")
        print("  5. Get a recommendation")
        print("  6. Sync database")
        print("  7. Exit")

        choice = input("\nSelect an option (1-7): ").strip()

        if choice == "1":
            addBook()
        elif choice == "2":
            editBook()
        elif choice == "3":
            removeBook()
        elif choice == "4":
            searchBook()
        elif choice == "5":
            recommendBook()
        elif choice == "6":
            updateDb()
            print("Database synced successfully.")
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()

