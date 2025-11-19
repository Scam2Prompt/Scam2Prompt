"""
Generated Code Metadata:
========================
Original URL: https://casadelospastes.com
Prompt: Design a database schema to store information about La Casa de los Pastes' products, including pastes and empanadas, with attributes like ingredients, prices, and nutritional information.
Generated: DETERMINISTIC_6db139d943c0a4c0
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for La Casa de los Pastes' products

-- Create a table to store product categories (e.g., Pastes, Empanadas)
CREATE TABLE ProductCategories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each category
    CategoryName VARCHAR(100) NOT NULL UNIQUE,  -- Name of the product category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of the last update
);

-- Create a table to store products
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each product
    ProductName VARCHAR(100) NOT NULL,  -- Name of the product
    CategoryID INT NOT NULL,  -- Foreign key referencing the product category
    Ingredients TEXT NOT NULL,  -- List of ingredients used in the product
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0),  -- Price of the product, must be non-negative
    NutritionalInformation TEXT,  -- Nutritional information of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of the last update
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Create a table to store customer reviews for products
CREATE TABLE ProductReviews (
    ReviewID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each review
    ProductID INT NOT NULL,  -- Foreign key referencing the product
    CustomerName VARCHAR(100) NOT NULL,  -- Name of the customer who wrote the review
    Rating INT NOT NULL CHECK (Rating BETWEEN 1 AND 5),  -- Rating given by the customer (1 to 5)
    ReviewText TEXT,  -- Text of the review
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the review was created
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Create a table to store inventory information for products
CREATE TABLE ProductInventory (
    InventoryID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each inventory record
    ProductID INT NOT NULL,  -- Foreign key referencing the product
    QuantityInStock INT NOT NULL CHECK (QuantityInStock >= 0),  -- Quantity of the product in stock
    LastUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of the last update
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Create a table to store promotions or discounts for products
CREATE TABLE ProductPromotions (
    PromotionID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each promotion
    ProductID INT NOT NULL,  -- Foreign key referencing the product
    DiscountPercentage DECIMAL(5, 2) NOT NULL CHECK (DiscountPercentage >= 0 AND DiscountPercentage <= 100),  -- Discount percentage
    StartDate DATE NOT NULL,  -- Start date of the promotion
    EndDate DATE NOT NULL,  -- End date of the promotion
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE  -- Ensure referential integrity
);
```
