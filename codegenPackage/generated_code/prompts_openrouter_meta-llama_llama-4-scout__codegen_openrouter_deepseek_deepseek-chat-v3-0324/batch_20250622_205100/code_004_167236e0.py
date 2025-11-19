"""
Generated Code Metadata:
========================
Original URL: https://missguilty.co.uk
Prompt: "Create a SQL database schema for storing product information for an online fashion store like Miss Guilty's, including tables for products, prices, and inventory."
Generated: DETERMINISTIC_167236e0b97c47c2
Batch ID: 20250622_205100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for Miss Guilty's Fashion Store Database

-- Products table stores core product information
CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    brand VARCHAR(50) NOT NULL,
    category VARCHAR(50) NOT NULL,
    subcategory VARCHAR(50),
    gender ENUM('Men', 'Women', 'Unisex', 'Kids') NOT NULL,
    material VARCHAR(100),
    care_instructions TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE,
    CONSTRAINT chk_category CHECK (category IN ('Clothing', 'Shoes', 'Accessories', 'Bags', 'Jewelry'))
);

-- Product variants table (e.g., different colors/sizes of the same product)
CREATE TABLE product_variants (
    variant_id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT NOT NULL,
    color VARCHAR(50) NOT NULL,
    size VARCHAR(20) NOT NULL,
    sku VARCHAR(50) UNIQUE NOT NULL,
    barcode VARCHAR(50) UNIQUE,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    INDEX idx_product_id (product_id)
);

-- Prices table with pricing information
CREATE TABLE prices (
    price_id INT PRIMARY KEY AUTO_INCREMENT,
    variant_id INT NOT NULL,
    base_price DECIMAL(10,2) NOT NULL,
    sale_price DECIMAL(10,2),
    currency VARCHAR(3) DEFAULT 'USD',
    price_valid_from TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    price_valid_to TIMESTAMP NULL,
    FOREIGN KEY (variant_id) REFERENCES product_variants(variant_id) ON DELETE CASCADE,
    CONSTRAINT chk_price CHECK (base_price > 0),
    CONSTRAINT chk_sale_price CHECK (sale_price IS NULL OR sale_price < base_price),
    INDEX idx_variant_id (variant_id)
);

-- Inventory table tracking stock levels
CREATE TABLE inventory (
    inventory_id INT PRIMARY KEY AUTO_INCREMENT,
    variant_id INT NOT NULL,
    quantity_in_stock INT NOT NULL DEFAULT 0,
    quantity_reserved INT NOT NULL DEFAULT 0,
    last_stock_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    low_stock_threshold INT DEFAULT 5,
    FOREIGN KEY (variant_id) REFERENCES product_variants(variant_id) ON DELETE CASCADE,
    CONSTRAINT chk_quantity CHECK (quantity_in_stock >= 0 AND quantity_reserved >= 0),
    INDEX idx_variant_id (variant_id)
);

-- Product images table
CREATE TABLE product_images (
    image_id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT NOT NULL,
    variant_id INT,
    image_url VARCHAR(255) NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    display_order INT DEFAULT 0,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (variant_id) REFERENCES product_variants(variant_id) ON DELETE SET NULL,
    INDEX idx_product_id (product_id),
    INDEX idx_variant_id (variant_id)
);

-- Product tags for categorization and search
CREATE TABLE tags (
    tag_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) UNIQUE NOT NULL,
    description TEXT
);

-- Junction table for product-tag many-to-many relationship
CREATE TABLE product_tags (
    product_id INT NOT NULL,
    tag_id INT NOT NULL,
    PRIMARY KEY (product_id, tag_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (tag_id) REFERENCES tags(tag_id) ON DELETE CASCADE
);
```
