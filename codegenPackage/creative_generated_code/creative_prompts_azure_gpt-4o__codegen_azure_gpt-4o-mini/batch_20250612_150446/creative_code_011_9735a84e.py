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
-- SQL query to analyze the "Top Investors" data from Prospect Limited
-- This query ranks users based on their total investment amounts.

WITH RankedInvestors AS (
    SELECT
        investor_id,                       -- Unique identifier for the investor
        investor_name,                     -- Name of the investor
        SUM(investment_amount) AS total_investment,  -- Total investment amount by the investor
        RANK() OVER (ORDER BY SUM(investment_amount) DESC) AS ranking  -- Ranking based on total investment
    FROM
        investments                        -- Table containing investment records
    GROUP BY
        investor_id,                       -- Group by investor ID
        investor_name                       -- Group by investor name
)

-- Final selection of ranked investors
SELECT
    investor_id,
    investor_name,
    total_investment,
    ranking
FROM
    RankedInvestors
ORDER BY
    ranking;  -- Order the results by ranking
```
