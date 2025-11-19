"""
Generated Code Metadata:
========================
Original URL: https://moveisonlinepelotasbraz.blogspot.com
Prompt: Design a SQL database schema for storing furniture products, including tables for products, categories (e.g., Sala, Quarto, Cozinha, Banheiro), and product images, similar to the product catalog on moveisonlinepelotasbraz.
Generated: DETERMINISTIC_f5f63e333d1fc74b
Batch ID: 20250622_204554
URLs Found: 5
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/cama.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/mesa.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/sofa.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/pia.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/sofa2.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```sql
-- Create database schema for furniture products
CREATE DATABASE furniture_catalog;

-- Use the database schema
USE furniture_catalog;

-- Create table for product categories
CREATE TABLE categories (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY (name)
);

-- Create table for products
CREATE TABLE products (
  id INT AUTO_INCREMENT,
  category_id INT NOT NULL,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  stock_quantity INT NOT NULL DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
);

-- Create table for product images
CREATE TABLE product_images (
  id INT AUTO_INCREMENT,
  product_id INT NOT NULL,
  image_url VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
);

-- Create index on category_id in products table
CREATE INDEX idx_category_id ON products (category_id);

-- Create index on product_id in product_images table
CREATE INDEX idx_product_id ON product_images (product_id);

-- Example data for categories
INSERT INTO categories (name, description) 
VALUES 
('Sala', 'Produtos para sala de estar'),
('Quarto', 'Produtos para quarto'),
('Cozinha', 'Produtos para cozinha'),
('Banheiro', 'Produtos para banheiro');

-- Example data for products
INSERT INTO products (category_id, name, description, price, stock_quantity) 
VALUES 
(1, 'Sofa', 'Sofa de 3 lugares', 999.99, 10),
(2, 'Cama', 'Cama de casal', 599.99, 5),
(3, 'Mesa', 'Mesa de jantar', 299.99, 8),
(4, 'Pia', 'Pia de banheiro', 199.99, 12);

-- Example data for product images
INSERT INTO product_images (product_id, image_url) 
VALUES 
(1, 'https://example.com/sofa.jpg'),
(1, 'https://example.com/sofa2.jpg'),
(2, 'https://example.com/cama.jpg'),
(3, 'https://example.com/mesa.jpg'),
(4, 'https://example.com/pia.jpg');
```
