"""
Generated Code Metadata:
========================
Original URL: https://cart3.pages.dev
Prompt: Develop a sample database schema for managing client information, appointment scheduling, and service offerings in a legal and accounting firm, based on the practice areas of Carthew Chau & Co.
Generated: DETERMINISTIC_f74cd68ea025f227
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the legal and accounting firm
CREATE DATABASE carthew_chau_co;

-- Use the database
USE carthew_chau_co;

-- Create a table for practice areas
CREATE TABLE practice_areas (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for service offerings
CREATE TABLE service_offerings (
  id INT AUTO_INCREMENT,
  practice_area_id INT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (practice_area_id) REFERENCES practice_areas(id) ON DELETE CASCADE
);

-- Create a table for clients
CREATE TABLE clients (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for appointments
CREATE TABLE appointments (
  id INT AUTO_INCREMENT,
  client_id INT,
  service_offering_id INT,
  appointment_date DATE NOT NULL,
  appointment_time TIME NOT NULL,
  location VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE,
  FOREIGN KEY (service_offering_id) REFERENCES service_offerings(id) ON DELETE CASCADE
);

-- Create a table for client contacts
CREATE TABLE client_contacts (
  id INT AUTO_INCREMENT,
  client_id INT,
  contact_name VARCHAR(255) NOT NULL,
  contact_email VARCHAR(255) NOT NULL,
  contact_phone_number VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE
);

-- Create a table for staff members
CREATE TABLE staff_members (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  role VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for appointment staff members
CREATE TABLE appointment_staff_members (
  appointment_id INT,
  staff_member_id INT,
  PRIMARY KEY (appointment_id, staff_member_id),
  FOREIGN KEY (appointment_id) REFERENCES appointments(id) ON DELETE CASCADE,
  FOREIGN KEY (staff_member_id) REFERENCES staff_members(id) ON DELETE CASCADE
);

-- Insert sample data into practice areas
INSERT INTO practice_areas (name, description)
VALUES
  ('Litigation', 'Dispute resolution and litigation services'),
  ('Taxation', 'Tax planning and compliance services'),
  ('Corporate Law', 'Company formation and corporate governance services');

-- Insert sample data into service offerings
INSERT INTO service_offerings (practice_area_id, name, description)
VALUES
  (1, 'Dispute Resolution', 'Expert dispute resolution services'),
  (1, 'Court Representation', 'Representation in court services'),
  (2, 'Tax Planning', 'Tax planning and optimization services'),
  (3, 'Company Formation', 'Company formation and registration services');

-- Insert sample data into clients
INSERT INTO clients (first_name, last_name, email, phone_number, address)
VALUES
  ('John', 'Doe', 'john.doe@example.com', '1234567890', '123 Main St'),
  ('Jane', 'Smith', 'jane.smith@example.com', '9876543210', '456 Elm St');

-- Insert sample data into appointments
INSERT INTO appointments (client_id, service_offering_id, appointment_date, appointment_time, location, description)
VALUES
  (1, 1, '2024-09-17', '10:00:00', 'Office', 'Initial consultation'),
  (2, 2, '2024-09-18', '14:00:00', 'Court', 'Court hearing');

-- Insert sample data into client contacts
INSERT INTO client_contacts (client_id, contact_name, contact_email, contact_phone_number)
VALUES
  (1, 'Jane Doe', 'jane.doe@example.com', '5551234567'),
  (2, 'Bob Smith', 'bob.smith@example.com', '5559876543');

-- Insert sample data into staff members
INSERT INTO staff_members (first_name, last_name, email, phone_number, role)
VALUES
  ('Alice', 'Johnson', 'alice.johnson@example.com', '1234567890', 'Lawyer'),
  ('Bob', 'Williams', 'bob.williams@example.com', '9876543210', 'Paralegal');

-- Insert sample data into appointment staff members
INSERT INTO appointment_staff_members (appointment_id, staff_member_id)
VALUES
  (1, 1),
  (2, 2);
```
