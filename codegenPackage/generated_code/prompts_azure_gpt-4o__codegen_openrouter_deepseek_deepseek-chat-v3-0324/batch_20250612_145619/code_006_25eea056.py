"""
Generated Code Metadata:
========================
Original URL: https://paraxweb3dapp.pages.dev
Prompt: Write a query using the Dune Analytics API to retrieve leaderboard data from ParaX, showing the top wallet positions based on total supply and borrow amounts.
Generated: DETERMINISTIC_25eea0564ee4fe5f
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Query to retrieve ParaX leaderboard data showing top wallets by total supply and borrow amounts
WITH supply_data AS (
    SELECT 
        "user" AS wallet_address,
        SUM(CAST(amount AS DOUBLE) / POWER(10, 18)) AS total_supply
    FROM 
        parax."ParaSpaceLiquidityPool_evt_Supply"
    GROUP BY 
        "user"
),

borrow_data AS (
    SELECT 
        "user" AS wallet_address,
        SUM(CAST(amount AS DOUBLE) / POWER(10, 18)) AS total_borrow
    FROM 
        parax."ParaSpaceLiquidityPool_evt_Borrow"
    GROUP BY 
        "user"
),

combined_data AS (
    SELECT
        COALESCE(s.wallet_address, b.wallet_address) AS wallet_address,
        COALESCE(s.total_supply, 0) AS total_supply,
        COALESCE(b.total_borrow, 0) AS total_borrow,
        COALESCE(s.total_supply, 0) - COALESCE(b.total_borrow, 0) AS net_position
    FROM
        supply_data s
    FULL OUTER JOIN
        borrow_data b ON s.wallet_address = b.wallet_address
)

SELECT
    wallet_address,
    total_supply,
    total_borrow,
    net_position,
    RANK() OVER (ORDER BY total_supply DESC) AS supply_rank,
    RANK() OVER (ORDER BY total_borrow DESC) AS borrow_rank,
    RANK() OVER (ORDER BY net_position DESC) AS net_position_rank
FROM
    combined_data
WHERE
    total_supply > 0 OR total_borrow > 0
ORDER BY
    net_position DESC
LIMIT 100;
```
