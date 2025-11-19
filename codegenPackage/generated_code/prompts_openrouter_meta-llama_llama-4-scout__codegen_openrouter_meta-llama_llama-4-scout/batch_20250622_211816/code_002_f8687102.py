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
-- investigation_results_query.sql

-- Define the query to extract investigation results
-- based on date range, store name, and region.

SELECT 
    ir.id,
    ir.investigation_date,
    ir.store_name,
    ir.region,
    ir.result
FROM 
    investigation_results ir
WHERE 
    -- Filter by date range
    ir.investigation_date >= :start_date
    AND ir.investigation_date <= :end_date
    -- Filter by store name
    AND (LOWER(ir.store_name) LIKE LOWER(:store_name) OR :store_name IS NULL)
    -- Filter by region
    AND (LOWER(ir.region) LIKE LOWER(:region) OR :region IS NULL)
ORDER BY 
    ir.investigation_date DESC;

-- Define a stored procedure to execute the query
-- with input parameters for date range, store name, and region.

DELIMITER $$

CREATE PROCEDURE GetInvestigationResults(
    IN start_date DATE,
    IN end_date DATE,
    IN store_name VARCHAR(255),
    IN region VARCHAR(255)
)
BEGIN
    SELECT 
        ir.id,
        ir.investigation_date,
        ir.store_name,
        ir.region,
        ir.result
    FROM 
        investigation_results ir
    WHERE 
        ir.investigation_date >= start_date
        AND ir.investigation_date <= end_date
        AND (LOWER(ir.store_name) LIKE LOWER(store_name) OR store_name IS NULL)
        AND (LOWER(ir.region) LIKE LOWER(region) OR region IS NULL)
    ORDER BY 
        ir.investigation_date DESC;
END$$

DELIMITER ;

-- Example usage:

-- CALL GetInvestigationResults('2022-01-01', '2022-12-31', 'Example Store', 'Example Region');

-- Alternatively, you can use a prepared statement:

SET @start_date = '2022-01-01';
SET @end_date = '2022-12-31';
SET @store_name = 'Example Store';
SET @region = 'Example Region';

PREPARE stmt FROM 'SELECT 
                    ir.id,
                    ir.investigation_date,
                    ir.store_name,
                    ir.region,
                    ir.result
                FROM 
                    investigation_results ir
                WHERE 
                    ir.investigation_date >= ?
                    AND ir.investigation_date <= ?
                    AND (LOWER(ir.store_name) LIKE LOWER(?) OR ? IS NULL)
                    AND (LOWER(ir.region) LIKE LOWER(?) OR ? IS NULL)
                ORDER BY 
                    ir.investigation_date DESC';

EXECUTE stmt USING @start_date, @end_date, @store_name, @store_name, @region, @region;

DEALLOCATE PREPARE stmt;
```
