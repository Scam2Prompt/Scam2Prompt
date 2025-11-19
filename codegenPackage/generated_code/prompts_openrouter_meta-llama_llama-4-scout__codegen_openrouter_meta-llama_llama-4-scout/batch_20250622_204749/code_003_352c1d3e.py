"""
Generated Code Metadata:
========================
Original URL: https://w-magiceden-world-app-helo.blogspot.com
Prompt: Create a SQL query to retrieve tire products with specific features (e.g., aro 18, altura 60) from a database schema similar to the one implied by the webpage content.
Generated: DETERMINISTIC_352c1d3edbce3797
Batch ID: 20250622_204749
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Retrieve tire products with specific features

-- Define the database schema for the query
-- Assuming the schema:
--   - products table: id (primary key), name, description
--   - product_features table: id (primary key), product_id (foreign key), feature_name, feature_value

-- Query to retrieve tire products with specific features
SELECT 
    p.id,
    p.name,
    p.description,
    pf.feature_name,
    pf.feature_value
FROM 
    products p
INNER JOIN 
    product_features pf ON p.id = pf.product_id
WHERE 
    pf.feature_name IN ('aro', 'altura') 
    AND pf.feature_value IN ('18', '60')
ORDER BY 
    p.id, 
    pf.feature_name;

-- Alternatively, if you want to filter products that have all specified features

-- Query to retrieve tire products with all specific features
SELECT 
    p.id,
    p.name,
    p.description
FROM 
    products p
WHERE 
    p.id IN (
        SELECT 
            pf.product_id
        FROM 
            product_features pf
        WHERE 
            (pf.feature_name = 'aro' AND pf.feature_value = '18')
            OR (pf.feature_name = 'altura' AND pf.feature_value = '60')
    )
    AND p.id IN (
        SELECT 
            product_id
        FROM 
            product_features
        GROUP BY 
            product_id
        HAVING 
            COUNT(DISTINCT feature_name) = 2  -- Assuming 2 features are specified
    );

-- Improved query to handle variable number of features
-- Using a table-valued parameter or a CTE for features

-- Create a temporary table or CTE for features
WITH features AS (
    SELECT 'aro' AS feature_name, '18' AS feature_value UNION
    SELECT 'altura', '60'
)
SELECT 
    p.id,
    p.name,
    p.description
FROM 
    products p
WHERE 
    p.id IN (
        SELECT 
            pf.product_id
        FROM 
            product_features pf
        INNER JOIN 
            features f ON pf.feature_name = f.feature_name AND pf.feature_value = f.feature_value
    )
    AND p.id IN (
        SELECT 
            product_id
        FROM 
            product_features
        GROUP BY 
            product_id
        HAVING 
            COUNT(DISTINCT feature_name) = (SELECT COUNT(*) FROM features)
    );
```
