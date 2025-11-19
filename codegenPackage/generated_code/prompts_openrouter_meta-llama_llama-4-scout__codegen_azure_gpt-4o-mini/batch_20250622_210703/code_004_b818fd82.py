"""
Generated Code Metadata:
========================
Original URL: https://yummydelivery.com.ve
Prompt: Design a database schema for a food delivery platform like Yummy Delivery, including tables for products, orders, customers, and delivery information.
Generated: DETERMINISTIC_b818fd826b2ea0f7
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a food delivery platform

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,             -- Customer's first name
    LastName VARCHAR(50) NOT NULL,              -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,         -- Customer's email address (unique)
    PhoneNumber VARCHAR(15),                     -- Customer's phone number
    Address VARCHAR(255) NOT NULL,               -- Customer's delivery address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the customer was created
);

-- Table to store product information
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each product
    Name VARCHAR(100) NOT NULL,                  -- Name of the product
    Description TEXT,                            -- Description of the product
    Price DECIMAL(10, 2) NOT NULL,               -- Price of the product
    Category VARCHAR(50),                        -- Category of the product (e.g., pizza, dessert)
    Stock INT NOT NULL DEFAULT 0,                -- Available stock for the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the product was added
);

-- Table to store order information
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each order
    CustomerID INT NOT NULL,                     -- Foreign key referencing Customers
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL,        -- Total amount for the order
    Status ENUM('Pending', 'In Progress', 'Delivered', 'Cancelled') DEFAULT 'Pending', -- Order status
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store order items (products in each order)
CREATE TABLE OrderItems (
    OrderItemID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each order item
    OrderID INT NOT NULL,                        -- Foreign key referencing Orders
    ProductID INT NOT NULL,                      -- Foreign key referencing Products
    Quantity INT NOT NULL,                       -- Quantity of the product ordered
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the product at the time of order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store delivery information
CREATE TABLE Deliveries (
    DeliveryID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each delivery
    OrderID INT NOT NULL,                        -- Foreign key referencing Orders
    DeliveryAddress VARCHAR(255) NOT NULL,      -- Address where the order is to be delivered
    DeliveryDate TIMESTAMP,                      -- Date and time when the order is delivered
    DeliveryStatus ENUM('Pending', 'In Transit', 'Delivered', 'Failed') DEFAULT 'Pending', -- Delivery status
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE -- Ensures referential integrity
);
```
