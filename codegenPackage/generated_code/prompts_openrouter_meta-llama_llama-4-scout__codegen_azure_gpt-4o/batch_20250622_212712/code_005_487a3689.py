"""
Generated Code Metadata:
========================
Original URL: https://medebooks.shop
Prompt: Design a database schema to store and manage inventory for an online store like medebooks.shop, including tables for books, courses, and customer information.
Generated: DETERMINISTIC_487a36892a3cae44
Batch ID: 20250622_212712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Online Store Inventory Management

-- Table: Books
CREATE TABLE Books (
    BookID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each book
    Title VARCHAR(255) NOT NULL,           -- Title of the book
    Author VARCHAR(255) NOT NULL,          -- Author of the book
    ISBN VARCHAR(13) UNIQUE NOT NULL,      -- ISBN number (unique)
    Price DECIMAL(10, 2) NOT NULL,         -- Price of the book
    Stock INT NOT NULL,                    -- Number of books in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table: Courses
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each course
    Title VARCHAR(255) NOT NULL,             -- Title of the course
    Instructor VARCHAR(255) NOT NULL,        -- Name of the instructor
    Price DECIMAL(10, 2) NOT NULL,           -- Price of the course
    Duration INT NOT NULL,                   -- Duration of the course in hours
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table: Customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(255) NOT NULL,           -- First name of the customer
    LastName VARCHAR(255) NOT NULL,            -- Last name of the customer
    Email VARCHAR(255) UNIQUE NOT NULL,        -- Email address (unique)
    PhoneNumber VARCHAR(15),                   -- Phone number of the customer
    Address TEXT,                              -- Address of the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table: Orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order
    CustomerID INT NOT NULL,                -- Foreign key referencing Customers table
    TotalAmount DECIMAL(10, 2) NOT NULL,    -- Total amount of the order
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for order creation
    Status ENUM('Pending', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Order status
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Cascade delete on customer removal
);

-- Table: OrderItems
CREATE TABLE OrderItems (
    OrderItemID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order item
    OrderID INT NOT NULL,                       -- Foreign key referencing Orders table
    ProductType ENUM('Book', 'Course') NOT NULL, -- Type of product (Book or Course)
    ProductID INT NOT NULL,                     -- ID of the product (BookID or CourseID)
    Quantity INT NOT NULL,                      -- Quantity of the product ordered
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the product
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE -- Cascade delete on order removal
);

-- Indexes for performance optimization
CREATE INDEX idx_books_title ON Books(Title);
CREATE INDEX idx_courses_title ON Courses(Title);
CREATE INDEX idx_customers_email ON Customers(Email);
CREATE INDEX idx_orders_customerid ON Orders(CustomerID);
CREATE INDEX idx_orderitems_orderid ON OrderItems(OrderID);
```
