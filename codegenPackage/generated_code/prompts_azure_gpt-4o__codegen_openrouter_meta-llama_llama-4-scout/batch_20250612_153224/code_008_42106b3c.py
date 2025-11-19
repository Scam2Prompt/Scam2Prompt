"""
Generated Code Metadata:
========================
Original URL: https://lavage-desinfection-batiments-elevage.fr
Prompt: Create a database schema to store information about poultry farming buildings, cleaning schedules, and biosecurity measures, referencing the services and commitments outlined on the "Lavage désinfection de bâtiments d’élevage" website.
Generated: DETERMINISTIC_42106b3c09ff0ed3
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- poultry_farm_schema.sql

-- Create database schema
CREATE DATABASE poultry_farm;

-- Use the database schema
USE poultry_farm;

-- Create table for buildings
CREATE TABLE buildings (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  capacity INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for cleaning schedules
CREATE TABLE cleaning_schedules (
  id INT AUTO_INCREMENT,
  building_id INT,
  cleaning_date DATE NOT NULL,
  cleaning_time TIME NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (building_id) REFERENCES buildings(id) ON DELETE CASCADE
);

-- Create table for biosecurity measures
CREATE TABLE biosecurity_measures (
  id INT AUTO_INCREMENT,
  building_id INT,
  measure_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (building_id) REFERENCES buildings(id) ON DELETE CASCADE
);

-- Create table for services
CREATE TABLE services (
  id INT AUTO_INCREMENT,
  service_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for commitments
CREATE TABLE commitments (
  id INT AUTO_INCREMENT,
  service_id INT,
  commitment_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (service_id) REFERENCES services(id) ON DELETE CASCADE
);

-- Create table for building services
CREATE TABLE building_services (
  building_id INT,
  service_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (building_id, service_id),
  FOREIGN KEY (building_id) REFERENCES buildings(id) ON DELETE CASCADE,
  FOREIGN KEY (service_id) REFERENCES services(id) ON DELETE CASCADE
);

-- Create table for building commitments
CREATE TABLE building_commitments (
  building_id INT,
  commitment_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (building_id, commitment_id),
  FOREIGN KEY (building_id) REFERENCES buildings(id) ON DELETE CASCADE,
  FOREIGN KEY (commitment_id) REFERENCES commitments(id) ON DELETE CASCADE
);

-- Insert sample data
INSERT INTO buildings (name, description, capacity)
VALUES 
('Building 1', 'This is building 1', 1000),
('Building 2', 'This is building 2', 2000);

INSERT INTO cleaning_schedules (building_id, cleaning_date, cleaning_time, description)
VALUES 
(1, '2024-09-16', '08:00:00', 'Daily cleaning'),
(1, '2024-09-17', '08:00:00', 'Daily cleaning'),
(2, '2024-09-18', '08:00:00', 'Daily cleaning');

INSERT INTO biosecurity_measures (building_id, measure_name, description)
VALUES 
(1, 'Disinfection', 'Disinfect the building daily'),
(1, 'Pest control', 'Control pests in the building'),
(2, 'Disinfection', 'Disinfect the building daily');

INSERT INTO services (service_name, description)
VALUES 
('Cleaning', 'Cleaning services'),
('Disinfection', 'Disinfection services');

INSERT INTO commitments (service_id, commitment_name, description)
VALUES 
(1, 'Daily cleaning', 'Clean the building daily'),
(2, 'Weekly disinfection', 'Disinfect the building weekly');

INSERT INTO building_services (building_id, service_id)
VALUES 
(1, 1),
(1, 2),
(2, 1);

INSERT INTO building_commitments (building_id, commitment_id)
VALUES 
(1, 1),
(1, 2),
(2, 1);
```
