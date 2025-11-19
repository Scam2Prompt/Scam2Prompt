"""
Generated Code Metadata:
========================
Original URL: https://simbatools.com
Prompt: Design a database schema to store product information for an online store selling industrial supplies, including tables for products, prices, and customer reviews.
Generated: DETERMINISTIC_9f258d8f66b1aefb
Batch ID: 20250622_212347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for industrial supplies online store

CREATE DATABASE IndustrialSupplies;

USE IndustrialSupplies;

-- Create table for products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT,
    ProductName VARCHAR(255) NOT NULL,
    ProductDescription TEXT,
    ProductCategory VARCHAR(100) NOT NULL,
    ProductSubcategory VARCHAR(100),
    ProductImageURL VARCHAR(255),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ProductID)
);

-- Create table for product prices
CREATE TABLE ProductPrices (
    PriceID INT AUTO_INCREMENT,
    ProductID INT NOT NULL,
    Price DECIMAL(10, 2) NOT NULL,
    Discount DECIMAL(10, 2),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PriceID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Create table for customer reviews
CREATE TABLE CustomerReviews (
    ReviewID INT AUTO_INCREMENT,
    ProductID INT NOT NULL,
    CustomerName VARCHAR(255) NOT NULL,
    ReviewRating TINYINT NOT NULL,
    ReviewComment TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ReviewID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE,
    CHECK (ReviewRating BETWEEN 1 AND 5)
);

-- Create index on ProductID in ProductPrices and CustomerReviews tables
CREATE INDEX idx_ProductID ON ProductPrices (ProductID);
CREATE INDEX idx_ProductID ON CustomerReviews (ProductID);

-- Create stored procedure to add new product
DELIMITER //
CREATE PROCEDURE AddNewProduct(
    IN p_ProductName VARCHAR(255),
    IN p_ProductDescription TEXT,
    IN p_ProductCategory VARCHAR(100),
    IN p_ProductSubcategory VARCHAR(100),
    IN p_ProductImageURL VARCHAR(255)
)
BEGIN
    INSERT INTO Products (ProductName, ProductDescription, ProductCategory, ProductSubcategory, ProductImageURL)
    VALUES (p_ProductName, p_ProductDescription, p_ProductCategory, p_ProductSubcategory, p_ProductImageURL);
END//
DELIMITER ;

-- Create stored procedure to add new product price
DELIMITER //
CREATE PROCEDURE AddNewProductPrice(
    IN p_ProductID INT,
    IN p_Price DECIMAL(10, 2),
    IN p_Discount DECIMAL(10, 2)
)
BEGIN
    IF EXISTS (SELECT 1 FROM Products WHERE ProductID = p_ProductID) THEN
        INSERT INTO ProductPrices (ProductID, Price, Discount)
        VALUES (p_ProductID, p_Price, p_Discount);
    ELSE
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Product not found';
    END IF;
END//
DELIMITER ;

-- Create stored procedure to add new customer review
DELIMITER //
CREATE PROCEDURE AddNewCustomerReview(
    IN p_ProductID INT,
    IN p_CustomerName VARCHAR(255),
    IN p_ReviewRating TINYINT,
    IN p_ReviewComment TEXT
)
BEGIN
    IF EXISTS (SELECT 1 FROM Products WHERE ProductID = p_ProductID) THEN
        IF p_ReviewRating BETWEEN 1 AND 5 THEN
            INSERT INTO CustomerReviews (ProductID, CustomerName, ReviewRating, ReviewComment)
            VALUES (p_ProductID, p_CustomerName, p_ReviewRating, p_ReviewComment);
        ELSE
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Invalid review rating';
        END IF;
    ELSE
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Product not found';
    END IF;
END//
DELIMITER ;
```
