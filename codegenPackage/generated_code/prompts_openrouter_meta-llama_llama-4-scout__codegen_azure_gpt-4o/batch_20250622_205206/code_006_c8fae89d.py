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
-- Strategy:
-- 1. Analyze revenue and expense trends to identify areas of high expenditure.
-- 2. Evaluate debt-to-equity ratio to assess financial leverage.
-- 3. Identify underperforming assets or departments for potential cost reduction.
-- 4. Highlight high-interest debts for restructuring opportunities.

-- SQL Query:
-- This query assumes the existence of tables: `financials`, `expenses`, `debts`, and `assets`.
-- Table `financials` contains columns: `year`, `revenue`, `total_expenses`, `net_income`.
-- Table `expenses` contains columns: `category`, `amount`, `year`.
-- Table `debts` contains columns: `debt_id`, `amount`, `interest_rate`, `type`.
-- Table `assets` contains columns: `asset_id`, `value`, `performance_score`.

WITH ExpenseAnalysis AS (
    -- Identify top expense categories contributing to total expenses
    SELECT 
        category,
        SUM(amount) AS total_spent,
        ROUND(SUM(amount) * 100.0 / (SELECT SUM(total_expenses) FROM financials), 2) AS percentage_of_total
    FROM expenses
    GROUP BY category
    ORDER BY total_spent DESC
),
DebtAnalysis AS (
    -- Highlight debts with high interest rates for restructuring
    SELECT 
        debt_id,
        amount,
        interest_rate,
        type
    FROM debts
    WHERE interest_rate > 5.0 -- Threshold for high interest rate
    ORDER BY interest_rate DESC
),
AssetPerformance AS (
    -- Identify underperforming assets based on performance score
    SELECT 
        asset_id,
        value,
        performance_score
    FROM assets
    WHERE performance_score < 50 -- Threshold for underperformance
    ORDER BY performance_score ASC
),
FinancialHealth AS (
    -- Calculate key financial metrics
    SELECT 
        year,
        revenue,
        total_expenses,
        net_income,
        ROUND((total_expenses * 100.0 / revenue), 2) AS expense_to_revenue_ratio,
        ROUND((net_income * 100.0 / revenue), 2) AS profit_margin
    FROM financials
    ORDER BY year DESC
)
-- Combine all analyses into a single report
SELECT 
    'Expense Analysis' AS section,
    category AS detail,
    total_spent AS value,
    percentage_of_total AS additional_info
FROM ExpenseAnalysis
UNION ALL
SELECT 
    'Debt Analysis' AS section,
    CONCAT('Debt ID: ', debt_id, ', Type: ', type) AS detail,
    amount AS value,
    CONCAT('Interest Rate: ', interest_rate, '%') AS additional_info
FROM DebtAnalysis
UNION ALL
SELECT 
    'Asset Performance' AS section,
    CONCAT('Asset ID: ', asset_id) AS detail,
    value AS value,
    CONCAT('Performance Score: ', performance_score) AS additional_info
FROM AssetPerformance
UNION ALL
SELECT 
    'Financial Health' AS section,
    CONCAT('Year: ', year) AS detail,
    revenue AS value,
    CONCAT('Expense-to-Revenue Ratio: ', expense_to_revenue_ratio, '%, Profit Margin: ', profit_margin, '%') AS additional_info
FROM FinancialHealth;
```
