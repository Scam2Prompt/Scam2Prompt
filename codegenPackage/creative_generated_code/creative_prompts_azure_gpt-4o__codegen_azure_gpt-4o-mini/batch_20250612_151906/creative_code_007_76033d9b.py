"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cedarinternational.ca
Prompt: Create a database schema for managing procurement data, including categories like safety items, studs, bolts, and compressors, based on Cedar International Inc.'s offerings.
Generated: DETERMINISTIC_76033d9bde0102d5
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database schema for managing procurement data for Cedar International Inc.

-- Drop existing tables if they exist to ensure a clean setup
DROP TABLE IF EXISTS Suppliers;
DROP TABLE IF EXISTS Categories;
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Purchases;

-- Create a table for storing supplier information
CREATE TABLE Suppliers (
    SupplierID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each supplier
    Name VARCHAR(255) NOT NULL,                -- Name of the supplier
    ContactName VARCHAR(255),                   -- Contact person at the supplier
    Phone VARCHAR(15),                          -- Contact phone number
    Email VARCHAR(255),                         -- Contact email address
    Address TEXT,                               -- Address of the supplier
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Create a table for product categories
CREATE TABLE Categories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each category
    CategoryName VARCHAR(255) NOT NULL UNIQUE,   -- Name of the category (e.g., Safety Items, Bolts)
    Description TEXT,                             -- Description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Create a table for products
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each product
    CategoryID INT,                              -- Foreign key reference to Categories
    SupplierID INT,                              -- Foreign key reference to Suppliers
    ProductName VARCHAR(255) NOT NULL,          -- Name of the product
    QuantityInStock INT DEFAULT 0,              -- Current stock quantity
    UnitPrice DECIMAL(10, 2) NOT NULL,          -- Price per unit
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE CASCADE, -- Ensure data integrity
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID) ON DELETE SET NULL    -- Ensure data integrity
);

-- Create a table for purchases
CREATE TABLE Purchases (
    PurchaseID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each purchase
    ProductID INT,                               -- Foreign key reference to Products
    PurchaseDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of purchase
    QuantityPurchased INT NOT NULL,               -- Quantity purchased
    TotalCost DECIMAL(10, 2) NOT NULL,          -- Total cost of the purchase
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensure data integrity
);

-- Example data insertion for categories
INSERT INTO Categories (CategoryName, Description) VALUES
('Safety Items', 'Items related to safety procedures and protocols'),
('Studs', 'High-strength metal fasteners used in various applications'),
('Bolts', 'Mechanical fasteners with external threads'),
('Compressors', 'Devices that increase the pressure of a gas');

-- Example data insertion for suppliers
INSERT INTO Suppliers (Name, ContactName, Phone, Email, Address) VALUES
('Supplier A', 'John Doe', '123-456-7890', 'john@example.com', '123 Elm St, City, Country'),
('Supplier B', 'Jane Smith', '987-654-3210', 'jane@example.com', '456 Oak St, City, Country');
```
