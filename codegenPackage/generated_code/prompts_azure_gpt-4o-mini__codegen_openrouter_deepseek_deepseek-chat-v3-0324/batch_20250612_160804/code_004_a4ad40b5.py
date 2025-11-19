"""
Generated Code Metadata:
========================
Original URL: https://connect-dapps.com
Prompt: Provide an example of using SQL to query data from a DApp mentioned on connect-dapps.com.
Generated: DETERMINISTIC_a4ad40b529a22513
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Example SQL query to fetch DApp data from a hypothetical database
-- This assumes a table structure similar to connect-dapps.com's DApp listings

-- Query to get basic DApp information
SELECT 
    dapp_id,
    name,
    description,
    category,
    blockchain_platform,
    website_url,
    created_at,
    updated_at
FROM 
    dapps
WHERE 
    is_active = TRUE
ORDER BY 
    created_at DESC
LIMIT 10;

-- Query to get DApp statistics with error handling for division by zero
SELECT 
    d.dapp_id,
    d.name,
    COUNT(DISTINCT u.user_id) AS active_users,
    COUNT(t.tx_id) AS total_transactions,
    CASE 
        WHEN COUNT(DISTINCT u.user_id) = 0 THEN 0
        ELSE COUNT(t.tx_id) / COUNT(DISTINCT u.user_id)
    END AS tx_per_user
FROM 
    dapps d
LEFT JOIN 
    users u ON d.dapp_id = u.dapp_id AND u.last_active > CURRENT_DATE - INTERVAL '30 days'
LEFT JOIN 
    transactions t ON d.dapp_id = t.dapp_id
GROUP BY 
    d.dapp_id, d.name
HAVING 
    COUNT(DISTINCT u.user_id) > 0
ORDER BY 
    active_users DESC;

-- Parameterized query to get DApps by category with pagination
PREPARE get_dapps_by_category (text, int, int) AS
SELECT 
    dapp_id,
    name,
    description,
    website_url
FROM 
    dapps
WHERE 
    category = $1
    AND is_active = TRUE
ORDER BY 
    name ASC
LIMIT $2 OFFSET $3;

-- Example execution of the prepared statement
EXECUTE get_dapps_by_category('DeFi', 10, 0);

-- Query with error logging for failed transactions
WITH failed_txs AS (
    SELECT 
        dapp_id,
        COUNT(*) AS failed_count
    FROM 
        transactions
    WHERE 
        status = 'failed'
        AND tx_time > CURRENT_DATE - INTERVAL '7 days'
    GROUP BY 
        dapp_id
)
SELECT 
    d.dapp_id,
    d.name,
    COALESCE(f.failed_count, 0) AS failed_transactions,
    CASE 
        WHEN COALESCE(f.failed_count, 0) > 10 THEN 'High'
        WHEN COALESCE(f.failed_count, 0) > 5 THEN 'Medium'
        ELSE 'Low'
    END AS failure_severity
FROM 
    dapps d
LEFT JOIN 
    failed_txs f ON d.dapp_id = f.dapp_id
WHERE 
    d.is_active = TRUE
ORDER BY 
    failed_transactions DESC;
```
