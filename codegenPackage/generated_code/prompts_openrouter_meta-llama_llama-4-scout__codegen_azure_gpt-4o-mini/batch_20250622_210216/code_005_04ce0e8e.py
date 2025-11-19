"""
Generated Code Metadata:
========================
Original URL: https://segrepin.com
Prompt: Write a SQL query to extract insights from a dataset related to business operations in the Congo, using techniques for data cleaning and visualization.
Generated: DETERMINISTIC_04ce0e8e02468f7f
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Query to extract insights from a business operations dataset in the Congo

-- Step 1: Create a temporary table to clean the data
CREATE TEMPORARY TABLE cleaned_data AS
SELECT 
    -- Select relevant columns and handle NULL values
    COALESCE(business_id, 'Unknown') AS business_id,
    COALESCE(business_name, 'Unnamed Business') AS business_name,
    COALESCE(location, 'Unknown Location') AS location,
    -- Convert revenue to a numeric type and handle invalid entries
    NULLIF(REPLACE(revenue, ',', ''), '')::NUMERIC AS revenue,
    -- Extract year from the date for analysis
    EXTRACT(YEAR FROM operation_date) AS operation_year
FROM 
    business_operations
WHERE 
    -- Filter out rows with critical missing data
    business_id IS NOT NULL 
    AND operation_date IS NOT NULL;

-- Step 2: Aggregate data to get insights
SELECT 
    operation_year,
    COUNT(DISTINCT business_id) AS total_businesses,
    SUM(revenue) AS total_revenue,
    AVG(revenue) AS average_revenue
FROM 
    cleaned_data
GROUP BY 
    operation_year
ORDER BY 
    operation_year;

-- Step 3: Clean up temporary table after use
DROP TABLE IF EXISTS cleaned_data;
```
