"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://baochuanco.com
Prompt: Create a database schema to store customer details, product information, and order history for a wire mesh product company like Baochuan Wire Mesh.
Generated: DETERMINISTIC_9172171df9336730
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for a wire mesh product company

-- Create a table to store customer details
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for the customer
    FirstName VARCHAR(50) NOT NULL,             -- First name of the customer
    LastName VARCHAR(50) NOT NULL,              -- Last name of the customer
    Email VARCHAR(100) UNIQUE NOT NULL,         -- Email address of the customer (must be unique)
    Phone VARCHAR(15),                          -- Phone number of the customer
    Address TEXT,                               -- Address of the customer
    City VARCHAR(50),                           -- City of the customer
    State VARCHAR(50),                          -- State of the customer
    PostalCode VARCHAR(10),                     -- Postal code of the customer
    Country VARCHAR(50),                        -- Country of the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last record update
);

-- Create a table to store product information
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for the product
    ProductName VARCHAR(100) NOT NULL,          -- Name of the product
    Description TEXT,                           -- Description of the product
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the product
    Stock INT NOT NULL,                         -- Number of items in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last record update
);

-- Create a table to store order history
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for the order
    CustomerID INT NOT NULL,                    -- Foreign key referencing Customers
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL,        -- Total amount for the order
    Status ENUM('Pending', 'Completed', 'Cancelled') NOT NULL, -- Status of the order
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last record update
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) -- Enforce relationship with Customers
);

-- Create a table to store order details (products in each order)
CREATE TABLE OrderDetails (
    OrderDetailID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for order detail
    OrderID INT NOT NULL,                         -- Foreign key referencing Orders
    ProductID INT NOT NULL,                       -- Foreign key referencing Products
    Quantity INT NOT NULL,                        -- Quantity of the product in the order
    Price DECIMAL(10, 2) NOT NULL,                -- Unit price of the product
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID), -- Enforce relationship with Orders
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) -- Enforce relationship with Products
);

-- Add indexes for faster searching
CREATE INDEX idx_customer_email ON Customers(Email);       -- Index on email for quick customer lookup
CREATE INDEX idx_product_name ON Products(ProductName);    -- Index on product name for quick product lookup
CREATE INDEX idx_order_customer ON Orders(CustomerID);     -- Index on customerID for quick order lookup
CREATE INDEX idx_order_date ON Orders(OrderDate);          -- Index on orderDate for quick date-based searches
CREATE INDEX idx_order_product ON OrderDetails(ProductID); -- Index on productID for quick product-based order lookup
```
