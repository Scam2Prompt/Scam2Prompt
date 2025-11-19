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
-- Retrieve product details for "Tấm Ốp Nano CASARY" models
-- including specifications and pricing

-- Assuming the database schema:
-- products table: id, name, description, price
-- product_specs table: id, product_id, spec_name, spec_value
-- product_prices table: id, product_id, price, created_at

-- Query to retrieve product details
SELECT 
  p.id,
  p.name,
  p.description,
  ps.spec_name,
  ps.spec_value,
  pp.price
FROM 
  products p
  LEFT JOIN product_specs ps ON p.id = ps.product_id
  LEFT JOIN product_prices pp ON p.id = pp.product_id
WHERE 
  p.name LIKE '%Tấm Ốp Nano CASARY%';

-- Query to retrieve product details with aggregated specs and latest price
SELECT 
  p.id,
  p.name,
  p.description,
  JSON_AGG(JSON_BUILD_OBJECT('spec_name', ps.spec_name, 'spec_value', ps.spec_value)) AS specs,
  pp.price
FROM 
  products p
  LEFT JOIN product_specs ps ON p.id = ps.product_id
  LEFT JOIN (
    SELECT 
      product_id, 
      price, 
      ROW_NUMBER() OVER (PARTITION BY product_id ORDER BY created_at DESC) AS row_num
    FROM 
      product_prices
  ) pp ON p.id = pp.product_id AND pp.row_num = 1
WHERE 
  p.name LIKE '%Tấm Ốp Nano CASARY%'
GROUP BY 
  p.id, p.name, p.description, pp.price;

-- Stored procedure to retrieve product details
CREATE OR REPLACE PROCEDURE get_product_details(product_name VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
  SELECT 
    p.id,
    p.name,
    p.description,
    JSON_AGG(JSON_BUILD_OBJECT('spec_name', ps.spec_name, 'spec_value', ps.spec_value)) AS specs,
    pp.price
  FROM 
    products p
    LEFT JOIN product_specs ps ON p.id = ps.product_id
    LEFT JOIN (
      SELECT 
        product_id, 
        price, 
        ROW_NUMBER() OVER (PARTITION BY product_id ORDER BY created_at DESC) AS row_num
      FROM 
        product_prices
    ) pp ON p.id = pp.product_id AND pp.row_num = 1
  WHERE 
    p.name LIKE CONCAT('%', product_name, '%')
  GROUP BY 
    p.id, p.name, p.description, pp.price;
END$$;

-- Example usage:
CALL get_product_details('Tấm Ốp Nano CASARY');
```
