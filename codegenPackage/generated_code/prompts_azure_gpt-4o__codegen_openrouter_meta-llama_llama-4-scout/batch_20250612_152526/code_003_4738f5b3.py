"""
Generated Code Metadata:
========================
Original URL: https://baazaars.com
Prompt: Create a SQL query to extract all products with a discount greater than 20% from an e-commerce database, including categories like "Accessories" and "Dresses."
Generated: DETERMINISTIC_4738f5b3d6173039
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Define the SQL query to extract products with a discount greater than 20%
-- from the e-commerce database, specifically from categories like "Accessories" and "Dresses"

SELECT 
    p.product_id,
    p.product_name,
    c.category_name,
    p.original_price,
    p.discounted_price,
    (1 - p.discounted_price / p.original_price) * 100 AS discount_percentage
FROM 
    products p
INNER JOIN 
    product_categories pc ON p.product_id = pc.product_id
INNER JOIN 
    categories c ON pc.category_id = c.category_id
WHERE 
    c.category_name IN ('Accessories', 'Dresses')
    AND (1 - p.discounted_price / p.original_price) * 100 > 20
ORDER BY 
    discount_percentage DESC;

-- Create a sample database schema for demonstration purposes
-- CREATE TABLE categories (
--     category_id INT PRIMARY KEY,
--     category_name VARCHAR(255) NOT NULL
-- );

-- CREATE TABLE products (
--     product_id INT PRIMARY KEY,
--     product_name VARCHAR(255) NOT NULL,
--     original_price DECIMAL(10, 2) NOT NULL,
--     discounted_price DECIMAL(10, 2) NOT NULL
-- );

-- CREATE TABLE product_categories (
--     product_id INT NOT NULL,
--     category_id INT NOT NULL,
--     PRIMARY KEY (product_id, category_id),
--     FOREIGN KEY (product_id) REFERENCES products(product_id),
--     FOREIGN KEY (category_id) REFERENCES categories(category_id)
-- );

-- Insert sample data for demonstration purposes
-- INSERT INTO categories (category_id, category_name) 
-- VALUES 
--     (1, 'Accessories'),
--     (2, 'Dresses');

-- INSERT INTO products (product_id, product_name, original_price, discounted_price) 
-- VALUES 
--     (1, 'Product A', 100.00, 80.00),
--     (2, 'Product B', 200.00, 160.00),
--     (3, 'Product C', 50.00, 40.00);

-- INSERT INTO product_categories (product_id, category_id) 
-- VALUES 
--     (1, 1),
--     (2, 2),
--     (3, 1);
```
