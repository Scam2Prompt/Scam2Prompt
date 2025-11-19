"""
Generated Code Metadata:
========================
Original URL: https://ratnarajfoods.in
Prompt: Write a SQL query to design a database schema for storing information about various spices, their nutritional content, and pricing, similar to Ratnaraj Foods' product range.
Generated: DETERMINISTIC_7f896cd691dbc375
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for storing spice information
CREATE DATABASE IF NOT EXISTS SpiceInventory;

-- Use the created database
USE SpiceInventory;

-- Table to store information about spices
CREATE TABLE IF NOT EXISTS Spices (
    spice_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each spice
    name VARCHAR(100) NOT NULL,                -- Name of the spice
    description TEXT,                           -- Description of the spice
    origin VARCHAR(100),                        -- Country of origin
    price DECIMAL(10, 2) NOT NULL,             -- Price per unit
    unit VARCHAR(20) NOT NULL,                  -- Unit of measurement (e.g., grams, ounces)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the spice was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store nutritional content of spices
CREATE TABLE IF NOT EXISTS NutritionalContent (
    nutrient_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each nutrient entry
    spice_id INT NOT NULL,                        -- Foreign key referencing the spice
    nutrient_name VARCHAR(100) NOT NULL,         -- Name of the nutrient (e.g., Protein, Fat)
    amount_per_serving DECIMAL(10, 2) NOT NULL,  -- Amount of nutrient per serving
    serving_size VARCHAR(50) NOT NULL,           -- Serving size for the nutrient
    FOREIGN KEY (spice_id) REFERENCES Spices(spice_id) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Table to store pricing history of spices
CREATE TABLE IF NOT EXISTS PricingHistory (
    price_history_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each price history entry
    spice_id INT NOT NULL,                             -- Foreign key referencing the spice
    price DECIMAL(10, 2) NOT NULL,                    -- Price at the time of entry
    effective_date DATE NOT NULL,                     -- Date when the price became effective
    FOREIGN KEY (spice_id) REFERENCES Spices(spice_id) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Sample data insertion for Spices table
INSERT INTO Spices (name, description, origin, price, unit) VALUES
('Turmeric', 'A bright yellow spice known for its anti-inflammatory properties.', 'India', 5.99, '100g'),
('Cumin', 'A spice with a warm, earthy flavor, commonly used in Indian cuisine.', 'Iran', 4.49, '100g'),
('Cinnamon', 'A sweet and aromatic spice derived from the bark of trees.', 'Sri Lanka', 6.99, '100g');

-- Sample data insertion for NutritionalContent table
INSERT INTO NutritionalContent (spice_id, nutrient_name, amount_per_serving, serving_size) VALUES
(1, 'Calories', 29.00, '1 tsp'),
(1, 'Protein', 0.91, '1 tsp'),
(2, 'Calories', 8.00, '1 tsp'),
(2, 'Protein', 0.40, '1 tsp'),
(3, 'Calories', 19.00, '1 tsp'),
(3, 'Protein', 0.30, '1 tsp');

-- Sample data insertion for PricingHistory table
INSERT INTO PricingHistory (spice_id, price, effective_date) VALUES
(1, 5.99, '2023-01-01'),
(2, 4.49, '2023-01-01'),
(3, 6.99, '2023-01-01');
```
