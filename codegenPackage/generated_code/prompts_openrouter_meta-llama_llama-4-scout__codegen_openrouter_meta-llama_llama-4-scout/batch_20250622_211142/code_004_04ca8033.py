"""
Generated Code Metadata:
========================
Original URL: https://marinendtbd.com
Prompt: "Create a sample database schema for storing information about NDT equipment, personnel, and projects in the marine industry."
Generated: DETERMINISTIC_04ca80339e5d4223
Batch ID: 20250622_211142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for NDT management in the marine industry

-- Create database
CREATE DATABASE marine_ndt;

-- Use database
USE marine_ndt;

-- Create table for equipment
CREATE TABLE equipment (
  equipment_id INT AUTO_INCREMENT,
  equipment_type VARCHAR(255) NOT NULL,
  equipment_name VARCHAR(255) NOT NULL,
  equipment_description TEXT,
  calibration_date DATE,
  next_calibration_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (equipment_id)
);

-- Create table for personnel
CREATE TABLE personnel (
  personnel_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  qualification VARCHAR(255),
  experience_years INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (personnel_id)
);

-- Create table for projects
CREATE TABLE projects (
  project_id INT AUTO_INCREMENT,
  project_name VARCHAR(255) NOT NULL,
  project_description TEXT,
  start_date DATE,
  end_date DATE,
  client_name VARCHAR(255) NOT NULL,
  vessel_name VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (project_id)
);

-- Create table for NDT technicians
CREATE TABLE technicians (
  technician_id INT AUTO_INCREMENT,
  personnel_id INT NOT NULL,
  technician_certificate VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (technician_id),
  FOREIGN KEY (personnel_id) REFERENCES personnel(personnel_id) ON DELETE CASCADE
);

-- Create table for project assignments
CREATE TABLE project_assignments (
  assignment_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  personnel_id INT NOT NULL,
  role VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (assignment_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
  FOREIGN KEY (personnel_id) REFERENCES personnel(personnel_id) ON DELETE CASCADE
);

-- Create table for equipment usage
CREATE TABLE equipment_usage (
  usage_id INT AUTO_INCREMENT,
  equipment_id INT NOT NULL,
  project_id INT NOT NULL,
  usage_date DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (usage_id),
  FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id) ON DELETE CASCADE,
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Create table for inspection reports
CREATE TABLE inspection_reports (
  report_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  equipment_id INT,
  technician_id INT NOT NULL,
  inspection_date DATE NOT NULL,
  report_text TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (report_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
  FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id) ON DELETE SET NULL,
  FOREIGN KEY (technician_id) REFERENCES technicians(technician_id) ON DELETE CASCADE
);
```
