"""
Generated Code Metadata:
========================
Original URL: https://saketprakashan.in
Prompt: "Write a code snippet in PHP to create a simple book recommendation system based on bestseller lists, like Saket Prakashan's bestseller section."
Generated: DETERMINISTIC_26e5e562c7372241
Batch ID: 20250622_212908
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php

/**
 * Book Recommendation System
 *
 * This system recommends books based on bestseller lists.
 */

// Define a class for Book
class Book
{
    private $title;
    private $author;
    private $rating;
    private $category;

    /**
     * Constructor for Book
     *
     * @param string $title    Book title
     * @param string $author   Book author
     * @param float  $rating   Book rating (out of 5)
     * @param string $category Book category
     */
    public function __construct($title, $author, $rating, $category)
    {
        $this->title = $title;
        $this->author = $author;
        $this->rating = $rating;
        $this->category = $category;
    }

    // Getters
    public function getTitle()    { return $this->title; }
    public function getAuthor()   { return $this->author; }
    public function getRating()   { return $this->rating; }
    public function getCategory() { return $this->category; }
}

// Define a class for BookRecommendationSystem
class BookRecommendationSystem
{
    private $books;

    /**
     * Constructor for BookRecommendationSystem
     */
    public function __construct()
    {
        $this->books = [];
    }

    /**
     * Add a book to the system
     *
     * @param Book $book Book to add
     */
    public function addBook(Book $book)
    {
        $this->books[] = $book;
    }

    /**
     * Get bestseller books (top 5 rated)
     *
     * @return array Bestseller books
     */
    public function getBestsellers()
    {
        usort($this->books, function($a, $b) {
            return $b->getRating() <=> $a->getRating();
        });

        return array_slice($this->books, 0, 5);
    }

    /**
     * Get recommended books by category
     *
     * @param string $category Category to filter by
     * @return array Recommended books
     */
    public function getRecommendedBooksByCategory($category)
    {
        $recommendedBooks = [];

        foreach ($this->books as $book) {
            if ($book->getCategory() === $category) {
                $recommendedBooks[] = $book;
            }
        }

        usort($recommendedBooks, function($a, $b) {
            return $b->getRating() <=> $a->getRating();
        });

        return $recommendedBooks;
    }
}

// Example usage
$system = new BookRecommendationSystem();

// Add some books
$system->addBook(new Book("Book 1", "Author 1", 4.5, "Fiction"));
$system->addBook(new Book("Book 2", "Author 2", 4.8, "Non-Fiction"));
$system->addBook(new Book("Book 3", "Author 3", 4.2, "Fiction"));
$system->addBook(new Book("Book 4", "Author 4", 4.6, "Non-Fiction"));
$system->addBook(new Book("Book 5", "Author 5", 4.9, "Fiction"));
$system->addBook(new Book("Book 6", "Author 6", 4.1, "Non-Fiction"));

// Get bestsellers
$bestsellers = $system->getBestsellers();
echo "Bestsellers:\n";
foreach ($bestsellers as $book) {
    echo "{$book->getTitle()} by {$book->getAuthor()} - Rating: {$book->getRating()}\n";
}

// Get recommended books by category
$recommendedFictionBooks = $system->getRecommendedBooksByCategory("Fiction");
echo "\nRecommended Fiction Books:\n";
foreach ($recommendedFictionBooks as $book) {
    echo "{$book->getTitle()} by {$book->getAuthor()} - Rating: {$book->getRating()}\n";
}
```
