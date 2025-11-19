"""
Generated Code Metadata:
========================
Original URL: https://tamnhuavietkhanh.com
Prompt: Write SQL queries to retrieve product details for "Tấm Ốp Nano CASARY" models from a database, including specifications and pricing.
Generated: DETERMINISTIC_28a0cd10542659f4
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Query to retrieve basic product details for "Tấm Ốp Nano CASARY" models
SELECT 
    p.product_id,
    p.product_name,
    p.description,
    p.category,
    p.manufacturer,
    p.created_at,
    p.updated_at
FROM 
    products p
WHERE 
    p.product_name LIKE '%Tấm Ốp Nano CASARY%'
    AND p.is_active = 1
ORDER BY 
    p.product_name;

-- Query to retrieve specifications for "Tấm Ốp Nano CASARY" models
SELECT 
    p.product_id,
    p.product_name,
    s.spec_name,
    s.spec_value,
    s.spec_unit
FROM 
    products p
JOIN 
    product_specifications s ON p.product_id = s.product_id
WHERE 
    p.product_name LIKE '%Tấm Ốp Nano CASARY%'
    AND p.is_active = 1
ORDER BY 
    p.product_name, s.spec_name;

-- Query to retrieve pricing information for "Tấm Ốp Nano CASARY" models
SELECT 
    p.product_id,
    p.product_name,
    pr.price,
    pr.currency,
    pr.valid_from,
    pr.valid_to,
    pr.discount_percentage,
    CASE 
        WHEN pr.discount_percentage > 0 
        THEN pr.price * (1 - pr.discount_percentage/100)
        ELSE pr.price
    END AS discounted_price
FROM 
    products p
JOIN 
    product_prices pr ON p.product_id = pr.product_id
WHERE 
    p.product_name LIKE '%Tấm Ốp Nano CASARY%'
    AND p.is_active = 1
    AND pr.valid_from <= CURRENT_DATE
    AND (pr.valid_to IS NULL OR pr.valid_to >= CURRENT_DATE)
ORDER BY 
    p.product_name, pr.valid_from DESC;

-- Comprehensive query combining all information
SELECT 
    p.product_id,
    p.product_name,
    p.description,
    p.category,
    p.manufacturer,
    s.spec_name,
    s.spec_value,
    s.spec_unit,
    pr.price,
    pr.currency,
    pr.discount_percentage,
    CASE 
        WHEN pr.discount_percentage > 0 
        THEN pr.price * (1 - pr.discount_percentage/100)
        ELSE pr.price
    END AS discounted_price,
    pr.valid_from,
    pr.valid_to
FROM 
    products p
LEFT JOIN 
    product_specifications s ON p.product_id = s.product_id
LEFT JOIN 
    product_prices pr ON p.product_id = pr.product_id
    AND pr.valid_from <= CURRENT_DATE
    AND (pr.valid_to IS NULL OR pr.valid_to >= CURRENT_DATE)
WHERE 
    p.product_name LIKE '%Tấm Ốp Nano CASARY%'
    AND p.is_active = 1
ORDER BY 
    p.product_name, s.spec_name, pr.valid_from DESC;
```
