"""
Generated Code Metadata:
========================
Original URL: https://germanierpropiedades.com
Prompt: "Design a database schema for storing real estate property listings, including details like location, price, property type, and contact information for the agency."
Generated: DETERMINISTIC_9a3ac5267714dfb4
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for real estate property listings
CREATE DATABASE real_estate;

-- Use the real_estate database
USE real_estate;

-- Create a table for locations
CREATE TABLE locations (
  location_id INT AUTO_INCREMENT,
  address VARCHAR(255) NOT NULL,
  city VARCHAR(100) NOT NULL,
  state VARCHAR(100) NOT NULL,
  zip_code VARCHAR(20) NOT NULL,
  country VARCHAR(100) NOT NULL,
  PRIMARY KEY (location_id)
);

-- Create a table for property types
CREATE TABLE property_types (
  property_type_id INT AUTO_INCREMENT,
  property_type VARCHAR(100) NOT NULL,
  description TEXT,
  PRIMARY KEY (property_type_id)
);

-- Create a table for agencies
CREATE TABLE agencies (
  agency_id INT AUTO_INCREMENT,
  agency_name VARCHAR(255) NOT NULL,
  phone_number VARCHAR(20),
  email VARCHAR(100) UNIQUE,
  PRIMARY KEY (agency_id)
);

-- Create a table for contacts
CREATE TABLE contacts (
  contact_id INT AUTO_INCREMENT,
  agency_id INT,
  contact_name VARCHAR(100) NOT NULL,
  phone_number VARCHAR(20),
  email VARCHAR(100) UNIQUE,
  PRIMARY KEY (contact_id),
  FOREIGN KEY (agency_id) REFERENCES agencies(agency_id)
);

-- Create a table for property listings
CREATE TABLE property_listings (
  listing_id INT AUTO_INCREMENT,
  location_id INT,
  agency_id INT,
  property_type_id INT,
  price DECIMAL(10, 2) NOT NULL,
  square_footage INT,
  bedrooms INT,
  bathrooms INT,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (listing_id),
  FOREIGN KEY (location_id) REFERENCES locations(location_id),
  FOREIGN KEY (agency_id) REFERENCES agencies(agency_id),
  FOREIGN KEY (property_type_id) REFERENCES property_types(property_type_id)
);

-- Create indexes for efficient querying
CREATE INDEX idx_location_id ON property_listings (location_id);
CREATE INDEX idx_agency_id ON property_listings (agency_id);
CREATE INDEX idx_property_type_id ON property_listings (property_type_id);

-- Insert sample data
INSERT INTO locations (address, city, state, zip_code, country)
VALUES 
('123 Main St', 'Anytown', 'CA', '12345', 'USA'),
('456 Elm St', 'Othertown', 'NY', '67890', 'USA');

INSERT INTO property_types (property_type, description)
VALUES 
('Residential', 'Single-family home'),
('Commercial', 'Office building');

INSERT INTO agencies (agency_name, phone_number, email)
VALUES 
('Anytown Realty', '555-1234', 'info@anytownrealty.com'),
('Othertown Properties', '555-5678', 'info@othertownproperties.com');

INSERT INTO contacts (agency_id, contact_name, phone_number, email)
VALUES 
(1, 'John Doe', '555-9012', 'john.doe@anytownrealty.com'),
(2, 'Jane Smith', '555-1111', 'jane.smith@othertownproperties.com');

INSERT INTO property_listings (location_id, agency_id, property_type_id, price, square_footage, bedrooms, bathrooms, description)
VALUES 
(1, 1, 1, 500000.00, 2000, 4, 2, 'Beautiful single-family home in Anytown'),
(2, 2, 2, 1000000.00, 5000, 0, 0, 'Commercial office building in Othertown');
```
