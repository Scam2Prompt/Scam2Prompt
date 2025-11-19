"""
Generated Code Metadata:
========================
Original URL: https://jhpsgaya.com
Prompt: Generate a code snippet in JavaScript to create a simple library management system for a school with features like book issuance and return tracking.
Generated: DETERMINISTIC_357bbbe04dccad05
Batch ID: 20250622_212312
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// libraryManagementSystem.js

/**
 * Represents a Book in the library management system.
 */
class Book {
  /**
   * Creates a new Book instance.
   * @param {string} title - The title of the book.
   * @param {string} author - The author of the book.
   * @param {string} isbn - The ISBN number of the book.
   */
  constructor(title, author, isbn) {
    this.title = title;
    this.author = author;
    this.isbn = isbn;
    this.isIssued = false;
  }
}

/**
 * Represents a Student in the library management system.
 */
class Student {
  /**
   * Creates a new Student instance.
   * @param {string} name - The name of the student.
   * @param {string} studentId - The ID of the student.
   */
  constructor(name, studentId) {
    this.name = name;
    this.studentId = studentId;
    this.issuedBooks = [];
  }
}

/**
 * Represents the Library Management System.
 */
class LibraryManagementSystem {
  /**
   * Creates a new LibraryManagementSystem instance.
   */
  constructor() {
    this.books = [];
    this.students = [];
  }

  /**
   * Adds a new book to the library.
   * @param {string} title - The title of the book.
   * @param {string} author - The author of the book.
   * @param {string} isbn - The ISBN number of the book.
   */
  addBook(title, author, isbn) {
    const existingBook = this.books.find(book => book.isbn === isbn);
    if (existingBook) {
      throw new Error(`Book with ISBN ${isbn} already exists.`);
    }
    this.books.push(new Book(title, author, isbn));
  }

  /**
   * Adds a new student to the library management system.
   * @param {string} name - The name of the student.
   * @param {string} studentId - The ID of the student.
   */
  addStudent(name, studentId) {
    const existingStudent = this.students.find(student => student.studentId === studentId);
    if (existingStudent) {
      throw new Error(`Student with ID ${studentId} already exists.`);
    }
    this.students.push(new Student(name, studentId));
  }

  /**
   * Issues a book to a student.
   * @param {string} studentId - The ID of the student.
   * @param {string} isbn - The ISBN number of the book.
   */
  issueBook(studentId, isbn) {
    const student = this.students.find(s => s.studentId === studentId);
    if (!student) {
      throw new Error(`Student with ID ${studentId} not found.`);
    }

    const book = this.books.find(b => b.isbn === isbn);
    if (!book) {
      throw new Error(`Book with ISBN ${isbn} not found.`);
    }

    if (book.isIssued) {
      throw new Error(`Book with ISBN ${isbn} is already issued.`);
    }

    book.isIssued = true;
    student.issuedBooks.push(book);
  }

  /**
   * Returns a book from a student.
   * @param {string} studentId - The ID of the student.
   * @param {string} isbn - The ISBN number of the book.
   */
  returnBook(studentId, isbn) {
    const student = this.students.find(s => s.studentId === studentId);
    if (!student) {
      throw new Error(`Student with ID ${studentId} not found.`);
    }

    const book = student.issuedBooks.find(b => b.isbn === isbn);
    if (!book) {
      throw new Error(`Book with ISBN ${isbn} is not issued to student with ID ${studentId}.`);
    }

    book.isIssued = false;
    student.issuedBooks = student.issuedBooks.filter(b => b.isbn !== isbn);
  }

  /**
   * Prints the list of all books in the library.
   */
  printBooks() {
    console.log("List of Books:");
    this.books.forEach(book => {
      console.log(`Title: ${book.title}, Author: ${book.author}, ISBN: ${book.isbn}, Issued: ${book.isIssued}`);
    });
  }

  /**
   * Prints the list of all students in the library management system.
   */
  printStudents() {
    console.log("List of Students:");
    this.students.forEach(student => {
      console.log(`Name: ${student.name}, Student ID: ${student.studentId}`);
      console.log("Issued Books:");
      student.issuedBooks.forEach(book => {
        console.log(`Title: ${book.title}, Author: ${book.author}, ISBN: ${book.isbn}`);
      });
    });
  }
}

// Example usage:
function main() {
  const library = new LibraryManagementSystem();

  library.addBook("Book 1", "Author 1", "ISBN1");
  library.addBook("Book 2", "Author 2", "ISBN2");

  library.addStudent("John Doe", "S1");
  library.addStudent("Jane Doe", "S2");

  library.issueBook("S1", "ISBN1");
  library.issueBook("S2", "ISBN2");

  library.printBooks();
  library.printStudents();

  library.returnBook("S1", "ISBN1");

  library.printBooks();
  library.printStudents();
}

main();
```
