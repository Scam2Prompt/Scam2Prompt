"""
Generated Code Metadata:
========================
Original URL: https://eferroeacobrza.blogspot.com
Prompt: "Write a SQL query to manage orders and customers for a company that distributes iron and steel products, including services like dobradeira de calhas and guilhotina."
Generated: DETERMINISTIC_0f515401711c6c8a
Batch ID: 20250622_204617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for Iron and Steel Products Distribution Company

-- Create Customers table
CREATE TABLE Customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    address TEXT,
    tax_id VARCHAR(20) UNIQUE,
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    active BOOLEAN DEFAULT TRUE
);

-- Create Products table
CREATE TABLE Products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    category ENUM('iron', 'steel', 'service') NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    stock_quantity INT DEFAULT 0,
    service_type VARCHAR(50),
    CHECK (
        (category = 'service' AND service_type IS NOT NULL) OR 
        (category != 'service' AND service_type IS NULL)
    )
);

-- Create Orders table
CREATE TABLE Orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    order_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    status ENUM('pending', 'processing', 'shipped', 'delivered', 'cancelled') DEFAULT 'pending',
    total_amount DECIMAL(12, 2) NOT NULL,
    payment_method ENUM('cash', 'credit', 'debit', 'transfer', 'check'),
    notes TEXT,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE RESTRICT
);

-- Create Order_Items table
CREATE TABLE Order_Items (
    order_item_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL CHECK (quantity > 0),
    unit_price DECIMAL(10, 2) NOT NULL,
    discount DECIMAL(5, 2) DEFAULT 0.00,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES Products(product_id) ON DELETE RESTRICT
);

-- Create Services table (for services like dobradeira de calhas and guilhotina)
CREATE TABLE Services (
    service_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT NOT NULL,
    service_type VARCHAR(50) NOT NULL,
    description TEXT,
    completion_date DATETIME,
    technician VARCHAR(100),
    status ENUM('scheduled', 'in_progress', 'completed', 'cancelled') DEFAULT 'scheduled',
    FOREIGN KEY (order_id) REFERENCES Orders(order_id) ON DELETE CASCADE
);

-- Insert sample services into Products table
INSERT INTO Products (name, description, category, unit_price, service_type)
VALUES 
    ('Dobradeira de Calhas', 'Professional gutter bending service', 'service', 150.00, 'gutter_bending'),
    ('Guilhotina', 'Precision cutting service', 'service', 200.00, 'cutting');

-- Query to get all orders with customer details
CREATE VIEW Order_Details AS
SELECT 
    o.order_id,
    c.name AS customer_name,
    c.email AS customer_email,
    o.order_date,
    o.status,
    o.total_amount,
    COUNT(oi.order_item_id) AS item_count
FROM 
    Orders o
JOIN 
    Customers c ON o.customer_id = c.customer_id
LEFT JOIN 
    Order_Items oi ON o.order_id = oi.order_id
GROUP BY 
    o.order_id;

-- Query to get order items with product details
CREATE VIEW Order_Items_Details AS
SELECT 
    oi.order_item_id,
    oi.order_id,
    p.name AS product_name,
    p.category,
    oi.quantity,
    oi.unit_price,
    oi.discount,
    (oi.quantity * oi.unit_price * (1 - oi.discount/100)) AS item_total
FROM 
    Order_Items oi
JOIN 
    Products p ON oi.product_id = p.product_id;

-- Stored procedure to create a new order
DELIMITER //
CREATE PROCEDURE CreateOrder(
    IN p_customer_id INT,
    IN p_payment_method VARCHAR(20),
    IN p_notes TEXT
)
BEGIN
    DECLARE v_order_id INT;
    
    INSERT INTO Orders (customer_id, payment_method, notes, total_amount)
    VALUES (p_customer_id, p_payment_method, p_notes, 0);
    
    SET v_order_id = LAST_INSERT_ID();
    
    SELECT v_order_id AS new_order_id;
END //
DELIMITER ;

-- Stored procedure to add item to order
DELIMITER //
CREATE PROCEDURE AddOrderItem(
    IN p_order_id INT,
    IN p_product_id INT,
    IN p_quantity INT,
    IN p_discount DECIMAL(5, 2)
)
BEGIN
    DECLARE v_unit_price DECIMAL(10, 2);
    DECLARE v_category VARCHAR(20);
    
    -- Get product details
    SELECT unit_price, category INTO v_unit_price, v_category
    FROM Products WHERE product_id = p_product_id;
    
    -- Add item to order
    INSERT INTO Order_Items (order_id, product_id, quantity, unit_price, discount)
    VALUES (p_order_id, p_product_id, p_quantity, v_unit_price, p_discount);
    
    -- Update order total
    UPDATE Orders 
    SET total_amount = total_amount + (p_quantity * v_unit_price * (1 - p_discount/100))
    WHERE order_id = p_order_id;
    
    -- If it's a physical product, reduce stock
    IF v_category != 'service' THEN
        UPDATE Products
        SET stock_quantity = stock_quantity - p_quantity
        WHERE product_id = p_product_id;
    END IF;
END //
DELIMITER ;

-- Trigger to validate stock before adding order item
DELIMITER //
CREATE TRIGGER before_order_item_insert
BEFORE INSERT ON Order_Items
FOR EACH ROW
BEGIN
    DECLARE v_stock INT;
    DECLARE v_category VARCHAR(20);
    
    SELECT stock_quantity, category INTO v_stock, v_category
    FROM Products WHERE product_id = NEW.product_id;
    
    IF v_category != 'service' AND v_stock < NEW.quantity THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Insufficient stock for this product';
    END IF;
END //
DELIMITER ;
```
