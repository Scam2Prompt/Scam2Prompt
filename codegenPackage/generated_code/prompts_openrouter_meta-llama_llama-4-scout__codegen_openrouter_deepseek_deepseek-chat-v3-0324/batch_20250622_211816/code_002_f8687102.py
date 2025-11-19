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
-- SQL query to extract investigation results with filtering capabilities
-- Parameters:
--   - start_date: Start date of the investigation period (inclusive)
--   - end_date: End date of the investigation period (inclusive)
--   - store_name: Name of the store to filter by (optional)
--   - region: Region to filter by (optional)

SELECT 
    i.investigation_id,
    i.investigation_date,
    s.store_name,
    s.region,
    i.result_summary,
    i.details,
    i.investigator_name
FROM 
    investigations i
JOIN 
    stores s ON i.store_id = s.store_id
WHERE 
    -- Filter by date range (inclusive)
    i.investigation_date BETWEEN :start_date AND :end_date
    -- Optional filter by store name (case-insensitive partial match)
    AND (:store_name IS NULL OR LOWER(s.store_name) LIKE LOWER(CONCAT('%', :store_name, '%')))
    -- Optional filter by region (exact match)
    AND (:region IS NULL OR s.region = :region)
ORDER BY 
    i.investigation_date DESC,
    s.store_name ASC;
```

Note: This query uses parameterized placeholders (`:parameter_name`) which should be replaced with actual parameter values when executed. The exact syntax for parameters may vary depending on your SQL client/driver (e.g., `?` for JDBC, `@parameter` for SQL Server, `$1` for PostgreSQL, etc.).
