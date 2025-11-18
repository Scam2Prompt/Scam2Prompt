"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mobleman-doostan.com
Prompt: Create a SQL query to retrieve all products with more than 20 variations, such as "صندلی آرایشگاهی" and "مبلمان اداری," from a database table.
Generated: DETERMINISTIC_166b85cd5ca4438c
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL query to retrieve products with more than 20 variations
SELECT 
    p.product_id,
    p.product_name,
    COUNT(v.variation_id) AS variation_count
FROM 
    products p
JOIN 
    variations v ON p.product_id = v.product_id
WHERE 
    p.product_name IN ('صندلی آرایشگاهی', 'مبلمان اداری')
GROUP BY 
    p.product_id, p.product_name
HAVING 
    COUNT(v.variation_id) > 20;
```
