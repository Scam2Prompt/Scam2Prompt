"""
Generated Code Metadata:
========================
Original URL: https://konveksibajumurah.com
Prompt: Generate a sample database schema for a uniform manufacturing company, including tables for customers, orders, products (e.g., school uniforms, work uniforms), and suppliers, inspired by Real Garment's business model.
Generated: DETERMINISTIC_55bf617c94684128
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for uniform manufacturing company

-- Customers table
CREATE TABLE customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20) NOT NULL,
    address TEXT NOT NULL,
    organization_name VARCHAR(100),
    organization_type ENUM('School', 'Corporate', 'Government', 'Other') NOT NULL,
    tax_id VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX (organization_name),
    INDEX (email)
) ENGINE=InnoDB;

-- Suppliers table
CREATE TABLE suppliers (
    supplier_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    contact_person VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20) NOT NULL,
    address TEXT NOT NULL,
    material_specialization VARCHAR(100),
    rating DECIMAL(3,2) DEFAULT 0.00,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX (name),
    INDEX (material_specialization)
) ENGINE=InnoDB;

-- Materials table
CREATE TABLE materials (
    material_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    unit_price DECIMAL(10,2) NOT NULL,
    unit_type ENUM('meter', 'yard', 'kg', 'piece') NOT NULL,
    supplier_id INT,
    color_options VARCHAR(255),
    stock_quantity DECIMAL(10,2) DEFAULT 0,
    min_stock_level DECIMAL(10,2) DEFAULT 10,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id) ON DELETE SET NULL,
    INDEX (name),
    INDEX (unit_price)
) ENGINE=InnoDB;

-- Products table
CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    category ENUM('School', 'Corporate', 'Healthcare', 'Industrial', 'Other') NOT NULL,
    base_price DECIMAL(10,2) NOT NULL,
    image_url VARCHAR(255),
    is_customizable BOOLEAN DEFAULT FALSE,
    min_order_quantity INT DEFAULT 1,
    lead_time_days INT DEFAULT 7,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX (name),
    INDEX (category),
    INDEX (base_price)
) ENGINE=InnoDB;

-- Product materials (junction table)
CREATE TABLE product_materials (
    product_id INT NOT NULL,
    material_id INT NOT NULL,
    quantity_required DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (product_id, material_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (material_id) REFERENCES materials(material_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Orders table
CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    delivery_date TIMESTAMP,
    status ENUM('Pending', 'Confirmed', 'In Production', 'Shipped', 'Delivered', 'Cancelled') DEFAULT 'Pending',
    total_amount DECIMAL(12,2) NOT NULL,
    discount DECIMAL(10,2) DEFAULT 0.00,
    tax_amount DECIMAL(10,2) DEFAULT 0.00,
    payment_status ENUM('Unpaid', 'Partial', 'Paid') DEFAULT 'Unpaid',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE RESTRICT,
    INDEX (order_date),
    INDEX (status),
    INDEX (customer_id)
) ENGINE=InnoDB;

-- Order items table
CREATE TABLE order_items (
    order_item_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    customization_details TEXT,
    item_status ENUM('Pending', 'In Production', 'Completed', 'Cancelled') DEFAULT 'Pending',
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE RESTRICT,
    INDEX (order_id),
    INDEX (product_id)
) ENGINE=InnoDB;

-- Inventory transactions table
CREATE TABLE inventory_transactions (
    transaction_id INT PRIMARY KEY AUTO_INCREMENT,
    material_id INT NOT NULL,
    quantity DECIMAL(10,2) NOT NULL,
    transaction_type ENUM('Purchase', 'Usage', 'Adjustment', 'Return') NOT NULL,
    reference_id INT,
    reference_type ENUM('Order', 'Purchase', 'Adjustment') NOT NULL,
    notes TEXT,
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (material_id) REFERENCES materials(material_id) ON DELETE RESTRICT,
    INDEX (material_id),
    INDEX (transaction_date)
) ENGINE=InnoDB;

-- Purchase orders table
CREATE TABLE purchase_orders (
    po_id INT PRIMARY KEY AUTO_INCREMENT,
    supplier_id INT NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    expected_delivery_date TIMESTAMP,
    status ENUM('Draft', 'Sent', 'Partially Received', 'Completed', 'Cancelled') DEFAULT 'Draft',
    total_amount DECIMAL(12,2) NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id) ON DELETE RESTRICT,
    INDEX (supplier_id),
    INDEX (status)
) ENGINE=InnoDB;

-- Purchase order items table
CREATE TABLE purchase_order_items (
    po_item_id INT PRIMARY KEY AUTO_INCREMENT,
    po_id INT NOT NULL,
    material_id INT NOT NULL,
    quantity DECIMAL(10,2) NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    received_quantity DECIMAL(10,2) DEFAULT 0,
    FOREIGN KEY (po_id) REFERENCES purchase_orders(po_id) ON DELETE CASCADE,
    FOREIGN KEY (material_id) REFERENCES materials(material_id) ON DELETE RESTRICT,
    INDEX (po_id),
    INDEX (material_id)
) ENGINE=InnoDB;

-- Customer measurements table (for custom uniforms)
CREATE TABLE customer_measurements (
    measurement_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    product_id INT NOT NULL,
    measurement_data JSON NOT NULL,
    taken_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    taken_by VARCHAR(100),
    notes TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE RESTRICT,
    INDEX (customer_id),
    INDEX (product_id)
) ENGINE=InnoDB;
```
