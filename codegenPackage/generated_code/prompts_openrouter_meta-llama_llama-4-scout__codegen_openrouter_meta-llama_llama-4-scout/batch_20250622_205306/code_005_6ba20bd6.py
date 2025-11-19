"""
Generated Code Metadata:
========================
Original URL: https://multiservicios3l.com
Prompt: Develop a simple database schema to store information about industrial machinery, including maintenance records and repair history, inspired by Multiservicios 3L's maintenance and repair services.
Generated: DETERMINISTIC_6ba20bd6b6223a7d
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for industrial machinery
CREATE DATABASE industrial_machinery;

-- Use the database
USE industrial_machinery;

-- Create table for machinery
CREATE TABLE machinery (
  id INT AUTO_INCREMENT,
  type VARCHAR(255) NOT NULL,
  model VARCHAR(255) NOT NULL,
  serial_number VARCHAR(255) UNIQUE NOT NULL,
  purchase_date DATE,
  PRIMARY KEY (id)
);

-- Create table for maintenance records
CREATE TABLE maintenance_records (
  id INT AUTO_INCREMENT,
  machinery_id INT NOT NULL,
  maintenance_date DATE NOT NULL,
  description TEXT,
  performed_by VARCHAR(255) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (machinery_id) REFERENCES machinery(id) ON DELETE CASCADE
);

-- Create table for repair history
CREATE TABLE repair_history (
  id INT AUTO_INCREMENT,
  machinery_id INT NOT NULL,
  repair_date DATE NOT NULL,
  description TEXT,
  performed_by VARCHAR(255) NOT NULL,
  cost DECIMAL(10, 2),
  PRIMARY KEY (id),
  FOREIGN KEY (machinery_id) REFERENCES machinery(id) ON DELETE CASCADE
);

-- Create table for spare parts
CREATE TABLE spare_parts (
  id INT AUTO_INCREMENT,
  part_number VARCHAR(255) UNIQUE NOT NULL,
  description TEXT,
  quantity INT,
  PRIMARY KEY (id)
);

-- Create table for spare parts usage
CREATE TABLE spare_parts_usage (
  id INT AUTO_INCREMENT,
  repair_history_id INT NOT NULL,
  spare_part_id INT NOT NULL,
  quantity_used INT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (repair_history_id) REFERENCES repair_history(id) ON DELETE CASCADE,
  FOREIGN KEY (spare_part_id) REFERENCES spare_parts(id) ON DELETE CASCADE
);

-- Create indexes for foreign keys
CREATE INDEX idx_maintenance_records_machinery_id ON maintenance_records (machinery_id);
CREATE INDEX idx_repair_history_machinery_id ON repair_history (machinery_id);
CREATE INDEX idx_spare_parts_usage_repair_history_id ON spare_parts_usage (repair_history_id);
CREATE INDEX idx_spare_parts_usage_spare_part_id ON spare_parts_usage (spare_part_id);

-- Example data
INSERT INTO machinery (type, model, serial_number, purchase_date)
VALUES 
('Pump', 'ABC123', 'SN12345', '2020-01-01'),
('Motor', 'DEF456', 'SN67890', '2019-06-01');

INSERT INTO maintenance_records (machinery_id, maintenance_date, description, performed_by)
VALUES 
(1, '2022-01-01', 'Regular maintenance', 'John Doe'),
(2, '2022-06-01', 'Regular maintenance', 'Jane Smith');

INSERT INTO repair_history (machinery_id, repair_date, description, performed_by, cost)
VALUES 
(1, '2022-02-01', 'Repaired pump', 'John Doe', 1000.00),
(2, '2022-07-01', 'Repaired motor', 'Jane Smith', 2000.00);

INSERT INTO spare_parts (part_number, description, quantity)
VALUES 
('SP12345', 'Pump seal', 10),
('SP67890', 'Motor bearing', 5);

INSERT INTO spare_parts_usage (repair_history_id, spare_part_id, quantity_used)
VALUES 
(1, 1, 2),
(2, 2, 1);
```
