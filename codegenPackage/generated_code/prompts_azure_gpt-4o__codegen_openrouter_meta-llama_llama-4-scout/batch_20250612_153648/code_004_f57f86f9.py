"""
Generated Code Metadata:
========================
Original URL: https://longhuigolf.com
Prompt: Create a database schema for storing golf grip profiles, including customization details like material type (PU, TPE, rubber), embossing style, and customer preferences, as described on the Longhui Golf website.
Generated: DETERMINISTIC_f57f86f9a440f9f3
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- golf_grip_profiles.sql

-- Create database schema for golf grip profiles
CREATE DATABASE golf_grip_db;

-- Use the golf grip database
USE golf_grip_db;

-- Create table for material types
CREATE TABLE material_types (
  id INT AUTO_INCREMENT,
  material_name VARCHAR(50) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for embossing styles
CREATE TABLE embossing_styles (
  id INT AUTO_INCREMENT,
  style_name VARCHAR(100) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for golf grip profiles
CREATE TABLE golf_grip_profiles (
  id INT AUTO_INCREMENT,
  profile_name VARCHAR(200) NOT NULL,
  material_type_id INT NOT NULL,
  embossing_style_id INT NOT NULL,
  size DECIMAL(3, 2) NOT NULL,
  weight DECIMAL(5, 2) NOT NULL,
  color VARCHAR(50),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (material_type_id) REFERENCES material_types(id),
  FOREIGN KEY (embossing_style_id) REFERENCES embossing_styles(id)
);

-- Create table for customer preferences
CREATE TABLE customer_preferences (
  id INT AUTO_INCREMENT,
  customer_name VARCHAR(200) NOT NULL,
  golf_grip_profile_id INT NOT NULL,
  preferred_color VARCHAR(50),
  preferred_size DECIMAL(3, 2),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (golf_grip_profile_id) REFERENCES golf_grip_profiles(id)
);

-- Create table for customization details
CREATE TABLE customization_details (
  id INT AUTO_INCREMENT,
  golf_grip_profile_id INT NOT NULL,
  material_type_id INT NOT NULL,
  embossing_style_id INT NOT NULL,
  logo VARCHAR(100),
  text VARCHAR(200),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (golf_grip_profile_id) REFERENCES golf_grip_profiles(id),
  FOREIGN KEY (material_type_id) REFERENCES material_types(id),
  FOREIGN KEY (embossing_style_id) REFERENCES embossing_styles(id)
);

-- Insert sample data for material types
INSERT INTO material_types (material_name, description)
VALUES
('PU', 'Polyurethane'),
('TPE', 'Thermoplastic Elastomer'),
('Rubber', 'Synthetic Rubber');

-- Insert sample data for embossing styles
INSERT INTO embossing_styles (style_name, description)
VALUES
('Embossed Logo', 'Raised logo embossing'),
('Diamond Pattern', 'Diamond-shaped pattern embossing'),
('Solid Color', 'Solid color embossing');

-- Insert sample data for golf grip profiles
INSERT INTO golf_grip_profiles (profile_name, material_type_id, embossing_style_id, size, weight, color)
VALUES
('Standard Grip', 1, 1, 2.50, 50.00, 'Black'),
('Premium Grip', 2, 2, 2.75, 60.00, 'Red'),
('Custom Grip', 3, 3, 3.00, 70.00, 'Blue');

-- Insert sample data for customer preferences
INSERT INTO customer_preferences (customer_name, golf_grip_profile_id, preferred_color, preferred_size)
VALUES
('John Doe', 1, 'Black', 2.50),
('Jane Smith', 2, 'Red', 2.75),
('Bob Johnson', 3, 'Blue', 3.00);

-- Insert sample data for customization details
INSERT INTO customization_details (golf_grip_profile_id, material_type_id, embossing_style_id, logo, text)
VALUES
(1, 1, 1, 'LH Logo', 'Longhui Golf'),
(2, 2, 2, 'Custom Logo', 'Personalized Grip'),
(3, 3, 3, 'Company Logo', 'Golf Grip Co.');
```
