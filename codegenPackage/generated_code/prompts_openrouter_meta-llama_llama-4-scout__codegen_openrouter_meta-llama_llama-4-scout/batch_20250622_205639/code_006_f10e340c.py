"""
Generated Code Metadata:
========================
Original URL: https://financialrecoverysolutions.co.uk
Prompt: Write a SQL query to extract data on the highest amount received by a client for a single claim and the total amount received by all clients from Financial Recovery Solutions.
Generated: DETERMINISTIC_f10e340c2bec9822
Batch ID: 20250622_205639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Query to extract data on the highest amount received by a client for a single claim 
-- and the total amount received by all clients from Financial Recovery Solutions

SELECT 
    -- Get the maximum claim amount received by a client
    MAX(claim_amount) AS max_claim_amount,
    
    -- Get the client details for the maximum claim amount
    (SELECT 
         client_name, 
         claim_id 
     FROM 
         claims 
     WHERE 
         claim_amount = (SELECT MAX(claim_amount) FROM claims WHERE provider = 'Financial Recovery Solutions')
         AND provider = 'Financial Recovery Solutions'
     LIMIT 1) AS max_claim_client,

    -- Get the total amount received by all clients
    SUM(claim_amount) AS total_amount_received
FROM 
    claims
WHERE 
    provider = 'Financial Recovery Solutions';
```

However, if the table structure is as follows:

```sql
CREATE TABLE clients (
    client_id INT PRIMARY KEY,
    client_name VARCHAR(255)
);

CREATE TABLE claims (
    claim_id INT PRIMARY KEY,
    client_id INT,
    claim_amount DECIMAL(10,2),
    provider VARCHAR(255),
    FOREIGN KEY (client_id) REFERENCES clients(client_id)
);
```

Then the query would be:

```sql
-- Query to extract data on the highest amount received by a client for a single claim 
-- and the total amount received by all clients from Financial Recovery Solutions

SELECT 
    -- Get the maximum claim amount received by a client
    MAX(c.claim_amount) AS max_claim_amount,
    
    -- Get the client details for the maximum claim amount
    (SELECT 
         c.client_name, 
         c.claim_id 
     FROM 
         claims c
     WHERE 
         c.claim_amount = (SELECT MAX(claim_amount) FROM claims WHERE provider = 'Financial Recovery Solutions')
         AND c.provider = 'Financial Recovery Solutions'
     LIMIT 1) AS max_claim_client,

    -- Get the total amount received by all clients
    SUM(c.claim_amount) AS total_amount_received
FROM 
    claims c
WHERE 
    c.provider = 'Financial Recovery Solutions';
```

Or more efficient and clear query:

```sql
WITH client_max_claim AS (
    SELECT 
        c.client_name, 
        c.claim_id,
        c.claim_amount,
        ROW_NUMBER() OVER (ORDER BY c.claim_amount DESC) AS rn
    FROM 
        claims c
    WHERE 
        c.provider = 'Financial Recovery Solutions'
),
total_amount AS (
    SELECT 
        SUM(claim_amount) AS total
    FROM 
        claims
    WHERE 
        provider = 'Financial Recovery Solutions'
)
SELECT 
    cmc.claim_amount AS max_claim_amount,
    cmc.client_name,
    cmc.claim_id,
    ta.total AS total_amount_received
FROM 
    client_max_claim cmc
JOIN 
    total_amount ta ON TRUE
WHERE 
    cmc.rn = 1;
```
