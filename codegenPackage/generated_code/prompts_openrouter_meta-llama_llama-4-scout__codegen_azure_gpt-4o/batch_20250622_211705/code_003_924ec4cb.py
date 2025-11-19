"""
Generated Code Metadata:
========================
Original URL: https://promodinamic.com
Prompt: "Design a database schema for storing information about promotional products, printing methods, and customer orders for a company like Promodinamic."
Generated: DETERMINISTIC_924ec4cb061aebf3
Batch ID: 20250622_211705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about promotional products, printing methods, and customer orders

-- Table to store information about promotional products
CREATE TABLE PromotionalProducts (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    Name VARCHAR(255) NOT NULL,               -- Name of the product
    Description TEXT,                         -- Detailed description of the product
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product
    Stock INT NOT NULL,                       -- Quantity available in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about printing methods
CREATE TABLE PrintingMethods (
    MethodID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each printing method
    Name VARCHAR(255) NOT NULL,              -- Name of the printing method
    Description TEXT,                        -- Detailed description of the printing method
    Cost DECIMAL(10, 2) NOT NULL,            -- Cost of using this printing method
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the method was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(255) NOT NULL,           -- First name of the customer
    LastName VARCHAR(255) NOT NULL,            -- Last name of the customer
    Email VARCHAR(255) NOT NULL UNIQUE,        -- Email address of the customer
    PhoneNumber VARCHAR(20),                   -- Phone number of the customer
    Address TEXT,                              -- Address of the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the customer was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store customer orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order
    CustomerID INT NOT NULL,                -- Foreign key referencing Customers table
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time when the order was placed
    TotalAmount DECIMAL(10, 2) NOT NULL,    -- Total amount for the order
    Status ENUM('Pending', 'Processing', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Status of the order
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the order was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE
);

-- Table to store order details (products and printing methods used in an order)
CREATE TABLE OrderDetails (
    OrderDetailID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order detail
    OrderID INT NOT NULL,                         -- Foreign key referencing Orders table
    ProductID INT NOT NULL,                       -- Foreign key referencing PromotionalProducts table
    MethodID INT NOT NULL,                        -- Foreign key referencing PrintingMethods table
    Quantity INT NOT NULL,                        -- Quantity of the product ordered
    Subtotal DECIMAL(10, 2) NOT NULL,             -- Subtotal for this line item
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the order detail was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE,
    FOREIGN KEY (ProductID) REFERENCES PromotionalProducts(ProductID) ON DELETE CASCADE,
    FOREIGN KEY (MethodID) REFERENCES PrintingMethods(MethodID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_customer_email ON Customers(Email); -- Index for quick lookup by email
CREATE INDEX idx_order_status ON Orders(Status);     -- Index for filtering orders by status
CREATE INDEX idx_order_product ON OrderDetails(ProductID); -- Index for filtering order details by product
CREATE INDEX idx_order_method ON OrderDetails(MethodID);   -- Index for filtering order details by printing method
```
