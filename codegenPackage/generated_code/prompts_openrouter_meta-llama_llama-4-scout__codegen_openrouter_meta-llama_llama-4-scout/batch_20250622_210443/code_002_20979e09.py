"""
Generated Code Metadata:
========================
Original URL: https://jlelectricista.com
Prompt: Generate a sample database schema for storing information about electrical services, including client details, service types (residential/commercial), and job status.
Generated: DETERMINISTIC_20979e0920225bc5
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- electrical_services_schema.sql

-- Create database
CREATE DATABASE IF NOT EXISTS electrical_services;

-- Use database
USE electrical_services;

-- Create table for clients
CREATE TABLE IF NOT EXISTS clients (
  client_id INT AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  address VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (client_id)
);

-- Create table for service types
CREATE TABLE IF NOT EXISTS service_types (
  service_type_id INT AUTO_INCREMENT,
  service_type VARCHAR(50) NOT NULL CHECK (service_type IN ('residential', 'commercial')),
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (service_type_id)
);

-- Insert default service types
INSERT INTO service_types (service_type, description) 
VALUES 
('residential', 'Electrical services for residential areas'),
('commercial', 'Electrical services for commercial areas');

-- Create table for jobs
CREATE TABLE IF NOT EXISTS jobs (
  job_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  service_type_id INT NOT NULL,
  job_status VARCHAR(50) NOT NULL CHECK (job_status IN ('pending', 'in_progress', 'completed', 'cancelled')),
  job_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (job_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
  FOREIGN KEY (service_type_id) REFERENCES service_types(service_type_id) ON DELETE RESTRICT
);

-- Create table for technicians
CREATE TABLE IF NOT EXISTS technicians (
  technician_id INT AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (technician_id)
);

-- Create table for job assignments
CREATE TABLE IF NOT EXISTS job_assignments (
  job_assignment_id INT AUTO_INCREMENT,
  job_id INT NOT NULL,
  technician_id INT NOT NULL,
  assigned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (job_assignment_id),
  FOREIGN KEY (job_id) REFERENCES jobs(job_id) ON DELETE CASCADE,
  FOREIGN KEY (technician_id) REFERENCES technicians(technician_id) ON DELETE RESTRICT
);

-- Create indexes
CREATE INDEX idx_client_id ON jobs(client_id);
CREATE INDEX idx_service_type_id ON jobs(service_type_id);
CREATE INDEX idx_job_id ON job_assignments(job_id);
CREATE INDEX idx_technician_id ON job_assignments(technician_id);
```
