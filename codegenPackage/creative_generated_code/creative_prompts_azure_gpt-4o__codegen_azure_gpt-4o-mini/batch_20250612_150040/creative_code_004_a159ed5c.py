"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://teeny-activity-colossal.on-fleek.app
Prompt: Suggest a database design for managing comic book sales, including tracking special editions like "Top G: Parallel Protocols" and customer purchase history.
Generated: DETERMINISTIC_a159ed5c0da54875
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script to create a database schema for managing comic book sales

-- Create database
CREATE DATABASE ComicBookSales;
USE ComicBookSales;

-- Table to store information about comic books
CREATE TABLE Comics (
    ComicID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each comic
    Title VARCHAR(255) NOT NULL,            -- Title of the comic
    IssueNumber INT NOT NULL,                -- Issue number of the comic
    SpecialEdition BOOLEAN DEFAULT FALSE,    -- Flag to indicate if it's a special edition
    EditionName VARCHAR(255),                -- Name of the special edition if applicable
    ReleaseDate DATE NOT NULL,               -- Release date of the comic
    Price DECIMAL(10, 2) NOT NULL,           -- Price of the comic
    StockQuantity INT DEFAULT 0              -- Quantity of comics available in stock
);

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(100) NOT NULL,           -- Customer's first name
    LastName VARCHAR(100) NOT NULL,            -- Customer's last name
    Email VARCHAR(255) UNIQUE NOT NULL,        -- Customer's email, must be unique
    Phone VARCHAR(15)                          -- Customer's phone number
);

-- Table to store purchase history
CREATE TABLE Purchases (
    PurchaseID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each purchase
    CustomerID INT NOT NULL,                    -- Foreign key referencing Customers
    ComicID INT NOT NULL,                       -- Foreign key referencing Comics
    PurchaseDate DATETIME DEFAULT CURRENT_TIMESTAMP, -- Date and time of purchase
    Quantity INT NOT NULL,                      -- Quantity purchased
    TotalPrice DECIMAL(10, 2) NOT NULL,        -- Total price for the purchase
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Ensure data integrity
    FOREIGN KEY (ComicID) REFERENCES Comics(ComicID) ON DELETE CASCADE          -- Ensure data integrity
);

-- Index for faster searches on comics and purchases
CREATE INDEX idx_comic_title ON Comics(Title);
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_purchase_date ON Purchases(PurchaseDate);

-- Sample data insertion for Comics
INSERT INTO Comics (Title, IssueNumber, SpecialEdition, EditionName, ReleaseDate, Price, StockQuantity) VALUES
('Top G: Parallel Protocols', 1, TRUE, 'Limited Edition', '2023-10-01', 19.99, 50),
('Spider-Man: No Way Home', 1, FALSE, NULL, '2021-12-17', 14.99, 100);

-- Sample data insertion for Customers
INSERT INTO Customers (FirstName, LastName, Email, Phone) VALUES
('John', 'Doe', 'john.doe@example.com', '123-456-7890'),
('Jane', 'Smith', 'jane.smith@example.com', '098-765-4321');

-- Sample data insertion for Purchases
INSERT INTO Purchases (CustomerID, ComicID, Quantity, TotalPrice) VALUES
(1, 1, 1, 19.99),
(2, 2, 2, 29.98;
```
