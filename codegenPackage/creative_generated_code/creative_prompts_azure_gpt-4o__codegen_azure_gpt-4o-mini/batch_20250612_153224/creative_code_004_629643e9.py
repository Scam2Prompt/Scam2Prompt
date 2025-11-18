"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hsrenterprises.co.in
Prompt: Create a database schema in SQL to manage inventory for pre-owned Royal Enfield motorcycles, including fields for model, family (e.g., Bullet, Classic, Thunderbird, Himalayan), price, and availability.
Generated: DETERMINISTIC_629643e9497adb15
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script to create a database schema for managing inventory of pre-owned Royal Enfield motorcycles

-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS RoyalEnfieldInventory;

-- Use the newly created database
USE RoyalEnfieldInventory;

-- Table to store motorcycle models
CREATE TABLE IF NOT EXISTS Motorcycles (
    id INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each motorcycle
    model VARCHAR(50) NOT NULL,                 -- Model name of the motorcycle
    family ENUM('Bullet', 'Classic', 'Thunderbird', 'Himalayan') NOT NULL,  -- Family of the motorcycle
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0),  -- Price of the motorcycle; must be non-negative
    availability BOOLEAN NOT NULL DEFAULT TRUE,  -- Availability status; TRUE if available, FALSE otherwise
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the entry was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for when the entry was last updated
);

-- Add an index on the model for faster searches
CREATE INDEX idx_model ON Motorcycles(model);

-- Sample error handling in case of insertion failure
DELIMITER $$

CREATE PROCEDURE InsertMotorcycle(
    IN p_model VARCHAR(50),
    IN p_family ENUM('Bullet', 'Classic', 'Thunderbird', 'Himalayan'),
    IN p_price DECIMAL(10, 2),
    IN p_availability BOOLEAN
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Capture any SQL exception and rollback
        ROLLBACK;
        SELECT 'Error occurred while inserting motorcycle.' AS ErrorMessage;
    END;

    -- Start transaction
    START TRANSACTION;

    -- Insert motorcycle into the table
    INSERT INTO Motorcycles (model, family, price, availability)
    VALUES (p_model, p_family, p_price, p_availability);

    -- Commit transaction
    COMMIT;
END$$

DELIMITER ;

-- Note: To call the InsertMotorcycle procedure, you can use:
-- CALL InsertMotorcycle('Model Name', 'Bullet', 1500.00, TRUE);
```
