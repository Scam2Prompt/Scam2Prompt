"""
Generated Code Metadata:
========================
Original URL: https://passandbrazzz.blogspot.com
Prompt: Design a database schema for storing information about commercial properties for sale, including fields for type of business, location, and price, inspired by the lighting store listing.
Generated: DETERMINISTIC_1942f099297cb395
Batch ID: 20250612_163924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for commercial properties
CREATE DATABASE commercial_properties;

-- Use the commercial_properties database
USE commercial_properties;

-- Create a table for property types
CREATE TABLE property_types (
  id INT AUTO_INCREMENT,
  type_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for locations
CREATE TABLE locations (
  id INT AUTO_INCREMENT,
  address VARCHAR(255) NOT NULL,
  city VARCHAR(100) NOT NULL,
  state VARCHAR(100) NOT NULL,
  zip_code VARCHAR(20) NOT NULL,
  country VARCHAR(100) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for commercial properties
CREATE TABLE commercial_properties (
  id INT AUTO_INCREMENT,
  property_type_id INT NOT NULL,
  location_id INT NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  square_footage INT,
  lot_size DECIMAL(10, 2),
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (property_type_id) REFERENCES property_types(id),
  FOREIGN KEY (location_id) REFERENCES locations(id)
);

-- Create a table for property features
CREATE TABLE property_features (
  id INT AUTO_INCREMENT,
  commercial_property_id INT NOT NULL,
  feature_name VARCHAR(255) NOT NULL,
  feature_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (commercial_property_id) REFERENCES commercial_properties(id)
);

-- Create a table for property listings
CREATE TABLE property_listings (
  id INT AUTO_INCREMENT,
  commercial_property_id INT NOT NULL,
  listing_agent VARCHAR(255) NOT NULL,
  listing_date DATE NOT NULL,
  expiration_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (commercial_property_id) REFERENCES commercial_properties(id)
);

-- Insert sample data into property types table
INSERT INTO property_types (type_name, description)
VALUES 
('Retail', 'Retail space for sale'),
('Office', 'Office space for sale'),
('Industrial', 'Industrial property for sale'),
('Restaurant', 'Restaurant space for sale');

-- Insert sample data into locations table
INSERT INTO locations (address, city, state, zip_code, country)
VALUES 
('123 Main St', 'Anytown', 'CA', '12345', 'USA'),
('456 Elm St', 'Othertown', 'NY', '67890', 'USA');

-- Insert sample data into commercial properties table
INSERT INTO commercial_properties (property_type_id, location_id, price, square_footage, lot_size, description)
VALUES 
(1, 1, 500000.00, 2000, 0.50, 'Great retail space for sale in Anytown'),
(2, 2, 750000.00, 3000, 1.00, 'Office space for sale in Othertown');

-- Insert sample data into property features table
INSERT INTO property_features (commercial_property_id, feature_name, feature_description)
VALUES 
(1, 'Parking', 'Ample parking available'),
(1, 'High Ceilings', 'High ceilings for retail display'),
(2, 'Security System', 'State-of-the-art security system');

-- Insert sample data into property listings table
INSERT INTO property_listings (commercial_property_id, listing_agent, listing_date, expiration_date)
VALUES 
(1, 'John Doe', '2022-01-01', '2023-01-01'),
(2, 'Jane Smith', '2022-06-01', '2023-06-01');
```
