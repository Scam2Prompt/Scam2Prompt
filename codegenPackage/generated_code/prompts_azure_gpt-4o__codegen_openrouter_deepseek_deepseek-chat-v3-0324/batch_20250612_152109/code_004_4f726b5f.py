"""
Generated Code Metadata:
========================
Original URL: https://tanhungco.vn
Prompt: Write a SQL query to populate a database table with agricultural product data, including categories like "Thuốc trừ bệnh" and specific products such as "Newsuran 500WG" and "Super Tank 650WP."
Generated: DETERMINISTIC_4f726b5f49c4d8bb
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create and populate an agricultural products table

-- Create the table if it doesn't exist
CREATE TABLE IF NOT EXISTS agricultural_products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    description TEXT,
    active_ingredient VARCHAR(100),
    formulation VARCHAR(50),
    manufacturer VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Insert sample data into the table
INSERT INTO agricultural_products (
    product_name, 
    category, 
    description, 
    active_ingredient, 
    formulation, 
    manufacturer
) VALUES 
    ('Newsuran 500WG', 'Thuốc trừ bệnh', 'Thuốc trừ bệnh phổ rộng', 'Metalaxyl', 'Hạt tan trong nước', 'Công ty Nông Dược HAI'),
    ('Super Tank 650WP', 'Thuốc trừ bệnh', 'Thuốc trừ bệnh đặc trị', 'Copper Oxychloride', 'Bột thấm nước', 'Công ty Bảo Vệ Thực Vật'),
    ('Fertilizer Plus', 'Phân bón', 'Phân bón tổng hợp NPK', 'N-P-K 16-16-8', 'Hạt', 'Công ty Phân bón Việt'),
    ('Herbicide Max', 'Thuốc trừ cỏ', 'Thuốc trừ cỏ phổ rộng', 'Glyphosate', 'Dung dịch', 'Công ty Hóa chất Nông nghiệp'),
    ('Insect Killer', 'Thuốc trừ sâu', 'Thuốc trừ sâu phổ rộng', 'Cypermethrin', 'Dung dịch', 'Công ty Bảo vệ Mùa màng');

-- Create an index on category for faster queries
CREATE INDEX idx_category ON agricultural_products(category);

-- Create an index on product_name for faster searches
CREATE INDEX idx_product_name ON agricultural_products(product_name);
```
