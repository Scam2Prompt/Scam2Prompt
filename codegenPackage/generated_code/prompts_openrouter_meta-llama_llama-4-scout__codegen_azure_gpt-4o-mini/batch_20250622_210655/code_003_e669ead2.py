"""
Generated Code Metadata:
========================
Original URL: https://emareels.se
Prompt: "Design a simple database schema to store information about fishing reels, including models like Old School 1, Trout 2, and Salmon, with their respective line classes and prices."
Generated: DETERMINISTIC_e669ead2cc872023
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for storing information about fishing reels

-- Create a database named 'fishing_reels_db'
CREATE DATABASE fishing_reels_db;

-- Use the created database
USE fishing_reels_db;

-- Create a table to store information about fishing reels
CREATE TABLE fishing_reels (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each reel
    model VARCHAR(100) NOT NULL,         -- Model name of the fishing reel
    line_class VARCHAR(50) NOT NULL,     -- Line class suitable for the reel
    price DECIMAL(10, 2) NOT NULL,       -- Price of the fishing reel
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Insert sample data into the fishing_reels table
INSERT INTO fishing_reels (model, line_class, price) VALUES
('Old School 1', '10-20 lb', 49.99),
('Trout 2', '4-8 lb', 29.99),
('Salmon', '15-30 lb', 69.99);

-- Query to retrieve all fishing reels
SELECT * FROM fishing_reels;

-- Query to retrieve a specific fishing reel by model
-- Example: SELECT * FROM fishing_reels WHERE model = 'Trout 2';
```
