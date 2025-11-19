"""
Generated Code Metadata:
========================
Original URL: https://semillasplantae.com
Prompt: "Create a sample database schema for an e-commerce platform selling organic seeds, including tables for products, orders, and customers, based on the structure of Semillas Plantae."
Generated: DETERMINISTIC_37d37b4ef8e6501a
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Sample database schema for an e-commerce platform selling organic seeds

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Customers;

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,              -- Customer's last name
    Email VARCHAR(100) NOT NULL UNIQUE,         -- Customer's email address (must be unique)
    Phone VARCHAR(15),                          -- Customer's phone number (optional)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the customer was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store product information
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each product
    ProductName VARCHAR(100) NOT NULL,          -- Name of the product
    Description TEXT,                            -- Description of the product
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0), -- Price of the product (must be non-negative)
    Stock INT NOT NULL CHECK (Stock >= 0),      -- Available stock for the product (must be non-negative)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store order information
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each order
    CustomerID INT NOT NULL,                     -- Foreign key referencing Customers
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL CHECK (TotalAmount >= 0), -- Total amount for the order
    Status ENUM('Pending', 'Shipped', 'Delivered', 'Cancelled') DEFAULT 'Pending', -- Order status
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Ensure referential integrity
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the order was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Sample data insertion (for testing purposes)
INSERT INTO Customers (FirstName, LastName, Email, Phone) VALUES
('John', 'Doe', 'john.doe@example.com', '123-456-7890'),
('Jane', 'Smith', 'jane.smith@example.com', '098-765-4321');

INSERT INTO Products (ProductName, Description, Price, Stock) VALUES
('Organic Tomato Seeds', 'High-quality organic tomato seeds.', 3.99, 100),
('Organic Basil Seeds', 'Fresh organic basil seeds for your garden.', 2.49, 50);

INSERT INTO Orders (CustomerID, TotalAmount, Status) VALUES
(1, 10.48, 'Pending'),
(2, 2.49, 'Shipped');
```
