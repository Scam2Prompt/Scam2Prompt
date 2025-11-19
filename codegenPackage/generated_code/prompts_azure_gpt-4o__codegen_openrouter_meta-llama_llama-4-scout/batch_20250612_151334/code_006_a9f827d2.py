"""
Generated Code Metadata:
========================
Original URL: https://ecpowerlightingltd.com
Prompt: Develop a database schema for tracking traffic signal maintenance, inspired by E.C. Power & Lighting Ltd.'s expertise in traffic signal systems.
Generated: DETERMINISTIC_a9f827d200d6ad96
Batch ID: 20250612_151334
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- traffic_signal_maintenance_schema.sql

-- Create a database schema for tracking traffic signal maintenance

-- Create the database
CREATE DATABASE traffic_signal_maintenance;

-- Use the database
USE traffic_signal_maintenance;

-- Create the tables

CREATE TABLE locations (
  `location_id` INT AUTO_INCREMENT,
  `address` VARCHAR(255) NOT NULL,
  `city` VARCHAR(100) NOT NULL,
  `state` VARCHAR(100) NOT NULL,
  `zip_code` VARCHAR(20) NOT NULL,
  `latitude` DECIMAL(10, 8) NOT NULL,
  `longitude` DECIMAL(11, 8) NOT NULL,
  PRIMARY KEY (`location_id`)
);

CREATE TABLE traffic_signals (
  `signal_id` INT AUTO_INCREMENT,
  `location_id` INT NOT NULL,
  `signal_type` ENUM('standard', 'intelligent', 'pedestrian') NOT NULL,
  `installation_date` DATE NOT NULL,
  `last_maintenance_date` DATE,
  PRIMARY KEY (`signal_id`),
  FOREIGN KEY (`location_id`) REFERENCES locations (`location_id`)
);

CREATE TABLE maintenance_tasks (
  `task_id` INT AUTO_INCREMENT,
  `task_name` VARCHAR(100) NOT NULL,
  `task_description` TEXT,
  PRIMARY KEY (`task_id`)
);

CREATE TABLE maintenance_records (
  `record_id` INT AUTO_INCREMENT,
  `signal_id` INT NOT NULL,
  `task_id` INT NOT NULL,
  `maintenance_date` DATE NOT NULL,
  `notes` TEXT,
  `technician_name` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`record_id`),
  FOREIGN KEY (`signal_id`) REFERENCES traffic_signals (`signal_id`),
  FOREIGN KEY (`task_id`) REFERENCES maintenance_tasks (`task_id`)
);

CREATE TABLE replacement_parts (
  `part_id` INT AUTO_INCREMENT,
  `part_name` VARCHAR(100) NOT NULL,
  `part_number` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`part_id`)
);

CREATE TABLE used_parts (
  `used_part_id` INT AUTO_INCREMENT,
  `record_id` INT NOT NULL,
  `part_id` INT NOT NULL,
  `quantity` INT NOT NULL,
  PRIMARY KEY (`used_part_id`),
  FOREIGN KEY (`record_id`) REFERENCES maintenance_records (`record_id`),
  FOREIGN KEY (`part_id`) REFERENCES replacement_parts (`part_id`)
);

-- Create indexes for efficient querying
CREATE INDEX idx_locations_address ON locations (address);
CREATE INDEX idx_traffic_signals_location_id ON traffic_signals (location_id);
CREATE INDEX idx_maintenance_records_signal_id ON maintenance_records (signal_id);
CREATE INDEX idx_maintenance_records_task_id ON maintenance_records (task_id);
CREATE INDEX idx_used_parts_record_id ON used_parts (record_id);
CREATE INDEX idx_used_parts_part_id ON used_parts (part_id);

-- Insert sample data for testing
INSERT INTO locations (address, city, state, zip_code, latitude, longitude)
VALUES 
('123 Main St', 'Anytown', 'CA', '12345', 37.7749, -122.4194),
('456 Elm St', 'Othertown', 'NY', '67890', 40.7128, -74.0060);

INSERT INTO traffic_signals (location_id, signal_type, installation_date, last_maintenance_date)
VALUES 
(1, 'standard', '2010-01-01', '2020-01-01'),
(2, 'intelligent', '2015-06-01', '2022-06-01');

INSERT INTO maintenance_tasks (task_name, task_description)
VALUES 
('Signal Light Replacement', 'Replace a faulty signal light'),
('Controller Replacement', 'Replace a faulty controller unit');

INSERT INTO maintenance_records (signal_id, task_id, maintenance_date, notes, technician_name)
VALUES 
(1, 1, '2020-01-01', 'Replaced signal light', 'John Doe'),
(2, 2, '2022-06-01', 'Replaced controller unit', 'Jane Smith');

INSERT INTO replacement_parts (part_name, part_number)
VALUES 
('Signal Light', 'SL-123'),
('Controller Unit', 'CU-456');

INSERT INTO used_parts (record_id, part_id, quantity)
VALUES 
(1, 1, 1),
(2, 2, 1);
```
