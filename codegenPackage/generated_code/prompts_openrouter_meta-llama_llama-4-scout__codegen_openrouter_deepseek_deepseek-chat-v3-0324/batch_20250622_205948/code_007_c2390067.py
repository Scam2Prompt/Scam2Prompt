"""
Generated Code Metadata:
========================
Original URL: https://kalpanaskitchen.com
Prompt: "Design a database schema to store information about different spices, including their prices and quantities available."
Generated: DETERMINISTIC_c2390067c85b3443
Batch ID: 20250622_205948
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for spice inventory management

-- Create the database
CREATE DATABASE IF NOT EXISTS spice_inventory;
USE spice_inventory;

-- Table for storing spice categories
CREATE TABLE IF NOT EXISTS categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY (name)
) ENGINE=InnoDB;

-- Table for storing spices
CREATE TABLE IF NOT EXISTS spices (
    spice_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category_id INT,
    description TEXT,
    origin_country VARCHAR(100),
    is_organic BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE SET NULL,
    UNIQUE KEY (name)
) ENGINE=InnoDB;

-- Table for storing inventory information
CREATE TABLE IF NOT EXISTS inventory (
    inventory_id INT AUTO_INCREMENT PRIMARY KEY,
    spice_id INT NOT NULL,
    quantity DECIMAL(10, 3) NOT NULL DEFAULT 0,
    unit VARCHAR(20) NOT NULL DEFAULT 'grams',
    price_per_unit DECIMAL(10, 2) NOT NULL,
    currency VARCHAR(3) DEFAULT 'USD',
    last_restocked DATE,
    expiry_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (spice_id) REFERENCES spices(spice_id) ON DELETE CASCADE,
    CHECK (quantity >= 0),
    CHECK (price_per_unit > 0)
) ENGINE=InnoDB;

-- Table for storing price history
CREATE TABLE IF NOT EXISTS price_history (
    history_id INT AUTO_INCREMENT PRIMARY KEY,
    inventory_id INT NOT NULL,
    old_price DECIMAL(10, 2) NOT NULL,
    new_price DECIMAL(10, 2) NOT NULL,
    changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    changed_by VARCHAR(100),
    FOREIGN KEY (inventory_id) REFERENCES inventory(inventory_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Indexes for better performance
CREATE INDEX idx_spice_name ON spices(name);
CREATE INDEX idx_spice_category ON spices(category_id);
CREATE INDEX idx_inventory_spice ON inventory(spice_id);
CREATE INDEX idx_price_history ON price_history(inventory_id, changed_at);
```
