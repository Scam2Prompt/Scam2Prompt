"""
Generated Code Metadata:
========================
Original URL: https://fox-sp.com
Prompt: Generate a SQL query to extract data from a database containing investigation results, filtering by date range, store name, and region, similar to the 絞り込み検索 functionality on the FOX website.
Generated: DETERMINISTIC_f86871022f06e9f7
Batch ID: 20250622_211816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL query to extract investigation results based on specified filters
-- This query retrieves records from the 'investigation_results' table
-- filtered by a date range, store name, and region.

SELECT 
    ir.investigation_id,        -- Unique identifier for the investigation
    ir.store_name,              -- Name of the store where the investigation took place
    ir.region,                  -- Region of the store
    ir.result_date,             -- Date of the investigation result
    ir.result_details           -- Details of the investigation result
FROM 
    investigation_results ir     -- Table containing investigation results
WHERE 
    ir.result_date BETWEEN :start_date AND :end_date  -- Filter by date range
    AND ir.store_name = :store_name                      -- Filter by store name
    AND ir.region = :region                                -- Filter by region
ORDER BY 
    ir.result_date DESC;       -- Order results by date in descending order

-- Note: 
-- Replace :start_date, :end_date, :store_name, and :region with actual values 
-- or bind parameters in your application code to prevent SQL injection.
```
