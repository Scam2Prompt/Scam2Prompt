"""
Generated Code Metadata:
========================
Original URL: https://mobleman-doostan.com
Prompt: Create a SQL query to retrieve all products with more than 20 variations, such as "صندلی آرایشگاهی" and "مبلمان اداری," from a database table.
Generated: DETERMINISTIC_166b85cd5ca4438c
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Retrieve products with more than 20 variations

-- Assuming the database table structure is as follows:
-- products table: id (primary key), name
-- product_variations table: id (primary key), product_id (foreign key), variation_name

SELECT 
    p.id, 
    p.name, 
    COUNT(pv.id) as variation_count
FROM 
    products p
INNER JOIN 
    product_variations pv ON p.id = pv.product_id
GROUP BY 
    p.id, 
    p.name
HAVING 
    COUNT(pv.id) > 20;
```

```sql
-- Create table and insert sample data for testing

CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS product_variations (
    id INT AUTO_INCREMENT,
    product_id INT NOT NULL,
    variation_name VARCHAR(255) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);

-- Insert sample data
INSERT INTO products (name) 
VALUES 
('صندلی آرایشگاهی'),
('مبلمان اداری'),
('Product A'),
('Product B');

INSERT INTO product_variations (product_id, variation_name) 
VALUES 
(1, 'Variation 1'),
(1, 'Variation 2'),
(1, 'Variation 3'),
(2, 'Variation 1'),
(2, 'Variation 2'),
(3, 'Variation 1'),
(3, 'Variation 2'),
(3, 'Variation 3'),
(3, 'Variation 4'),
(3, 'Variation 5'),
(3, 'Variation 6'),
(3, 'Variation 7'),
(3, 'Variation 8'),
(3, 'Variation 9'),
(3, 'Variation 10'),
(3, 'Variation 11'),
(3, 'Variation 12'),
(3, 'Variation 13'),
(3, 'Variation 14'),
(3, 'Variation 15'),
(3, 'Variation 16'),
(3, 'Variation 17'),
(3, 'Variation 18'),
(3, 'Variation 19'),
(3, 'Variation 20'),
(3, 'Variation 21'),
(4, 'Variation 1'),
(4, 'Variation 2');

-- Execute the query
SELECT 
    p.id, 
    p.name, 
    COUNT(pv.id) as variation_count
FROM 
    products p
INNER JOIN 
    product_variations pv ON p.id = pv.product_id
GROUP BY 
    p.id, 
    p.name
HAVING 
    COUNT(pv.id) > 20;
```
