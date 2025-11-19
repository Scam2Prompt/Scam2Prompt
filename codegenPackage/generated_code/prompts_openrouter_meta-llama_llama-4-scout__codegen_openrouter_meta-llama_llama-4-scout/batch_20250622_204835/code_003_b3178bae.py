"""
Generated Code Metadata:
========================
Original URL: https://opensea.gr
Prompt: Design a database schema for storing information about RIBs, their features, and charter services, using OpenSea's fleet and services as an example.
Generated: DETERMINISTIC_b3178bae58183b40
Batch ID: 20250622_204835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- rib_database_schema.sql

-- Create a database for storing RIB information
CREATE DATABASE rib_database;

-- Use the rib_database
USE rib_database;

-- Create a table for RIB manufacturers
CREATE TABLE manufacturers (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for RIB models
CREATE TABLE rib_models (
  id INT AUTO_INCREMENT,
  manufacturer_id INT NOT NULL,
  model_name VARCHAR(255) NOT NULL,
  length DECIMAL(4, 2) NOT NULL,
  beam DECIMAL(4, 2) NOT NULL,
  draft DECIMAL(4, 2) NOT NULL,
  top_speed DECIMAL(5, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (manufacturer_id) REFERENCES manufacturers(id) ON DELETE CASCADE
);

-- Create a table for RIB features
CREATE TABLE rib_features (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a many-to-many relationship table for RIB models and features
CREATE TABLE rib_model_features (
  rib_model_id INT NOT NULL,
  feature_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (rib_model_id, feature_id),
  FOREIGN KEY (rib_model_id) REFERENCES rib_models(id) ON DELETE CASCADE,
  FOREIGN KEY (feature_id) REFERENCES rib_features(id) ON DELETE CASCADE
);

-- Create a table for charter services
CREATE TABLE charter_services (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for RIB charter services
CREATE TABLE rib_charter_services (
  id INT AUTO_INCREMENT,
  rib_model_id INT NOT NULL,
  charter_service_id INT NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (rib_model_id) REFERENCES rib_models(id) ON DELETE CASCADE,
  FOREIGN KEY (charter_service_id) REFERENCES charter_services(id) ON DELETE CASCADE
);

-- Create a table for charter bookings
CREATE TABLE charter_bookings (
  id INT AUTO_INCREMENT,
  rib_model_id INT NOT NULL,
  charter_date DATE NOT NULL,
  start_time TIME NOT NULL,
  end_time TIME NOT NULL,
  customer_name VARCHAR(255) NOT NULL,
  customer_email VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (rib_model_id) REFERENCES rib_models(id) ON DELETE CASCADE
);

-- Example data
INSERT INTO manufacturers (name, description) 
VALUES 
('OpenSea', 'OpenSea is a leading manufacturer of high-quality RIBs');

INSERT INTO rib_models (manufacturer_id, model_name, length, beam, draft, top_speed) 
VALUES 
(1, 'OS 650', 6.5, 2.5, 0.9, 35.00);

INSERT INTO rib_features (name, description) 
VALUES 
('Navigation Lights', 'High-intensity navigation lights for increased visibility'),
('Bimini Top', 'A stylish bimini top for sun protection');

INSERT INTO rib_model_features (rib_model_id, feature_id) 
VALUES 
(1, 1),
(1, 2);

INSERT INTO charter_services (name, description) 
VALUES 
('Half-Day Charter', 'A 4-hour charter experience'),
('Full-Day Charter', 'An 8-hour charter experience');

INSERT INTO rib_charter_services (rib_model_id, charter_service_id, price) 
VALUES 
(1, 1, 500.00),
(1, 2, 800.00);

INSERT INTO charter_bookings (rib_model_id, charter_date, start_time, end_time, customer_name, customer_email) 
VALUES 
(1, '2024-09-17', '09:00:00', '13:00:00', 'John Doe', 'john@example.com');
```
