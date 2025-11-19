"""
Generated Code Metadata:
========================
Original URL: https://bllabs.co
Prompt: "Design a database schema to store information about research peptides, bioregulators, and small molecules, including product details, pricing, and shipping information for a supplier like BioLongevity Labs."
Generated: DETERMINISTIC_b8284ab93e194dd8
Batch ID: 20250622_212712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about research peptides, bioregulators, and small molecules

-- Create a table for suppliers
CREATE TABLE Suppliers (
    SupplierID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each supplier
    SupplierName VARCHAR(255) NOT NULL,         -- Name of the supplier
    ContactEmail VARCHAR(255),                   -- Contact email for the supplier
    PhoneNumber VARCHAR(20),                     -- Contact phone number
    Address VARCHAR(255),                        -- Supplier address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Create a table for product categories
CREATE TABLE ProductCategories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each category
    CategoryName VARCHAR(100) NOT NULL UNIQUE,   -- Name of the product category
    Description TEXT                             -- Description of the category
);

-- Create a table for products
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,           -- Name of the product
    CategoryID INT,                               -- Foreign key referencing ProductCategories
    SupplierID INT,                               -- Foreign key referencing Suppliers
    Description TEXT,                             -- Detailed description of the product
    Price DECIMAL(10, 2) NOT NULL,               -- Price of the product
    StockQuantity INT DEFAULT 0,                 -- Quantity in stock
    ShippingInfo VARCHAR(255),                    -- Shipping information
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) ON DELETE SET NULL,
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID) ON DELETE CASCADE
);

-- Create a table for product reviews
CREATE TABLE ProductReviews (
    ReviewID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each review
    ProductID INT,                                -- Foreign key referencing Products
    ReviewText TEXT,                              -- Text of the review
    Rating INT CHECK (Rating BETWEEN 1 AND 5),   -- Rating from 1 to 5
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Create a table for orders
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each order
    SupplierID INT,                               -- Foreign key referencing Suppliers
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of the order
    TotalAmount DECIMAL(10, 2) NOT NULL,         -- Total amount for the order
    ShippingAddress VARCHAR(255),                 -- Shipping address for the order
    Status VARCHAR(50) DEFAULT 'Pending',         -- Status of the order
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID) ON DELETE CASCADE
);

-- Create a table for order items
CREATE TABLE OrderItems (
    OrderItemID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each order item
    OrderID INT,                                  -- Foreign key referencing Orders
    ProductID INT,                                -- Foreign key referencing Products
    Quantity INT NOT NULL,                        -- Quantity of the product ordered
    Price DECIMAL(10, 2) NOT NULL,               -- Price of the product at the time of order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Indexes for performance optimization
CREATE INDEX idx_product_name ON Products(ProductName);
CREATE INDEX idx_supplier_name ON Suppliers(SupplierName);
CREATE INDEX idx_order_date ON Orders(OrderDate);
```
