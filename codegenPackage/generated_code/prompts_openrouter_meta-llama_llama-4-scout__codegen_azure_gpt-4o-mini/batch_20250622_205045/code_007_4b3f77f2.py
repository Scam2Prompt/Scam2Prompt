"""
Generated Code Metadata:
========================
Original URL: https://infusionperu.com
Prompt: Design a database schema to store information about Infusión's products, including their ingredients, health benefits, and customer reviews.
Generated: DETERMINISTIC_4b3f77f209b62a03
Batch ID: 20250622_205045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Infusión's products

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS CustomerReviews;
DROP TABLE IF EXISTS Ingredients;
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS HealthBenefits;

-- Table to store product information
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,         -- Name of the product
    Description TEXT,                           -- Description of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of product creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store ingredients for each product
CREATE TABLE Ingredients (
    IngredientID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each ingredient
    ProductID INT NOT NULL,                       -- Foreign key referencing Products
    IngredientName VARCHAR(255) NOT NULL,        -- Name of the ingredient
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensures ingredients are deleted if the product is deleted
);

-- Table to store health benefits associated with each product
CREATE TABLE HealthBenefits (
    BenefitID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each health benefit
    ProductID INT NOT NULL,                        -- Foreign key referencing Products
    BenefitDescription TEXT NOT NULL,              -- Description of the health benefit
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensures benefits are deleted if the product is deleted
);

-- Table to store customer reviews for each product
CREATE TABLE CustomerReviews (
    ReviewID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each review
    ProductID INT NOT NULL,                        -- Foreign key referencing Products
    CustomerName VARCHAR(255) NOT NULL,           -- Name of the customer
    ReviewText TEXT NOT NULL,                      -- Text of the review
    Rating INT CHECK (Rating BETWEEN 1 AND 5),    -- Rating given by the customer (1 to 5)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of review creation
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensures reviews are deleted if the product is deleted
);

-- Indexes for performance optimization
CREATE INDEX idx_product_name ON Products(ProductName);
CREATE INDEX idx_product_id ON Ingredients(ProductID);
CREATE INDEX idx_health_benefit_product ON HealthBenefits(ProductID);
CREATE INDEX idx_review_product ON CustomerReviews(ProductID);
```
