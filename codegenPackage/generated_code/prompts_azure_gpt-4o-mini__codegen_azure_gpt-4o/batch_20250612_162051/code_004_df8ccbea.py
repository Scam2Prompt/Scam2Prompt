"""
Generated Code Metadata:
========================
Original URL: https://harinderfarms.com
Prompt: Design a database schema for managing orders and deliveries of agricultural products like corn silage bales and potato seeds from Harinder Farms.
Generated: DETERMINISTIC_df8ccbea3241cac1
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing orders and deliveries of agricultural products from Harinder Farms

-- Table to store information about customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    Name VARCHAR(100) NOT NULL,                -- Customer's name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Customer's email address
    PhoneNumber VARCHAR(15),                   -- Customer's phone number
    Address TEXT NOT NULL,                     -- Customer's delivery address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the customer was added
);

-- Table to store information about products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    Name VARCHAR(100) NOT NULL,               -- Name of the product (e.g., Corn Silage Bales, Potato Seeds)
    Description TEXT,                         -- Description of the product
    UnitPrice DECIMAL(10, 2) NOT NULL,        -- Price per unit of the product
    StockQuantity INT NOT NULL,               -- Quantity of the product available in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the product was added
);

-- Table to store orders placed by customers
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each order
    CustomerID INT NOT NULL,                  -- Foreign key referencing the Customers table
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL,      -- Total amount for the order
    Status ENUM('Pending', 'Processing', 'Shipped', 'Delivered', 'Cancelled') DEFAULT 'Pending', -- Status of the order
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Cascade delete if customer is removed
);

-- Table to store details of products in each order
CREATE TABLE OrderDetails (
    OrderDetailID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order detail
    OrderID INT NOT NULL,                         -- Foreign key referencing the Orders table
    ProductID INT NOT NULL,                       -- Foreign key referencing the Products table
    Quantity INT NOT NULL,                        -- Quantity of the product ordered
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the product at the time of order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE, -- Cascade delete if order is removed
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Cascade delete if product is removed
);

-- Table to store delivery information for orders
CREATE TABLE Deliveries (
    DeliveryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each delivery
    OrderID INT NOT NULL,                      -- Foreign key referencing the Orders table
    DeliveryDate TIMESTAMP,                    -- Date and time of delivery
    DeliveryStatus ENUM('Scheduled', 'In Transit', 'Delivered', 'Failed') DEFAULT 'Scheduled', -- Status of the delivery
    Notes TEXT,                                -- Additional notes about the delivery
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE -- Cascade delete if order is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_customer_email ON Customers(Email); -- Index for quick lookup of customers by email
CREATE INDEX idx_order_status ON Orders(Status);     -- Index for quick lookup of orders by status
CREATE INDEX idx_delivery_status ON Deliveries(DeliveryStatus); -- Index for quick lookup of deliveries by status
```
