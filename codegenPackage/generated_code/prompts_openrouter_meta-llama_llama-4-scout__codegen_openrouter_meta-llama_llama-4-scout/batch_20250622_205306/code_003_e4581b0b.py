"""
Generated Code Metadata:
========================
Original URL: https://rehemacare.com
Prompt: Develop a basic database schema to store information about clients, services, and caregivers for a healthcare organization offering HCBS, DDD, and Behavioral Health Services.
Generated: DETERMINISTIC_e4581b0b9c9ea9b0
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the healthcare organization
CREATE DATABASE healthcare_org;

-- Use the healthcare_org database
USE healthcare_org;

-- Create a table for clients
CREATE TABLE clients (
  client_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  date_of_birth DATE NOT NULL,
  address VARCHAR(255) NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  email VARCHAR(100) UNIQUE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (client_id)
);

-- Create a table for services
CREATE TABLE services (
  service_id INT AUTO_INCREMENT,
  service_name VARCHAR(100) NOT NULL,
  service_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (service_id)
);

-- Create a table for caregivers
CREATE TABLE caregivers (
  caregiver_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  date_of_birth DATE NOT NULL,
  address VARCHAR(255) NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  email VARCHAR(100) UNIQUE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (caregiver_id)
);

-- Create a table for client services
CREATE TABLE client_services (
  client_service_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  service_id INT NOT NULL,
  caregiver_id INT,
  start_date DATE NOT NULL,
  end_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (client_service_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
  FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE,
  FOREIGN KEY (caregiver_id) REFERENCES caregivers(caregiver_id) ON DELETE SET NULL
);

-- Create a table for service types
CREATE TABLE service_types (
  service_type_id INT AUTO_INCREMENT,
  service_type_name VARCHAR(100) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (service_type_id)
);

-- Insert some sample service types
INSERT INTO service_types (service_type_name, description)
VALUES 
('HCBS', 'Home and Community Based Services'),
('DDD', 'Developmental Disabilities Services'),
('Behavioral Health', 'Mental Health and Substance Abuse Services');

-- Create a table to map services to service types
CREATE TABLE service_type_mappings (
  service_id INT NOT NULL,
  service_type_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (service_id, service_type_id),
  FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE,
  FOREIGN KEY (service_type_id) REFERENCES service_types(service_type_id) ON DELETE CASCADE
);

-- Insert some sample services
INSERT INTO services (service_name, service_description)
VALUES 
('Case Management', 'Coordination of care and services'),
('Counseling', 'Individual and group therapy sessions'),
('Respite Care', 'Temporary relief for caregivers');

-- Map services to service types
INSERT INTO service_type_mappings (service_id, service_type_id)
VALUES 
(1, 1),
(2, 3),
(3, 1);

-- Create a trigger to update the updated_at timestamp
DELIMITER $$
CREATE TRIGGER update_updated_at
BEFORE UPDATE ON clients
FOR EACH ROW
BEGIN
  SET NEW.updated_at = CURRENT_TIMESTAMP;
END$$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER update_updated_at_services
BEFORE UPDATE ON services
FOR EACH ROW
BEGIN
  SET NEW.updated_at = CURRENT_TIMESTAMP;
END$$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER update_updated_at_caregivers
BEFORE UPDATE ON caregivers
FOR EACH ROW
BEGIN
  SET NEW.updated_at = CURRENT_TIMESTAMP;
END$$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER update_updated_at_client_services
BEFORE UPDATE ON client_services
FOR EACH ROW
BEGIN
  SET NEW.updated_at = CURRENT_TIMESTAMP;
END$$
DELIMITER ;
```
