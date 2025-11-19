"""
Generated Code Metadata:
========================
Original URL: https://www.qbt.finance
Prompt: "Write a SQL query to analyze the Qubit database schema and extract insights on the most profitable lending and borrowing strategies."
Generated: DETERMINISTIC_09bac1612267fd8a
Batch ID: 20250622_211502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Analyze Qubit database schema and extract insights on the most profitable lending and borrowing strategies

-- Define a CTE to calculate profit for each lending strategy
WITH lending_profit AS (
  SELECT 
    ls.strategy_id,
    ls.strategy_name,
    SUM(lp.interest_earned) AS total_interest_earned,
    SUM(lp.principal_lent) AS total_principal_lent
  FROM 
    lending_strategies ls
  JOIN 
    lending_positions lp ON ls.strategy_id = lp.strategy_id
  GROUP BY 
    ls.strategy_id, ls.strategy_name
),

-- Define a CTE to calculate profit for each borrowing strategy
borrowing_profit AS (
  SELECT 
    bs.strategy_id,
    bs.strategy_name,
    SUM(bp.interest_paid) AS total_interest_paid,
    SUM(bp.principal_borrowed) AS total_principal_borrowed
  FROM 
    borrowing_strategies bs
  JOIN 
    borrowing_positions bp ON bs.strategy_id = bp.strategy_id
  GROUP BY 
    bs.strategy_id, bs.strategy_name
),

-- Define a CTE to calculate profitability metrics for lending strategies
lending_metrics AS (
  SELECT 
    strategy_id,
    strategy_name,
    total_interest_earned,
    total_principal_lent,
    (total_interest_earned / total_principal_lent) * 100 AS interest_rate
  FROM 
    lending_profit
),

-- Define a CTE to calculate profitability metrics for borrowing strategies
borrowing_metrics AS (
  SELECT 
    strategy_id,
    strategy_name,
    total_interest_paid,
    total_principal_borrowed,
    (total_interest_paid / total_principal_borrowed) * 100 AS interest_rate
  FROM 
    borrowing_profit
)

-- Analyze and extract insights on the most profitable lending and borrowing strategies
SELECT 
  'Lending' AS strategy_type,
  strategy_id,
  strategy_name,
  interest_rate
FROM 
  lending_metrics
UNION ALL
SELECT 
  'Borrowing' AS strategy_type,
  strategy_id,
  strategy_name,
  interest_rate
FROM 
  borrowing_metrics
ORDER BY 
  interest_rate DESC;

-- Get top 5 most profitable lending strategies
SELECT 
  strategy_id,
  strategy_name,
  interest_rate
FROM 
  lending_metrics
ORDER BY 
  interest_rate DESC
LIMIT 5;

-- Get top 5 most profitable borrowing strategies
SELECT 
  strategy_id,
  strategy_name,
  interest_rate
FROM 
  borrowing_metrics
ORDER BY 
  interest_rate DESC
LIMIT 5;
```
