"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://glowconsultants.org
Prompt: How can I implement a data-driven decision support system using SQL and Tableau based on the methodologies outlined by GLOW Consultants?
Generated: DETERMINISTIC_19d236a18dfb1c42
Batch ID: 20250612_135637
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL Script to Create the Data Models for a Decision Support System

-- Step 1: Create a table for storing sales data
CREATE TABLE SalesData (
    SaleID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each sale
    ProductID INT NOT NULL,                -- Reference to the product being sold
    CustomerID INT NOT NULL,               -- Reference to the customer
    SaleDate DATE NOT NULL,                -- Date of the sale
    QuantitySold INT NOT NULL,             -- Number of units sold
    SaleAmount DECIMAL(10, 2) NOT NULL     -- Total amount of the sale
);

-- Step 2: Create a table for product details
CREATE TABLE ProductDetails (
    ProductID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each product
    ProductName VARCHAR(100) NOT NULL,        -- Name of the product
    Category VARCHAR(50) NOT NULL,            -- Category of the product
    Price DECIMAL(10, 2) NOT NULL             -- Price per unit
);

-- Step 3: Create a table for customer details
CREATE TABLE CustomerDetails (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each customer
    CustomerName VARCHAR(100) NOT NULL,        -- Name of the customer
    Location VARCHAR(100),                     -- Location of the customer
    Email VARCHAR(100)                         -- Email of the customer
);

-- Step 4: Insert sample data into the tables
INSERT INTO ProductDetails (ProductName, Category, Price) VALUES
('Laptop', 'Electronics', 800.00),
('Smartphone', 'Electronics', 600.00),
('Office Chair', 'Furniture', 150.00);

INSERT INTO CustomerDetails (CustomerName, Location, Email) VALUES
('Alice Johnson', 'New York', 'alice@example.com'),
('Bob Smith', 'California', 'bob@example.com'),
('Charlie Lee', 'Texas', 'charlie@example.com');

INSERT INTO SalesData (ProductID, CustomerID, SaleDate, QuantitySold, SaleAmount) VALUES
(1, 1, '2023-01-15', 1, 800.00),
(2, 2, '2023-02-20', 2, 1200.00),
(3, 3, '2023-03-10', 1, 150.00);

-- Step 5: Create a view to aggregate sales by product and category
CREATE VIEW ProductSalesSummary AS
SELECT
    PD.Category,
    PD.ProductName,
    SUM(SD.QuantitySold) AS TotalUnitsSold,
    SUM(SD.SaleAmount) AS TotalRevenue
FROM
    SalesData SD
JOIN
    ProductDetails PD ON SD.ProductID = PD.ProductID
GROUP BY
    PD.Category, PD.ProductName;

-- Step 6: Create a view to aggregate sales by customer and location
CREATE VIEW CustomerSalesSummary AS
SELECT
    CD.Location,
    CD.CustomerName,
    COUNT(SD.SaleID) AS TotalPurchases,
    SUM(SD.SaleAmount) AS TotalSpent
FROM
    SalesData SD
JOIN
    CustomerDetails CD ON SD.CustomerID = CD.CustomerID
GROUP BY
    CD.Location, CD.CustomerName;

-- Step 7: Add error handling: Ensure foreign key constraints for data integrity

-- Enforce relationships between tables
ALTER TABLE SalesData
ADD FOREIGN KEY (ProductID) REFERENCES ProductDetails(ProductID) ON DELETE CASCADE,
ADD FOREIGN KEY (CustomerID) REFERENCES CustomerDetails(CustomerID) ON DELETE CASCADE;

-- Step 8: Test the created views with sample queries

-- Query product sales summary
SELECT * FROM ProductSalesSummary;

-- Query customer sales summary
SELECT * FROM CustomerSalesSummary;

-- Step 9: Prepare Tableau Integration
-- Tableau can connect directly to the database to visualize the "ProductSalesSummary" and "CustomerSalesSummary" views

-- Ensure the database is accessible via a connection (e.g., MySQL, PostgreSQL)
-- Tableau users can use these views for dashboards, charts, and further analytics.
```

This SQL code forms the backbone of the data-driven decision support system. Tableau can connect to the database and use the `ProductSalesSummary` and `CustomerSalesSummary` views for analytical purposes, enabling informed decision-making.
