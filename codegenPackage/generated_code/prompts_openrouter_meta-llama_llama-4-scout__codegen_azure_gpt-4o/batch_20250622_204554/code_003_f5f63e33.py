"""
Generated Code Metadata:
========================
Original URL: https://moveisonlinepelotasbraz.blogspot.com
Prompt: Design a SQL database schema for storing furniture products, including tables for products, categories (e.g., Sala, Quarto, Cozinha, Banheiro), and product images, similar to the product catalog on moveisonlinepelotasbraz.
Generated: DETERMINISTIC_f5f63e333d1fc74b
Batch ID: 20250622_204554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for Furniture Products Catalog

-- Table: Categories
<<<<<<< HEAD
-- Stores the categories of furniture products (e.g., Sala, Quarto, Cozinha, Banheiro)
=======
-- Stores information about product categories (e.g., Sala, Quarto, Cozinha, Banheiro)
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    Name VARCHAR(100) NOT NULL,                -- Name of the category
    Description TEXT                           -- Optional description of the category
);

-- Table: Products
<<<<<<< HEAD
-- Stores the furniture products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each product
    Name VARCHAR(255) NOT NULL,                -- Name of the product
    Description TEXT,                          -- Optional description of the product
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    Stock INT NOT NULL DEFAULT 0,              -- Quantity of the product in stock
    CategoryID INT NOT NULL,                   -- Foreign key linking to Categories table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE CASCADE -- Cascade delete if category is removed
);

-- Table: ProductImages
-- Stores images associated with furniture products
CREATE TABLE ProductImages (
    ImageID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each image
    ProductID INT NOT NULL,                    -- Foreign key linking to Products table
    ImageURL VARCHAR(2083) NOT NULL,           -- URL of the image
    AltText VARCHAR(255),                      -- Alternative text for the image (useful for accessibility)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the image was added
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Cascade delete if product is removed
=======
-- Stores information about furniture products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    Name VARCHAR(255) NOT NULL,               -- Name of the product
    Description TEXT,                         -- Optional description of the product
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product
    Stock INT NOT NULL DEFAULT 0,             -- Quantity of the product in stock
    CategoryID INT NOT NULL,                  -- Foreign key linking to Categories table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table: ProductImages
-- Stores images associated with products
CREATE TABLE ProductImages (
    ImageID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each image
    ProductID INT NOT NULL,                   -- Foreign key linking to Products table
    ImageURL VARCHAR(2083) NOT NULL,          -- URL of the image
    AltText VARCHAR(255),                     -- Alternative text for the image (useful for accessibility)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the image was added
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensures referential integrity
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
);

-- Indexes for performance optimization
CREATE INDEX idx_category_name ON Categories(Name); -- Index for quick lookup of categories by name
CREATE INDEX idx_product_name ON Products(Name);    -- Index for quick lookup of products by name
<<<<<<< HEAD
CREATE INDEX idx_product_category ON Products(CategoryID); -- Index for quick lookup of products by category
CREATE INDEX idx_image_product ON ProductImages(ProductID); -- Index for quick lookup of images by product

-- Example of error handling: Ensure strict mode is enabled for better data integrity
SET sql_mode = 'STRICT_TRANS_TABLES';
=======
CREATE INDEX idx_product_category ON Products(CategoryID); -- Index for filtering products by category
CREATE INDEX idx_image_product ON ProductImages(ProductID); -- Index for filtering images by product

-- Example of error handling: Ensure strict mode is enabled for better data validation
SET sql_mode = 'STRICT_ALL_TABLES';
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
```
