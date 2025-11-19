"""
Generated Code Metadata:
========================
Original URL: https://carehelpers.pt
Prompt: "Design a database schema to store information about clients, caregivers, and services provided by a home care company like CARE HELPERS."
Generated: DETERMINISTIC_16875a7cdd155ffd
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the home care company
CREATE DATABASE care_helpers;

-- Use the care_helpers database
USE care_helpers;

-- Create a table to store client information
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

-- Create a table to store caregiver information
CREATE TABLE caregivers (
  caregiver_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  date_of_birth DATE NOT NULL,
  address VARCHAR(255) NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  email VARCHAR(100) UNIQUE,
  qualifications VARCHAR(255),
  experience INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (caregiver_id)
);

-- Create a table to store service information
CREATE TABLE services (
  service_id INT AUTO_INCREMENT,
  service_name VARCHAR(255) NOT NULL,
  description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (service_id)
);

-- Create a table to store client-caregiver assignments
CREATE TABLE client_caregiver_assignments (
  assignment_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  caregiver_id INT NOT NULL,
  assigned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (assignment_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
  FOREIGN KEY (caregiver_id) REFERENCES caregivers(caregiver_id) ON DELETE CASCADE,
  UNIQUE (client_id, caregiver_id)
);

-- Create a table to store service bookings
CREATE TABLE service_bookings (
  booking_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  service_id INT NOT NULL,
  booking_date DATE NOT NULL,
  booking_time TIME NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (booking_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
  FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE
);

-- Create a table to store caregiver service provision
CREATE TABLE caregiver_service_provision (
  provision_id INT AUTO_INCREMENT,
  caregiver_id INT NOT NULL,
  service_id INT NOT NULL,
  client_id INT NOT NULL,
  provision_date DATE NOT NULL,
  provision_time TIME NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (provision_id),
  FOREIGN KEY (caregiver_id) REFERENCES caregivers(caregiver_id) ON DELETE CASCADE,
  FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE,
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Create indexes on foreign key columns
CREATE INDEX idx_client_caregiver_assignments_client_id ON client_caregiver_assignments(client_id);
CREATE INDEX idx_client_caregiver_assignments_caregiver_id ON client_caregiver_assignments(caregiver_id);
CREATE INDEX idx_service_bookings_client_id ON service_bookings(client_id);
CREATE INDEX idx_service_bookings_service_id ON service_bookings(service_id);
CREATE INDEX idx_caregiver_service_provision_caregiver_id ON caregiver_service_provision(caregiver_id);
CREATE INDEX idx_caregiver_service_provision_service_id ON caregiver_service_provision(service_id);
CREATE INDEX idx_caregiver_service_provision_client_id ON caregiver_service_provision(client_id);
```
