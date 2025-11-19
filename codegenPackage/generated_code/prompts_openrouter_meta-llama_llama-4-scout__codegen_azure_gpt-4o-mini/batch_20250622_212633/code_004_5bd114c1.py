"""
Generated Code Metadata:
========================
Original URL: https://artpelbrazz.blogspot.com
Prompt: Design a database schema for an e-commerce platform that sells art supplies, including tables for products, customers, orders, and payments, considering the various discounts and promotions offered by Art Pel.
Generated: DETERMINISTIC_5bd114c101f5a47d
Batch ID: 20250622_212633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an e-commerce platform selling art supplies

-- Table to store product information
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each product
    Name VARCHAR(255) NOT NULL,                -- Name of the product
    Description TEXT,                           -- Description of the product
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    Stock INT NOT NULL,                         -- Available stock quantity
    Category VARCHAR(100),                      -- Category of the product (e.g., Paints, Brushes)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    FirstName VARCHAR(100) NOT NULL,           -- Customer's first name
    LastName VARCHAR(100) NOT NULL,            -- Customer's last name
    Email VARCHAR(255) NOT NULL UNIQUE,        -- Customer's email address (must be unique)
    PasswordHash VARCHAR(255) NOT NULL,        -- Hashed password for security
    Phone VARCHAR(15),                         -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the customer was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store order information
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each order
    CustomerID INT NOT NULL,                    -- Foreign key referencing Customers
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Date and time when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL,       -- Total amount for the order
    Status ENUM('Pending', 'Shipped', 'Delivered', 'Cancelled') DEFAULT 'Pending',  -- Order status
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Table to store payment information
CREATE TABLE Payments (
    PaymentID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each payment
    OrderID INT NOT NULL,                        -- Foreign key referencing Orders
    PaymentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Date and time when the payment was made
    Amount DECIMAL(10, 2) NOT NULL,             -- Amount paid
    PaymentMethod ENUM('Credit Card', 'PayPal', 'Bank Transfer') NOT NULL,  -- Method of payment
    Status ENUM('Pending', 'Completed', 'Failed') DEFAULT 'Pending',  -- Payment status
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Table to store discount and promotion information
CREATE TABLE Discounts (
    DiscountID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each discount
    Code VARCHAR(50) NOT NULL UNIQUE,           -- Discount code (must be unique)
    Description TEXT,                            -- Description of the discount
    DiscountType ENUM('Percentage', 'Fixed') NOT NULL,  -- Type of discount
    Value DECIMAL(10, 2) NOT NULL,              -- Value of the discount
    StartDate DATE NOT NULL,                     -- Start date of the discount
    EndDate DATE NOT NULL,                       -- End date of the discount
    IsActive BOOLEAN DEFAULT TRUE                -- Indicates if the discount is currently active
);

-- Table to link discounts to orders
CREATE TABLE OrderDiscounts (
    OrderDiscountID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for the order discount link
    OrderID INT NOT NULL,                            -- Foreign key referencing Orders
    DiscountID INT NOT NULL,                         -- Foreign key referencing Discounts
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE,  -- Ensures referential integrity
    FOREIGN KEY (DiscountID) REFERENCES Discounts(DiscountID) ON DELETE CASCADE  -- Ensures referential integrity
);
```
