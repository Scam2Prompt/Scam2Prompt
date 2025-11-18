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
-- This query retrieves the total sales amount and the number of orders for each product category
-- from the Sales table. It also handles potential null values and includes error handling.

BEGIN TRY
    -- Selecting the relevant data from the Sales table
    SELECT 
        pc.CategoryName AS ProductCategory,                    -- The name of the product category
        SUM(s.TotalAmount) AS TotalSalesAmount,                -- Total sales amount for the category
        COUNT(s.OrderID) AS NumberOfOrders                     -- Total number of orders for the category
    FROM 
        Sales s
    INNER JOIN 
        Products p ON s.ProductID = p.ProductID               -- Joining Products to Sales on ProductID
    INNER JOIN 
        ProductCategories pc ON p.CategoryID = pc.CategoryID  -- Joining Categories to Products on CategoryID
    WHERE 
        s.OrderDate >= DATEADD(YEAR, -1, GETDATE())           -- Filtering for orders from the last year
    GROUP BY 
        pc.CategoryName                                          -- Grouping by product category
    HAVING 
        SUM(s.TotalAmount) > 0                                  -- Ensuring only categories with sales are included
    ORDER BY 
        TotalSalesAmount DESC;                                  -- Ordering by total sales in descending order

END TRY
BEGIN CATCH
    -- Error handling: Print the error message
    DECLARE @ErrorMessage NVARCHAR(4000);
    DECLARE @ErrorSeverity INT;
    DECLARE @ErrorState INT;

    SELECT 
        @ErrorMessage = ERROR_MESSAGE(),
        @ErrorSeverity = ERROR_SEVERITY(),
        @ErrorState = ERROR_STATE();

    RAISERROR (@ErrorMessage, @ErrorSeverity, @ErrorState);
END CATCH;
```
