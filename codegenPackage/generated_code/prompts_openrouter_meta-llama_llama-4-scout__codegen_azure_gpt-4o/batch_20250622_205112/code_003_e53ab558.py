"""
Generated Code Metadata:
========================
Original URL: https://opticalize.com
Prompt: Design a simple database schema to store information about eyeglass and sunglass products, including details like frame type, material, and UV protection, inspired by Optic Alizé's product offerings.
Generated: DETERMINISTIC_e53ab55870dcf351
Batch ID: 20250622_205112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing eyeglass and sunglass product information

-- Table to store product categories (e.g., eyeglasses, sunglasses)
CREATE TABLE ProductCategory (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the category
    Name VARCHAR(50) NOT NULL,                 -- Name of the category (e.g., "Eyeglasses", "Sunglasses")
    Description TEXT                           -- Optional description of the category
);

-- Table to store product details
CREATE TABLE Product (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for the product
    Name VARCHAR(100) NOT NULL,                -- Name of the product
    CategoryID INT NOT NULL,                   -- Foreign key referencing ProductCategory
    FrameType VARCHAR(50) NOT NULL,            -- Type of frame (e.g., "Full Rim", "Half Rim", "Rimless")
    Material VARCHAR(50) NOT NULL,             -- Material of the frame (e.g., "Metal", "Plastic", "Titanium")
    UVProtection BOOLEAN NOT NULL,             -- Indicates whether the product has UV protection (true/false)
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    Stock INT NOT NULL,                        -- Number of items available in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CategoryID) REFERENCES ProductCategory(CategoryID) ON DELETE CASCADE
);

-- Table to store product images
CREATE TABLE ProductImage (
    ImageID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for the image
    ProductID INT NOT NULL,                    -- Foreign key referencing Product
    ImageURL VARCHAR(255) NOT NULL,            -- URL of the product image
    AltText VARCHAR(100),                      -- Alternative text for the image (useful for accessibility)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the image was added
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID) ON DELETE CASCADE
);

-- Table to store customer reviews for products
CREATE TABLE ProductReview (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for the review
    ProductID INT NOT NULL,                    -- Foreign key referencing Product
    CustomerName VARCHAR(100) NOT NULL,        -- Name of the customer who left the review
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating given by the customer (1 to 5)
    Comment TEXT,                              -- Optional comment provided by the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the review was added
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_product_category ON Product(CategoryID); -- Index for faster lookups by category
CREATE INDEX idx_product_name ON Product(Name);           -- Index for faster lookups by product name
CREATE INDEX idx_review_product ON ProductReview(ProductID); -- Index for faster lookups by product in reviews
```
