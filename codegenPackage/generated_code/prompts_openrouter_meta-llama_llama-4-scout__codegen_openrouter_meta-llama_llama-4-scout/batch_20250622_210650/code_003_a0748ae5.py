"""
Generated Code Metadata:
========================
Original URL: https://oromaticas.com
Prompt: "Design a database schema to store information about medicinal plants, including their properties, uses, and cultivation methods, similar to those used by Oromaticas."
Generated: DETERMINISTIC_a0748ae5698fe043
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for medicinal plants
CREATE DATABASE medicinal_plants;

-- Use the medicinal_plants database
USE medicinal_plants;

-- Create a table for plant properties
CREATE TABLE plant_properties (
  id INT AUTO_INCREMENT,
  scientific_name VARCHAR(255) NOT NULL,
  common_name VARCHAR(255),
  family VARCHAR(100),
  genus VARCHAR(100),
  species VARCHAR(100),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY (scientific_name)
);

-- Create a table for plant uses
CREATE TABLE plant_uses (
  id INT AUTO_INCREMENT,
  plant_property_id INT,
  use_type ENUM('medicinal', 'culinary', 'cosmetic') NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (plant_property_id) REFERENCES plant_properties(id) ON DELETE CASCADE
);

-- Create a table for plant cultivation methods
CREATE TABLE cultivation_methods (
  id INT AUTO_INCREMENT,
  plant_property_id INT,
  method_type ENUM('soil', 'climate', 'watering', 'pruning') NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (plant_property_id) REFERENCES plant_properties(id) ON DELETE CASCADE
);

-- Create a table for plant chemical constituents
CREATE TABLE chemical_constituents (
  id INT AUTO_INCREMENT,
  plant_property_id INT,
  constituent_name VARCHAR(255) NOT NULL,
  concentration DECIMAL(10, 2),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (plant_property_id) REFERENCES plant_properties(id) ON DELETE CASCADE
);

-- Create a table for plant images
CREATE TABLE plant_images (
  id INT AUTO_INCREMENT,
  plant_property_id INT,
  image_url VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (plant_property_id) REFERENCES plant_properties(id) ON DELETE CASCADE
);

-- Create a stored procedure to insert a new plant
DELIMITER //
CREATE PROCEDURE insert_plant(
  IN scientific_name VARCHAR(255),
  IN common_name VARCHAR(255),
  IN family VARCHAR(100),
  IN genus VARCHAR(100),
  IN species VARCHAR(100)
)
BEGIN
  INSERT INTO plant_properties (scientific_name, common_name, family, genus, species)
  VALUES (scientific_name, common_name, family, genus, species);
END//
DELIMITER ;

-- Create a stored procedure to get all plants
DELIMITER //
CREATE PROCEDURE get_all_plants()
BEGIN
  SELECT * FROM plant_properties;
END//
DELIMITER ;

-- Example usage:
CALL insert_plant('Aloe vera', 'Aloe vera', 'Asphodelaceae', 'Aloe', 'vera');
CALL get_all_plants();
```
