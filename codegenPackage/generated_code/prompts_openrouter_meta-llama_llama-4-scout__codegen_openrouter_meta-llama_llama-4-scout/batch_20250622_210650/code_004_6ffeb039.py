"""
Generated Code Metadata:
========================
Original URL: https://agnelosfx.in
Prompt: "Design a database schema for storing information about special effects equipment and their usage in events like weddings and movies."
Generated: DETERMINISTIC_6ffeb03904eb89c3
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for storing special effects equipment and their usage
CREATE DATABASE special_effects;

-- Use the database
USE special_effects;

-- Create table for equipment categories
CREATE TABLE equipment_categories (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for equipment
CREATE TABLE equipment (
  id INT AUTO_INCREMENT,
  category_id INT NOT NULL,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  rental_cost DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (category_id) REFERENCES equipment_categories(id) ON DELETE CASCADE
);

-- Create table for event types
CREATE TABLE event_types (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for events
CREATE TABLE events (
  id INT AUTO_INCREMENT,
  event_type_id INT NOT NULL,
  name VARCHAR(255) NOT NULL,
  date DATE NOT NULL,
  start_time TIME NOT NULL,
  end_time TIME NOT NULL,
  location VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (event_type_id) REFERENCES event_types(id) ON DELETE CASCADE
);

-- Create table for equipment usage
CREATE TABLE equipment_usage (
  id INT AUTO_INCREMENT,
  event_id INT NOT NULL,
  equipment_id INT NOT NULL,
  quantity INT NOT NULL,
  rental_duration INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (event_id) REFERENCES events(id) ON DELETE CASCADE,
  FOREIGN KEY (equipment_id) REFERENCES equipment(id) ON DELETE CASCADE
);

-- Create table for equipment maintenance
CREATE TABLE equipment_maintenance (
  id INT AUTO_INCREMENT,
  equipment_id INT NOT NULL,
  maintenance_date DATE NOT NULL,
  description TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (equipment_id) REFERENCES equipment(id) ON DELETE CASCADE
);

-- Create table for equipment suppliers
CREATE TABLE equipment_suppliers (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  contact_name VARCHAR(255) NOT NULL,
  contact_email VARCHAR(255) NOT NULL,
  contact_phone VARCHAR(20) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for equipment purchases
CREATE TABLE equipment_purchases (
  id INT AUTO_INCREMENT,
  equipment_id INT NOT NULL,
  supplier_id INT NOT NULL,
  purchase_date DATE NOT NULL,
  cost DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (equipment_id) REFERENCES equipment(id) ON DELETE CASCADE,
  FOREIGN KEY (supplier_id) REFERENCES equipment_suppliers(id) ON DELETE CASCADE
);

-- Example data for testing
INSERT INTO equipment_categories (name, description) 
VALUES 
('Pyrotechnics', 'Fireworks and flame effects'),
('Lighting', 'Stage and event lighting'),
('Special Effects', 'Smoke, fog, and haze machines');

INSERT INTO equipment (category_id, name, description, rental_cost) 
VALUES 
(1, 'Pyrotechnic Launcher', 'A machine that launches fireworks', 500.00),
(2, 'LED Light Panel', 'A high-intensity LED light panel', 200.00),
(3, 'Fog Machine', 'A machine that produces fog effects', 100.00);

INSERT INTO event_types (name, description) 
VALUES 
('Wedding', 'A wedding event'),
('Movie', 'A movie production'),
('Theater', 'A theater performance');

INSERT INTO events (event_type_id, name, date, start_time, end_time, location) 
VALUES 
(1, 'John Doe Wedding', '2024-06-01', '14:00:00', '18:00:00', 'New York'),
(2, 'Movie Shoot', '2024-07-01', '08:00:00', '18:00:00', 'Los Angeles'),
(3, 'Theater Performance', '2024-08-01', '19:00:00', '22:00:00', 'Broadway');

INSERT INTO equipment_usage (event_id, equipment_id, quantity, rental_duration) 
VALUES 
(1, 1, 2, 4),
(1, 2, 5, 4),
(2, 3, 1, 8);

INSERT INTO equipment_maintenance (equipment_id, maintenance_date, description) 
VALUES 
(1, '2024-01-01', 'Regular maintenance'),
(2, '2024-02-01', 'Replaced light bulbs');

INSERT INTO equipment_suppliers (name, contact_name, contact_email, contact_phone) 
VALUES 
('Pyrotechnic Supplies', 'John Smith', 'john.smith@pyrotechnicsupplies.com', '123-456-7890'),
('Lighting Solutions', 'Jane Doe', 'jane.doe@lightingsolutions.com', '987-654-3210');

INSERT INTO equipment_purchases (equipment_id, supplier_id, purchase_date, cost) 
VALUES 
(1, 1, '2024-03-01', 1000.00),
(2, 2, '2024-04-01', 500.00);
```
