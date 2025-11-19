"""
Generated Code Metadata:
========================
Original URL: https://coworkingcomercio.com.br
Prompt: "Design a database schema to store information about coworking spaces, including their location, infrastructure, and available plans, using a relational database management system."
Generated: DETERMINISTIC_987c8d3e619d590b
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for coworking spaces
CREATE DATABASE coworking_spaces;

-- Use the database
USE coworking_spaces;

-- Create a table for locations
CREATE TABLE locations (
  id INT AUTO_INCREMENT,
  address VARCHAR(255) NOT NULL,
  city VARCHAR(100) NOT NULL,
  state VARCHAR(100) NOT NULL,
  country VARCHAR(100) NOT NULL,
  zip_code VARCHAR(20) NOT NULL,
  latitude DECIMAL(10, 8) NOT NULL,
  longitude DECIMAL(11, 8) NOT NULL,
  PRIMARY KEY (id)
);

-- Create a table for infrastructures
CREATE TABLE infrastructures (
  id INT AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  description TEXT,
  PRIMARY KEY (id)
);

-- Create a table for infrastructure options
CREATE TABLE infrastructure_options (
  id INT AUTO_INCREMENT,
  infrastructure_id INT NOT NULL,
  option_name VARCHAR(100) NOT NULL,
  option_description TEXT,
  PRIMARY KEY (id),
  FOREIGN KEY (infrastructure_id) REFERENCES infrastructures(id) ON DELETE CASCADE
);

-- Create a table for plans
CREATE TABLE plans (
  id INT AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (id)
);

-- Create a table for coworking spaces
CREATE TABLE coworking_spaces (
  id INT AUTO_INCREMENT,
  location_id INT NOT NULL,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  PRIMARY KEY (id),
  FOREIGN KEY (location_id) REFERENCES locations(id) ON DELETE CASCADE
);

-- Create a many-to-many relationship table for coworking space infrastructures
CREATE TABLE coworking_space_infrastructures (
  coworking_space_id INT NOT NULL,
  infrastructure_id INT NOT NULL,
  PRIMARY KEY (coworking_space_id, infrastructure_id),
  FOREIGN KEY (coworking_space_id) REFERENCES coworking_spaces(id) ON DELETE CASCADE,
  FOREIGN KEY (infrastructure_id) REFERENCES infrastructures(id) ON DELETE CASCADE
);

-- Create a many-to-many relationship table for coworking space plans
CREATE TABLE coworking_space_plans (
  coworking_space_id INT NOT NULL,
  plan_id INT NOT NULL,
  PRIMARY KEY (coworking_space_id, plan_id),
  FOREIGN KEY (coworking_space_id) REFERENCES coworking_spaces(id) ON DELETE CASCADE,
  FOREIGN KEY (plan_id) REFERENCES plans(id) ON DELETE CASCADE
);

-- Insert sample data
INSERT INTO locations (address, city, state, country, zip_code, latitude, longitude)
VALUES 
  ('123 Main St', 'New York', 'NY', 'USA', '10001', 40.7128, -74.0060),
  ('456 Broadway', 'San Francisco', 'CA', 'USA', '94111', 37.7749, -122.4194);

INSERT INTO infrastructures (name, description)
VALUES 
  ('High-speed internet', 'Fast and reliable internet connection'),
  ('Meeting rooms', 'Fully equipped meeting rooms');

INSERT INTO infrastructure_options (infrastructure_id, option_name, option_description)
VALUES 
  (1, 'Wi-Fi', 'Wireless internet connection'),
  (1, 'Ethernet', 'Wired internet connection'),
  (2, 'Whiteboard', 'Whiteboard for presentations');

INSERT INTO plans (name, description, price)
VALUES 
  ('Basic', 'Basic plan with limited access', 100.00),
  ('Premium', 'Premium plan with full access', 500.00);

INSERT INTO coworking_spaces (location_id, name, description)
VALUES 
  (1, 'NYC Coworking', 'Coworking space in New York City'),
  (2, 'SF Coworking', 'Coworking space in San Francisco');

INSERT INTO coworking_space_infrastructures (coworking_space_id, infrastructure_id)
VALUES 
  (1, 1),
  (1, 2),
  (2, 1);

INSERT INTO coworking_space_plans (coworking_space_id, plan_id)
VALUES 
  (1, 1),
  (1, 2),
  (2, 1);
```
