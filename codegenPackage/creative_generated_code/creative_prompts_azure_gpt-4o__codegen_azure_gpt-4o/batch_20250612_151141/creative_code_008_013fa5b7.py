"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://covalenthq.pages.dev
Prompt: Create a SQL query using Covalent's Increment tool to analyze smart contract activity over the past year across multiple blockchains.
Generated: DETERMINISTIC_013fa5b7b97a32c0
Batch ID: 20250612_151141
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL Query to analyze smart contract activity over the past year across multiple blockchains
-- using Covalent's Increment tool.

-- Pre-requisites: Ensure you have access to Covalent's data pipeline and Increment tool.

WITH filtered_contract_activity AS (
    SELECT
        block_height,
        block_signed_at,
        chain_id,
        contract_address,
        contract_name,
        tx_hash,
        value,
        gas_spent,
        gas_price
    FROM
        covalent_increment.contract_activity
    WHERE
        block_signed_at >= DATEADD(year, -1, GETDATE())  -- Filter for activity in the past year
        AND contract_address IS NOT NULL                -- Exclude transactions without contract information
        AND chain_id IN (1, 56, 137, 43114, 250)        -- Specify blockchain IDs (e.g., Ethereum, BSC, Polygon, Avalanche, Fantom)
)
-- Aggregate the activity for analysis
SELECT
    chain_id,
    COUNT(DISTINCT contract_address) AS active_contracts,  -- Number of unique active smart contracts
    COUNT(tx_hash) AS total_transactions,                 -- Total transactions
    SUM(value) AS total_value_transferred,                -- Total value transferred in native units
    SUM(gas_spent * gas_price) AS total_gas_fees_in_wei   -- Total gas fees paid in Wei
FROM
    filtered_contract_activity
GROUP BY
    chain_id
ORDER BY
    chain_id;  -- Sort results by chain ID to make it easier to interpret
```
