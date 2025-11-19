"""
Generated Code Metadata:
========================
Original URL: https://dashboard-gpu.pages.dev
Prompt: "Write a query to retrieve the top 10 node holders with the most nodes holding, along with their wallet addresses and total rewards earned."
Generated: DETERMINISTIC_af7fb56b5096553c
Batch ID: 20250622_204843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL query to retrieve the top 10 node holders with the most nodes holding,
-- along with their wallet addresses and total rewards earned.

SELECT 
    nh.wallet_address,          -- The wallet address of the node holder
    COUNT(nh.node_id) AS total_nodes,  -- Count of nodes held by the wallet address
    SUM(nh.rewards) AS total_rewards  -- Total rewards earned by the wallet address
FROM 
    node_holders nh              -- Table containing node holder information
GROUP BY 
    nh.wallet_address             -- Grouping by wallet address to aggregate data
ORDER BY 
    total_nodes DESC              -- Ordering by the number of nodes held in descending order
LIMIT 10;                        -- Limiting the result to the top 10 node holders
```

**Note:** Ensure that the `node_holders` table contains the columns `wallet_address`, `node_id`, and `rewards` for this query to work correctly. Adjust the table and column names as necessary to fit your database schema.
