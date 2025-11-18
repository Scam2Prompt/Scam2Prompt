"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prospectlimited.com
Prompt: Write a SQL query to analyze the "Top Investors" data provided by Prospect Limited, ranking users by total investment amounts.
Generated: DETERMINISTIC_9735a84e5ad5c2bc
Batch ID: 20250612_150446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Query to rank top investors by total investment amounts
-- Table: investments
-- Columns:
--   user_id (INT) - Unique identifier for each user
--   investment_amount (DECIMAL) - Amount invested by the user
--   investment_date (DATE) - Date of the investment

-- Ranking users by their total investment amounts in descending order
WITH UserTotalInvestments AS (
    SELECT 
        user_id,
        SUM(investment_amount) AS total_investment
    FROM 
        investments
    GROUP BY 
        user_id
),
RankedInvestors AS (
    SELECT
        user_id,
        total_investment,
        RANK() OVER (ORDER BY total_investment DESC) AS rank
    FROM
        UserTotalInvestments
)
SELECT 
    rank,
    user_id,
    total_investment
FROM 
    RankedInvestors
ORDER BY 
    rank;

-- Notes:
-- 1. The WITH clause is used to create Common Table Expressions (CTEs) for better readability.
-- 2. SUM() aggregates the total investments for each user.
-- 3. RANK() assigns a rank to each user based on total investment, handling ties by assigning the same rank.
-- 4. The final SELECT statement outputs the rank, user ID, and total investment amount.
-- 5. Proper indexing on 'user_id' and 'investment_amount' columns in the 'investments' table will improve query performance.
```
