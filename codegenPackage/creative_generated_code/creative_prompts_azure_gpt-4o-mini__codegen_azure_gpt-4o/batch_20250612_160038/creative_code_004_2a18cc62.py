"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smarts-invests.net
Prompt: Construct a SQL query to analyze the total amount invested and withdrawn by users on the Smarts-invests platform, based on the statistics provided on their website.
Generated: DETERMINISTIC_2a18cc62badb059d
Batch ID: 20250612_160038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL query to analyze the total amount invested and withdrawn by users on the Smarts-invests platform
-- Assuming a database schema with the following structure:
-- Table: Transactions
-- Columns:
-- - transaction_id (Primary Key)
-- - user_id (Foreign Key referencing Users table)
-- - transaction_type (ENUM: 'invest' or 'withdraw')
-- - amount (DECIMAL representing the transaction amount)
-- - transaction_date (DATETIME for when the transaction occurred)

-- Query begins
SELECT 
    user_id,                                   -- Unique identifier for the user
    SUM(CASE WHEN transaction_type = 'invest' THEN amount ELSE 0 END) AS total_invested,   -- Total amount invested by the user
    SUM(CASE WHEN transaction_type = 'withdraw' THEN amount ELSE 0 END) AS total_withdrawn -- Total amount withdrawn by the user
FROM 
    Transactions -- Source table containing all transaction records
GROUP BY 
    user_id     -- Grouping results by user to aggregate totals
ORDER BY 
    user_id;    -- Sorting results by user ID for better readability
```

Note: Ensure the database schema matches the assumptions made in the query, and indexes are applied appropriately for optimal performance.
