"""
Generated Code Metadata:
========================
Original URL: https://tamstrucks.com
Prompt: Develop a basic inventory management system using SQL that can be used by TAMS TRUCKS to track their cargo and equipment.
Generated: DETERMINISTIC_51e2f57170713853
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for TAMS TRUCKS inventory management system
CREATE DATABASE tams_trucks_inventory;

-- Use the database
USE tams_trucks_inventory;

-- Create a table for cargo
CREATE TABLE cargo (
    cargo_id INT AUTO_INCREMENT,
    cargo_type VARCHAR(255) NOT NULL,
    description TEXT,
    quantity INT NOT NULL DEFAULT 0,
    weight DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (cargo_id)
);

-- Create a table for equipment
CREATE TABLE equipment (
    equipment_id INT AUTO_INCREMENT,
    equipment_type VARCHAR(255) NOT NULL,
    description TEXT,
    quantity INT NOT NULL DEFAULT 0,
    condition VARCHAR(255) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (equipment_id)
);

-- Create a table for trucks
CREATE TABLE trucks (
    truck_id INT AUTO_INCREMENT,
    truck_number VARCHAR(255) NOT NULL,
    cargo_capacity DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    equipment_capacity INT NOT NULL DEFAULT 0,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (truck_id)
);

-- Create a table for truck cargo
CREATE TABLE truck_cargo (
    truck_cargo_id INT AUTO_INCREMENT,
    truck_id INT NOT NULL,
    cargo_id INT NOT NULL,
    quantity INT NOT NULL,
    loaded_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (truck_cargo_id),
    FOREIGN KEY (truck_id) REFERENCES trucks(truck_id),
    FOREIGN KEY (cargo_id) REFERENCES cargo(cargo_id)
);

-- Create a table for truck equipment
CREATE TABLE truck_equipment (
    truck_equipment_id INT AUTO_INCREMENT,
    truck_id INT NOT NULL,
    equipment_id INT NOT NULL,
    quantity INT NOT NULL,
    loaded_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (truck_equipment_id),
    FOREIGN KEY (truck_id) REFERENCES trucks(truck_id),
    FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id)
);

-- Insert some sample data
INSERT INTO cargo (cargo_type, description, quantity, weight)
VALUES 
('Container', 'Standard shipping container', 10, 1000.00),
('Vehicle', 'Car or small truck', 5, 2000.00);

INSERT INTO equipment (equipment_type, description, quantity, condition)
VALUES 
('Crane', 'Truck-mounted crane', 2, 'Good'),
('Winch', 'Truck-mounted winch', 3, 'Fair');

INSERT INTO trucks (truck_number, cargo_capacity, equipment_capacity)
VALUES 
('TAMS-001', 5000.00, 5),
('TAMS-002', 3000.00, 3);

INSERT INTO truck_cargo (truck_id, cargo_id, quantity)
VALUES 
(1, 1, 2),
(2, 2, 1);

INSERT INTO truck_equipment (truck_id, equipment_id, quantity)
VALUES 
(1, 1, 1),
(2, 2, 1);

-- Procedures to manage inventory

DELIMITER $$

CREATE PROCEDURE add_cargo(
    IN p_cargo_type VARCHAR(255),
    IN p_description TEXT,
    IN p_quantity INT,
    IN p_weight DECIMAL(10, 2)
)
BEGIN
    INSERT INTO cargo (cargo_type, description, quantity, weight)
    VALUES (p_cargo_type, p_description, p_quantity, p_weight);
END$$

CREATE PROCEDURE add_equipment(
    IN p_equipment_type VARCHAR(255),
    IN p_description TEXT,
    IN p_quantity INT,
    IN p_condition VARCHAR(255)
)
BEGIN
    INSERT INTO equipment (equipment_type, description, quantity, condition)
    VALUES (p_equipment_type, p_description, p_quantity, p_condition);
END$$

CREATE PROCEDURE add_truck(
    IN p_truck_number VARCHAR(255),
    IN p_cargo_capacity DECIMAL(10, 2),
    IN p_equipment_capacity INT
)
BEGIN
    INSERT INTO trucks (truck_number, cargo_capacity, equipment_capacity)
    VALUES (p_truck_number, p_cargo_capacity, p_equipment_capacity);
END$$

CREATE PROCEDURE load_cargo_on_truck(
    IN p_truck_id INT,
    IN p_cargo_id INT,
    IN p_quantity INT
)
BEGIN
    IF (SELECT quantity FROM cargo WHERE cargo_id = p_cargo_id) >= p_quantity THEN
        INSERT INTO truck_cargo (truck_id, cargo_id, quantity)
        VALUES (p_truck_id, p_cargo_id, p_quantity);
        UPDATE cargo SET quantity = quantity - p_quantity WHERE cargo_id = p_cargo_id;
    ELSE
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Insufficient cargo quantity';
    END IF;
END$$

CREATE PROCEDURE load_equipment_on_truck(
    IN p_truck_id INT,
    IN p_equipment_id INT,
    IN p_quantity INT
)
BEGIN
    IF (SELECT quantity FROM equipment WHERE equipment_id = p_equipment_id) >= p_quantity THEN
        INSERT INTO truck_equipment (truck_id, equipment_id, quantity)
        VALUES (p_truck_id, p_equipment_id, p_quantity);
        UPDATE equipment SET quantity = quantity - p_quantity WHERE equipment_id = p_equipment_id;
    ELSE
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Insufficient equipment quantity';
    END IF;
END$$

DELIMITER ;
```
