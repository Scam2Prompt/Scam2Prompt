"""
Generated Code Metadata:
========================
Original URL: https://kalgatetechnology.com.ng
Prompt: Create a SQL query to analyze the financial performance of a logistics company, focusing on sustainable financial performance metrics, similar to Kalgate Technology's goals.
Generated: DETERMINISTIC_d4a8bc3d0ff1c86b
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Query to analyze the financial performance of a logistics company
-- focusing on sustainable financial performance metrics.

-- This query assumes the existence of a database schema with relevant tables
-- such as `financials`, `operations`, and `sustainability_metrics`.

-- The query calculates key metrics like revenue, profit margin, carbon footprint,
-- and operational efficiency, grouped by year.

-- Ensure the database has proper indexes on columns used in WHERE, JOIN, and GROUP BY clauses
-- for optimal performance.

SELECT 
    f.year AS Year,
    SUM(f.revenue) AS Total_Revenue, -- Total revenue for the year
    SUM(f.profit) AS Total_Profit, -- Total profit for the year
    ROUND(SUM(f.profit) / NULLIF(SUM(f.revenue), 0) * 100, 2) AS Profit_Margin_Percentage, -- Profit margin percentage
    SUM(s.carbon_emissions) AS Total_Carbon_Emissions, -- Total carbon emissions for the year
    ROUND(SUM(o.shipments) / NULLIF(SUM(o.operational_cost), 0), 2) AS Operational_Efficiency -- Shipments per unit cost
FROM 
    financials f
LEFT JOIN 
    sustainability_metrics s ON f.year = s.year -- Join sustainability metrics by year
LEFT JOIN 
    operations o ON f.year = o.year -- Join operational data by year
WHERE 
    f.year >= 2018 -- Filter for data from 2018 onwards
GROUP BY 
    f.year -- Group by year for annual analysis
ORDER BY 
    f.year ASC; -- Sort results by year in ascending order

-- Notes:
-- 1. NULLIF is used to prevent division by zero errors.
-- 2. Ensure the database schema includes relevant columns such as `revenue`, `profit`, 
--    `carbon_emissions`, `shipments`, and `operational_cost`.
-- 3. Add indexes on `year` columns in all tables for faster query execution.
-- 4. Validate the data integrity and handle missing or inconsistent data in the ETL process.
```
