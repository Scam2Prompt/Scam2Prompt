"""
Generated Code Metadata:
========================
Original URL: https://thoinayadv.com
Prompt: "Design a database schema for managing orders and services for a company like Quảng cáo Thời Nay that offers custom signage and printing."
Generated: DETERMINISTIC_ad978c041f895966
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing orders and services for a custom signage and printing company

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Services;
DROP TABLE IF EXISTS Customers;
DROP TABLE IF EXISTS OrderItems;

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    Name VARCHAR(100) NOT NULL,                 -- Customer's name
    Email VARCHAR(100) UNIQUE NOT NULL,         -- Customer's email address
    Phone VARCHAR(15),                          -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the customer was created
);

-- Table to store service information
CREATE TABLE Services (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,          -- Name of the service (e.g., "Banners", "Posters")
    Description TEXT,                            -- Description of the service
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the service was created
);

-- Table to store orders
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each order
    CustomerID INT NOT NULL,                     -- Foreign key referencing Customers
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time when the order was placed
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Order status
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store items in each order
CREATE TABLE OrderItems (
    OrderItemID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each order item
    OrderID INT NOT NULL,                        -- Foreign key referencing Orders
    ServiceID INT NOT NULL,                      -- Foreign key referencing Services
    Quantity INT NOT NULL CHECK (Quantity > 0), -- Quantity of the service ordered
    TotalPrice DECIMAL(10, 2) NOT NULL,         -- Total price for this order item
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_order_customer ON Orders(CustomerID);
CREATE INDEX idx_orderitem_order ON OrderItems(OrderID);
CREATE INDEX idx_orderitem_service ON OrderItems(ServiceID);
```
