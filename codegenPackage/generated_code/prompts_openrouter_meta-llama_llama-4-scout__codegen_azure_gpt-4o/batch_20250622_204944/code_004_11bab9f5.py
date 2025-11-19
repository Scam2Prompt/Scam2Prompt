"""
Generated Code Metadata:
========================
Original URL: https://naimatabbasind.com
Prompt: "Design a database schema to store information about sports wear products, including product categories, materials, and sizes, similar to Naimat Abbas Industries' product range."
Generated: DETERMINISTIC_11bab9f59a2cc293
Batch ID: 20250622_204944
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about sports wear products

-- Table to store product categories
CREATE TABLE ProductCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    CategoryName VARCHAR(100) NOT NULL,        -- Name of the category (e.g., "T-Shirts", "Shorts")
    Description TEXT                           -- Optional description of the category
);

-- Table to store materials used in products
CREATE TABLE Materials (
    MaterialID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each material
    MaterialName VARCHAR(100) NOT NULL,        -- Name of the material (e.g., "Cotton", "Polyester")
    Description TEXT                           -- Optional description of the material
);

-- Table to store available sizes for products
CREATE TABLE Sizes (
    SizeID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each size
    SizeName VARCHAR(50) NOT NULL,             -- Name of the size (e.g., "Small", "Medium", "Large")
    Description TEXT                           -- Optional description of the size
);

-- Table to store sports wear products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each product
    ProductName VARCHAR(150) NOT NULL,         -- Name of the product (e.g., "Men's Running T-Shirt")
    CategoryID INT NOT NULL,                   -- Foreign key referencing ProductCategories
    MaterialID INT NOT NULL,                   -- Foreign key referencing Materials
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    StockQuantity INT NOT NULL,                -- Quantity available in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) ON DELETE CASCADE,
    FOREIGN KEY (MaterialID) REFERENCES Materials(MaterialID) ON DELETE CASCADE
);

-- Table to store product sizes (many-to-many relationship between Products and Sizes)
CREATE TABLE ProductSizes (
    ProductID INT NOT NULL,                    -- Foreign key referencing Products
    SizeID INT NOT NULL,                       -- Foreign key referencing Sizes
    PRIMARY KEY (ProductID, SizeID),           -- Composite primary key
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE,
    FOREIGN KEY (SizeID) REFERENCES Sizes(SizeID) ON DELETE CASCADE
);

-- Example indexes for optimizing queries
CREATE INDEX idx_category_name ON ProductCategories(CategoryName);
CREATE INDEX idx_material_name ON Materials(MaterialName);
CREATE INDEX idx_size_name ON Sizes(SizeName);
CREATE INDEX idx_product_name ON Products(ProductName);
```
