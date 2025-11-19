"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-209--nervous-kare-6f3c45.netlify.app
Prompt: Design a simple database schema to store information about recycling centers and collection routes for a city like York.
Generated: DETERMINISTIC_81be54931d9bf94e
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for recycling center information
CREATE DATABASE york_recycling;

-- Use the york_recycling database
USE york_recycling;

-- Create table for recycling centers
CREATE TABLE recycling_centers (
  center_id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  address VARCHAR(255) NOT NULL,
  city VARCHAR(100) NOT NULL,
  state VARCHAR(100) NOT NULL,
  zip_code VARCHAR(20) NOT NULL,
  phone_number VARCHAR(20),
  email VARCHAR(100),
  hours_of_operation TEXT,
  PRIMARY KEY (center_id)
);

-- Create table for collection routes
CREATE TABLE collection_routes (
  route_id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  PRIMARY KEY (route_id)
);

-- Create table for collection route stops
CREATE TABLE collection_route_stops (
  stop_id INT AUTO_INCREMENT,
  route_id INT NOT NULL,
  stop_name VARCHAR(255) NOT NULL,
  address VARCHAR(255) NOT NULL,
  collection_day ENUM('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday') NOT NULL,
  collection_time TIME NOT NULL,
  PRIMARY KEY (stop_id),
  FOREIGN KEY (route_id) REFERENCES collection_routes(route_id)
);

-- Create table for recycling center collection routes
CREATE TABLE center_routes (
  center_id INT NOT NULL,
  route_id INT NOT NULL,
  PRIMARY KEY (center_id, route_id),
  FOREIGN KEY (center_id) REFERENCES recycling_centers(center_id),
  FOREIGN KEY (route_id) REFERENCES collection_routes(route_id)
);

-- Create table for accepted materials at recycling centers
CREATE TABLE accepted_materials (
  material_id INT AUTO_INCREMENT,
  center_id INT NOT NULL,
  material_name VARCHAR(100) NOT NULL,
  description TEXT,
  PRIMARY KEY (material_id),
  FOREIGN KEY (center_id) REFERENCES recycling_centers(center_id)
);

-- Example data insertion
INSERT INTO recycling_centers (name, address, city, state, zip_code, phone_number, email, hours_of_operation)
VALUES 
('York Recycling Center', '123 Main St', 'York', 'PA', '17401', '555-555-5555', 'info@yorkrecycling.com', 'Mon-Fri 8am-5pm');

INSERT INTO collection_routes (name, description)
VALUES 
('Route 1', 'Collection route for downtown York'),
('Route 2', 'Collection route for uptown York');

INSERT INTO collection_route_stops (route_id, stop_name, address, collection_day, collection_time)
VALUES 
(1, 'Stop 1', '456 Elm St', 'Monday', '08:00:00'),
(1, 'Stop 2', '789 Oak St', 'Wednesday', '14:00:00'),
(2, 'Stop 3', '321 Pine St', 'Friday', '10:00:00');

INSERT INTO center_routes (center_id, route_id)
VALUES 
(1, 1),
(1, 2);

INSERT INTO accepted_materials (center_id, material_name, description)
VALUES 
(1, 'Paper', 'Newspaper, cardboard, and mixed paper'),
(1, 'Plastic', 'Bottles, jugs, and containers');
```
