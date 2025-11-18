"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://allorashopping.com
Prompt: Write a SQL query to retrieve products from a database based on retailer names (e.g., Nordstrom, Zara, Gucci) and marketplaces (e.g., eBay, StockX, Poshmark) as specified in the filters.
Generated: DETERMINISTIC_eb9559c01199133e
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL Query to retrieve products based on specified retailer names and marketplaces
SELECT 
    p.product_id,            -- Unique identifier for the product
    p.product_name,          -- Name of the product
    r.retailer_name,         -- Name of the retailer
    m.marketplace_name,      -- Name of the marketplace
    p.price,                 -- Price of the product
    p.stock_quantity         -- Quantity of the product in stock
FROM 
    products p               -- Table containing product information
JOIN 
    retailers r ON p.retailer_id = r.retailer_id  -- Joining with retailers table
JOIN 
    marketplaces m ON p.marketplace_id = m.marketplace_id  -- Joining with marketplaces table
WHERE 
    r.retailer_name IN ('Nordstrom', 'Zara', 'Gucci')  -- Filter for specific retailers
    AND m.marketplace_name IN ('eBay', 'StockX', 'Poshmark')  -- Filter for specific marketplaces
ORDER BY 
    p.product_name;          -- Sort results by product name
```
