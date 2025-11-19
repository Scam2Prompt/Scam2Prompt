"""
Generated Code Metadata:
========================
Original URL: https://homemerce.com
Prompt: "Design a simple database schema to store information about different types of coving products, including their dimensions, materials, and prices, as seen on Homemerce."
Generated: DETERMINISTIC_d9c7037d7bb29081
Batch ID: 20250622_212712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about coving products

-- Table to store information about coving products
CREATE TABLE CovingProducts (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    Name VARCHAR(255) NOT NULL,              -- Name of the coving product
    Description TEXT,                        -- Detailed description of the product
    Material VARCHAR(100) NOT NULL,          -- Material of the coving (e.g., plaster, wood, PVC)
    Length DECIMAL(10, 2) NOT NULL,          -- Length of the coving in meters
    Width DECIMAL(10, 2) NOT NULL,           -- Width of the coving in meters
    Height DECIMAL(10, 2) NOT NULL,          -- Height of the coving in meters
    Price DECIMAL(10, 2) NOT NULL,           -- Price of the coving in USD
    StockQuantity INT NOT NULL DEFAULT 0,    -- Quantity available in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Table to store categories for coving products
CREATE TABLE CovingCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    Name VARCHAR(100) NOT NULL,                -- Name of the category (e.g., Modern, Classic)
    Description TEXT                           -- Description of the category
);

-- Table to associate coving products with categories (many-to-many relationship)
CREATE TABLE ProductCategoryMapping (
    MappingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each mapping
    ProductID INT NOT NULL,                   -- Foreign key referencing CovingProducts
    CategoryID INT NOT NULL,                  -- Foreign key referencing CovingCategories
    FOREIGN KEY (ProductID) REFERENCES CovingProducts(ProductID) ON DELETE CASCADE,
    FOREIGN KEY (CategoryID) REFERENCES CovingCategories(CategoryID) ON DELETE CASCADE
);

-- Table to store reviews for coving products
CREATE TABLE ProductReviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each review
    ProductID INT NOT NULL,                  -- Foreign key referencing CovingProducts
    Rating INT NOT NULL CHECK (Rating BETWEEN 1 AND 5), -- Rating (1 to 5 stars)
    ReviewText TEXT,                         -- Text of the review
    ReviewerName VARCHAR(100),               -- Name of the reviewer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the review was added
    FOREIGN KEY (ProductID) REFERENCES CovingProducts(ProductID) ON DELETE CASCADE
);

-- Indexes for faster querying
CREATE INDEX idx_product_name ON CovingProducts(Name);
CREATE INDEX idx_category_name ON CovingCategories(Name);
CREATE INDEX idx_product_category ON ProductCategoryMapping(ProductID, CategoryID);
CREATE INDEX idx_review_product ON ProductReviews(ProductID);
```
