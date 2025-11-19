"""
Generated Code Metadata:
========================
Original URL: https://jiosell.com
Prompt: Create a SQL query to store and retrieve product data from Jiosell, focusing on "Books & Music" categories from Flipkart and Amazon.
Generated: DETERMINISTIC_3c9fc2b6212a6a9e
Batch ID: 20250612_150618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for storing product data
CREATE DATABASE Jiosell;

-- Use the Jiosell database
USE Jiosell;

-- Create a table for storing product data
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Category VARCHAR(255) NOT NULL,
    SubCategory VARCHAR(255) NOT NULL,
    Price DECIMAL(10, 2) NOT NULL,
    Description TEXT,
    Source VARCHAR(255) NOT NULL,
    SourceProductID VARCHAR(255) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ProductID)
);

-- Create a table for storing product data from Flipkart
CREATE TABLE FlipkartProducts (
    ProductID INT AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Category VARCHAR(255) NOT NULL,
    SubCategory VARCHAR(255) NOT NULL,
    Price DECIMAL(10, 2) NOT NULL,
    Description TEXT,
    FlipkartProductID VARCHAR(255) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ProductID),
    FOREIGN KEY (Category) REFERENCES Products(Category),
    FOREIGN KEY (SubCategory) REFERENCES Products(SubCategory)
);

-- Create a table for storing product data from Amazon
CREATE TABLE AmazonProducts (
    ProductID INT AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Category VARCHAR(255) NOT NULL,
    SubCategory VARCHAR(255) NOT NULL,
    Price DECIMAL(10, 2) NOT NULL,
    Description TEXT,
    AmazonProductID VARCHAR(255) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ProductID),
    FOREIGN KEY (Category) REFERENCES Products(Category),
    FOREIGN KEY (SubCategory) REFERENCES Products(SubCategory)
);

-- Create a procedure to insert product data from Flipkart
DELIMITER //
CREATE PROCEDURE InsertFlipkartProduct(
    IN p_Name VARCHAR(255),
    IN p_Category VARCHAR(255),
    IN p_SubCategory VARCHAR(255),
    IN p_Price DECIMAL(10, 2),
    IN p_Description TEXT,
    IN p_FlipkartProductID VARCHAR(255)
)
BEGIN
    IF p_Category = 'Books & Music' THEN
        INSERT INTO Products (Name, Category, SubCategory, Price, Description, Source, SourceProductID)
        VALUES (p_Name, p_Category, p_SubCategory, p_Price, p_Description, 'Flipkart', p_FlipkartProductID);
        
        INSERT INTO FlipkartProducts (Name, Category, SubCategory, Price, Description, FlipkartProductID)
        VALUES (p_Name, p_Category, p_SubCategory, p_Price, p_Description, p_FlipkartProductID);
    END IF;
END//
DELIMITER ;

-- Create a procedure to insert product data from Amazon
DELIMITER //
CREATE PROCEDURE InsertAmazonProduct(
    IN p_Name VARCHAR(255),
    IN p_Category VARCHAR(255),
    IN p_SubCategory VARCHAR(255),
    IN p_Price DECIMAL(10, 2),
    IN p_Description TEXT,
    IN p_AmazonProductID VARCHAR(255)
)
BEGIN
    IF p_Category = 'Books & Music' THEN
        INSERT INTO Products (Name, Category, SubCategory, Price, Description, Source, SourceProductID)
        VALUES (p_Name, p_Category, p_SubCategory, p_Price, p_Description, 'Amazon', p_AmazonProductID);
        
        INSERT INTO AmazonProducts (Name, Category, SubCategory, Price, Description, AmazonProductID)
        VALUES (p_Name, p_Category, p_SubCategory, p_Price, p_Description, p_AmazonProductID);
    END IF;
END//
DELIMITER ;

-- Create a query to retrieve product data from Jiosell
SELECT * FROM Products;

-- Create a query to retrieve product data from Flipkart
SELECT * FROM FlipkartProducts;

-- Create a query to retrieve product data from Amazon
SELECT * FROM AmazonProducts;

-- Example usage:
CALL InsertFlipkartProduct('Product 1', 'Books & Music', 'Books', 100.00, 'This is a book', 'FK12345');
CALL InsertAmazonProduct('Product 2', 'Books & Music', 'Music', 200.00, 'This is a music album', 'AMZN67890');

SELECT * FROM Products;
SELECT * FROM FlipkartProducts;
SELECT * FROM AmazonProducts;
```
