"""
Generated Code Metadata:
========================
Original URL: https://cedarinternational.ca
Prompt: Create a database schema for managing procurement data, including categories like safety items, studs, bolts, and compressors, based on Cedar International Inc.'s offerings.
Generated: DETERMINISTIC_76033d9bde0102d5
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Cedar International Inc. procurement management

-- Create the database
CREATE DATABASE IF NOT EXISTS cedar_procurement;
USE cedar_procurement;

-- Create suppliers table
CREATE TABLE IF NOT EXISTS suppliers (
    supplier_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    contact_person VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    address TEXT,
    tax_id VARCHAR(50),
    payment_terms VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX (name),
    INDEX (email)
) ENGINE=InnoDB;

-- Create product categories table
CREATE TABLE IF NOT EXISTS categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Create products table
CREATE TABLE IF NOT EXISTS products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    category_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    unit_of_measure VARCHAR(20) NOT NULL,
    specifications TEXT,
    min_stock_level INT DEFAULT 0,
    lead_time_days INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE RESTRICT,
    INDEX (name),
    INDEX (category_id)
) ENGINE=InnoDB;

-- Create inventory table
CREATE TABLE IF NOT EXISTS inventory (
    inventory_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    quantity_on_hand INT NOT NULL DEFAULT 0,
    quantity_reserved INT NOT NULL DEFAULT 0,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    INDEX (product_id)
) ENGINE=InnoDB;

-- Create supplier_products table (many-to-many relationship)
CREATE TABLE IF NOT EXISTS supplier_products (
    supplier_product_id INT AUTO_INCREMENT PRIMARY KEY,
    supplier_id INT NOT NULL,
    product_id INT NOT NULL,
    supplier_product_code VARCHAR(50),
    unit_price DECIMAL(10, 2) NOT NULL,
    currency VARCHAR(3) DEFAULT 'USD',
    min_order_quantity INT DEFAULT 1,
    lead_time_days INT,
    is_active BOOLEAN DEFAULT TRUE,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    UNIQUE KEY (supplier_id, product_id),
    INDEX (supplier_id),
    INDEX (product_id)
) ENGINE=InnoDB;

-- Create purchase_orders table
CREATE TABLE IF NOT EXISTS purchase_orders (
    po_id INT AUTO_INCREMENT PRIMARY KEY,
    po_number VARCHAR(20) NOT NULL UNIQUE,
    supplier_id INT NOT NULL,
    order_date DATE NOT NULL,
    expected_delivery_date DATE,
    status ENUM('draft', 'sent', 'partially_received', 'completed', 'cancelled') DEFAULT 'draft',
    total_amount DECIMAL(12, 2) NOT NULL,
    currency VARCHAR(3) DEFAULT 'USD',
    notes TEXT,
    created_by VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id) ON DELETE RESTRICT,
    INDEX (po_number),
    INDEX (supplier_id),
    INDEX (status)
) ENGINE=InnoDB;

-- Create purchase_order_items table
CREATE TABLE IF NOT EXISTS purchase_order_items (
    po_item_id INT AUTO_INCREMENT PRIMARY KEY,
    po_id INT NOT NULL,
    product_id INT NOT NULL,
    supplier_product_id INT NOT NULL,
    quantity INT NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    total_price DECIMAL(10, 2) NOT NULL,
    received_quantity INT DEFAULT 0,
    status ENUM('pending', 'partially_received', 'completed') DEFAULT 'pending',
    FOREIGN KEY (po_id) REFERENCES purchase_orders(po_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE RESTRICT,
    FOREIGN KEY (supplier_product_id) REFERENCES supplier_products(supplier_product_id) ON DELETE RESTRICT,
    INDEX (po_id),
    INDEX (product_id)
) ENGINE=InnoDB;

-- Create goods_receipts table
CREATE TABLE IF NOT EXISTS goods_receipts (
    receipt_id INT AUTO_INCREMENT PRIMARY KEY,
    po_id INT NOT NULL,
    receipt_date DATE NOT NULL,
    received_by VARCHAR(50) NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (po_id) REFERENCES purchase_orders(po_id) ON DELETE RESTRICT,
    INDEX (po_id)
) ENGINE=InnoDB;

-- Create goods_receipt_items table
CREATE TABLE IF NOT EXISTS goods_receipt_items (
    receipt_item_id INT AUTO_INCREMENT PRIMARY KEY,
    receipt_id INT NOT NULL,
    po_item_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity_received INT NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    batch_number VARCHAR(50),
    expiry_date DATE,
    condition_notes TEXT,
    FOREIGN KEY (receipt_id) REFERENCES goods_receipts(receipt_id) ON DELETE CASCADE,
    FOREIGN KEY (po_item_id) REFERENCES purchase_order_items(po_item_id) ON DELETE RESTRICT,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE RESTRICT,
    INDEX (receipt_id),
    INDEX (po_item_id)
) ENGINE=InnoDB;

-- Create initial categories (based on Cedar International Inc.'s offerings)
INSERT IGNORE INTO categories (name, description) VALUES
    ('Safety Items', 'Personal protective equipment and safety gear'),
    ('Studs', 'Various types of threaded studs and rods'),
    ('Bolts', 'Different bolt types including hex bolts, anchor bolts, etc.'),
    ('Compressors', 'Air compressors and related equipment'),
    ('Fasteners', 'Nuts, washers, and other fastening components'),
    ('Tools', 'Hand tools and power tools'),
    ('Pipes & Fittings', 'Pipes, valves, and fittings'),
    ('Electrical', 'Electrical components and wiring');
```
