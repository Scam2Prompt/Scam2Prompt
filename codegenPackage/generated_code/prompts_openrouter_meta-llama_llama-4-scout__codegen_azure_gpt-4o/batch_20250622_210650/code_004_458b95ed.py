"""
Generated Code Metadata:
========================
Original URL: https://obsidiajeans.com.br
Prompt: Create a SQL database schema for managing clothing products, including shorts and jeans, with attributes like product ID, name, price, and material, inspired by the product catalog of Obsidia Jeans.
Generated: DETERMINISTIC_458b95ede761d953
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL schema for managing clothing products, including shorts and jeans

-- Create a database named 'ClothingStore'
CREATE DATABASE ClothingStore;

-- Use the newly created database
USE ClothingStore;

-- Table to store product categories (e.g., shorts, jeans)
CREATE TABLE ProductCategory (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    CategoryName VARCHAR(50) NOT NULL,         -- Name of the category (e.g., 'Shorts', 'Jeans')
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the category was created
);

-- Table to store clothing products
CREATE TABLE ClothingProduct (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each product
    Name VARCHAR(100) NOT NULL,                -- Name of the product
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    Material VARCHAR(50) NOT NULL,             -- Material of the product (e.g., 'Denim', 'Cotton')
    CategoryID INT NOT NULL,                   -- Foreign key linking to ProductCategory
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CategoryID) REFERENCES ProductCategory(CategoryID) -- Enforce category relationship
);

-- Table to store inventory details for each product
CREATE TABLE Inventory (
    InventoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for inventory record
    ProductID INT NOT NULL,                     -- Foreign key linking to ClothingProduct
    StockQuantity INT NOT NULL,                 -- Quantity of the product in stock
    LastRestocked TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for last restocking
    FOREIGN KEY (ProductID) REFERENCES ClothingProduct(ProductID) -- Enforce product relationship
);

-- Insert sample categories into ProductCategory
INSERT INTO ProductCategory (CategoryName) VALUES
('Shorts'),
('Jeans');

-- Insert sample products into ClothingProduct
INSERT INTO ClothingProduct (Name, Price, Material, CategoryID) VALUES
('Classic Denim Shorts', 29.99, 'Denim', 1),
('Slim Fit Jeans', 49.99, 'Denim', 2),
('Cotton Cargo Shorts', 34.99, 'Cotton', 1),
('Ripped Skinny Jeans', 59.99, 'Denim', 2);

-- Insert sample inventory data into Inventory
INSERT INTO Inventory (ProductID, StockQuantity) VALUES
(1, 100),
(2, 50),
(3, 75),
(4, 30);

-- Query to verify the schema and data
-- SELECT * FROM ProductCategory;
-- SELECT * FROM ClothingProduct;
-- SELECT * FROM Inventory;
```
