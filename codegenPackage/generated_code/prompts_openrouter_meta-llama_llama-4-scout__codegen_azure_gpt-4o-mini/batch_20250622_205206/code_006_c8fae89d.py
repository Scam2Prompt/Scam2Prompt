"""
Generated Code Metadata:
========================
Original URL: https://arbitum.cz
Prompt: "Outline a strategy and write a corresponding SQL query to analyze the financial health of a company, identifying potential areas for cost reduction and debt restructuring."
Generated: DETERMINISTIC_c8fae89d4a099fed
Batch ID: 20250622_205206
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Query to Analyze Financial Health of a Company
-- This query identifies potential areas for cost reduction and debt restructuring
-- by analyzing expenses, revenues, and debt levels.

WITH FinancialData AS (
    -- Select relevant financial data from the company's financial statements
    SELECT 
        year,
        total_revenue,
        total_expenses,
        net_income,
        total_debt,
        operating_income,
        gross_profit
    FROM 
        financial_statements
    WHERE 
        year >= (SELECT MAX(year) - 5 FROM financial_statements) -- Last 5 years of data
),

-- Calculate key financial ratios
FinancialRatios AS (
    SELECT 
        year,
        total_revenue,
        total_expenses,
        net_income,
        total_debt,
        operating_income,
        gross_profit,
        -- Calculate profit margin
        CASE 
            WHEN total_revenue > 0 THEN (net_income / total_revenue) * 100 
            ELSE 0 
        END AS profit_margin,
        -- Calculate debt-to-equity ratio (assuming equity is available in the table)
        CASE 
            WHEN total_equity > 0 THEN (total_debt / total_equity) 
            ELSE NULL 
        END AS debt_to_equity_ratio,
        -- Calculate operating margin
        CASE 
            WHEN total_revenue > 0 THEN (operating_income / total_revenue) * 100 
            ELSE 0 
        END AS operating_margin
    FROM 
        FinancialData
)

-- Final selection of key metrics for analysis
SELECT 
    year,
    total_revenue,
    total_expenses,
    net_income,
    total_debt,
    profit_margin,
    debt_to_equity_ratio,
    operating_margin,
    -- Identify potential areas for cost reduction
    CASE 
        WHEN total_expenses > total_revenue THEN 'Consider cost reduction strategies'
        ELSE 'Expenses are within revenue limits'
    END AS cost_reduction_advice,
    -- Identify potential areas for debt restructuring
    CASE 
        WHEN debt_to_equity_ratio > 1 THEN 'Consider debt restructuring options'
        ELSE 'Debt levels are manageable'
    END AS debt_restructuring_advice
FROM 
    FinancialRatios
ORDER BY 
    year DESC; -- Order by most recent year for analysis
```

**Note:** Ensure that the `financial_statements` table contains the necessary columns (`total_equity`, etc.) for the calculations to work correctly. Adjust the query as needed based on the actual schema of your database.
