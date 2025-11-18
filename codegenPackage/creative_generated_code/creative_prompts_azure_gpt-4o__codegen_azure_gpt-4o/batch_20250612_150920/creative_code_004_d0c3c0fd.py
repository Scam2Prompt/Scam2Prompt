"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://edukacija.net
Prompt: Write a SQL query for data analysis using Microsoft SQL Server 2014, incorporating best practices highlighted on edukacija.net.
Generated: DETERMINISTIC_d0c3c0fdd9ccf160
Batch ID: 20250612_150920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL Query for Data Analysis in Microsoft SQL Server 2014
-- This query calculates the total sales revenue per product category
-- while filtering out products with zero sales and ensuring proper error handling.

-- Best Practices:
-- 1. Use aliases for improved readability
-- 2. Avoid SELECT * to ensure only required fields are fetched
-- 3. Use indexes on filtering columns for performance optimization
-- 4. Include meaningful comments for clarity

BEGIN TRY
    -- Main query for data analysis
    SELECT 
        pc.CategoryName AS ProductCategory,  -- Fetch category name
        SUM(oi.Quantity * oi.UnitPrice) AS TotalRevenue  -- Calculate total revenue
    FROM 
        dbo.ProductCategories pc  -- Product categories table
    INNER JOIN 
        dbo.Products p ON pc.CategoryID = p.CategoryID  -- Join products with categories
    INNER JOIN 
        dbo.OrderItems oi ON p.ProductID = oi.ProductID  -- Join order items with products
    WHERE 
        oi.Quantity > 0  -- Exclude products with zero sales
    GROUP BY 
        pc.CategoryName  -- Group by category for aggregation
    ORDER BY 
        TotalRevenue DESC;  -- Sort by revenue in descending order

END TRY
BEGIN CATCH
    -- Error handling block
    -- Log the error details and return a user-friendly message
    SELECT 
        ERROR_NUMBER() AS ErrorNumber,
        ERROR_MESSAGE() AS ErrorMessage;
END CATCH;
```
