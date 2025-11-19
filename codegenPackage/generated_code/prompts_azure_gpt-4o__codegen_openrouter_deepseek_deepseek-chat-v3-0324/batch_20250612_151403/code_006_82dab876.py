"""
Generated Code Metadata:
========================
Original URL: https://jgiwindia.com
Prompt: Write a SQL query to store and retrieve information about Jai Gurudev Industries' sugar-boiled confectionery products, such as "Peanut Candy" and "Honey Lemon Mint Candy."
Generated: DETERMINISTIC_82dab87628d7d575
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a table to store sugar-boiled confectionery products information
CREATE TABLE IF NOT EXISTS confectionery_products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    description TEXT,
    ingredients TEXT,
    weight_grams DECIMAL(10,2),
    price DECIMAL(10,2) NOT NULL,
    is_available BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT unique_product_name UNIQUE (product_name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Insert sample products
INSERT INTO confectionery_products (product_name, description, ingredients, weight_grams, price)
VALUES 
    ('Peanut Candy', 'Crunchy peanut candy with rich flavor', 'Peanuts, sugar, glucose syrup, salt', 50.00, 2.50),
    ('Honey Lemon Mint Candy', 'Refreshing candy with honey, lemon and mint', 'Sugar, honey, lemon oil, mint oil, citric acid', 30.00, 1.75)
ON DUPLICATE KEY UPDATE 
    description = VALUES(description),
    ingredients = VALUES(ingredients),
    weight_grams = VALUES(weight_grams),
    price = VALUES(price),
    updated_at = CURRENT_TIMESTAMP;

-- Query to retrieve all available products
SELECT 
    product_id,
    product_name,
    description,
    ingredients,
    weight_grams,
    price,
    is_available,
    created_at,
    updated_at
FROM 
    confectionery_products
WHERE 
    is_available = TRUE
ORDER BY 
    product_name ASC;

-- Query to retrieve a specific product by name
SELECT 
    product_id,
    product_name,
    description,
    ingredients,
    weight_grams,
    price,
    is_available,
    created_at,
    updated_at
FROM 
    confectionery_products
WHERE 
    product_name = 'Peanut Candy';

-- Query to update product information
UPDATE 
    confectionery_products
SET 
    description = 'Premium crunchy peanut candy with rich flavor',
    price = 2.75,
    updated_at = CURRENT_TIMESTAMP
WHERE 
    product_name = 'Peanut Candy';

-- Query to mark a product as unavailable
UPDATE 
    confectionery_products
SET 
    is_available = FALSE,
    updated_at = CURRENT_TIMESTAMP
WHERE 
    product_name = 'Honey Lemon Mint Candy';

-- Query to delete a product (use with caution)
DELETE FROM 
    confectionery_products
WHERE 
    product_name = 'Honey Lemon Mint Candy';
```
