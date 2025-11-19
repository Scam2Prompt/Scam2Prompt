"""
Generated Code Metadata:
========================
Original URL: https://app-chainbase.com
Prompt: Generate a sample query to retrieve data from Chainbase's extensive datasets for a specific blockchain project.
Generated: DETERMINISTIC_0a8c2dc0f68af23c
Batch ID: 20250612_155632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Query to retrieve transaction data for a specific blockchain project from Chainbase
-- This example fetches Ethereum transactions for a given contract address within a time range

SELECT 
    t.transaction_hash,
    t.block_number,
    t.block_timestamp,
    t.from_address,
    t.to_address,
    t.value,
    t.gas_price,
    t.gas_used,
    t.input_data
FROM 
    ethereum.transactions t
WHERE 
    t.to_address = LOWER('0xContractAddressHere') -- Replace with actual contract address
    AND t.block_timestamp BETWEEN '2023-01-01' AND '2023-12-31'
    AND t.status = 1 -- Successful transactions only
ORDER BY 
    t.block_timestamp DESC
LIMIT 1000;
```
