"""
Generated Code Metadata:
========================
Original URL: https://laotaigroup.com
Prompt: Develop a database schema for managing real estate assets and rental services, inspired by the operations of Lao Tai Trading - Investment Group.
Generated: DETERMINISTIC_1be63a220719483b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for real estate management
CREATE DATABASE real_estate_management;

-- Use the database
USE real_estate_management;

-- Create table for locations
CREATE TABLE locations (
  location_id INT AUTO_INCREMENT,
  address VARCHAR(255) NOT NULL,
  city VARCHAR(100) NOT NULL,
  state VARCHAR(100) NOT NULL,
  country VARCHAR(100) NOT NULL,
  zip_code VARCHAR(20) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (location_id)
);

-- Create table for property types
CREATE TABLE property_types (
  property_type_id INT AUTO_INCREMENT,
  type_name VARCHAR(100) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (property_type_id)
);

-- Create table for properties
CREATE TABLE properties (
  property_id INT AUTO_INCREMENT,
  location_id INT NOT NULL,
  property_type_id INT NOT NULL,
  property_name VARCHAR(255) NOT NULL,
  description TEXT,
  purchase_date DATE,
  purchase_price DECIMAL(10, 2),
  current_value DECIMAL(10, 2),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (property_id),
  FOREIGN KEY (location_id) REFERENCES locations(location_id),
  FOREIGN KEY (property_type_id) REFERENCES property_types(property_type_id)
);

-- Create table for rental services
CREATE TABLE rental_services (
  rental_service_id INT AUTO_INCREMENT,
  property_id INT NOT NULL,
  rental_type VARCHAR(100) NOT NULL,
  rental_price DECIMAL(10, 2) NOT NULL,
  security_deposit DECIMAL(10, 2) NOT NULL,
  lease_duration INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (rental_service_id),
  FOREIGN KEY (property_id) REFERENCES properties(property_id)
);

-- Create table for tenants
CREATE TABLE tenants (
  tenant_id INT AUTO_INCREMENT,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (tenant_id)
);

-- Create table for leases
CREATE TABLE leases (
  lease_id INT AUTO_INCREMENT,
  rental_service_id INT NOT NULL,
  tenant_id INT NOT NULL,
  lease_start_date DATE NOT NULL,
  lease_end_date DATE NOT NULL,
  rent DECIMAL(10, 2) NOT NULL,
  security_deposit DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (lease_id),
  FOREIGN KEY (rental_service_id) REFERENCES rental_services(rental_service_id),
  FOREIGN KEY (tenant_id) REFERENCES tenants(tenant_id)
);

-- Create table for payments
CREATE TABLE payments (
  payment_id INT AUTO_INCREMENT,
  lease_id INT NOT NULL,
  payment_date DATE NOT NULL,
  payment_amount DECIMAL(10, 2) NOT NULL,
  payment_method VARCHAR(100) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (payment_id),
  FOREIGN KEY (lease_id) REFERENCES leases(lease_id)
);

-- Create table for maintenance requests
CREATE TABLE maintenance_requests (
  maintenance_request_id INT AUTO_INCREMENT,
  property_id INT NOT NULL,
  tenant_id INT NOT NULL,
  request_date DATE NOT NULL,
  description TEXT NOT NULL,
  status VARCHAR(100) NOT NULL DEFAULT 'open',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (maintenance_request_id),
  FOREIGN KEY (property_id) REFERENCES properties(property_id),
  FOREIGN KEY (tenant_id) REFERENCES tenants(tenant_id)
);

-- Create table for maintenance services
CREATE TABLE maintenance_services (
  maintenance_service_id INT AUTO_INCREMENT,
  maintenance_request_id INT NOT NULL,
  service_date DATE NOT NULL,
  description TEXT NOT NULL,
  cost DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (maintenance_service_id),
  FOREIGN KEY (maintenance_request_id) REFERENCES maintenance_requests(maintenance_request_id)
);
```
