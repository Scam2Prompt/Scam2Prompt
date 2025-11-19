"""
Generated Code Metadata:
========================
Original URL: https://edukacija.net
Prompt: Write a SQL query for data analysis using Microsoft SQL Server 2014, incorporating best practices highlighted on edukacija.net.
Generated: DETERMINISTIC_d0c3c0fdd9ccf160
Batch ID: 20250612_150920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- This SQL query retrieves sales data for analysis, 
-- including total sales, average sales per transaction, 
-- and the number of transactions per customer.

-- Use a Common Table Expression (CTE) for better readability and organization
WITH SalesData AS (
    SELECT 
        CustomerID,
        SUM(TotalAmount) AS TotalSales,
        COUNT(TransactionID) AS TransactionCount,
        AVG(TotalAmount) AS AverageSale
    FROM 
        SalesTransactions
    WHERE 
        TransactionDate >= DATEADD(YEAR, -1, GETDATE()) -- Filter for the last year
    GROUP BY 
        CustomerID
)

-- Select from the CTE to get the final results
SELECT 
    CustomerID,
    TotalSales,
    TransactionCount,
    AverageSale
FROM 
    SalesData
ORDER BY 
    TotalSales DESC; -- Order by total sales in descending order

-- Error handling: Check if the SalesTransactions table exists before executing the query
IF OBJECT_ID('dbo.SalesTransactions', 'U') IS NOT NULL
BEGIN
    -- Execute the query if the table exists
    EXEC sp_executesql N'
        WITH SalesData AS (
            SELECT 
                CustomerID,
                SUM(TotalAmount) AS TotalSales,
                COUNT(TransactionID) AS TransactionCount,
                AVG(TotalAmount) AS AverageSale
            FROM 
                SalesTransactions
            WHERE 
                TransactionDate >= DATEADD(YEAR, -1, GETDATE())
            GROUP BY 
                CustomerID
        )
        SELECT 
            CustomerID,
            TotalSales,
            TransactionCount,
            AverageSale
        FROM 
            SalesData
        ORDER BY 
            TotalSales DESC;'
END
ELSE
BEGIN
    -- Log an error message if the table does not exist
    PRINT 'Error: The SalesTransactions table does not exist.';
END
```
