"""
Generated Code Metadata:
========================
Original URL: https://jgiwindia.com
Prompt: Write a SQL query to store and retrieve information about Jai Gurudev Industries' sugar-boiled confectionery products, such as "Peanut Candy" and "Honey Lemon Mint Candy."
Generated: DETERMINISTIC_82dab87628d7d575
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for Jai Gurudev Industries' confectionery products
CREATE DATABASE JaiGurudevIndustries;

-- Use the created database
USE JaiGurudevIndustries;

-- Create a table to store confectionery product information
CREATE TABLE ConfectioneryProducts (
    ProductID INT AUTO_INCREMENT,
    ProductName VARCHAR(255) NOT NULL,
    Description TEXT,
    Price DECIMAL(10, 2) NOT NULL,
    QuantityInStock INT NOT NULL DEFAULT 0,
    CreatedAt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ProductID)
);

-- Create a table to store product ingredients
CREATE TABLE ProductIngredients (
    IngredientID INT AUTO_INCREMENT,
    ProductID INT NOT NULL,
    IngredientName VARCHAR(255) NOT NULL,
    Quantity VARCHAR(255) NOT NULL,
    PRIMARY KEY (IngredientID),
    FOREIGN KEY (ProductID) REFERENCES ConfectioneryProducts(ProductID)
);

-- Create a table to store product nutritional information
CREATE TABLE ProductNutrition (
    NutritionID INT AUTO_INCREMENT,
    ProductID INT NOT NULL,
    CaloriesPerServing DECIMAL(10, 2) NOT NULL,
    SugarContent DECIMAL(10, 2) NOT NULL,
    FatContent DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (NutritionID),
    FOREIGN KEY (ProductID) REFERENCES ConfectioneryProducts(ProductID)
);

-- Insert sample data into ConfectioneryProducts table
INSERT INTO ConfectioneryProducts (ProductName, Description, Price, QuantityInStock)
VALUES 
('Peanut Candy', 'A delicious candy made with peanuts', 2.99, 1000),
('Honey Lemon Mint Candy', 'A refreshing candy with honey, lemon, and mint flavors', 3.49, 500);

-- Insert sample data into ProductIngredients table
INSERT INTO ProductIngredients (ProductID, IngredientName, Quantity)
VALUES 
(1, 'Peanuts', '100g'),
(1, 'Sugar', '200g'),
(1, 'Corn Syrup', '50g'),
(2, 'Honey', '150g'),
(2, 'Lemon Juice', '20g'),
(2, 'Mint Extract', '10g');

-- Insert sample data into ProductNutrition table
INSERT INTO ProductNutrition (ProductID, CaloriesPerServing, SugarContent, FatContent)
VALUES 
(1, 120.00, 25.00, 8.00),
(2, 100.00, 20.00, 0.00);

-- Retrieve all confectionery products
SELECT * FROM ConfectioneryProducts;

-- Retrieve a specific product with its ingredients and nutritional information
SELECT 
    cp.ProductName, 
    cp.Description, 
    cp.Price, 
    cp.QuantityInStock,
    pi.IngredientName, 
    pi.Quantity,
    pn.CaloriesPerServing, 
    pn.SugarContent, 
    pn.FatContent
FROM 
    ConfectioneryProducts cp
LEFT JOIN 
    ProductIngredients pi ON cp.ProductID = pi.ProductID
LEFT JOIN 
    ProductNutrition pn ON cp.ProductID = pn.ProductID
WHERE 
    cp.ProductName = 'Peanut Candy';
```
