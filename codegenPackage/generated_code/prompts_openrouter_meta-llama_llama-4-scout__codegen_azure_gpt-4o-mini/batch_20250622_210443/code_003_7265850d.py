"""
Generated Code Metadata:
========================
Original URL: https://pavingblockcirebon.com
Prompt: "Design a database schema to store information about different types of concrete products, such as paving blocks, kanstin, and buis beton, similar to those offered by Komando Block Cirebon."
Generated: DETERMINISTIC_7265850d21ddb48f
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about concrete products

CREATE DATABASE ConcreteProductsDB;

USE ConcreteProductsDB;

-- Table to store product categories (e.g., Paving Blocks, Kanstin, Buis Beton)
CREATE TABLE ProductCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each category
    CategoryName VARCHAR(100) NOT NULL,          -- Name of the product category
    Description TEXT,                             -- Description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the category was last updated
);

-- Table to store concrete products
CREATE TABLE ConcreteProducts (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each product
    ProductName VARCHAR(100) NOT NULL,            -- Name of the concrete product
    CategoryID INT NOT NULL,                       -- Foreign key referencing ProductCategories
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the product
    Dimensions VARCHAR(50),                        -- Dimensions of the product (e.g., length x width x height)
    Weight DECIMAL(10, 2),                        -- Weight of the product
    Color VARCHAR(50),                            -- Color of the product
    StockQuantity INT DEFAULT 0,                  -- Quantity available in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the product was last updated
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store product images
CREATE TABLE ProductImages (
    ImageID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each image
    ProductID INT NOT NULL,                       -- Foreign key referencing ConcreteProducts
    ImageURL VARCHAR(255) NOT NULL,               -- URL of the product image
    AltText VARCHAR(100),                         -- Alternative text for the image
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the image was added
    FOREIGN KEY (ProductID) REFERENCES ConcreteProducts(ProductID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store customer reviews for products
CREATE TABLE ProductReviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each review
    ProductID INT NOT NULL,                       -- Foreign key referencing ConcreteProducts
    CustomerName VARCHAR(100) NOT NULL,           -- Name of the customer who reviewed the product
    Rating INT CHECK (Rating BETWEEN 1 AND 5),    -- Rating given by the customer (1 to 5)
    ReviewText TEXT,                              -- Text of the review
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the review was created
    FOREIGN KEY (ProductID) REFERENCES ConcreteProducts(ProductID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Sample data insertion for ProductCategories
INSERT INTO ProductCategories (CategoryName, Description) VALUES
('Paving Blocks', 'Durable paving blocks for outdoor use.'),
('Kanstin', 'Concrete curbs for road and landscape edging.'),
('Buis Beton', 'Concrete pipes for drainage and construction.');

-- Sample data insertion for ConcreteProducts
INSERT INTO ConcreteProducts (ProductName, CategoryID, Price, Dimensions, Weight, Color, StockQuantity) VALUES
('Standard Paving Block', 1, 2.50, '40x40x5 cm', 3.5, 'Gray', 100),
('Curved Kanstin', 2, 3.00, '50x25x15 cm', 5.0, 'Gray', 50),
('Concrete Drain Pipe', 3, 15.00, '100 cm', 25.0, 'Gray', 30);
```
