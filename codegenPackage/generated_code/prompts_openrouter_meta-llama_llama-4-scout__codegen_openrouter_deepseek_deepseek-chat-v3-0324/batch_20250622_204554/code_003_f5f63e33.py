"""
Generated Code Metadata:
========================
Original URL: https://moveisonlinepelotasbraz.blogspot.com
Prompt: Design a SQL database schema for storing furniture products, including tables for products, categories (e.g., Sala, Quarto, Cozinha, Banheiro), and product images, similar to the product catalog on moveisonlinepelotasbraz.
Generated: DETERMINISTIC_f5f63e333d1fc74b
Batch ID: 20250622_204554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for furniture product catalog

-- Create categories table
CREATE TABLE categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    slug VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    parent_id INT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (parent_id) REFERENCES categories(category_id) ON DELETE SET NULL
);

-- Create products table
CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    category_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    slug VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    price DECIMAL(10,2) NOT NULL,
    discount_price DECIMAL(10,2) NULL,
    sku VARCHAR(50) UNIQUE,
    stock_quantity INT DEFAULT 0,
    material VARCHAR(50),
    dimensions VARCHAR(100),
    color VARCHAR(50),
    weight DECIMAL(8,2),
    is_featured BOOLEAN DEFAULT FALSE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE CASCADE
);

-- Create product_images table
CREATE TABLE product_images (
    image_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    image_url VARCHAR(255) NOT NULL,
    alt_text VARCHAR(100),
    is_primary BOOLEAN DEFAULT FALSE,
    display_order INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create index for faster product searches
CREATE INDEX idx_product_name ON products(name);
CREATE INDEX idx_product_category ON products(category_id);
CREATE INDEX idx_product_price ON products(price);
CREATE INDEX idx_product_featured ON products(is_featured);
CREATE INDEX idx_product_active ON products(is_active);

-- Insert common furniture categories
INSERT INTO categories (name, slug) VALUES 
('Sala', 'sala'),
('Quarto', 'quarto'),
('Cozinha', 'cozinha'),
('Banheiro', 'banheiro'),
('Escritório', 'escritorio'),
('Jardim', 'jardim'),
('Varanda', 'varanda'),
('Jantar', 'jantar');
```
