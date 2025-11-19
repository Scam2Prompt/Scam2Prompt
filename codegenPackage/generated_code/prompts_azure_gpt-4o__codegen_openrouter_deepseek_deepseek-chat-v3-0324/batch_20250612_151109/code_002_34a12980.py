"""
Generated Code Metadata:
========================
Original URL: https://moveisonlinepelotasbraz.blogspot.com
Prompt: Create a database schema in SQL to store furniture product information from "moveisonlinepelotasbraz," including columns for product name, price range, category (e.g., "Sala," "Quarto"), and availability.
Generated: DETERMINISTIC_34a129806760b415
Batch ID: 20250612_151109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for furniture products from moveisonlinepelotasbraz
CREATE TABLE categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    description TEXT,
    min_price DECIMAL(10, 2),
    max_price DECIMAL(10, 2),
    category_id INT NOT NULL,
    is_available BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE CASCADE
);

-- Insert common furniture categories
INSERT INTO categories (category_name, description) VALUES
    ('Sala', 'Móveis para sala de estar'),
    ('Quarto', 'Móveis para quarto'),
    ('Cozinha', 'Móveis para cozinha'),
    ('Escritório', 'Móveis para escritório'),
    ('Jardim', 'Móveis para área externa');

-- Create index for better query performance
CREATE INDEX idx_product_name ON products(product_name);
CREATE INDEX idx_product_category ON products(category_id);
CREATE INDEX idx_product_availability ON products(is_available);
```
