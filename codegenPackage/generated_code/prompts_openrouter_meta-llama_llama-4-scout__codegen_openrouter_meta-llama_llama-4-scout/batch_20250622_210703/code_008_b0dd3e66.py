"""
Generated Code Metadata:
========================
Original URL: https://www.sundancespasadvantage.com
Prompt: Write a SQL query to analyze sales data for a Sundance Spas retailer, focusing on product innovation and customer preferences.
Generated: DETERMINISTIC_b0dd3e666e4061c5
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Analyze sales data for Sundance Spas retailer

-- Create a sample database schema
CREATE TABLE IF NOT EXISTS Sales (
    SaleID INT PRIMARY KEY,
    ProductID INT,
    CustomerID INT,
    SaleDate DATE,
    Quantity INT,
    SalePrice DECIMAL(10, 2)
);

CREATE TABLE IF NOT EXISTS Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(255),
    ModelYear INT,
    Category VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS Customers (
    CustomerID INT PRIMARY KEY,
    Name VARCHAR(255),
    Email VARCHAR(255),
    Location VARCHAR(100)
);

-- Insert sample data
INSERT INTO Products (ProductID, ProductName, ModelYear, Category)
VALUES 
(1, 'Sundance Spas - Serenity', 2022, 'Hot Tub'),
(2, 'Sundance Spas - Utopia', 2023, 'Hot Tub'),
(3, 'Sundance Spas - Paradise', 2022, 'Swim Spa');

INSERT INTO Customers (CustomerID, Name, Email, Location)
VALUES 
(1, 'John Doe', 'john.doe@example.com', 'New York'),
(2, 'Jane Doe', 'jane.doe@example.com', 'California'),
(3, 'Bob Smith', 'bob.smith@example.com', 'Florida');

INSERT INTO Sales (SaleID, ProductID, CustomerID, SaleDate, Quantity, SalePrice)
VALUES 
(1, 1, 1, '2022-01-01', 1, 9999.99),
(2, 2, 2, '2023-06-01', 1, 10999.99),
(3, 3, 3, '2022-12-01', 1, 8999.99),
(4, 1, 1, '2023-01-01', 1, 9999.99),
(5, 2, 2, '2023-07-01', 1, 10999.99);

-- SQL query to analyze sales data
WITH 
-- Calculate total sales by product
ProductSales AS (
    SELECT 
        p.ProductID,
        p.ProductName,
        SUM(s.Quantity) AS TotalQuantitySold,
        SUM(s.SalePrice) AS TotalSalesRevenue
    FROM 
        Sales s
    JOIN 
        Products p ON s.ProductID = p.ProductID
    GROUP BY 
        p.ProductID, p.ProductName
),

-- Calculate customer purchase frequency
CustomerPurchases AS (
    SELECT 
        c.CustomerID,
        c.Name,
        COUNT(s.SaleID) AS PurchaseFrequency
    FROM 
        Sales s
    JOIN 
        Customers c ON s.CustomerID = c.CustomerID
    GROUP BY 
        c.CustomerID, c.Name
),

-- Identify top-selling products by category
TopSellingProducts AS (
    SELECT 
        p.Category,
        p.ProductName,
        SUM(s.Quantity) AS TotalQuantitySold
    FROM 
        Sales s
    JOIN 
        Products p ON s.ProductID = p.ProductID
    GROUP BY 
        p.Category, p.ProductName
)

-- Analyze sales data
SELECT 
    -- Product innovation analysis
    'Product Innovation' AS AnalysisCategory,
    ps.ProductID,
    ps.ProductName,
    ps.TotalQuantitySold,
    ps.TotalSalesRevenue
FROM 
    ProductSales ps
ORDER BY 
    ps.TotalSalesRevenue DESC;

-- Customer preference analysis
SELECT 
    -- Customer preference analysis
    'Customer Preferences' AS AnalysisCategory,
    cp.CustomerID,
    cp.Name,
    cp.PurchaseFrequency
FROM 
    CustomerPurchases cp
ORDER BY 
    cp.PurchaseFrequency DESC;

-- Top-selling products by category
SELECT 
    -- Top-selling products by category
    'Top-Selling Products' AS AnalysisCategory,
    tsp.Category,
    tsp.ProductName,
    tsp.TotalQuantitySold
FROM 
    TopSellingProducts tsp
WHERE 
    tsp.TotalQuantitySold > (SELECT AVG(TotalQuantitySold) FROM TopSellingProducts)
ORDER BY 
    tsp.TotalQuantitySold DESC;
```
