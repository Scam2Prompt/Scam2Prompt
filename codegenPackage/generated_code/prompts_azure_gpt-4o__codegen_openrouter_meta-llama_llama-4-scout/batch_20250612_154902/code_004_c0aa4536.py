"""
Generated Code Metadata:
========================
Original URL: https://uniair.id
Prompt: Develop a database schema for managing customs clearance processes in Indonesia, referencing Uniair Cargo's customs services.
Generated: DETERMINISTIC_c0aa45367d233272
Batch ID: 20250612_154902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for customs clearance management
CREATE DATABASE indonesia_customs_clearance;

-- Use the database
USE indonesia_customs_clearance;

-- Create table for customs services
CREATE TABLE customs_services (
  service_id INT AUTO_INCREMENT,
  service_name VARCHAR(255) NOT NULL,
  service_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (service_id)
);

-- Create table for shipping companies
CREATE TABLE shipping_companies (
  company_id INT AUTO_INCREMENT,
  company_name VARCHAR(255) NOT NULL,
  company_address TEXT,
  contact_person VARCHAR(255),
  contact_email VARCHAR(255),
  contact_phone VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (company_id)
);

-- Create table for customs brokers
CREATE TABLE customs_brokers (
  broker_id INT AUTO_INCREMENT,
  broker_name VARCHAR(255) NOT NULL,
  broker_address TEXT,
  contact_person VARCHAR(255),
  contact_email VARCHAR(255),
  contact_phone VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (broker_id)
);

-- Create table for shipments
CREATE TABLE shipments (
  shipment_id INT AUTO_INCREMENT,
  shipping_company_id INT,
  customs_broker_id INT,
  shipment_date DATE,
  shipment_status VARCHAR(50),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (shipment_id),
  FOREIGN KEY (shipping_company_id) REFERENCES shipping_companies(company_id),
  FOREIGN KEY (customs_broker_id) REFERENCES customs_brokers(broker_id)
);

-- Create table for customs declarations
CREATE TABLE customs_declarations (
  declaration_id INT AUTO_INCREMENT,
  shipment_id INT,
  declaration_date DATE,
  hs_code VARCHAR(20),
  commodity_description TEXT,
  quantity DECIMAL(10, 2),
  value DECIMAL(10, 2),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (declaration_id),
  FOREIGN KEY (shipment_id) REFERENCES shipments(shipment_id)
);

-- Create table for customs payments
CREATE TABLE customs_payments (
  payment_id INT AUTO_INCREMENT,
  declaration_id INT,
  payment_date DATE,
  payment_amount DECIMAL(10, 2),
  payment_method VARCHAR(50),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (payment_id),
  FOREIGN KEY (declaration_id) REFERENCES customs_declarations(declaration_id)
);

-- Create table for customs clearance status
CREATE TABLE customs_clearance_status (
  status_id INT AUTO_INCREMENT,
  declaration_id INT,
  status_date DATE,
  status VARCHAR(50),
  remarks TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (status_id),
  FOREIGN KEY (declaration_id) REFERENCES customs_declarations(declaration_id)
);

-- Create indexes for foreign keys
CREATE INDEX idx_shipments_shipping_company_id ON shipments (shipping_company_id);
CREATE INDEX idx_shipments_customs_broker_id ON shipments (customs_broker_id);
CREATE INDEX idx_customs_declarations_shipment_id ON customs_declarations (shipment_id);
CREATE INDEX idx_customs_payments_declaration_id ON customs_payments (declaration_id);
CREATE INDEX idx_customs_clearance_status_declaration_id ON customs_clearance_status (declaration_id);
```

```sql
-- sample_data.sql

-- Insert sample data into customs services table
INSERT INTO customs_services (service_name, service_description)
VALUES
  ('Customs Clearance', 'Customs clearance services for import and export shipments'),
  ('Customs Brokerage', 'Customs brokerage services for import and export shipments'),
  ('Logistics Services', 'Logistics services for import and export shipments');

-- Insert sample data into shipping companies table
INSERT INTO shipping_companies (company_name, company_address, contact_person, contact_email, contact_phone)
VALUES
  ('Uniair Cargo', 'Jl. Raya Jakarta, Jakarta', 'John Doe', 'john.doe@uniaircargo.com', '021-1234567'),
  ('DHL Indonesia', 'Jl. Raya Bandung, Bandung', 'Jane Doe', 'jane.doe@dhl.com', '022-1234567'),
  ('FedEx Indonesia', 'Jl. Raya Surabaya, Surabaya', 'Bob Smith', 'bob.smith@fedex.com', '031-1234567');

-- Insert sample data into customs brokers table
INSERT INTO customs_brokers (broker_name, broker_address, contact_person, contact_email, contact_phone)
VALUES
  ('PT. Custom Broker Indonesia', 'Jl. Raya Jakarta, Jakarta', 'John Doe', 'john.doe@custombroker.co.id', '021-1234567'),
  ('CV. Indonesia Customs Service', 'Jl. Raya Bandung, Bandung', 'Jane Doe', 'jane.doe@ics.co.id', '022-1234567');

-- Insert sample data into shipments table
INSERT INTO shipments (shipping_company_id, customs_broker_id, shipment_date, shipment_status)
VALUES
  (1, 1, '2022-01-01', 'pending'),
  (2, 2, '2022-01-15', 'in_progress'),
  (3, 1, '2022-02-01', 'completed');

-- Insert sample data into customs declarations table
INSERT INTO customs_declarations (shipment_id, declaration_date, hs_code, commodity_description, quantity, value)
VALUES
  (1, '2022-01-01', '8517.12.00', 'Televisions', 100, 100000.00),
  (2, '2022-01-15', '8528.12.00', 'Radio receivers', 50, 50000.00),
  (3, '2022-02-01', '8531.10.00', 'Electrical capacitors', 200, 200000.00);

-- Insert sample data into customs payments table
INSERT INTO customs_payments (declaration_id, payment_date, payment_amount, payment_method)
VALUES
  (1, '2022-01-01', 10000.00, 'bank_transfer'),
  (2, '2022-01-15', 5000.00, 'cash'),
  (3, '2022-02-01', 20000.00, 'credit_card');

-- Insert sample data into customs clearance status table
INSERT INTO customs_clearance_status (declaration_id, status_date, status, remarks)
VALUES
  (1, '2022-01-01', 'pending', 'Waiting for payment'),
  (2, '2022-01-15', 'in_progress', 'Processing customs clearance'),
  (3, '2022-02-01', 'completed', 'Customs clearance completed');
```
