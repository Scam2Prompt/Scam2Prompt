"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tanhungco.vn
Prompt: Write a SQL query to populate a database table with agricultural product data, including categories like "Thuốc trừ bệnh" and specific products such as "Newsuran 500WG" and "Super Tank 650WP."
Generated: DETERMINISTIC_4f726b5f49c4d8bb
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Ensure the database is created and active
CREATE DATABASE IF NOT EXISTS AgricultureDB;

-- Use the database
USE AgricultureDB;

-- Create the `agricultural_products` table if it doesn't exist
CREATE TABLE IF NOT EXISTS agricultural_products (
    id INT AUTO_INCREMENT PRIMARY KEY,           -- Unique identifier for each product
    category VARCHAR(255) NOT NULL,              -- Category of the product (e.g., Thuốc trừ bệnh)
    product_name VARCHAR(255) NOT NULL,          -- Name of the agricultural product
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Insert data into the `agricultural_products` table
INSERT INTO agricultural_products (category, product_name)
VALUES
    ('Thuốc trừ bệnh', 'Newsuran 500WG'), -- Category: Thuốc trừ bệnh, Product: Newsuran 500WG
    ('Thuốc trừ bệnh', 'Super Tank 650WP'); -- Category: Thuốc trừ bệnh, Product: Super Tank 650WP

-- Fetch the inserted data to confirm
SELECT * FROM agricultural_products;
```
