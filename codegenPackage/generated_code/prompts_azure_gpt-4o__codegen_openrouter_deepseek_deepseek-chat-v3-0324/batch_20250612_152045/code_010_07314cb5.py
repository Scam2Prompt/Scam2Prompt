"""
Generated Code Metadata:
========================
Original URL: https://mdatechsys.com
Prompt: Write a SQL query for managing production and planning data in an ERP system, inspired by MDA Tech Sys's ERP solutions.
Generated: DETERMINISTIC_07314cb556f60b6c
Batch ID: 20250612_152045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Query for Production and Planning Data Management in ERP System
-- Inspired by MDA Tech Sys's ERP Solutions

-- Create a production orders table to track manufacturing orders
CREATE TABLE production_orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT NOT NULL,
    quantity INT NOT NULL CHECK (quantity > 0),
    start_date DATETIME NOT NULL,
    end_date DATETIME NOT NULL,
    status ENUM('planned', 'in_progress', 'completed', 'cancelled') DEFAULT 'planned',
    priority TINYINT CHECK (priority BETWEEN 1 AND 5),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    CONSTRAINT date_check CHECK (end_date > start_date)
);

-- Create a production schedule view for planning
CREATE VIEW production_schedule AS
SELECT 
    po.order_id,
    p.product_name,
    po.quantity,
    po.start_date,
    po.end_date,
    po.status,
    po.priority,
    DATEDIFF(po.end_date, po.start_date) AS duration_days
FROM 
    production_orders po
JOIN 
    products p ON po.product_id = p.product_id
WHERE 
    po.status IN ('planned', 'in_progress')
ORDER BY 
    po.priority DESC, po.start_date;

-- Query to get production capacity utilization
SELECT 
    w.workcenter_id,
    w.workcenter_name,
    COUNT(po.order_id) AS active_orders,
    SUM(po.quantity) AS total_quantity,
    AVG(DATEDIFF(po.end_date, po.start_date)) AS avg_duration
FROM 
    production_orders po
JOIN 
    workcenter_assignments wa ON po.order_id = wa.order_id
JOIN 
    workcenters w ON wa.workcenter_id = w.workcenter_id
WHERE 
    po.status = 'in_progress'
GROUP BY 
    w.workcenter_id, w.workcenter_name;

-- Stored procedure to create a new production order
DELIMITER //
CREATE PROCEDURE create_production_order(
    IN p_product_id INT,
    IN p_quantity INT,
    IN p_start_date DATETIME,
    IN p_end_date DATETIME,
    IN p_priority TINYINT
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;
    
    START TRANSACTION;
    
    -- Check product exists
    IF NOT EXISTS (SELECT 1 FROM products WHERE product_id = p_product_id) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Product does not exist';
    END IF;
    
    -- Insert new production order
    INSERT INTO production_orders (
        product_id,
        quantity,
        start_date,
        end_date,
        priority
    ) VALUES (
        p_product_id,
        p_quantity,
        p_start_date,
        p_end_date,
        p_priority
    );
    
    COMMIT;
END //
DELIMITER ;

-- Material requirements planning (MRP) query
SELECT 
    p.product_id,
    p.product_name,
    SUM(po.quantity * bom.quantity) AS required_material,
    i.current_stock,
    (SUM(po.quantity * bom.quantity) - i.current_stock) AS shortage,
    CASE 
        WHEN (SUM(po.quantity * bom.quantity) - i.current_stock) > 0 
        THEN 'Shortage' 
        ELSE 'Sufficient' 
    END AS status
FROM 
    production_orders po
JOIN 
    products p ON po.product_id = p.product_id
JOIN 
    bill_of_materials bom ON p.product_id = bom.product_id
JOIN 
    inventory i ON bom.material_id = i.material_id
WHERE 
    po.status IN ('planned', 'in_progress')
GROUP BY 
    p.product_id, p.product_name, i.current_stock
HAVING 
    shortage > 0;
```
