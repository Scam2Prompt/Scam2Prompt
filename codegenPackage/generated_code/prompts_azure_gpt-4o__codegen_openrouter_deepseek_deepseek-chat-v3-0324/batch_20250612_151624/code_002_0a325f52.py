"""
Generated Code Metadata:
========================
Original URL: https://glowconsultants.org
Prompt: Generate SQL queries for managing consistent and accurate data in a business intelligence system, referencing GLOW Consultants' approach to data management and BI.
Generated: DETERMINISTIC_0a325f52bd892a05
Batch ID: 20250612_151624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Queries for Business Intelligence Data Management
-- Inspired by GLOW Consultants' Data Management Best Practices

-- 1. Data Quality Check: Identify missing values in critical dimensions
SELECT 
    column_name,
    COUNT(*) AS missing_count
FROM 
    your_table
WHERE 
    column_name IS NULL
GROUP BY 
    column_name
HAVING 
    COUNT(*) > 0;

-- 2. Data Consistency: Find duplicate records in fact tables
SELECT 
    COUNT(*) AS duplicate_count,
    column1, column2, column3 -- Key identifying columns
FROM 
    your_fact_table
GROUP BY 
    column1, column2, column3
HAVING 
    COUNT(*) > 1;

-- 3. Data Accuracy: Validate numerical ranges in measures
SELECT 
    column_name,
    MIN(value) AS min_value,
    MAX(value) AS max_value,
    AVG(value) AS avg_value
FROM 
    your_measure_table
GROUP BY 
    column_name;

-- 4. Temporal Data Integrity: Check for future-dated transactions
SELECT 
    COUNT(*) AS future_dated_records
FROM 
    your_transaction_table
WHERE 
    transaction_date > CURRENT_DATE;

-- 5. Referential Integrity: Find orphaned foreign keys
SELECT 
    fk.foreign_key_column,
    COUNT(*) AS orphaned_records
FROM 
    child_table fk
LEFT JOIN 
    parent_table pk ON fk.foreign_key_column = pk.primary_key_column
WHERE 
    pk.primary_key_column IS NULL
GROUP BY 
    fk.foreign_key_column;

-- 6. Slowly Changing Dimension Type 2 Management
-- Current records
SELECT 
    COUNT(*) AS current_records
FROM 
    your_scd_table
WHERE 
    current_flag = 'Y' 
    AND expiration_date IS NULL;

-- Expired records
SELECT 
    COUNT(*) AS expired_records
FROM 
    your_scd_table
WHERE 
    current_flag = 'N' 
    AND expiration_date IS NOT NULL;

-- 7. Data Freshness: Check last update timestamps
SELECT 
    table_name,
    MAX(last_updated) AS last_update_time,
    DATEDIFF(DAY, MAX(last_updated), CURRENT_DATE) AS days_since_update
FROM 
    your_metadata_table
GROUP BY 
    table_name
ORDER BY 
    days_since_update DESC;

-- 8. Data Lineage Tracking
SELECT 
    source_system,
    COUNT(*) AS record_count,
    MIN(load_date) AS earliest_load,
    MAX(load_date) AS latest_load
FROM 
    your_data_lineage_table
GROUP BY 
    source_system;

-- 9. Data Volume Monitoring
SELECT 
    table_schema,
    table_name,
    ROUND(SUM(data_length + index_length) / 1024 / 1024, 2) AS size_mb
FROM 
    information_schema.tables
WHERE 
    table_schema = 'your_database'
GROUP BY 
    table_schema, table_name
ORDER BY 
    size_mb DESC;

-- 10. Data Access Pattern Analysis
SELECT 
    user_name,
    COUNT(*) AS query_count,
    AVG(query_duration) AS avg_duration_ms,
    MAX(query_time) AS last_query_time
FROM 
    query_log_table
WHERE 
    query_time >= DATEADD(DAY, -30, CURRENT_DATE)
GROUP BY 
    user_name
ORDER BY 
    query_count DESC;
```
