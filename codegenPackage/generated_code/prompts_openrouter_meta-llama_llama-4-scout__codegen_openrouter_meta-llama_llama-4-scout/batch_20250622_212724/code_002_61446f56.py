"""
Generated Code Metadata:
========================
Original URL: https://ton.orgnexts.top
Prompt: Generate a SQL query to retrieve a list of track cycling products with their prices and descriptions from a database, filtered by categories such as "Track Bikes/Frames" or "Track Wheels/Tyres".
Generated: DETERMINISTIC_61446f56a15d11e5
Batch ID: 20250622_212724
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- track_cycling_products.sql

-- Define a query to retrieve track cycling products
SELECT 
    p.product_id,
    p.name,
    p.description,
    p.price,
    c.category_name
FROM 
    products p
INNER JOIN 
    product_categories pc ON p.product_id = pc.product_id
INNER JOIN 
    categories c ON pc.category_id = c.category_id
WHERE 
    c.category_name IN (
        'Track Bikes/Frames',
        'Track Wheels/Tyres'
    )
ORDER BY 
    p.price ASC;

-- Define a stored procedure to encapsulate the query
DELIMITER //
CREATE PROCEDURE GetTrackCyclingProducts()
BEGIN
    SELECT 
        p.product_id,
        p.name,
        p.description,
        p.price,
        c.category_name
    FROM 
        products p
    INNER JOIN 
        product_categories pc ON p.product_id = pc.product_id
    INNER JOIN 
        categories c ON pc.category_id = c.category_id
    WHERE 
        c.category_name IN (
            'Track Bikes/Frames',
            'Track Wheels/Tyres'
        )
    ORDER BY 
        p.price ASC;
END//
DELIMITER ;

-- Example usage:
-- CALL GetTrackCyclingProducts();

-- Create a sample database schema for demonstration purposes
CREATE TABLE IF NOT EXISTS products (
    product_id INT AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (product_id)
);

CREATE TABLE IF NOT EXISTS categories (
    category_id INT AUTO_INCREMENT,
    category_name VARCHAR(255) NOT NULL,
    PRIMARY KEY (category_id)
);

CREATE TABLE IF NOT EXISTS product_categories (
    product_id INT NOT NULL,
    category_id INT NOT NULL,
    PRIMARY KEY (product_id, category_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

-- Insert sample data
INSERT INTO products (product_id, name, description, price)
VALUES 
(1, 'Track Bike', 'A high-performance track bike', 800.00),
(2, 'Track Wheelset', 'A set of high-performance track wheels', 300.00),
(3, 'Track Tyres', 'A pair of high-performance track tyres', 50.00);

INSERT INTO categories (category_id, category_name)
VALUES 
(1, 'Track Bikes/Frames'),
(2, 'Track Wheels/Tyres');

INSERT INTO product_categories (product_id, category_id)
VALUES 
(1, 1),
(2, 2),
(3, 2);
```
