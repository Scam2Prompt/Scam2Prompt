"""
Generated Code Metadata:
========================
Original URL: https://fuel-dapp-template-nextjs.vercel.app
Prompt: Write a Sway Book code snippet for a smart contract on the FuelVM.
Generated: DETERMINISTIC_9ec50b01850917c1
Batch ID: 20250622_205218
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sway
contract;

use std::{constants::ZERO_B256, hash::*, storage::*};

// A simple book storage contract that allows adding and retrieving book information
storage {
    books: StorageMap<u64, Book> = StorageMap {},
    next_id: u64 = 0,
}

// Book structure definition
struct Book {
    title: String,
    author: String,
    isbn: String,
    published_year: u16,
}

// Error enum for contract operations
enum BookError {
    BookNotFound: (),
    InvalidInput: (),
}

impl Book {
    // Creates a new Book instance
    fn new(title: String, author: String, isbn: String, published_year: u16) -> Self {
        Book {
            title,
            author,
            isbn,
            published_year,
        }
    }
}

abi BookContract {
    // Adds a new book to storage and returns its ID
    #[storage(read, write)]
    fn add_book(title: String, author: String, isbn: String, published_year: u16) -> u64;

    // Retrieves a book by its ID
    #[storage(read)]
    fn get_book(id: u64) -> Option<Book>;

    // Gets the total count of books stored
    #[storage(read)]
    fn get_book_count() -> u64;
}

impl BookContract for Contract {
    #[storage(read, write)]
    fn add_book(title: String, author: String, isbn: String, published_year: u16) -> u64 {
        // Validate input
        if title.is_empty() || author.is_empty() || isbn.is_empty() {
            revert(BookError::InvalidInput);
        }

        // Create new book
        let book = Book::new(title, author, isbn, published_year);
        let id = storage.next_id;

        // Store the book and increment ID counter
        storage.books.insert(id, book);
        storage.next_id = id + 1;

        id
    }

    #[storage(read)]
    fn get_book(id: u64) -> Option<Book> {
        storage.books.get(id)
    }

    #[storage(read)]
    fn get_book_count() -> u64 {
        storage.next_id
    }
}
```
