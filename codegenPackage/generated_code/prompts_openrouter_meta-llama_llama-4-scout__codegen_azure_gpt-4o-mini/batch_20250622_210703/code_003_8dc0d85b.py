"""
Generated Code Metadata:
========================
Original URL: https://farmaciasantiagoapostol.com
Prompt: Design a database schema for an online pharmacy, including tables for products, customers, orders, and news articles, inspired by the structure of farmaciasantiagoapostol.com.
Generated: DETERMINISTIC_8dc0d85bdfca9f5a
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an online pharmacy

-- Table to store product information
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each product
    Name VARCHAR(255) NOT NULL,               -- Name of the product
    Description TEXT,                          -- Description of the product
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product
    Stock INT NOT NULL DEFAULT 0,              -- Available stock quantity
    Category VARCHAR(100),                     -- Category of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each customer
    FirstName VARCHAR(100) NOT NULL,           -- Customer's first name
    LastName VARCHAR(100) NOT NULL,            -- Customer's last name
    Email VARCHAR(255) NOT NULL UNIQUE,        -- Customer's email address
    PasswordHash VARCHAR(255) NOT NULL,        -- Hashed password for security
    Phone VARCHAR(15),                         -- Customer's phone number
    Address TEXT,                              -- Customer's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the customer was registered
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store order information
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each order
    CustomerID INT NOT NULL,                    -- Foreign key referencing Customers
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL,       -- Total amount for the order
    Status ENUM('Pending', 'Shipped', 'Delivered', 'Cancelled') DEFAULT 'Pending', -- Order status
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store order items (products in each order)
CREATE TABLE OrderItems (
    OrderItemID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each order item
    OrderID INT NOT NULL,                        -- Foreign key referencing Orders
    ProductID INT NOT NULL,                      -- Foreign key referencing Products
    Quantity INT NOT NULL,                       -- Quantity of the product ordered
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the product at the time of order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store news articles
CREATE TABLE NewsArticles (
    ArticleID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each article
    Title VARCHAR(255) NOT NULL,                 -- Title of the news article
    Content TEXT NOT NULL,                        -- Content of the news article
    Author VARCHAR(100),                          -- Author of the article
    PublishedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the article was published
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);
```
