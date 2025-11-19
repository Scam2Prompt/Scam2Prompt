"""
Generated Code Metadata:
========================
Original URL: https://somoscorujasbraz.blogspot.com
Prompt: Design a database schema to store customer reviews and ratings for an e-commerce platform, like Somos Corujas, with fields for review text, rating (1-5), and product ID.
Generated: DETERMINISTIC_09c042205165a37c
Batch ID: 20250622_212549
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing customer reviews and ratings for an e-commerce platform

CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,         -- Name of the product
    ProductDescription TEXT,                    -- Description of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the product was created
);

CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    CustomerName VARCHAR(255) NOT NULL,         -- Name of the customer
    Email VARCHAR(255) UNIQUE NOT NULL,         -- Unique email for the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the customer was created
);

CREATE TABLE Reviews (
    ReviewID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each review
    ProductID INT NOT NULL,                      -- Foreign key referencing the Products table
    CustomerID INT NOT NULL,                     -- Foreign key referencing the Customers table
    ReviewText TEXT NOT NULL,                    -- Text of the review
    Rating INT CHECK (Rating BETWEEN 1 AND 5),  -- Rating value between 1 and 5
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the review was created
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_product ON Reviews(ProductID);
CREATE INDEX idx_customer ON Reviews(CustomerID);
```
