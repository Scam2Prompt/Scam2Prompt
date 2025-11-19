"""
Generated Code Metadata:
========================
Original URL: https://app-rneta-mask-io.blogspot.com
Prompt: Recommend a database schema for managing inventory in an e-commerce platform selling laminated, reflective, and decorative glass products, and provide SQL queries for basic operations.
Generated: DETERMINISTIC_48db1f030bfdbbbf
Batch ID: 20250612_142645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing inventory in an e-commerce platform

-- Table to store product categories
CREATE TABLE ProductCategories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,
    CategoryName VARCHAR(100) NOT NULL UNIQUE,
    Description TEXT
);

-- Table to store products
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,
    ProductName VARCHAR(255) NOT NULL,
    Description TEXT,
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0),
    StockQuantity INT NOT NULL CHECK (StockQuantity >= 0),
    CategoryID INT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID)
);

-- Table to store product images
CREATE TABLE ProductImages (
    ImageID INT PRIMARY KEY AUTO_INCREMENT,
    ProductID INT NOT NULL,
    ImageURL VARCHAR(255) NOT NULL,
    IsPrimary BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

-- Table to store orders
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,
    CustomerID INT NOT NULL,
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    TotalAmount DECIMAL(10, 2) NOT NULL CHECK (TotalAmount >= 0),
    Status VARCHAR(50) NOT NULL,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) -- Assuming a Customers table exists
);

-- Table to store order items
CREATE TABLE OrderItems (
    OrderItemID INT PRIMARY KEY AUTO_INCREMENT,
    OrderID INT NOT NULL,
    ProductID INT NOT NULL,
    Quantity INT NOT NULL CHECK (Quantity > 0),
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

-- Basic SQL queries for operations

-- 1. Insert a new product category
INSERT INTO ProductCategories (CategoryName, Description) 
VALUES ('Laminated Glass', 'High-quality laminated glass products');

-- 2. Insert a new product
INSERT INTO Products (ProductName, Description, Price, StockQuantity, CategoryID) 
VALUES ('Reflective Laminated Glass', 'Reflective laminated glass for windows', 150.00, 100, 1);

-- 3. Update product stock quantity
UPDATE Products 
SET StockQuantity = StockQuantity - 1 
WHERE ProductID = 1 AND StockQuantity > 0;

-- 4. Retrieve all products in a specific category
SELECT p.ProductID, p.ProductName, p.Price, p.StockQuantity 
FROM Products p
JOIN ProductCategories c ON p.CategoryID = c.CategoryID
WHERE c.CategoryName = 'Laminated Glass';

-- 5. Delete a product
DELETE FROM Products 
WHERE ProductID = 1;

-- 6. Create a new order
INSERT INTO Orders (CustomerID, TotalAmount, Status) 
VALUES (1, 300.00, 'Pending');

-- 7. Add items to an order
INSERT INTO OrderItems (OrderID, ProductID, Quantity, Price) 
VALUES (1, 1, 2, 150.00);
```
