"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://harinderfarms.com
Prompt: Design a database schema for managing orders and deliveries of agricultural products like corn silage bales and potato seeds from Harinder Farms.
Generated: DETERMINISTIC_df8ccbea3241cac1
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Managing Orders and Deliveries from Harinder Farms

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each customer
    FullName VARCHAR(100) NOT NULL,                   -- Full name of the customer
    Email VARCHAR(100) NOT NULL UNIQUE,               -- Email address of the customer
    PhoneNumber VARCHAR(15),                          -- Contact phone number
    Address TEXT NOT NULL,                            -- Shipping address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp for when the customer was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last updated timestamp
);

-- Table to store product information
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each product
    ProductName VARCHAR(100) NOT NULL,                -- Name of the product (e.g., "Corn Silage Bales")
    Description TEXT,                                 -- Description of the product
    UnitPrice DECIMAL(10, 2) NOT NULL,                -- Price per unit of the product
    StockQuantity INT NOT NULL,                       -- Quantity of product available in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp for when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last updated timestamp
);

-- Table to store order information
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,           -- Unique identifier for each order
    CustomerID INT NOT NULL,                          -- Reference to the customer who placed the order
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Date and time the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL,              -- Total amount for the order
    Status ENUM('Pending', 'Processing', 'Shipped', 'Delivered', 'Cancelled') NOT NULL DEFAULT 'Pending', -- Status of the order
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp for when the order was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last updated timestamp
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store details of products in each order
CREATE TABLE OrderDetails (
    OrderDetailID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each order detail
    OrderID INT NOT NULL,                             -- Reference to the order
    ProductID INT NOT NULL,                           -- Reference to the product
    Quantity INT NOT NULL,                            -- Quantity of the product ordered
    SubTotal DECIMAL(10, 2) NOT NULL,                 -- Subtotal amount for this product in the order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store delivery information
CREATE TABLE Deliveries (
    DeliveryID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each delivery
    OrderID INT NOT NULL,                             -- Reference to the order being delivered
    DeliveryDate DATE NOT NULL,                       -- Scheduled or actual delivery date
    DeliveryStatus ENUM('Scheduled', 'Out for Delivery', 'Delivered', 'Delayed') NOT NULL DEFAULT 'Scheduled', -- Current delivery status
    TrackingNumber VARCHAR(50),                       -- Optional tracking number for the delivery
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp for when the delivery record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last updated timestamp
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Add indexes to optimize queries
CREATE INDEX idx_customer_email ON Customers (Email); -- Index for quick customer email lookups
CREATE INDEX idx_order_status ON Orders (Status);     -- Index for quick order status filtering

-- End of Schema
```
