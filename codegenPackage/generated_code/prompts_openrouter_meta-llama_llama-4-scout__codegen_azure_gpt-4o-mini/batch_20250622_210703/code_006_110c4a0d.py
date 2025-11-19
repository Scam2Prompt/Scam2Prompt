"""
Generated Code Metadata:
========================
Original URL: https://chayatime.com
Prompt: Create a SQL query to analyze sales data for a ChayaTime franchise, identifying the most popular tea and snack items.
Generated: DETERMINISTIC_110c4a0d51ff042c
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL query to analyze sales data for ChayaTime franchise
-- This query identifies the most popular tea and snack items based on sales volume

WITH SalesSummary AS (
    -- Summarize sales data by item type (tea or snack)
    SELECT 
        item_name,
        item_type,
        SUM(quantity_sold) AS total_quantity_sold
    FROM 
        sales_data
    WHERE 
        franchise_name = 'ChayaTime'  -- Filter for ChayaTime franchise
    GROUP BY 
        item_name, item_type
)

-- Select the most popular tea and snack items
SELECT 
    item_type,
    item_name,
    total_quantity_sold
FROM 
    SalesSummary
WHERE 
    (item_type = 'Tea' OR item_type = 'Snack')  -- Filter for tea and snack items
ORDER BY 
    item_type, total_quantity_sold DESC  -- Order by item type and sales volume
LIMIT 10;  -- Limit results to top 10 items per type
```

```sql
-- Error handling: Ensure that the sales_data table exists before running the query
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'sales_data') THEN
        RAISE EXCEPTION 'Table sales_data does not exist.';
    END IF;
END $$;
```
