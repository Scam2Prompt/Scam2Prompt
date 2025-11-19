"""
Generated Code Metadata:
========================
Original URL: https://ipolattibraz.blogspot.com
Prompt: Create a SQL query to retrieve product information for bicycles with specific features (e.g., aro 12, feminino) from a database like the one used by ipolattibraz.
Generated: DETERMINISTIC_5125f6c6f928c247
Batch ID: 20250622_212010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Retrieve product information for bicycles with specific features

-- Define the query
SELECT 
    p.id,
    p.name,
    p.description,
    p.price,
    p.image_url,
    pf.feature_name,
    pf.feature_value
FROM 
    products p
INNER JOIN 
    product_features pf ON p.id = pf.product_id
WHERE 
    p.category = 'bicicleta'
    AND (pf.feature_name = 'aro' AND pf.feature_value = '12' 
         OR pf.feature_name = 'genero' AND pf.feature_value = 'feminino')
ORDER BY 
    p.id;

-- Or, for better performance, consider using a single pass through product_features
-- and joining on a subquery or CTE for feature filtering

-- Define an alternative query
WITH target_features AS (
    SELECT 
        'aro' AS feature_name, 
        '12' AS feature_value
    UNION
    SELECT 
        'genero', 
        'feminino'
)
SELECT 
    p.id,
    p.name,
    p.description,
    p.price,
    p.image_url
FROM 
    products p
WHERE 
    p.category = 'bicicleta'
    AND p.id IN (
        SELECT 
            pf.product_id
        FROM 
            product_features pf
        INNER JOIN 
            target_features tf ON pf.feature_name = tf.feature_name AND pf.feature_value = tf.feature_value
        GROUP BY 
            pf.product_id
        HAVING 
            COUNT(DISTINCT pf.feature_name) = (SELECT COUNT(*) FROM target_features)
    )
ORDER BY 
    p.id;
```
