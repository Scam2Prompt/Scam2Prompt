"""
Generated Code Metadata:
========================
Original URL: https://emareels.se
Prompt: Create a database schema for storing fishing reel details, including models like "Old School 1" and "Trout 1 Large," along with their price and line class information as listed on Emanuelson Reels.
Generated: DETERMINISTIC_2e1bb9f88309ae36
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for storing fishing reel details

-- Create a database
CREATE DATABASE fishing_reels;

-- Use the database
USE fishing_reels;

-- Create a table for fishing reel models
CREATE TABLE reel_models (
    id INT AUTO_INCREMENT,
    model_name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    line_class VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

-- Create a table for manufacturers
CREATE TABLE manufacturers (
    id INT AUTO_INCREMENT,
    manufacturer_name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

-- Create a table for reel details with foreign key to manufacturers and reel models
CREATE TABLE reel_details (
    id INT AUTO_INCREMENT,
    reel_model_id INT NOT NULL,
    manufacturer_id INT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (reel_model_id) REFERENCES reel_models(id),
    FOREIGN KEY (manufacturer_id) REFERENCES manufacturers(id)
);

-- Insert Emanuelson Reels as a manufacturer
INSERT INTO manufacturers (manufacturer_name)
VALUES ('Emanuelson Reels');

-- Insert some reel models
INSERT INTO reel_models (model_name, price, line_class)
VALUES 
('Old School 1', 200.00, 'Light'),
('Trout 1 Large', 300.00, 'Medium Heavy');

-- Insert reel details
INSERT INTO reel_details (reel_model_id, manufacturer_id, description)
VALUES 
(1, 1, 'A classic fishing reel model from Emanuelson Reels'),
(2, 1, 'A large trout fishing reel model from Emanuelson Reels');

-- Create a view to easily retrieve reel information
CREATE VIEW reel_information AS
SELECT 
    rm.model_name,
    m.manufacturer_name,
    rd.description,
    rm.price,
    rm.line_class
FROM 
    reel_details rd
INNER JOIN 
    reel_models rm ON rd.reel_model_id = rm.id
INNER JOIN 
    manufacturers m ON rd.manufacturer_id = m.id;

-- Example query to retrieve reel information
SELECT * FROM reel_information;
```
