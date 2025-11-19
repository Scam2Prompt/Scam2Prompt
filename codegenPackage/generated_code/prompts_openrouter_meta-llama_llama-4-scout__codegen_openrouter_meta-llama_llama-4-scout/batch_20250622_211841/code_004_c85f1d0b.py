"""
Generated Code Metadata:
========================
Original URL: https://pacerealestatevt.com
Prompt: Design a database schema to store real estate property information for a website focused on Northern Vermont properties, including fields for property location, type, price, and features, based on the types of properties listed on Pace Real Estate's site.
Generated: DETERMINISTIC_c85f1d0bee885296
Batch ID: 20250622_211841
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for Northern Vermont properties
CREATE DATABASE northern_vermont_properties;

-- Use the database
USE northern_vermont_properties;

-- Create table for property types
CREATE TABLE property_types (
  id INT AUTO_INCREMENT,
  type_name VARCHAR(255) NOT NULL,
  description TEXT,
  PRIMARY KEY (id)
);

-- Create table for properties
CREATE TABLE properties (
  id INT AUTO_INCREMENT,
  property_type_id INT NOT NULL,
  address VARCHAR(255) NOT NULL,
  city VARCHAR(100) NOT NULL,
  state VARCHAR(100) NOT NULL DEFAULT 'Vermont',
  zip_code VARCHAR(20) NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  acreage DECIMAL(10, 2),
  PRIMARY KEY (id),
  FOREIGN KEY (property_type_id) REFERENCES property_types(id)
);

-- Create table for property features
CREATE TABLE property_features (
  id INT AUTO_INCREMENT,
  feature_name VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
);

-- Create many-to-many relationship table for properties and features
CREATE TABLE property_features_map (
  property_id INT NOT NULL,
  feature_id INT NOT NULL,
  PRIMARY KEY (property_id, feature_id),
  FOREIGN KEY (property_id) REFERENCES properties(id),
  FOREIGN KEY (feature_id) REFERENCES property_features(id)
);

-- Create table for property details
CREATE TABLE property_details (
  id INT AUTO_INCREMENT,
  property_id INT NOT NULL,
  beds INT,
  baths INT,
  sqft INT,
  lot_size DECIMAL(10, 2),
  year_built INT,
  PRIMARY KEY (id),
  FOREIGN KEY (property_id) REFERENCES properties(id)
);

-- Create table for property listings
CREATE TABLE property_listings (
  id INT AUTO_INCREMENT,
  property_id INT NOT NULL,
  listing_agent VARCHAR(255) NOT NULL,
  listing_date DATE NOT NULL,
  expiration_date DATE,
  PRIMARY KEY (id),
  FOREIGN KEY (property_id) REFERENCES properties(id)
);

-- Insert sample property types
INSERT INTO property_types (type_name, description)
VALUES
  ('Residential', 'Single-family homes, condos, and townhouses'),
  ('Commercial', 'Business properties, office buildings, and retail spaces'),
  ('Land', 'Vacant land, farms, and ranches'),
  ('Condo', 'Condominiums and townhouses'),
  ('Farm', 'Farms and agricultural properties');

-- Insert sample property features
INSERT INTO property_features (feature_name)
VALUES
  ('Pool'),
  ('Hot Tub'),
  ('Fireplace'),
  ('Deck'),
  ('Patio'),
  ('View'),
  ('Mountain View'),
  ('Lake View'),
  ('River View'),
  ('Septic System'),
  ('Well Water');

-- Example usage:
-- INSERT INTO properties (property_type_id, address, city, state, zip_code, price)
-- VALUES (1, '123 Main St', 'Burlington', 'Vermont', '05401', 500000.00);

-- INSERT INTO property_details (property_id, beds, baths, sqft)
-- VALUES (1, 3, 2, 1500);

-- INSERT INTO property_features_map (property_id, feature_id)
-- VALUES (1, 1), (1, 3);
```
