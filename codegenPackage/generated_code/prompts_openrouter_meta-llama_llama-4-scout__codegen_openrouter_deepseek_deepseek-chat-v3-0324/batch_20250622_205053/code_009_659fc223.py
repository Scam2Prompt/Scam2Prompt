"""
Generated Code Metadata:
========================
Original URL: https://www.tiktokshopvn.com.vn
Prompt: Write a SQL query to manage product inventory and orders for an e-commerce platform like TikTok Shop VN, considering factors like product variants, prices, and shipping costs.
Generated: DETERMINISTIC_659fc2235bbd3a33
Batch ID: 20250622_205053
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# SQL Schema for E-commerce Platform Inventory and Orders Management

```sql
-- Database schema for TikTok Shop VN like e-commerce platform
-- Includes tables for products, variants, inventory, orders, and shipping

-- Products table
CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    category_id INT NOT NULL,
    brand_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (category_id) REFERENCES categories(category_id),
    FOREIGN KEY (brand_id) REFERENCES brands(brand_id)
) ENGINE=InnoDB;

-- Product variants table (for different sizes, colors, etc.)
CREATE TABLE product_variants (
    variant_id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT NOT NULL,
    sku VARCHAR(50) UNIQUE NOT NULL,
    variant_name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL CHECK (price > 0),
    sale_price DECIMAL(10, 2),
    weight DECIMAL(10, 2) COMMENT 'in grams',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    INDEX idx_product_id (product_id),
    INDEX idx_sku (sku)
) ENGINE=InnoDB;

-- Inventory tracking
CREATE TABLE inventory (
    inventory_id INT PRIMARY KEY AUTO_INCREMENT,
    variant_id INT NOT NULL,
    quantity INT NOT NULL DEFAULT 0 CHECK (quantity >= 0),
    low_stock_threshold INT DEFAULT 5,
    last_restocked_at TIMESTAMP NULL,
    FOREIGN KEY (variant_id) REFERENCES product_variants(variant_id) ON DELETE CASCADE,
    INDEX idx_variant_id (variant_id)
) ENGINE=InnoDB;

-- Customers table
CREATE TABLE customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_email (email)
) ENGINE=InnoDB;

-- Orders table
CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status ENUM('pending', 'processing', 'shipped', 'delivered', 'cancelled', 'refunded') DEFAULT 'pending',
    total_amount DECIMAL(12, 2) NOT NULL,
    shipping_cost DECIMAL(10, 2) NOT NULL,
    tax_amount DECIMAL(10, 2) NOT NULL,
    payment_method VARCHAR(50),
    shipping_address TEXT NOT NULL,
    billing_address TEXT,
    notes TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    INDEX idx_customer_id (customer_id),
    INDEX idx_order_date (order_date),
    INDEX idx_status (status)
) ENGINE=InnoDB;

-- Order items table
CREATE TABLE order_items (
    order_item_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT NOT NULL,
    variant_id INT NOT NULL,
    quantity INT NOT NULL CHECK (quantity > 0),
    unit_price DECIMAL(10, 2) NOT NULL,
    discount_amount DECIMAL(10, 2) DEFAULT 0,
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (variant_id) REFERENCES product_variants(variant_id),
    INDEX idx_order_id (order_id),
    INDEX idx_variant_id (variant_id)
) ENGINE=InnoDB;

-- Shipping methods table
CREATE TABLE shipping_methods (
    shipping_method_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    base_cost DECIMAL(10, 2) NOT NULL,
    cost_per_kg DECIMAL(10, 2) DEFAULT 0,
    estimated_delivery_days INT,
    is_active BOOLEAN DEFAULT TRUE
) ENGINE=InnoDB;

-- Order shipping details
CREATE TABLE order_shipping (
    order_shipping_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT NOT NULL,
    shipping_method_id INT NOT NULL,
    tracking_number VARCHAR(100),
    shipped_at TIMESTAMP NULL,
    delivered_at TIMESTAMP NULL,
    estimated_delivery_date DATE,
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (shipping_method_id) REFERENCES shipping_methods(shipping_method_id),
    INDEX idx_order_id (order_id),
    INDEX idx_tracking_number (tracking_number)
) ENGINE=InnoDB;

-- Inventory transaction log
CREATE TABLE inventory_transactions (
    transaction_id INT PRIMARY KEY AUTO_INCREMENT,
    variant_id INT NOT NULL,
    quantity_change INT NOT NULL COMMENT 'Positive for addition, negative for deduction',
    transaction_type ENUM('purchase', 'sale', 'return', 'adjustment', 'damage') NOT NULL,
    reference_id INT COMMENT 'order_id or other reference',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_by INT COMMENT 'user_id who performed the action',
    FOREIGN KEY (variant_id) REFERENCES product_variants(variant_id),
    INDEX idx_variant_id (variant_id),
    INDEX idx_created_at (created_at)
) ENGINE=InnoDB;

-- Stored procedure to update inventory when order is placed
DELIMITER //
CREATE PROCEDURE process_order_inventory(
    IN p_order_id INT,
    OUT p_success BOOLEAN,
    OUT p_message VARCHAR(255)
)
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE v_variant_id INT;
    DECLARE v_quantity INT;
    DECLARE v_current_stock INT;
    DECLARE v_order_status VARCHAR(20);
    
    DECLARE cur CURSOR FOR 
        SELECT variant_id, quantity 
        FROM order_items 
        WHERE order_id = p_order_id;
    
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
    
    -- Check order status
    SELECT status INTO v_order_status FROM orders WHERE order_id = p_order_id;
    
    IF v_order_status != 'pending' THEN
        SET p_success = FALSE;
        SET p_message = 'Order is not in pending status';
        LEAVE PROCEDURE;
    END IF;
    
    -- Start transaction
    START TRANSACTION;
    
    -- Open cursor for order items
    OPEN cur;
    
    inventory_loop: LOOP
        FETCH cur INTO v_variant_id, v_quantity;
        IF done THEN
            LEAVE inventory_loop;
        END IF;
        
        -- Check current inventory
        SELECT quantity INTO v_current_stock 
        FROM inventory 
        WHERE variant_id = v_variant_id 
        FOR UPDATE;
        
        IF v_current_stock < v_quantity THEN
            SET p_success = FALSE;
            SET p_message = CONCAT('Insufficient stock for variant ID: ', v_variant_id);
            ROLLBACK;
            LEAVE PROCEDURE;
        END IF;
        
        -- Update inventory
        UPDATE inventory 
        SET quantity = quantity - v_quantity 
        WHERE variant_id = v_variant_id;
        
        -- Log transaction
        INSERT INTO inventory_transactions 
        (variant_id, quantity_change, transaction_type, reference_id, notes)
        VALUES 
        (v_variant_id, -v_quantity, 'sale', p_order_id, 'Order processed');
    END LOOP;
    
    CLOSE cur;
    
    -- Update order status
    UPDATE orders SET status = 'processing' WHERE order_id = p_order_id;
    
    SET p_success = TRUE;
    SET p_message = 'Inventory updated successfully';
    
    COMMIT;
END //
DELIMITER ;

-- View for low stock alert
CREATE VIEW low_stock_products AS
SELECT 
    p.product_id,
    p.name AS product_name,
    pv.variant_id,
    pv.variant_name,
    pv.sku,
    i.quantity,
    i.low_stock_threshold
FROM 
    products p
JOIN 
    product_variants pv ON p.product_id = pv.product_id
JOIN 
    inventory i ON pv.variant_id = i.variant_id
WHERE 
    i.quantity <= i.low_stock_threshold
    AND p.is_active = TRUE;
```
