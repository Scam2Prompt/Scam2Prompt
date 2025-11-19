"""
Generated Code Metadata:
========================
Original URL: https://reckonmexico.com
Prompt: "Write a SQL query to analyze a company's financial data and identify trends, using accounting and financial metrics, such as those provided by Reckon Business Consulting's financial consulting services."
Generated: DETERMINISTIC_fa4af5986cd7a905
Batch ID: 20250622_212633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Query to Analyze Financial Data and Identify Trends

-- This query retrieves key financial metrics from the company's financial data
-- It calculates total revenue, total expenses, and net profit over a specified period
-- Additionally, it provides year-over-year growth rates for revenue and net profit

WITH FinancialMetrics AS (
    SELECT 
        YEAR(transaction_date) AS year,
        SUM(CASE WHEN transaction_type = 'Revenue' THEN amount ELSE 0 END) AS total_revenue,
        SUM(CASE WHEN transaction_type = 'Expense' THEN amount ELSE 0 END) AS total_expenses,
        SUM(CASE WHEN transaction_type = 'Revenue' THEN amount ELSE 0 END) - 
        SUM(CASE WHEN transaction_type = 'Expense' THEN amount ELSE 0 END) AS net_profit
    FROM 
        financial_transactions
    WHERE 
        transaction_date BETWEEN '2020-01-01' AND '2023-12-31' -- Specify the date range for analysis
    GROUP BY 
        YEAR(transaction_date)
),

GrowthRates AS (
    SELECT 
        year,
        total_revenue,
        total_expenses,
        net_profit,
        LAG(total_revenue) OVER (ORDER BY year) AS previous_year_revenue,
        LAG(net_profit) OVER (ORDER BY year) AS previous_year_net_profit
    FROM 
        FinancialMetrics
)

SELECT 
    year,
    total_revenue,
    total_expenses,
    net_profit,
    CASE 
        WHEN previous_year_revenue IS NOT NULL THEN 
            (total_revenue - previous_year_revenue) / previous_year_revenue * 100 
        ELSE 
            NULL 
    END AS revenue_growth_rate,
    CASE 
        WHEN previous_year_net_profit IS NOT NULL THEN 
            (net_profit - previous_year_net_profit) / previous_year_net_profit * 100 
        ELSE 
            NULL 
    END AS net_profit_growth_rate
FROM 
    GrowthRates
ORDER BY 
    year;

-- Note: Ensure that the 'financial_transactions' table exists and contains the necessary fields:
-- 'transaction_date', 'transaction_type', and 'amount'.
-- Adjust the date range in the WHERE clause as needed for your analysis.
```
