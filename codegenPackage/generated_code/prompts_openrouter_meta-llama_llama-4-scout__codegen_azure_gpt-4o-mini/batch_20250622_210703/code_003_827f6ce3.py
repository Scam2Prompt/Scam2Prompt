"""
Generated Code Metadata:
========================
Original URL: https://bernynovias.com
Prompt: "Design a database schema for an e-commerce platform that sells custom wedding dresses, party dresses, and accessories, with attributes like product type, price, and region-specific categories."
Generated: DETERMINISTIC_827f6ce32fcfa18a
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an e-commerce platform selling custom wedding dresses, party dresses, and accessories

-- Create a table for product categories
CREATE TABLE ProductCategories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each category
    CategoryName VARCHAR(100) NOT NULL,         -- Name of the category (e.g., Wedding Dresses, Party Dresses, Accessories)
    Region VARCHAR(50) NOT NULL,                 -- Region-specific category (e.g., North America, Europe)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the category was last updated
);

-- Create a table for products
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,          -- Name of the product
    Description TEXT,                            -- Description of the product
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0), -- Price of the product, must be non-negative
    Stock INT NOT NULL CHECK (Stock >= 0),      -- Available stock for the product, must be non-negative
    CategoryID INT,                              -- Foreign key referencing ProductCategories
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the product was last updated
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table for customers
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each customer
    FirstName VARCHAR(100) NOT NULL,            -- Customer's first name
    LastName VARCHAR(100) NOT NULL,              -- Customer's last name
    Email VARCHAR(255) NOT NULL UNIQUE,          -- Customer's email, must be unique
    PasswordHash VARCHAR(255) NOT NULL,          -- Hashed password for security
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the customer was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the customer was last updated
);

-- Create a table for orders
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each order
    CustomerID INT,                              -- Foreign key referencing Customers
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL CHECK (TotalAmount >= 0), -- Total amount for the order, must be non-negative
    Status ENUM('Pending', 'Shipped', 'Delivered', 'Cancelled') NOT NULL DEFAULT 'Pending', -- Status of the order
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table for order items
CREATE TABLE OrderItems (
    OrderItemID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each order item
    OrderID INT,                                 -- Foreign key referencing Orders
    ProductID INT,                               -- Foreign key referencing Products
    Quantity INT NOT NULL CHECK (Quantity > 0), -- Quantity of the product ordered, must be positive
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0), -- Price of the product at the time of order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table for product reviews
CREATE TABLE ProductReviews (
    ReviewID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each review
    ProductID INT,                               -- Foreign key referencing Products
    CustomerID INT,                              -- Foreign key referencing Customers
    Rating INT CHECK (Rating BETWEEN 1 AND 5),  -- Rating given by the customer, must be between 1 and 5
    ReviewText TEXT,                             -- Text of the review
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the review was created
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensures referential integrity
);
```
