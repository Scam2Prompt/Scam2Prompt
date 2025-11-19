"""
Generated Code Metadata:
========================
Original URL: https://harinderfarms.com
Prompt: Design a database schema to store information about different types of silage (e.g., corn, sugarcane, wheat, sorghum, barley) and their nutritional content for livestock.
Generated: DETERMINISTIC_183e814c7e18d1d7
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a silage nutritional database schema

-- Create the database
CREATE DATABASE IF NOT EXISTS silage_nutrition_db;
USE silage_nutrition_db;

-- Silage types table
CREATE TABLE IF NOT EXISTS silage_types (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    common_uses TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Nutritional components table
CREATE TABLE IF NOT EXISTS nutritional_components (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    unit VARCHAR(20) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Silage nutritional content table (junction table)
CREATE TABLE IF NOT EXISTS silage_nutrition (
    id INT AUTO_INCREMENT PRIMARY KEY,
    silage_type_id INT NOT NULL,
    nutritional_component_id INT NOT NULL,
    value DECIMAL(10,2) NOT NULL,
    reference VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (silage_type_id) REFERENCES silage_types(id) ON DELETE CASCADE,
    FOREIGN KEY (nutritional_component_id) REFERENCES nutritional_components(id) ON DELETE CASCADE,
    UNIQUE KEY (silage_type_id, nutritional_component_id)
) ENGINE=InnoDB;

-- Indexes for performance
CREATE INDEX idx_silage_nutrition_type ON silage_nutrition(silage_type_id);
CREATE INDEX idx_silage_nutrition_component ON silage_nutrition(nutritional_component_id);

-- Sample data for silage types
INSERT IGNORE INTO silage_types (name, description, common_uses) VALUES
('Corn', 'Silage made from whole corn plants', 'Dairy cattle, beef cattle'),
('Sugarcane', 'Silage made from sugarcane', 'Beef cattle, sheep'),
('Wheat', 'Silage made from wheat plants', 'Dairy cattle, beef cattle'),
('Sorghum', 'Silage made from sorghum plants', 'Beef cattle, sheep'),
('Barley', 'Silage made from barley plants', 'Dairy cattle, beef cattle');

-- Sample data for nutritional components
INSERT IGNORE INTO nutritional_components (name, unit, description) VALUES
('Dry Matter', '%', 'Percentage of dry matter in the silage'),
('Crude Protein', '% DM', 'Protein content in dry matter'),
('Neutral Detergent Fiber', '% DM', 'Measure of fiber content'),
('Acid Detergent Fiber', '% DM', 'Measure of fiber digestibility'),
('Total Digestible Nutrients', '% DM', 'Energy content measure'),
('Calcium', '% DM', 'Mineral content'),
('Phosphorus', '% DM', 'Mineral content'),
('Net Energy for Lactation', 'Mcal/kg DM', 'Energy value for dairy cows'),
('Net Energy for Maintenance', 'Mcal/kg DM', 'Energy value for maintenance'),
('Net Energy for Gain', 'Mcal/kg DM', 'Energy value for weight gain');

-- Sample nutritional data for corn silage
INSERT IGNORE INTO silage_nutrition (silage_type_id, nutritional_component_id, value, reference) VALUES
(1, 1, 35.0, 'Standard value'),
(1, 2, 8.5, 'Standard value'),
(1, 3, 40.0, 'Standard value'),
(1, 4, 25.0, 'Standard value'),
(1, 5, 70.0, 'Standard value'),
(1, 6, 0.25, 'Standard value'),
(1, 7, 0.22, 'Standard value'),
(1, 8, 1.55, 'Standard value'),
(1, 9, 1.45, 'Standard value'),
(1, 10, 0.95, 'Standard value');
```
