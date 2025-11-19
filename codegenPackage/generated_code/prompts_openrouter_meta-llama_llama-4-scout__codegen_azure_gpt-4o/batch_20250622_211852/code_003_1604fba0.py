"""
Generated Code Metadata:
========================
Original URL: https://et-magiic-soll-enter-eth-9.blogspot.com
Prompt: Create a SQL query to manage inventory for an online clothing store like Dandaloja, including tables for products, sizes, and prices.
Generated: DETERMINISTIC_1604fba0fb78632d
Batch ID: 20250622_211852
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a table to store product information
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,        -- Name of the product
    Description TEXT,                         -- Description of the product
    Category VARCHAR(100),                    -- Category of the product (e.g., shirts, pants, etc.)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table to store size information for products
CREATE TABLE Sizes (
    SizeID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each size
    ProductID INT NOT NULL,                   -- Foreign key linking to Products table
    Size VARCHAR(50) NOT NULL,                -- Size of the product (e.g., S, M, L, XL)
    Quantity INT NOT NULL DEFAULT 0,          -- Quantity available for this size
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the size was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Cascade delete if product is removed
);

-- Create a table to store price information for products
CREATE TABLE Prices (
    PriceID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each price entry
    ProductID INT NOT NULL,                   -- Foreign key linking to Products table
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product
    Currency VARCHAR(10) NOT NULL DEFAULT 'USD', -- Currency for the price (default is USD)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the price was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Cascade delete if product is removed
);

-- Example query to add a new product
INSERT INTO Products (ProductName, Description, Category)
VALUES ('Men\'s T-Shirt', 'Comfortable cotton t-shirt', 'Shirts');

-- Example query to add sizes for the product
INSERT INTO Sizes (ProductID, Size, Quantity)
VALUES 
    (1, 'S', 50),
    (1, 'M', 100),
    (1, 'L', 75);

-- Example query to add price for the product
INSERT INTO Prices (ProductID, Price, Currency)
VALUES (1, 19.99, 'USD');

-- Example query to retrieve inventory details for a product
SELECT 
    p.ProductName,
    p.Description,
    p.Category,
    s.Size,
    s.Quantity,
    pr.Price,
    pr.Currency
FROM Products p
JOIN Sizes s ON p.ProductID = s.ProductID
JOIN Prices pr ON p.ProductID = pr.ProductID
WHERE p.ProductID = 1;

-- Example query to update the quantity of a specific size
UPDATE Sizes
SET Quantity = Quantity - 1
WHERE ProductID = 1 AND Size = 'M';

-- Example query to delete a product and its associated data
DELETE FROM Products
WHERE ProductID = 1;
```
