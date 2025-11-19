"""
Generated Code Metadata:
========================
Original URL: https://trackdieselperu.com
Prompt: "Create a SQL database schema to store information about heavy machinery, their spare parts, and maintenance services offered by a company like Track Diesel Peru S.R.L."
Generated: DETERMINISTIC_0391f4c7bb75d285
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

-- Create database
CREATE DATABASE track_diesel_peru;

-- Use database
USE track_diesel_peru;

-- Create table for heavy machinery
CREATE TABLE heavy_machinery (
  id INT AUTO_INCREMENT,
  type VARCHAR(255) NOT NULL,
  model VARCHAR(255) NOT NULL,
  serial_number VARCHAR(255) UNIQUE NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for spare parts
CREATE TABLE spare_parts (
  id INT AUTO_INCREMENT,
  part_number VARCHAR(255) NOT NULL,
  part_name VARCHAR(255) NOT NULL,
  description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  stock_quantity INT NOT NULL DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for machinery spare parts
CREATE TABLE machinery_spare_parts (
  machinery_id INT NOT NULL,
  spare_part_id INT NOT NULL,
  quantity INT NOT NULL DEFAULT 1,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (machinery_id, spare_part_id),
  FOREIGN KEY (machinery_id) REFERENCES heavy_machinery(id) ON DELETE CASCADE,
  FOREIGN KEY (spare_part_id) REFERENCES spare_parts(id) ON DELETE CASCADE
);

-- Create table for maintenance services
CREATE TABLE maintenance_services (
  id INT AUTO_INCREMENT,
  service_name VARCHAR(255) NOT NULL,
  description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for machinery maintenance services
CREATE TABLE machinery_maintenance_services (
  machinery_id INT NOT NULL,
  maintenance_service_id INT NOT NULL,
  service_date DATE NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (machinery_id, maintenance_service_id),
  FOREIGN KEY (machinery_id) REFERENCES heavy_machinery(id) ON DELETE CASCADE,
  FOREIGN KEY (maintenance_service_id) REFERENCES maintenance_services(id) ON DELETE CASCADE
);

-- Create table for maintenance service providers
CREATE TABLE maintenance_service_providers (
  id INT AUTO_INCREMENT,
  provider_name VARCHAR(255) NOT NULL,
  contact_person VARCHAR(255) NOT NULL,
  phone VARCHAR(20) NOT NULL,
  email VARCHAR(100) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for maintenance service provider assignments
CREATE TABLE maintenance_service_provider_assignments (
  maintenance_service_id INT NOT NULL,
  provider_id INT NOT NULL,
  assigned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (maintenance_service_id, provider_id),
  FOREIGN KEY (maintenance_service_id) REFERENCES maintenance_services(id) ON DELETE CASCADE,
  FOREIGN KEY (provider_id) REFERENCES maintenance_service_providers(id) ON DELETE CASCADE
);

-- Create indexes
CREATE INDEX idx_heavy_machinery_serial_number ON heavy_machinery (serial_number);
CREATE INDEX idx_spare_parts_part_number ON spare_parts (part_number);
CREATE INDEX idx_maintenance_services_service_name ON maintenance_services (service_name);
```
