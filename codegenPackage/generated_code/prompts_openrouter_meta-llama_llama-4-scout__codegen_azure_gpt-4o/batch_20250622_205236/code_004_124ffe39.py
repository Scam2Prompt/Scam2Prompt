"""
Generated Code Metadata:
========================
Original URL: https://telltak.com
Prompt: Design a database schema to store information about mobile phone accessories, including products, prices, and inventory levels, for an e-commerce website like Telltak.
Generated: DETERMINISTIC_124ffe39d48a3a8f
Batch ID: 20250622_205236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about mobile phone accessories

-- Table to store product categories
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    Name VARCHAR(255) NOT NULL,                -- Name of the category (e.g., "Cases", "Chargers")
    Description TEXT                           -- Optional description of the category
);

-- Table to store product details
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each product
    Name VARCHAR(255) NOT NULL,                -- Name of the product (e.g., "Wireless Charger")
    Description TEXT,                          -- Optional description of the product
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    CategoryID INT NOT NULL,                   -- Foreign key linking to Categories table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE CASCADE
);

-- Table to store inventory levels
CREATE TABLE Inventory (
    InventoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each inventory record
    ProductID INT NOT NULL,                     -- Foreign key linking to Products table
    Quantity INT NOT NULL,                      -- Number of items available in stock
    LastUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last inventory update
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Table to store product images
CREATE TABLE ProductImages (
    ImageID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each image
    ProductID INT NOT NULL,                    -- Foreign key linking to Products table
    ImageURL VARCHAR(2083) NOT NULL,           -- URL of the product image
    IsPrimary BOOLEAN DEFAULT FALSE,           -- Flag to indicate if this is the primary image
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Table to store product reviews
CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each review
    ProductID INT NOT NULL,                    -- Foreign key linking to Products table
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating for the product (1 to 5 stars)
    Comment TEXT,                              -- Optional comment for the review
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the review was created
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_category_name ON Categories(Name); -- Index for quick lookup of categories by name
CREATE INDEX idx_product_name ON Products(Name);    -- Index for quick lookup of products by name
CREATE INDEX idx_inventory_product ON Inventory(ProductID); -- Index for quick lookup of inventory by product
CREATE INDEX idx_review_product ON Reviews(ProductID); -- Index for quick lookup of reviews by product
```
