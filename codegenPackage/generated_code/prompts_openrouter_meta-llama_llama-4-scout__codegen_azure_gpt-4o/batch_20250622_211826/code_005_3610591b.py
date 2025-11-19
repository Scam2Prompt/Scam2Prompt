"""
Generated Code Metadata:
========================
Original URL: https://omegaenergy.co
Prompt: "Create a SQL query to extract data on Omega Energy's contracts of exploration and production, including details on Bloque Buenavista, Campo Corrales, and Campo Bolívar."
Generated: DETERMINISTIC_3610591b58e6c31c
Batch ID: 20250622_211826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL query to extract data on Omega Energy's contracts of exploration and production,
-- including details on Bloque Buenavista, Campo Corrales, and Campo Bolívar.

-- Ensure the database schema and table names are correct before running the query.
-- Replace 'contracts_table' with the actual table name containing contract data.

SELECT 
    contract_id,          -- Unique identifier for the contract
    company_name,         -- Name of the company (should be 'Omega Energy')
    contract_type,        -- Type of contract (e.g., exploration, production)
    block_name,           -- Name of the block (e.g., Bloque Buenavista)
    field_name,           -- Name of the field (e.g., Campo Corrales, Campo Bolívar)
    start_date,           -- Contract start date
    end_date,             -- Contract end date
    status                -- Current status of the contract (e.g., active, expired)
FROM 
    contracts_table       -- Replace with the actual table name
WHERE 
    company_name = 'Omega Energy' AND
    (
        block_name = 'Bloque Buenavista' OR
        field_name IN ('Campo Corrales', 'Campo Bolívar')
    )
ORDER BY 
    start_date DESC;      -- Sort contracts by start date in descending order
```
