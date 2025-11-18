"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://frigoterm.ro
Prompt: Provide an example of a database schema for managing product categories (e.g., residential systems, commercial systems, accessories) and promotions, as seen on Frigoterm.ro.
Generated: DETERMINISTIC_8f5e41b2e40e0af8
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing product categories and promotions

-- Drop existing tables if they exist (for re-creation during development)
DROP TABLE IF EXISTS promotions;
DROP TABLE IF EXISTS categories;

-- Table for product categories
CREATE TABLE categories (
    category_id SERIAL PRIMARY KEY,          -- Unique identifier for each category
    category_name VARCHAR(255) NOT NULL,    -- Name of the category (e.g., Residential Systems)
    description TEXT,                        -- Optional description for the category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table for managing promotions
CREATE TABLE promotions (
    promotion_id SERIAL PRIMARY KEY,         -- Unique identifier for each promotion
    promotion_name VARCHAR(255) NOT NULL,   -- Name of the promotion
    discount_percentage DECIMAL(5, 2) CHECK (discount_percentage >= 0 AND discount_percentage <= 100), -- Discount percentage must be between 0 and 100
    start_date DATE NOT NULL,                -- Start date of the promotion
    end_date DATE NOT NULL,                  -- End date of the promotion
    category_id INT REFERENCES categories(category_id) ON DELETE CASCADE, -- Foreign key linking to categories
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the promotion was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Sample data insertion for categories
INSERT INTO categories (category_name, description) VALUES 
('Residential Systems', 'Products designed for home use'),
('Commercial Systems', 'Products designed for business use'),
('Accessories', 'Additional products and components');

-- Sample data insertion for promotions
INSERT INTO promotions (promotion_name, discount_percentage, start_date, end_date, category_id) VALUES 
('Summer Sale', 20.00, '2023-06-01', '2023-08-31', 1),  -- Promotion for Residential Systems
('Business Boost', 15.00, '2023-07-01', '2023-09-30', 2); -- Promotion for Commercial Systems

-- Query to get categories with their promotions
SELECT c.category_id, c.category_name, p.promotion_name, p.discount_percentage
FROM categories c
LEFT JOIN promotions p ON c.category_id = p.category_id
ORDER BY c.category_id;
```
