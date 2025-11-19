"""
Generated Code Metadata:
========================
Original URL: https://theprintnan.app
Prompt: "Design a database schema for storing information about various printing services, including อักษรโลหะ, อักษรอะคริลิค/คอมโพสิต, and สติ๊กเกอร์ไดคัท."
Generated: DETERMINISTIC_f5f2dae725c74fdd
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- printing_services_schema.sql

-- Create a database schema for storing information about various printing services

CREATE DATABASE printing_services;

USE printing_services;

-- Define a table for printing services
CREATE TABLE printing_services (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Define a table for service types
CREATE TABLE service_types (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Insert service types
INSERT INTO service_types (name, description) 
VALUES 
  ('อักษรโลหะ', 'Metal lettering service'),
  ('อักษรอะคริลิค/คอมโพสิต', 'Acrylic/Composite lettering service'),
  ('สติ๊กเกอร์ไดคัท', 'Sticker cutting service');

-- Define a table for service providers
CREATE TABLE service_providers (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone VARCHAR(20),
  address TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Define a table for printing service offerings
CREATE TABLE service_offerings (
  id INT AUTO_INCREMENT,
  service_provider_id INT NOT NULL,
  service_type_id INT NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (service_provider_id) REFERENCES service_providers(id),
  FOREIGN KEY (service_type_id) REFERENCES service_types(id)
);

-- Define a table for customer orders
CREATE TABLE customer_orders (
  id INT AUTO_INCREMENT,
  customer_name VARCHAR(255) NOT NULL,
  service_offering_id INT NOT NULL,
  order_date DATE NOT NULL,
  delivery_date DATE,
  status VARCHAR(50) NOT NULL DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (service_offering_id) REFERENCES service_offerings(id)
);

-- Create indexes for efficient querying
CREATE INDEX idx_service_providers_email ON service_providers(email);
CREATE INDEX idx_service_offerings_service_provider_id ON service_offerings(service_provider_id);
CREATE INDEX idx_service_offerings_service_type_id ON service_offerings(service_type_id);
CREATE INDEX idx_customer_orders_service_offering_id ON customer_orders(service_offering_id);
```
