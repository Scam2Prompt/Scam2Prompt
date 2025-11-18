"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://curaheridas.com
Prompt: Write a SQL query to retrieve the most sold products from a database table containing items like "Aquacel AG + Extra" and "Ulcoderma Ungüento" along with their sales data.
Generated: DETERMINISTIC_0bc97d5673276be8
Batch ID: 20250612_152426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Retrieve the most sold products along with their sales data
SELECT 
    product_name,            -- Name of the product
    SUM(sales_quantity) AS total_sales -- Total quantity sold for each product
FROM 
    sales_data               -- Table containing sales records
WHERE 
    product_name IN ('Aquacel AG + Extra', 'Ulcoderma Ungüento') -- Filter for specific products
GROUP BY 
    product_name             -- Group results by product name
ORDER BY 
    total_sales DESC         -- Order products by total sales in descending order
LIMIT 10;                   -- Limit results to the top 10 most sold products
```

**Note:** Replace `sales_data` with the actual table name if it's different in your database schema. Adjust the filtering criteria as needed to match your data context.
