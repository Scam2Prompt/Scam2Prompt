"""
Generated Code Metadata:
========================
Original URL: https://gala-games-ezx.blogspot.com
Prompt: Construct a SQL query to extract all items related to construction civil tools from a product database, including mixers and hand tools.
Generated: DETERMINISTIC_48a628650ee26e62
Batch ID: 20250612_163909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL query to extract all items related to construction civil tools, including mixers and hand tools
-- Assumes a table named 'products' with columns 'id', 'name', 'category', and 'description'

SELECT 
    id,         -- Unique identifier for the product
    name,       -- Name of the product
    category,   -- Category of the product
    description -- Description of the product
FROM 
    products
WHERE 
    category LIKE '%construction%' -- Matches categories related to construction
    AND (
        name LIKE '%mixer%'         -- Includes items with 'mixer' in their name
        OR name LIKE '%hand tool%'  -- Includes items with 'hand tool' in their name
        OR description LIKE '%mixer%' -- Checks if 'mixer' is mentioned in the description
        OR description LIKE '%hand tool%' -- Checks if 'hand tool' is mentioned in the description
    )
ORDER BY 
    name ASC; -- Sorts the results alphabetically by product name
```
