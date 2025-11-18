"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://malkeenz.com
Prompt: Write a SQL query to retrieve all jewelry products with a price range between Rs.5,000 and Rs.15,000, specifically filtering for moissanite gemstone rings.
Generated: DETERMINISTIC_cb31bf6bd2764401
Batch ID: 20250612_154506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL query to retrieve all jewelry products that are moissanite gemstone rings
-- with a price range between Rs. 5,000 and Rs. 15,000.

SELECT 
    product_id,         -- Unique identifier for the product
    product_name,       -- Name of the jewelry product
    price,              -- Price of the product
    gemstone_type,      -- Type of gemstone used in the product
    category            -- Category of the jewelry product
FROM 
    jewelry_products    -- The table containing jewelry product details
WHERE 
    gemstone_type = 'Moissanite'    -- Filter for Moissanite gemstone
    AND category = 'Ring'            -- Filter for Rings category
    AND price BETWEEN 5000 AND 15000 -- Price range filter
ORDER BY 
    price;               -- Order results by price in ascending order
```
