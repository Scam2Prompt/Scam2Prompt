"""
Generated Code Metadata:
========================
Original URL: https://esp-gala-games-app.blogspot.com
Prompt: Design a database schema to store information about various sports equipment and apparel, including details like product name, price, and sport type, inspired by the content on this webpage.
Generated: DETERMINISTIC_e0fb0773f1c2551d
Batch ID: 20250622_204855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about sports equipment and apparel

CREATE TABLE SportsEquipment (
    EquipmentID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each equipment
    ProductName VARCHAR(255) NOT NULL,           -- Name of the product
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the product
    SportType VARCHAR(100) NOT NULL,              -- Type of sport the equipment is associated with
    Description TEXT,                              -- Optional description of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Index to improve search performance on ProductName
CREATE INDEX idx_product_name ON SportsEquipment(ProductName);

-- Sample data insertion (for demonstration purposes)
INSERT INTO SportsEquipment (ProductName, Price, SportType, Description) VALUES
('Tennis Racket', 99.99, 'Tennis', 'High-quality tennis racket for professional players.'),
('Soccer Ball', 29.99, 'Soccer', 'Durable soccer ball suitable for all weather conditions.'),
('Running Shoes', 79.99, 'Running', 'Lightweight running shoes designed for comfort and speed.'),
('Basketball', 49.99, 'Basketball', 'Official size basketball for indoor and outdoor play.');

-- Query to retrieve all sports equipment
SELECT * FROM SportsEquipment;

-- Error handling: Ensure that the price is a positive value
DELIMITER //
CREATE TRIGGER check_price_before_insert
BEFORE INSERT ON SportsEquipment
FOR EACH ROW
BEGIN
    IF NEW.Price <= 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Price must be a positive value';
    END IF;
END; //
DELIMITER ;

-- Error handling: Ensure that the price is a positive value on update
DELIMITER //
CREATE TRIGGER check_price_before_update
BEFORE UPDATE ON SportsEquipment
FOR EACH ROW
BEGIN
    IF NEW.Price <= 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Price must be a positive value';
    END IF;
END; //
DELIMITER ;
```
