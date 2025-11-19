"""
Generated Code Metadata:
========================
Original URL: https://www.apos.cl
Prompt: "Design a database schema for an e-commerce platform specializing in paper roll distribution, with tables for products, customers, orders, and pricing information specific to the Chilean market."
Generated: DETERMINISTIC_6caa336d734af67a
Batch ID: 20250622_205138
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an e-commerce platform specializing in paper roll distribution

-- Create a table for storing product information
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,       -- Name of the product
    Description TEXT,                         -- Description of the product
    Price DECIMAL(10, 2) NOT NULL,           -- Price of the product in Chilean Pesos
    StockQuantity INT NOT NULL,               -- Quantity available in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the product was last updated
);

-- Create a table for storing customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each customer
    FirstName VARCHAR(100) NOT NULL,          -- Customer's first name
    LastName VARCHAR(100) NOT NULL,           -- Customer's last name
    Email VARCHAR(255) NOT NULL UNIQUE,       -- Customer's email address (must be unique)
    PhoneNumber VARCHAR(20),                   -- Customer's phone number
    Address VARCHAR(255) NOT NULL,             -- Customer's shipping address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the customer was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the customer was last updated
);

-- Create a table for storing order information
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each order
    CustomerID INT NOT NULL,                   -- Foreign key referencing the Customers table
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL,      -- Total amount for the order
    Status ENUM('Pending', 'Shipped', 'Delivered', 'Cancelled') DEFAULT 'Pending', -- Status of the order
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table for storing pricing information specific to the Chilean market
CREATE TABLE Pricing (
    PricingID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each pricing record
    ProductID INT NOT NULL,                    -- Foreign key referencing the Products table
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product in Chilean Pesos
    EffectiveDate DATE NOT NULL,               -- Date when the price becomes effective
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table for storing order items (products within an order)
CREATE TABLE OrderItems (
    OrderItemID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each order item
    OrderID INT NOT NULL,                       -- Foreign key referencing the Orders table
    ProductID INT NOT NULL,                     -- Foreign key referencing the Products table
    Quantity INT NOT NULL,                      -- Quantity of the product ordered
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product at the time of order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensures referential integrity
);
```
