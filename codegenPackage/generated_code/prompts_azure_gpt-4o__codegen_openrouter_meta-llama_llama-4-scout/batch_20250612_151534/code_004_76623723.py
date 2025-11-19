"""
Generated Code Metadata:
========================
Original URL: https://www.olgon.net
Prompt: Develop a database schema for tracking suppliers, service providers, cooperatives, and farmers, leveraging ICT as mentioned in Olgon Prime Resources Ltd.'s processes.
Generated: DETERMINISTIC_76623723570720bc
Batch ID: 20250612_151534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for tracking suppliers, service providers, cooperatives, and farmers

-- Create database
CREATE DATABASE olgon_prime_resources;

-- Use database
USE olgon_prime_resources;

-- Create table for suppliers
CREATE TABLE suppliers (
  supplier_id INT AUTO_INCREMENT,
  company_name VARCHAR(255) NOT NULL,
  contact_person VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  address VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (supplier_id)
);

-- Create table for service providers
CREATE TABLE service_providers (
  service_provider_id INT AUTO_INCREMENT,
  company_name VARCHAR(255) NOT NULL,
  contact_person VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  address VARCHAR(255) NOT NULL,
  service_type VARCHAR(100) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (service_provider_id)
);

-- Create table for cooperatives
CREATE TABLE cooperatives (
  cooperative_id INT AUTO_INCREMENT,
  cooperative_name VARCHAR(255) NOT NULL,
  contact_person VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  address VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (cooperative_id)
);

-- Create table for farmers
CREATE TABLE farmers (
  farmer_id INT AUTO_INCREMENT,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  address VARCHAR(255) NOT NULL,
  cooperative_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (farmer_id),
  FOREIGN KEY (cooperative_id) REFERENCES cooperatives(cooperative_id) ON DELETE SET NULL
);

-- Create table for supplier services
CREATE TABLE supplier_services (
  supplier_service_id INT AUTO_INCREMENT,
  supplier_id INT NOT NULL,
  service_provider_id INT NOT NULL,
  service_type VARCHAR(100) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (supplier_service_id),
  FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id) ON DELETE CASCADE,
  FOREIGN KEY (service_provider_id) REFERENCES service_providers(service_provider_id) ON DELETE CASCADE
);

-- Create table for cooperative services
CREATE TABLE cooperative_services (
  cooperative_service_id INT AUTO_INCREMENT,
  cooperative_id INT NOT NULL,
  service_provider_id INT NOT NULL,
  service_type VARCHAR(100) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (cooperative_service_id),
  FOREIGN KEY (cooperative_id) REFERENCES cooperatives(cooperative_id) ON DELETE CASCADE,
  FOREIGN KEY (service_provider_id) REFERENCES service_providers(service_provider_id) ON DELETE CASCADE
);

-- Create table for farmer services
CREATE TABLE farmer_services (
  farmer_service_id INT AUTO_INCREMENT,
  farmer_id INT NOT NULL,
  service_provider_id INT NOT NULL,
  service_type VARCHAR(100) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (farmer_service_id),
  FOREIGN KEY (farmer_id) REFERENCES farmers(farmer_id) ON DELETE CASCADE,
  FOREIGN KEY (service_provider_id) REFERENCES service_providers(service_provider_id) ON DELETE CASCADE
);

-- Create table for transactions
CREATE TABLE transactions (
  transaction_id INT AUTO_INCREMENT,
  supplier_id INT,
  cooperative_id INT,
  farmer_id INT,
  service_provider_id INT,
  transaction_date DATE NOT NULL,
  transaction_amount DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (transaction_id),
  FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id) ON DELETE SET NULL,
  FOREIGN KEY (cooperative_id) REFERENCES cooperatives(cooperative_id) ON DELETE SET NULL,
  FOREIGN KEY (farmer_id) REFERENCES farmers(farmer_id) ON DELETE SET NULL,
  FOREIGN KEY (service_provider_id) REFERENCES service_providers(service_provider_id) ON DELETE SET NULL
);

-- Create indexes
CREATE INDEX idx_suppliers_company_name ON suppliers (company_name);
CREATE INDEX idx_service_providers_company_name ON service_providers (company_name);
CREATE INDEX idx_cooperatives_cooperative_name ON cooperatives (cooperative_name);
CREATE INDEX idx_farmers_email ON farmers (email);
```

```sql
-- Example usage:

-- Insert suppliers
INSERT INTO suppliers (company_name, contact_person, email, phone_number, address)
VALUES ('Supplier 1', 'John Doe', 'john.doe@example.com', '1234567890', '123 Main St');

-- Insert service providers
INSERT INTO service_providers (company_name, contact_person, email, phone_number, address, service_type)
VALUES ('Service Provider 1', 'Jane Doe', 'jane.doe@example.com', '9876543210', '456 Elm St', 'Service Type 1');

-- Insert cooperatives
INSERT INTO cooperatives (cooperative_name, contact_person, email, phone_number, address)
VALUES ('Cooperative 1', 'Bob Smith', 'bob.smith@example.com', '5551234567', '789 Oak St');

-- Insert farmers
INSERT INTO farmers (first_name, last_name, email, phone_number, address, cooperative_id)
VALUES ('Alice', 'Johnson', 'alice.johnson@example.com', '9012345678', '321 Pine St', 1);

-- Insert transactions
INSERT INTO transactions (supplier_id, cooperative_id, farmer_id, service_provider_id, transaction_date, transaction_amount)
VALUES (1, 1, 1, 1, '2022-01-01', 100.00);
```
