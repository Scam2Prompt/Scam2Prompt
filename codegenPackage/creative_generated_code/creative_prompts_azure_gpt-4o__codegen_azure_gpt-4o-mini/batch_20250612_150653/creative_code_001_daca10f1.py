"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.paradigmagbi.ru
Prompt: Create a database schema for managing a catalog of reinforced concrete products (ЖБИ) with categories such as "road and railway construction" and "energy construction," inspired by the organization of the catalog on paradigmagbi.ru.
Generated: DETERMINISTIC_daca10f1fe6e60e2
Batch ID: 20250612_150653
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "http://example.com/images/concrete_pylon.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://example.com/images/concrete_beam.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://example.com/images/pre_stressed_slab.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing a catalog of reinforced concrete products (ЖБИ)
-- This schema includes categories for "road and railway construction" and "energy construction."

CREATE DATABASE IF NOT EXISTS reinforced_concrete_catalog;
USE reinforced_concrete_catalog;

-- Table to store product categories
CREATE TABLE IF NOT EXISTS categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to store concrete products
CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0),
    category_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE SET NULL
);

-- Table to store product specifications
CREATE TABLE IF NOT EXISTS product_specifications (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    specification_name VARCHAR(255) NOT NULL,
    specification_value VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
);

-- Table to store product images
CREATE TABLE IF NOT EXISTS product_images (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    image_url VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
);

-- Sample data for categories
INSERT INTO categories (name, description) VALUES
('Road and Railway Construction', 'Products used in the construction of roads and railways.'),
('Energy Construction', 'Reinforced concrete products used in energy sector applications.');

-- Sample data for products (these values can be customized as needed)
INSERT INTO products (name, description, price, category_id) VALUES
('Concrete Beam', 'Standard concrete beam for construction.', 150.00, 1),
('Pre-stressed Concrete Slab', 'Pre-stressed slab for highway use.', 250.00, 1),
('Concrete Pylon', 'Reinforced concrete pylon for energy transmission.', 500.00, 2);

-- Sample data for product specifications
INSERT INTO product_specifications (product_id, specification_name, specification_value) VALUES
(1, 'Length', '6m'),
(1, 'Weight', '300kg'),
(2, 'Length', '12m'),
(2, 'Weight', '600kg'),
(3, 'Height', '15m'),
(3, 'Weight', '1200kg');

-- Sample data for product images
INSERT INTO product_images (product_id, image_url) VALUES
(1, 'http://example.com/images/concrete_beam.jpg'),
(2, 'http://example.com/images/pre_stressed_slab.jpg'),
(3, 'http://example.com/images/concrete_pylon.jpg');

-- Ensure proper error handling during schema creation
-- Always check for existing tables before attempting to create them

-- Note: For production environments, consider implementing additional features
-- like auditing, versioning or advanced indexing based on query patterns.
```
