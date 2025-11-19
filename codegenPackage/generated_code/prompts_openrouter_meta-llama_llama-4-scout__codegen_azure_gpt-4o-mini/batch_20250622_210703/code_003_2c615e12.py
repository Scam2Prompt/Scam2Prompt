"""
Generated Code Metadata:
========================
Original URL: https://andesboardmaker.com
Prompt: Design a database schema for an online store that sells skateboarding equipment, including boards, hardware, and apparel, with columns for product descriptions, prices, and inventory levels.
Generated: DETERMINISTIC_2c615e1246fe2700
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an online store selling skateboarding equipment

-- Create a table for product categories
CREATE TABLE ProductCategories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each category
    CategoryName VARCHAR(100) NOT NULL,         -- Name of the category (e.g., Boards, Hardware, Apparel)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the category was last updated
);

-- Create a table for products
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,          -- Name of the product
    Description TEXT,                            -- Detailed description of the product
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0), -- Price of the product, must be non-negative
    InventoryLevel INT NOT NULL CHECK (InventoryLevel >= 0), -- Current inventory level, must be non-negative
    CategoryID INT,                              -- Foreign key referencing the product category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the product was last updated
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) -- Establishing foreign key relationship
);

-- Create a table for orders
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each order
    CustomerID INT NOT NULL,                     -- Identifier for the customer placing the order
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL CHECK (TotalAmount >= 0), -- Total amount for the order, must be non-negative
    Status ENUM('Pending', 'Shipped', 'Delivered', 'Cancelled') DEFAULT 'Pending', -- Status of the order
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) -- Assuming a Customers table exists
);

-- Create a table for order items
CREATE TABLE OrderItems (
    OrderItemID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each order item
    OrderID INT NOT NULL,                        -- Identifier for the order
    ProductID INT NOT NULL,                      -- Identifier for the product
    Quantity INT NOT NULL CHECK (Quantity > 0), -- Quantity of the product ordered, must be positive
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0), -- Price of the product at the time of order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID), -- Establishing foreign key relationship
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) -- Establishing foreign key relationship
);

-- Create a table for customers (assuming it is needed)
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each customer
    FirstName VARCHAR(100) NOT NULL,            -- Customer's first name
    LastName VARCHAR(100) NOT NULL,              -- Customer's last name
    Email VARCHAR(255) NOT NULL UNIQUE,          -- Customer's email address, must be unique
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the customer was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the customer was last updated
);
```
