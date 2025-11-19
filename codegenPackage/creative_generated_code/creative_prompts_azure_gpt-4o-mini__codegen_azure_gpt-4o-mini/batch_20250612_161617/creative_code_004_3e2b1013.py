"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rosebudhds.com
Prompt: Construct a SQL query to analyze the performance of the property portfolio managed by Rosebud Holdings Property Income REIT, based on the provided financial metrics.
Generated: DETERMINISTIC_3e2b101385fbfd3d
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL query to analyze the performance of the property portfolio managed by Rosebud Holdings Property Income REIT

-- The following query retrieves key financial metrics from the property portfolio.
-- It aggregates data based on property type and calculates relevant performance indicators.

SELECT 
    p.property_type AS PropertyType,
    COUNT(p.id) AS TotalProperties,                      -- Count of properties by type
    SUM(f.income) AS TotalIncome,                        -- Total income from properties
    SUM(f.expenses) AS TotalExpenses,                    -- Total expenses related to properties
    SUM(f.income) - SUM(f.expenses) AS NetOperatingIncome, -- Net Operating Income (NOI)
    AVG(f.occupancy_rate) AS AverageOccupancyRate,      -- Average occupancy rate across properties
    SUM(f.income) / NULLIF(SUM(f.expenses), 0) AS IncomeExpenseRatio -- Income to Expense ratio, avoiding division by zero
FROM 
    properties p
JOIN 
    financial_metrics f ON p.id = f.property_id          -- Joining properties with their financial metrics
WHERE 
    p.management_company = 'Rosebud Holdings Property Income REIT' -- Filtering for specific management company
GROUP BY 
    p.property_type                                        -- Grouping results by property type
ORDER BY 
    TotalIncome DESC;                                     -- Ordering results by total income in descending order

-- Error handling is done via NULLIF to prevent division by zero in the IncomeExpenseRatio calculation.
```
