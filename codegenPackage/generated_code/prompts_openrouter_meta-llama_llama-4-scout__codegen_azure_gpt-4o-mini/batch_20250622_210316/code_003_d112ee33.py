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
-- Database schema for storing information about gemstones

CREATE DATABASE BismillahGems;

USE BismillahGems;

-- Table to store gemstone types
CREATE TABLE GemstoneTypes (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each gemstone type
    name VARCHAR(100) NOT NULL UNIQUE,   -- Name of the gemstone type (e.g., Diamond, Ruby)
    description TEXT,                     -- Description of the gemstone type
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store gemstones
CREATE TABLE Gemstones (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each gemstone
    type_id INT NOT NULL,                -- Foreign key referencing the GemstoneTypes table
    carat_weight DECIMAL(5, 2) NOT NULL, -- Carat weight of the gemstone
    price DECIMAL(10, 2) NOT NULL,       -- Price of the gemstone
    image_url VARCHAR(255),               -- URL of the gemstone image
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of last update
    FOREIGN KEY (type_id) REFERENCES GemstoneTypes(id) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Table to store gemstone inventory
CREATE TABLE GemstoneInventory (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each inventory record
    gemstone_id INT NOT NULL,            -- Foreign key referencing the Gemstones table
    quantity INT NOT NULL DEFAULT 0,     -- Quantity of the gemstone in stock
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of last update
    FOREIGN KEY (gemstone_id) REFERENCES Gemstones(id) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Table to store gemstone sales
CREATE TABLE GemstoneSales (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each sale record
    gemstone_id INT NOT NULL,            -- Foreign key referencing the Gemstones table
    sale_price DECIMAL(10, 2) NOT NULL,  -- Sale price of the gemstone
    sale_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Date and time of the sale
    quantity_sold INT NOT NULL DEFAULT 1,  -- Quantity sold in the transaction
    FOREIGN KEY (gemstone_id) REFERENCES Gemstones(id) ON DELETE CASCADE  -- Ensures referential integrity
);
```
