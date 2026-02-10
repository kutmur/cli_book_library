# CLI Book Library

A command-line book library application built with Python and MongoDB. Manage your reading lists by adding, editing, searching, and removing books across two collections: **already_read** and **to_read**. The app also recommends a random book from your to-read list by genre and syncs books between collections based on their read status.

This project was built as a hands-on learning experience with MongoDB.

## Features

- **Add** books to your already-read or to-read collection
- **Edit** existing book entries
- **Remove** books by various search criteria
- **Search** books by ID, title, author, genre, or read status
- **Recommend** a random book from your to-read list filtered by genre
- **Sync** the database -- automatically moves books between collections when their `alreadyRead` flag changes

## Prerequisites

- Python 3.10+
- A MongoDB instance (local or [MongoDB Atlas](https://www.mongodb.com/atlas))

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/halilkutmur/cli_book_library.git
   cd cli_book_library
   ```

2. **Install dependencies**

   ```bash
   pip install pymongo python-dotenv
   ```

3. **Set up environment variables**

   Copy the example env file and fill in your MongoDB connection string:

   ```bash
   cp .env.example .env
   ```

   Then edit `.env` and replace the placeholder with your actual connection string.

## Usage

```bash
cd src
python main.py
```

You will see the main menu:

```
========================================
  CLI Book Library
========================================

--- Main Menu ---
  1. Add a book
  2. Edit a book
  3. Remove a book
  4. Search for a book
  5. Get a recommendation
  6. Sync database
  7. Exit

Select an option (1-7):
```

## Database Structure

The app uses a MongoDB database called `books_db` with two collections:

| Collection     | Description                        |
| -------------- | ---------------------------------- |
| `already_read` | Books you have finished reading    |
| `to_read`      | Books you plan to read             |

Each book document has the following fields:

```json
{
  "bookId": "1",
  "title": "Dune",
  "author": "Frank Herbert",
  "genre": "Science Fiction",
  "alreadyRead": false
}
```

## Project Structure

```
cli_book_library/
  src/
    main.py        -- CLI menu and entry point
    addbook.py     -- Add a new book
    editbook.py    -- Edit an existing book
    removebook.py  -- Remove a book
    search.py      -- Search for books
    recommend.py   -- Get a random book recommendation by genre
    updatedb.py    -- Sync books between collections
  .env.example     -- Example environment variables
  LICENSE
  README.md
```

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.