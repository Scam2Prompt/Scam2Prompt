"""
Generated Code Metadata:
========================
Original URL: https://allorashopping.com
Prompt: Design a database schema to store product information, including attributes like size, material, style, and price, for an e-commerce platform similar to Allora Shopping.
Generated: DETERMINISTIC_2da52b21cc8f10b7
Batch ID: 20250622_212519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing product information for an e-commerce platform

-- Table to store product categories
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    Name VARCHAR(255) NOT NULL,                -- Name of the category
    Description TEXT,                          -- Optional description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the category was last updated
);

-- Table to store products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each product
    Name VARCHAR(255) NOT NULL,                -- Name of the product
    Description TEXT,                          -- Detailed description of the product
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    CategoryID INT,                            -- Foreign key to the Categories table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the product was last updated
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE SET NULL -- Maintain referential integrity
);

-- Table to store product attributes
CREATE TABLE ProductAttributes (
    AttributeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each attribute
    ProductID INT NOT NULL,                     -- Foreign key to the Products table
    AttributeName VARCHAR(255) NOT NULL,        -- Name of the attribute (e.g., size, material, style)
    AttributeValue VARCHAR(255) NOT NULL,       -- Value of the attribute (e.g., "Large", "Cotton", "Casual")
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the attribute was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the attribute was last updated
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Maintain referential integrity
);

-- Table to store product images
CREATE TABLE ProductImages (
    ImageID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each image
    ProductID INT NOT NULL,                    -- Foreign key to the Products table
    ImageURL VARCHAR(2083) NOT NULL,           -- URL of the product image
    IsPrimary BOOLEAN DEFAULT FALSE,           -- Flag to indicate if this is the primary image
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the image was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the image was last updated
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Maintain referential integrity
);

-- Table to store product inventory
CREATE TABLE ProductInventory (
    InventoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each inventory record
    ProductID INT NOT NULL,                     -- Foreign key to the Products table
    Quantity INT NOT NULL DEFAULT 0,            -- Quantity of the product in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the inventory record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the inventory record was last updated
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Maintain referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_product_name ON Products(Name);
CREATE INDEX idx_category_name ON Categories(Name);
CREATE INDEX idx_attribute_name ON ProductAttributes(AttributeName);
CREATE INDEX idx_image_product ON ProductImages(ProductID);
CREATE INDEX idx_inventory_product ON ProductInventory(ProductID);
```
