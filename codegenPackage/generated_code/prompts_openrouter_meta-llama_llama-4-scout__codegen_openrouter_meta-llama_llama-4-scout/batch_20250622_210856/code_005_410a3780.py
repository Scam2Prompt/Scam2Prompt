"""
Generated Code Metadata:
========================
Original URL: https://presval.co
Prompt: Design a database schema for storing property listings and their associated details, suitable for a real estate platform like Presval, and write SQL queries to retrieve specific data.
Generated: DETERMINISTIC_410a37801a5b242a
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema
CREATE DATABASE presval;

-- Use database
USE presval;

-- Create table for property listings
CREATE TABLE properties (
    id INT AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

-- Create table for property types
CREATE TABLE property_types (
    id INT AUTO_INCREMENT,
    type_name VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);

-- Create table for property features
CREATE TABLE property_features (
    id INT AUTO_INCREMENT,
    feature_name VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);

-- Create table for property listings with types and features
CREATE TABLE property_listings (
    id INT AUTO_INCREMENT,
    property_id INT NOT NULL,
    property_type_id INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (property_id) REFERENCES properties(id),
    FOREIGN KEY (property_type_id) REFERENCES property_types(id)
);

-- Create table for property features mapping
CREATE TABLE property_features_map (
    property_id INT NOT NULL,
    feature_id INT NOT NULL,
    PRIMARY KEY (property_id, feature_id),
    FOREIGN KEY (property_id) REFERENCES properties(id),
    FOREIGN KEY (feature_id) REFERENCES property_features(id)
);

-- Create table for property locations
CREATE TABLE property_locations (
    id INT AUTO_INCREMENT,
    property_id INT NOT NULL,
    address VARCHAR(255) NOT NULL,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL,
    zip_code VARCHAR(10) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (property_id) REFERENCES properties(id)
);

-- Create table for property agents
CREATE TABLE agents (
    id INT AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    PRIMARY KEY (id)
);

-- Create table for property agents mapping
CREATE TABLE property_agents_map (
    property_id INT NOT NULL,
    agent_id INT NOT NULL,
    PRIMARY KEY (property_id, agent_id),
    FOREIGN KEY (property_id) REFERENCES properties(id),
    FOREIGN KEY (agent_id) REFERENCES agents(id)
);

-- Insert sample data
INSERT INTO property_types (type_name) 
VALUES 
('Residential'),
('Commercial'),
('Industrial');

INSERT INTO property_features (feature_name) 
VALUES 
('Swimming Pool'),
('Garden'),
('Parking');

INSERT INTO properties (title, description, price) 
VALUES 
('Luxury House', 'Beautiful 5 bedroom house', 500000.00),
('Office Space', 'Modern office space for rent', 2000.00),
('Warehouse', 'Large industrial warehouse for sale', 1000000.00);

INSERT INTO property_listings (property_id, property_type_id) 
VALUES 
(1, 1),
(2, 2),
(3, 3);

INSERT INTO property_features_map (property_id, feature_id) 
VALUES 
(1, 1),
(1, 2),
(2, 3);

INSERT INTO property_locations (property_id, address, city, state, zip_code) 
VALUES 
(1, '123 Main St', 'New York', 'NY', '10001'),
(2, '456 Broadway', 'Los Angeles', 'CA', '90001'),
(3, '789 Industrial Blvd', 'Chicago', 'IL', '60001');

INSERT INTO agents (name, email, phone) 
VALUES 
('John Doe', 'john.doe@example.com', '123-456-7890'),
('Jane Smith', 'jane.smith@example.com', '987-654-3210');

INSERT INTO property_agents_map (property_id, agent_id) 
VALUES 
(1, 1),
(2, 2),
(3, 1);

-- SQL queries to retrieve specific data

-- Retrieve all properties with their types and features
SELECT 
    p.id,
    p.title,
    pt.type_name,
    GROUP_CONCAT(pf.feature_name SEPARATOR ', ') as features
FROM 
    properties p
JOIN 
    property_listings pl ON p.id = pl.property_id
JOIN 
    property_types pt ON pl.property_type_id = pt.id
LEFT JOIN 
    property_features_map pfm ON p.id = pfm.property_id
LEFT JOIN 
    property_features pf ON pfm.feature_id = pf.id
GROUP BY 
    p.id;

-- Retrieve properties by city
SELECT 
    p.id,
    p.title,
    pl.address,
    pl.city,
    pl.state,
    pl.zip_code
FROM 
    properties p
JOIN 
    property_locations pl ON p.id = pl.property_id
WHERE 
    pl.city = 'New York';

-- Retrieve properties by agent
SELECT 
    p.id,
    p.title,
    a.name,
    a.email,
    a.phone
FROM 
    properties p
JOIN 
    property_agents_map pam ON p.id = pam.property_id
JOIN 
    agents a ON pam.agent_id = a.id
WHERE 
    a.name = 'John Doe';

-- Retrieve property details by id
SELECT 
    p.id,
    p.title,
    p.description,
    p.price,
    pt.type_name,
    GROUP_CONCAT(pf.feature_name SEPARATOR ', ') as features,
    pl.address,
    pl.city,
    pl.state,
    pl.zip_code,
    a.name,
    a.email,
    a.phone
FROM 
    properties p
JOIN 
    property_listings plst ON p.id = plst.property_id
JOIN 
    property_types pt ON plst.property_type_id = pt.id
LEFT JOIN 
    property_features_map pfm ON p.id = pfm.property_id
LEFT JOIN 
    property_features pf ON pfm.feature_id = pf.id
JOIN 
    property_locations pl ON p.id = pl.property_id
LEFT JOIN 
    property_agents_map pam ON p.id = pam.property_id
LEFT JOIN 
    agents a ON pam.agent_id = a.id
WHERE 
    p.id = 1;
```
