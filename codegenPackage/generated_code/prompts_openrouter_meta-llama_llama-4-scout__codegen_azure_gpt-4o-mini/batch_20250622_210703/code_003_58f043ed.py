"""
Generated Code Metadata:
========================
Original URL: https://thewatchplaza53.pk
Prompt: Design a database schema to store information about replica watches, including brand, model, price, and product description, inspired by The Watch Plaza product catalog.
Generated: DETERMINISTIC_58f043ed3b1e1fc8
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about replica watches

CREATE DATABASE IF NOT EXISTS WatchReplicaDB;

USE WatchReplicaDB;

-- Table to store information about watch brands
CREATE TABLE IF NOT EXISTS Brands (
    brand_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each brand
    brand_name VARCHAR(100) NOT NULL UNIQUE,  -- Name of the brand
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the brand was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of the last update
);

-- Table to store information about watch models
CREATE TABLE IF NOT EXISTS Watches (
    watch_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each watch
    brand_id INT NOT NULL,  -- Foreign key referencing the Brands table
    model_name VARCHAR(100) NOT NULL,  -- Name of the watch model
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0),  -- Price of the watch, must be non-negative
    product_description TEXT,  -- Description of the watch
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the watch was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of the last update
    FOREIGN KEY (brand_id) REFERENCES Brands(brand_id) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Index for faster search on model_name
CREATE INDEX idx_model_name ON Watches(model_name);

-- Sample data insertion (optional)
INSERT INTO Brands (brand_name) VALUES ('Rolex'), ('Omega'), ('Tag Heuer');

INSERT INTO Watches (brand_id, model_name, price, product_description) VALUES
(1, 'Submariner', 999.99, 'A classic diving watch with a timeless design.'),
(2, 'Speedmaster', 799.99, 'The first watch worn on the moon.'),
(3, 'Carrera', 649.99, 'A racing-inspired chronograph with a sleek look.');

-- Note: Ensure to handle errors during data insertion and retrieval in application code.
```
