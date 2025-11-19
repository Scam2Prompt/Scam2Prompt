"""
Generated Code Metadata:
========================
Original URL: https://co-djs.com
Prompt: Design a database schema to store information about DJ services, including packages (e.g., "Full" DJ Package with a 3.1 channel 3000 watt PA), add-ons (e.g., karaoke, video, and lighting), and client event details.
Generated: DETERMINISTIC_f5f7af00351687c5
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for DJ services
CREATE DATABASE dj_services;

-- Use the dj_services database
USE dj_services;

-- Create table for packages
CREATE TABLE packages (
  package_id INT AUTO_INCREMENT,
  package_name VARCHAR(255) NOT NULL,
  package_description TEXT,
  package_price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (package_id)
);

-- Create table for add-ons
CREATE TABLE add_ons (
  add_on_id INT AUTO_INCREMENT,
  add_on_name VARCHAR(255) NOT NULL,
  add_on_description TEXT,
  add_on_price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (add_on_id)
);

-- Create table for package add-ons
CREATE TABLE package_add_ons (
  package_id INT NOT NULL,
  add_on_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (package_id, add_on_id),
  FOREIGN KEY (package_id) REFERENCES packages(package_id) ON DELETE CASCADE,
  FOREIGN KEY (add_on_id) REFERENCES add_ons(add_on_id) ON DELETE CASCADE
);

-- Create table for clients
CREATE TABLE clients (
  client_id INT AUTO_INCREMENT,
  client_name VARCHAR(255) NOT NULL,
  client_email VARCHAR(255) UNIQUE NOT NULL,
  client_phone VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (client_id)
);

-- Create table for events
CREATE TABLE events (
  event_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  package_id INT NOT NULL,
  event_date DATE NOT NULL,
  event_time TIME NOT NULL,
  event_location VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (event_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
  FOREIGN KEY (package_id) REFERENCES packages(package_id) ON DELETE CASCADE
);

-- Create table for event add-ons
CREATE TABLE event_add_ons (
  event_id INT NOT NULL,
  add_on_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (event_id, add_on_id),
  FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE,
  FOREIGN KEY (add_on_id) REFERENCES add_ons(add_on_id) ON DELETE CASCADE
);

-- Create table for payments
CREATE TABLE payments (
  payment_id INT AUTO_INCREMENT,
  event_id INT NOT NULL,
  payment_date DATE NOT NULL,
  payment_amount DECIMAL(10, 2) NOT NULL,
  payment_method VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (payment_id),
  FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE
);
```

```sql
-- example_data.sql

-- Insert example data into packages table
INSERT INTO packages (package_name, package_description, package_price)
VALUES 
('Full DJ Package', 'Our full DJ package includes a 3.1 channel 3000 watt PA', 1000.00),
('Basic DJ Package', 'Our basic DJ package includes a 2.1 channel 1000 watt PA', 500.00);

-- Insert example data into add_ons table
INSERT INTO add_ons (add_on_name, add_on_description, add_on_price)
VALUES 
('Karaoke', 'Add karaoke to your event', 200.00),
('Video', 'Add video services to your event', 300.00),
('Lighting', 'Add custom lighting to your event', 400.00);

-- Insert example data into package_add_ons table
INSERT INTO package_add_ons (package_id, add_on_id)
VALUES 
(1, 1),
(1, 2),
(2, 3);

-- Insert example data into clients table
INSERT INTO clients (client_name, client_email, client_phone)
VALUES 
('John Doe', 'john.doe@example.com', '123-456-7890'),
('Jane Doe', 'jane.doe@example.com', '987-654-3210');

-- Insert example data into events table
INSERT INTO events (client_id, package_id, event_date, event_time, event_location)
VALUES 
(1, 1, '2024-09-20', '18:00:00', 'New York'),
(2, 2, '2024-10-01', '19:00:00', 'Los Angeles');

-- Insert example data into event_add_ons table
INSERT INTO event_add_ons (event_id, add_on_id)
VALUES 
(1, 1),
(2, 3);

-- Insert example data into payments table
INSERT INTO payments (event_id, payment_date, payment_amount, payment_method)
VALUES 
(1, '2024-09-01', 1200.00, 'Credit Card'),
(2, '2024-09-15', 700.00, 'Cash');
```
