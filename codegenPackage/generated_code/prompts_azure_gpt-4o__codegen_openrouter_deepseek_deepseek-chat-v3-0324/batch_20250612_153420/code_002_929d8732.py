"""
Generated Code Metadata:
========================
Original URL: https://staderlabs-53o.pages.dev
Prompt: Create a dashboard using Dune Analytics to visualize SD decentralization stats, including total node operators and SD delegated, based on the data provided by Stader Labs.
Generated: DETERMINISTIC_929d8732cd782a53
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Dune Analytics Dashboard for Stader Labs SD Decentralization Stats
-- This dashboard visualizes key metrics around SD token decentralization
-- including total node operators and SD delegated

-- Query 1: Total Node Operators Over Time
WITH node_operators AS (
    SELECT 
        DATE_TRUNC('day', evt_block_time) AS day,
        COUNT(DISTINCT operator) AS unique_operators
    FROM stader_labs_contract.OperatorAdded
    GROUP BY 1
)

SELECT 
    day,
    SUM(unique_operators) OVER (ORDER BY day) AS total_node_operators
FROM node_operators
ORDER BY day DESC;

-- Query 2: SD Delegated Over Time
WITH sd_delegated AS (
    SELECT 
        DATE_TRUNC('day', evt_block_time) AS day,
        SUM(amount) / 1e18 AS sd_delegated
    FROM stader_labs_contract.SDDelegated
    GROUP BY 1
)

SELECT 
    day,
    SUM(sd_delegated) OVER (ORDER BY day) AS total_sd_delegated
FROM sd_delegated
ORDER BY day DESC;

-- Query 3: Current Node Operator Distribution
SELECT 
    operator,
    COUNT(*) AS pools_operated,
    SUM(amount) / 1e18 AS total_sd_delegated
FROM stader_labs_contract.SDDelegated
GROUP BY operator
ORDER BY total_sd_delegated DESC
LIMIT 50;

-- Query 4: Recent Delegation Activity
SELECT 
    DATE_TRUNC('day', evt_block_time) AS day,
    COUNT(*) AS delegation_events,
    SUM(amount) / 1e18 AS sd_delegated
FROM stader_labs_contract.SDDelegated
WHERE evt_block_time >= NOW() - INTERVAL '30 days'
GROUP BY 1
ORDER BY day DESC;

-- Query 5: Node Operator Growth Rate
WITH daily_operators AS (
    SELECT 
        DATE_TRUNC('day', evt_block_time) AS day,
        COUNT(DISTINCT operator) AS new_operators
    FROM stader_labs_contract.OperatorAdded
    GROUP BY 1
)

SELECT 
    day,
    new_operators,
    SUM(new_operators) OVER (ORDER BY day) AS total_operators,
    (SUM(new_operators) OVER (ORDER BY day) - 
     LAG(SUM(new_operators) OVER (ORDER BY day), 1) OVER (ORDER BY day)) / 
     LAG(SUM(new_operators) OVER (ORDER BY day), 1) OVER (ORDER BY day) * 100 AS growth_rate
FROM daily_operators
ORDER BY day DESC;

-- Dashboard Configuration:
-- 1. Create a dashboard titled "Stader Labs SD Decentralization Dashboard"
-- 2. Add the following visualizations:
--    - Time series chart of total_node_operators (Query 1)
--    - Time series chart of total_sd_delegated (Query 2)
--    - Bar chart of top node operators by SD delegated (Query 3)
--    - Bar chart of recent delegation activity (Query 4)
--    - Table showing node operator growth metrics (Query 5)
-- 3. Set appropriate titles, axis labels, and formatting for each visualization
-- 4. Add dashboard description explaining the metrics and data sources
```
