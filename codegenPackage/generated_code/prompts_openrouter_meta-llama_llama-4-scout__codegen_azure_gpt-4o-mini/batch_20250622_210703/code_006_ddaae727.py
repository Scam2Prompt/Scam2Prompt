"""
Generated Code Metadata:
========================
Original URL: https://www.pensar.inf.br
Prompt: "Write a SQL query to generate a report on business performance metrics using data from the Solpen ERP system."
Generated: DETERMINISTIC_ddaae727fc31d068
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Query to generate a report on business performance metrics
-- from the Solpen ERP system.

-- This query retrieves key performance indicators (KPIs) such as total sales,
-- total expenses, and net profit for a specified date range.

WITH SalesData AS (
    SELECT 
        SUM(amount) AS total_sales,
        DATE_TRUNC('month', sale_date) AS sale_month
    FROM 
        sales
    WHERE 
        sale_date BETWEEN '2023-01-01' AND '2023-12-31'  -- Specify the date range
    GROUP BY 
        sale_month
),

ExpensesData AS (
    SELECT 
        SUM(amount) AS total_expenses,
        DATE_TRUNC('month', expense_date) AS expense_month
    FROM 
        expenses
    WHERE 
        expense_date BETWEEN '2023-01-01' AND '2023-12-31'  -- Specify the date range
    GROUP BY 
        expense_month
)

SELECT 
    COALESCE(s.sale_month, e.expense_month) AS month,
    COALESCE(s.total_sales, 0) AS total_sales,
    COALESCE(e.total_expenses, 0) AS total_expenses,
    (COALESCE(s.total_sales, 0) - COALESCE(e.total_expenses, 0)) AS net_profit
FROM 
    SalesData s
FULL OUTER JOIN 
    ExpensesData e ON s.sale_month = e.expense_month
ORDER BY 
    month;  -- Order the results by month
```
