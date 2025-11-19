"""
Generated Code Metadata:
========================
Original URL: https://w-magiceden-world-app-helo.blogspot.com
Prompt: Develop a SQL query to store and retrieve tire product data, including width, height, rim size, and price, as structured on the "Dal Cortivo Pneus" website.
Generated: DETERMINISTIC_da38abf496379e02
Batch ID: 20250612_151334
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create and manage tire product data

-- Create database if not exists
CREATE DATABASE IF NOT EXISTS dal_cortivo_pneus;
USE dal_cortivo_pneus;

-- Create tire products table
CREATE TABLE IF NOT EXISTS tires (
    id INT AUTO_INCREMENT PRIMARY KEY,
    brand VARCHAR(50) NOT NULL,
    model VARCHAR(100) NOT NULL,
    width INT NOT NULL COMMENT 'Tire width in millimeters',
    height INT NOT NULL COMMENT 'Aspect ratio as percentage of width',
    rim_size DECIMAL(3,1) NOT NULL COMMENT 'Rim diameter in inches',
    season ENUM('summer', 'winter', 'all-season') NOT NULL,
    load_index VARCHAR(5) NOT NULL COMMENT 'Load capacity code',
    speed_rating CHAR(1) NOT NULL COMMENT 'Speed rating code',
    price DECIMAL(10,2) NOT NULL,
    stock_quantity INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_width CHECK (width BETWEEN 100 AND 400),
    CONSTRAINT chk_height CHECK (height BETWEEN 25 AND 100),
    CONSTRAINT chk_rim_size CHECK (rim_size BETWEEN 10 AND 25),
    CONSTRAINT chk_price CHECK (price > 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Create index for common search patterns
CREATE INDEX idx_tire_dimensions ON tires (width, height, rim_size);
CREATE INDEX idx_tire_brand_model ON tires (brand, model);
CREATE INDEX idx_tire_price ON tires (price);

-- Stored procedure to insert new tire product
DELIMITER //
CREATE PROCEDURE sp_insert_tire(
    IN p_brand VARCHAR(50),
    IN p_model VARCHAR(100),
    IN p_width INT,
    IN p_height INT,
    IN p_rim_size DECIMAL(3,1),
    IN p_season ENUM('summer', 'winter', 'all-season'),
    IN p_load_index VARCHAR(5),
    IN p_speed_rating CHAR(1),
    IN p_price DECIMAL(10,2),
    IN p_stock_quantity INT
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;
    
    START TRANSACTION;
    
    INSERT INTO tires (
        brand, 
        model, 
        width, 
        height, 
        rim_size, 
        season, 
        load_index, 
        speed_rating, 
        price, 
        stock_quantity
    ) VALUES (
        p_brand,
        p_model,
        p_width,
        p_height,
        p_rim_size,
        p_season,
        p_load_index,
        p_speed_rating,
        p_price,
        p_stock_quantity
    );
    
    COMMIT;
END //
DELIMITER ;

-- Stored procedure to get tires by dimensions
DELIMITER //
CREATE PROCEDURE sp_get_tires_by_dimensions(
    IN p_width INT,
    IN p_height INT,
    IN p_rim_size DECIMAL(3,1)
)
BEGIN
    SELECT 
        id,
        brand,
        model,
        width,
        height,
        rim_size,
        season,
        load_index,
        speed_rating,
        price,
        stock_quantity
    FROM 
        tires
    WHERE 
        width = p_width
        AND height = p_height
        AND rim_size = p_rim_size
    ORDER BY 
        brand, model, price;
END //
DELIMITER ;

-- Stored procedure to get tires by price range
DELIMITER //
CREATE PROCEDURE sp_get_tires_by_price_range(
    IN p_min_price DECIMAL(10,2),
    IN p_max_price DECIMAL(10,2)
)
BEGIN
    SELECT 
        id,
        brand,
        model,
        width,
        height,
        rim_size,
        season,
        load_index,
        speed_rating,
        price,
        stock_quantity
    FROM 
        tires
    WHERE 
        price BETWEEN p_min_price AND p_max_price
    ORDER BY 
        price, brand, model;
END //
DELIMITER ;

-- View for available tires (in stock)
CREATE VIEW vw_available_tires AS
SELECT 
    id,
    brand,
    model,
    width,
    height,
    rim_size,
    season,
    load_index,
    speed_rating,
    price
FROM 
    tires
WHERE 
    stock_quantity > 0
ORDER BY 
    brand, model, price;
```
