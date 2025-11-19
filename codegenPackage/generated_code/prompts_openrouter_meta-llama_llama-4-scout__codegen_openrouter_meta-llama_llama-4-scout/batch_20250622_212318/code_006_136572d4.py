"""
Generated Code Metadata:
========================
Original URL: https://förderohr.de
Prompt: Generate a sample database schema for storing customer information, appointments, and services offered by a plumbing company like ERA ElbeRohr & Abwassertechnik GmbH & Co. KG.
Generated: DETERMINISTIC_136572d4dda1ec3f
Batch ID: 20250622_212318
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for plumbing company
CREATE DATABASE plumbing_company;

-- Use the database
USE plumbing_company;

-- Create table for customers
CREATE TABLE customers (
  customer_id INT AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  address VARCHAR(255) NOT NULL,
  city VARCHAR(50) NOT NULL,
  state VARCHAR(50) NOT NULL,
  zip_code VARCHAR(10) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (customer_id)
);

-- Create table for services offered
CREATE TABLE services (
  service_id INT AUTO_INCREMENT,
  service_name VARCHAR(100) NOT NULL,
  service_description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (service_id)
);

-- Create table for appointments
CREATE TABLE appointments (
  appointment_id INT AUTO_INCREMENT,
  customer_id INT NOT NULL,
  service_id INT NOT NULL,
  appointment_date DATE NOT NULL,
  appointment_time TIME NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (appointment_id),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
  FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE
);

-- Create table for technicians
CREATE TABLE technicians (
  technician_id INT AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (technician_id)
);

-- Create table for appointment technicians
CREATE TABLE appointment_technicians (
  appointment_id INT NOT NULL,
  technician_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (appointment_id, technician_id),
  FOREIGN KEY (appointment_id) REFERENCES appointments(appointment_id) ON DELETE CASCADE,
  FOREIGN KEY (technician_id) REFERENCES technicians(technician_id) ON DELETE CASCADE
);

-- Create indexes for foreign keys
CREATE INDEX idx_appointments_customer_id ON appointments(customer_id);
CREATE INDEX idx_appointments_service_id ON appointments(service_id);
CREATE INDEX idx_appointment_technicians_appointment_id ON appointment_technicians(appointment_id);
CREATE INDEX idx_appointment_technicians_technician_id ON appointment_technicians(technician_id);
```

```sql
-- sample_data.sql

-- Insert sample data into customers table
INSERT INTO customers (first_name, last_name, email, phone_number, address, city, state, zip_code)
VALUES
  ('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St', 'Anytown', 'CA', '12345'),
  ('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', '456 Elm St', 'Othertown', 'NY', '67890');

-- Insert sample data into services table
INSERT INTO services (service_name, service_description, price)
VALUES
  ('Drain Cleaning', 'Cleaning of clogged drains', 100.00),
  ('Pipe Repair', 'Repair of leaky pipes', 200.00),
  ('Toilet Installation', 'Installation of new toilets', 500.00);

-- Insert sample data into appointments table
INSERT INTO appointments (customer_id, service_id, appointment_date, appointment_time, description)
VALUES
  (1, 1, '2024-09-20', '09:00:00', 'Drain cleaning for John Doe'),
  (2, 2, '2024-09-22', '10:00:00', 'Pipe repair for Jane Smith');

-- Insert sample data into technicians table
INSERT INTO technicians (first_name, last_name, email, phone_number)
VALUES
  ('Bob', 'Johnson', 'bob.johnson@example.com', '555-123-4567'),
  ('Alice', 'Williams', 'alice.williams@example.com', '555-987-6543');

-- Insert sample data into appointment_technicians table
INSERT INTO appointment_technicians (appointment_id, technician_id)
VALUES
  (1, 1),
  (2, 2);
```
