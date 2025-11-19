"""
Generated Code Metadata:
========================
Original URL: https://piscorealestate.com
Prompt: "Create a SQL database schema to store information about properties, including features like price, location, number of bedrooms, and amenities."
Generated: DETERMINISTIC_f8d20f05efd80fc0
Batch ID: 20250622_211659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for property information
CREATE DATABASE property_database;

-- Use the property database
USE property_database;

-- Create a table for locations
CREATE TABLE locations (
    location_id INT AUTO_INCREMENT,
    street_address VARCHAR(255) NOT NULL,
    city VARCHAR(100) NOT NULL,
    state VARCHAR(100) NOT NULL,
    postal_code VARCHAR(20) NOT NULL,
    country VARCHAR(100) NOT NULL,
    latitude DECIMAL(10, 8) NOT NULL,
    longitude DECIMAL(11, 8) NOT NULL,
    PRIMARY KEY (location_id)
);

-- Create a table for amenities
CREATE TABLE amenities (
    amenity_id INT AUTO_INCREMENT,
    amenity_name VARCHAR(100) NOT NULL,
    description TEXT,
    PRIMARY KEY (amenity_id)
);

-- Create a many-to-many relationship table for property amenities
CREATE TABLE property_amenities (
    property_id INT NOT NULL,
    amenity_id INT NOT NULL,
    PRIMARY KEY (property_id, amenity_id),
    FOREIGN KEY (property_id) REFERENCES properties(property_id),
    FOREIGN KEY (amenity_id) REFERENCES amenities(amenity_id)
);

-- Create a table for properties
CREATE TABLE properties (
    property_id INT AUTO_INCREMENT,
    location_id INT NOT NULL,
    price DECIMAL(15, 2) NOT NULL,
    num_bedrooms INT NOT NULL,
    num_bathrooms INT,
    sqft INT,
    lot_size DECIMAL(10, 2),
    property_type ENUM('Residential', 'Commercial') NOT NULL,
    status ENUM('Active', 'Pending', 'Sold') NOT NULL DEFAULT 'Active',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (property_id),
    FOREIGN KEY (location_id) REFERENCES locations(location_id)
);

-- Create a table for property features
CREATE TABLE property_features (
    feature_id INT AUTO_INCREMENT,
    property_id INT NOT NULL,
    feature_name VARCHAR(100) NOT NULL,
    feature_value VARCHAR(255),
    PRIMARY KEY (feature_id),
    FOREIGN KEY (property_id) REFERENCES properties(property_id)
);

-- Create indexes for faster queries
CREATE INDEX idx_properties_location_id ON properties (location_id);
CREATE INDEX idx_properties_price ON properties (price);
CREATE INDEX idx_properties_num_bedrooms ON properties (num_bedrooms);
CREATE INDEX idx_property_amenities_property_id ON property_amenities (property_id);
CREATE INDEX idx_property_amenities_amenity_id ON property_amenities (amenity_id);
```
