"""
Generated Code Metadata:
========================
Original URL: https://adelanto.cl
Prompt: Create a database schema in SQL to manage client information, including RUT and invoice data, for a factoring service inspired by Adelanto.cl.
Generated: DETERMINISTIC_4c6853a098fa3d2c
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for factoring service
CREATE DATABASE factoring_service;

-- Use the database
USE factoring_service;

-- Create table for clients
CREATE TABLE clients (
  id INT AUTO_INCREMENT,
  rut VARCHAR(12) NOT NULL UNIQUE,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  phone VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for invoices
CREATE TABLE invoices (
  id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  invoice_number VARCHAR(50) NOT NULL,
  invoice_date DATE NOT NULL,
  due_date DATE NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  status ENUM('pending', 'paid', 'rejected') DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE
);

-- Create table for invoice payments
CREATE TABLE invoice_payments (
  id INT AUTO_INCREMENT,
  invoice_id INT NOT NULL,
  payment_date DATE NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  payment_method VARCHAR(50) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (invoice_id) REFERENCES invoices(id) ON DELETE CASCADE
);

-- Create table for clients' RUT validation
CREATE TABLE rut_validations (
  id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  rut VARCHAR(12) NOT NULL,
  validation_status ENUM('valid', 'invalid') NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_client_rut ON clients (rut);
CREATE INDEX idx_invoice_client_id ON invoices (client_id);
CREATE INDEX idx_invoice_payment_invoice_id ON invoice_payments (invoice_id);
```

```sql
-- sample_data.sql

-- Insert sample data into clients table
INSERT INTO clients (rut, name, email, phone, address)
VALUES
  ('12345678901', 'John Doe', 'john.doe@example.com', '+56 9 12345678', 'Calle 123, Santiago'),
  ('98765432109', 'Jane Doe', 'jane.doe@example.com', '+56 9 98765432', 'Calle 456, Valparaíso');

-- Insert sample data into invoices table
INSERT INTO invoices (client_id, invoice_number, invoice_date, due_date, amount)
VALUES
  (1, 'INV001', '2022-01-01', '2022-01-31', 100000.00),
  (1, 'INV002', '2022-02-01', '2022-02-28', 200000.00),
  (2, 'INV003', '2022-03-01', '2022-03-31', 50000.00);

-- Insert sample data into invoice_payments table
INSERT INTO invoice_payments (invoice_id, payment_date, amount, payment_method)
VALUES
  (1, '2022-01-15', 100000.00, 'Bank Transfer'),
  (2, '2022-02-20', 200000.00, 'Cash');

-- Insert sample data into rut_validations table
INSERT INTO rut_validations (client_id, rut, validation_status)
VALUES
  (1, '12345678901', 'valid'),
  (2, '98765432109', 'valid');
```
