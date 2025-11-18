"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xeluudong.com
Prompt: Write a SQL query to filter furniture products by category (e.g., "tủ bếp chữ L" or "giường ngủ") and price range, ensuring the results include only items made from "gỗ Viva."
Generated: DETERMINISTIC_39dbfcbfd4e44c16
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL query to filter furniture products by category and price range,
-- ensuring that the results only include items made from "gỗ Viva".
-- Replace placeholders (:category, :min_price, :max_price) with actual values or bind parameters in your application.

SELECT 
    product_id,       -- Unique identifier for the product
    product_name,     -- Name of the product
    category,         -- Product category
    material,         -- Material of the product (e.g., "gỗ Viva")
    price             -- Price of the product
FROM 
    furniture_products -- Table containing products related to furniture
WHERE 
    category = :category               -- Filter by the specified category (e.g., "tủ bếp chữ L", "giường ngủ")
    AND material = 'gỗ Viva'           -- Ensure the product is made of "gỗ Viva"
    AND price BETWEEN :min_price AND :max_price -- Filter products within the specified price range
ORDER BY 
    price ASC;                         -- Sort the results by price in ascending order
```
