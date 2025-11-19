"""
Generated Code Metadata:
========================
Original URL: https://bismillahgems.com
Prompt: Design a database schema to store information about gemstones, including their types, carat weights, prices, and images, for a website like Bismillah Gems.
Generated: DETERMINISTIC_d112ee332b6845db
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing gemstone information

-- Table: gemstones
CREATE TABLE gemstones (
    gemstone_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each gemstone
    name VARCHAR(255) NOT NULL,                 -- Name of the gemstone (e.g., Ruby, Sapphire)
    type VARCHAR(100) NOT NULL,                 -- Type of gemstone (e.g., Precious, Semi-Precious)
    carat_weight DECIMAL(10, 2) NOT NULL,       -- Weight of the gemstone in carats
    price DECIMAL(10, 2) NOT NULL,              -- Price of the gemstone in USD
    image_url VARCHAR(2083),                    -- URL to the image of the gemstone
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the record was last updated
);

-- Table: gemstone_types
CREATE TABLE gemstone_types (
    type_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each gemstone type
    type_name VARCHAR(100) NOT NULL UNIQUE, -- Name of the gemstone type (e.g., Precious, Semi-Precious)
    description TEXT                         -- Description of the gemstone type
);

-- Foreign key relationship: gemstones.type -> gemstone_types.type_name
ALTER TABLE gemstones
ADD CONSTRAINT fk_gemstone_type
FOREIGN KEY (type) REFERENCES gemstone_types(type_name)
ON DELETE SET NULL ON UPDATE CASCADE;

-- Indexes for faster queries
CREATE INDEX idx_gemstone_name ON gemstones(name); -- Index for gemstone name
CREATE INDEX idx_gemstone_type ON gemstones(type); -- Index for gemstone type
CREATE INDEX idx_gemstone_price ON gemstones(price); -- Index for gemstone price

-- Example error handling: Ensure price and carat_weight are positive
CREATE TRIGGER validate_gemstone_data
BEFORE INSERT ON gemstones
FOR EACH ROW
BEGIN
    IF NEW.price <= 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Price must be greater than zero.';
    END IF;
    IF NEW.carat_weight <= 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Carat weight must be greater than zero.';
    END IF;
END;
```
