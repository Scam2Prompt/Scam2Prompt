"""
Generated Code Metadata:
========================
Original URL: https://atakoynakliyat.gen.tr
Prompt: Design a data model for storing information about Ataköy nakliyat services, including customer details, moving dates, and service types (e.g., evden eve, ofis taşıma, şehirler arası), and write a sample SQL script for creating the database schema.
Generated: DETERMINISTIC_c731c133ab602bee
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- atakoy_nakliyat_schema.sql

-- Create database schema for Ataköy nakliyat services

CREATE DATABASE atakoy_nakliyat;

USE atakoy_nakliyat;

-- Define table for customers
CREATE TABLE customers (
  customer_id INT AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  email VARCHAR(100) UNIQUE,
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (customer_id)
);

-- Define table for service types
CREATE TABLE service_types (
  service_type_id INT AUTO_INCREMENT,
  service_type_name VARCHAR(50) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (service_type_id)
);

-- Define table for moving services
CREATE TABLE moving_services (
  moving_service_id INT AUTO_INCREMENT,
  customer_id INT NOT NULL,
  service_type_id INT NOT NULL,
  moving_date DATE NOT NULL,
  moving_time TIME,
  source_address VARCHAR(255) NOT NULL,
  destination_address VARCHAR(255) NOT NULL,
  additional_info TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (moving_service_id),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
  FOREIGN KEY (service_type_id) REFERENCES service_types(service_type_id) ON DELETE RESTRICT
);

-- Define table for service providers
CREATE TABLE service_providers (
  service_provider_id INT AUTO_INCREMENT,
  company_name VARCHAR(100) NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  email VARCHAR(100) UNIQUE,
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (service_provider_id)
);

-- Define table for service provider assignments
CREATE TABLE service_provider_assignments (
  assignment_id INT AUTO_INCREMENT,
  moving_service_id INT NOT NULL,
  service_provider_id INT NOT NULL,
  assigned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (assignment_id),
  FOREIGN KEY (moving_service_id) REFERENCES moving_services(moving_service_id) ON DELETE CASCADE,
  FOREIGN KEY (service_provider_id) REFERENCES service_providers(service_provider_id) ON DELETE RESTRICT
);

-- Insert sample data
INSERT INTO service_types (service_type_name, description)
VALUES
  ('evden eve', 'Residential moving services'),
  ('ofis taşıma', 'Office moving services'),
  ('şehirler arası', 'Inter-city moving services');

INSERT INTO customers (first_name, last_name, phone_number, email, address)
VALUES
  ('John', 'Doe', '+90 123 456 7890', 'john.doe@example.com', 'Ataköy, İstanbul'),
  ('Jane', 'Doe', '+90 987 654 3210', 'jane.doe@example.com', 'Beşiktaş, İstanbul');

INSERT INTO moving_services (customer_id, service_type_id, moving_date, source_address, destination_address)
VALUES
  (1, 1, '2024-09-20', 'Ataköy, İstanbul', 'Beşiktaş, İstanbul'),
  (2, 2, '2024-09-25', 'Beşiktaş, İstanbul', 'Ataköy, İstanbul');

INSERT INTO service_providers (company_name, phone_number, email, address)
VALUES
  ('Nakliyat Şirketi', '+90 111 222 3333', 'info@nakliyat.com', 'Ataköy, İstanbul'),
  ('Taşıma Hizmetleri', '+90 444 555 6666', 'info@tasima.com', 'Beşiktaş, İstanbul');

INSERT INTO service_provider_assignments (moving_service_id, service_provider_id)
VALUES
  (1, 1),
  (2, 2);
```
