"""
Generated Code Metadata:
========================
Original URL: https://autocarescosme.com
Prompt: Generate a SQL database schema to store information about bus vehicles, including their capacity, accessibility features, and maintenance records, for a company like Autocares Cosme.
Generated: DETERMINISTIC_d9cb4d35f9eca28c
Batch ID: 20250622_212855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for Autocares Cosme
CREATE DATABASE autocares_cosme;

-- Use the autocares_cosme database
USE autocares_cosme;

-- Create a table for bus vehicles
CREATE TABLE vehicles (
  `id` INT AUTO_INCREMENT,
  `license_plate` VARCHAR(10) NOT NULL,
  `make` VARCHAR(50) NOT NULL,
  `model` VARCHAR(50) NOT NULL,
  `year` INT NOT NULL,
  `capacity` INT NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `license_plate` (`license_plate`)
);

-- Create a table for accessibility features
CREATE TABLE accessibility_features (
  `id` INT AUTO_INCREMENT,
  `name` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`)
);

-- Create a many-to-many relationship table for vehicle accessibility features
CREATE TABLE vehicle_accessibility_features (
  `vehicle_id` INT NOT NULL,
  `feature_id` INT NOT NULL,
  PRIMARY KEY (`vehicle_id`, `feature_id`),
  FOREIGN KEY (`vehicle_id`) REFERENCES vehicles (`id`) ON DELETE CASCADE,
  FOREIGN KEY (`feature_id`) REFERENCES accessibility_features (`id`) ON DELETE CASCADE
);

-- Create a table for maintenance records
CREATE TABLE maintenance_records (
  `id` INT AUTO_INCREMENT,
  `vehicle_id` INT NOT NULL,
  `maintenance_date` DATE NOT NULL,
  `description` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`vehicle_id`) REFERENCES vehicles (`id`) ON DELETE CASCADE
);

-- Create a table for maintenance types
CREATE TABLE maintenance_types (
  `id` INT AUTO_INCREMENT,
  `name` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`)
);

-- Create a many-to-many relationship table for maintenance records and types
CREATE TABLE maintenance_record_types (
  `maintenance_record_id` INT NOT NULL,
  `maintenance_type_id` INT NOT NULL,
  PRIMARY KEY (`maintenance_record_id`, `maintenance_type_id`),
  FOREIGN KEY (`maintenance_record_id`) REFERENCES maintenance_records (`id`) ON DELETE CASCADE,
  FOREIGN KEY (`maintenance_type_id`) REFERENCES maintenance_types (`id`) ON DELETE CASCADE
);

-- Insert some sample data
INSERT INTO vehicles (license_plate, make, model, year, capacity)
VALUES
  ('ABC123', 'Mercedes-Benz', 'Sprinter', 2015, 50),
  ('DEF456', 'Ford', 'Transit', 2018, 70);

INSERT INTO accessibility_features (name)
VALUES
  ('Wheelchair Ramp'),
  ('Lift'),
  ('Audio Announcements');

INSERT INTO vehicle_accessibility_features (vehicle_id, feature_id)
VALUES
  (1, 1),
  (1, 3),
  (2, 2);

INSERT INTO maintenance_types (name)
VALUES
  ('Oil Change'),
  ('Tire Rotation'),
  ('Brake Inspection');

INSERT INTO maintenance_records (vehicle_id, maintenance_date, description)
VALUES
  (1, '2022-01-01', 'Oil change and tire rotation'),
  (2, '2022-06-01', 'Brake inspection and repair');

INSERT INTO maintenance_record_types (maintenance_record_id, maintenance_type_id)
VALUES
  (1, 1),
  (1, 2),
  (2, 3);
```
