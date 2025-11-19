"""
Generated Code Metadata:
========================
Original URL: https://felixtrujillofalla.com
Prompt: "Design a database schema for a real estate platform that includes tables for properties (with types like apartments, houses, offices), locations (cities, neighborhoods), and property features (number of bedrooms, bathrooms, parking spots), considering the services offered by Inmobiliaria Félix Trujillo Falla."
Generated: DETERMINISTIC_1029e59c48086193
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for real estate platform
CREATE DATABASE inmobiliaria_felix_trujillo_falla;

-- Use database
USE inmobiliaria_felix_trujillo_falla;

-- Create table for locations (cities)
CREATE TABLE cities (
    city_id INT AUTO_INCREMENT,
    city_name VARCHAR(255) NOT NULL,
    state VARCHAR(255) NOT NULL,
    country VARCHAR(255) NOT NULL,
    PRIMARY KEY (city_id)
);

-- Create table for neighborhoods
CREATE TABLE neighborhoods (
    neighborhood_id INT AUTO_INCREMENT,
    neighborhood_name VARCHAR(255) NOT NULL,
    city_id INT NOT NULL,
    PRIMARY KEY (neighborhood_id),
    FOREIGN KEY (city_id) REFERENCES cities(city_id)
);

-- Create table for property types
CREATE TABLE property_types (
    property_type_id INT AUTO_INCREMENT,
    property_type_name VARCHAR(255) NOT NULL,
    PRIMARY KEY (property_type_id)
);

-- Insert property types (apartments, houses, offices)
INSERT INTO property_types (property_type_name)
VALUES 
('Apartment'),
('House'),
('Office');

-- Create table for properties
CREATE TABLE properties (
    property_id INT AUTO_INCREMENT,
    property_type_id INT NOT NULL,
    neighborhood_id INT NOT NULL,
    address VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (property_id),
    FOREIGN KEY (property_type_id) REFERENCES property_types(property_type_id),
    FOREIGN KEY (neighborhood_id) REFERENCES neighborhoods(neighborhood_id)
);

-- Create table for property features
CREATE TABLE property_features (
    property_feature_id INT AUTO_INCREMENT,
    property_id INT NOT NULL,
    number_of_bedrooms INT,
    number_of_bathrooms INT,
    number_of_parking_spots INT,
    square_footage DECIMAL(10, 2),
    PRIMARY KEY (property_feature_id),
    FOREIGN KEY (property_id) REFERENCES properties(property_id)
);

-- Create table for services offered
CREATE TABLE services (
    service_id INT AUTO_INCREMENT,
    service_name VARCHAR(255) NOT NULL,
    PRIMARY KEY (service_id)
);

-- Insert services offered by Inmobiliaria Félix Trujillo Falla
INSERT INTO services (service_name)
VALUES 
('Property Management'),
('Real Estate Consulting'),
('Property Valuation');

-- Create table for property services
CREATE TABLE property_services (
    property_id INT NOT NULL,
    service_id INT NOT NULL,
    PRIMARY KEY (property_id, service_id),
    FOREIGN KEY (property_id) REFERENCES properties(property_id),
    FOREIGN KEY (service_id) REFERENCES services(service_id)
);

-- Create index on foreign keys
CREATE INDEX idx_properties_neighborhood_id ON properties (neighborhood_id);
CREATE INDEX idx_properties_property_type_id ON properties (property_type_id);
CREATE INDEX idx_property_features_property_id ON property_features (property_id);
CREATE INDEX idx_property_services_property_id ON property_services (property_id);
CREATE INDEX idx_property_services_service_id ON property_services (service_id);
```
