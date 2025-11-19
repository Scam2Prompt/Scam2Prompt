"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gala-games-ezx.blogspot.com
Prompt: Construct a SQL query to extract all items related to construction civil tools from a product database, including mixers and hand tools.
Generated: DETERMINISTIC_48a628650ee26e62
Batch ID: 20250612_163909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL query to extract all items related to construction civil tools,
-- including mixers and hand tools from the product database.

SELECT 
    product_id,        -- Unique identifier for the product
    product_name,      -- Name of the product
    product_category,   -- Category of the product
    price,             -- Price of the product
    stock_quantity     -- Available quantity in stock
FROM 
    products           -- Table containing product information
WHERE 
    product_category IN ('Construction Tools', 'Mixers', 'Hand Tools')  -- Filter for relevant categories
    AND is_active = TRUE -- Ensure only active products are retrieved
ORDER BY 
    product_name;      -- Sort results by product name for better readability
```
