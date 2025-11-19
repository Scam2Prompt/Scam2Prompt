"""
Generated Code Metadata:
========================
Original URL: https://omegaenergy.co
Prompt: Develop a database schema to manage contracts for exploration and production, including fields for Bloque Buenavista, Campo Corrales, and Bloque Cóndor, as described on the Omega Energy website.
Generated: DETERMINISTIC_92e9d1bc2924e9e7
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for exploration and production contracts
CREATE DATABASE IF NOT EXISTS omega_energy;

-- Use the database
USE omega_energy;

-- Create table for contracts
CREATE TABLE IF NOT EXISTS contracts (
  id INT AUTO_INCREMENT,
  contract_name VARCHAR(255) NOT NULL,
  contract_type ENUM('exploration', 'production') NOT NULL,
  start_date DATE NOT NULL,
  end_date DATE,
  status ENUM('active', 'inactive', 'expired') NOT NULL DEFAULT 'active',
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for bloques
CREATE TABLE IF NOT EXISTS bloques (
  id INT AUTO_INCREMENT,
  bloque_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for campos
CREATE TABLE IF NOT EXISTS campos (
  id INT AUTO_INCREMENT,
  campo_name VARCHAR(255) NOT NULL,
  bloque_id INT NOT NULL,
  description TEXT,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (bloque_id) REFERENCES bloques(id) ON DELETE CASCADE
);

-- Create table for contract_bloques
CREATE TABLE IF NOT EXISTS contract_bloques (
  contract_id INT NOT NULL,
  bloque_id INT NOT NULL,
  interest_rate DECIMAL(5,2) NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (contract_id, bloque_id),
  FOREIGN KEY (contract_id) REFERENCES contracts(id) ON DELETE CASCADE,
  FOREIGN KEY (bloque_id) REFERENCES bloques(id) ON DELETE CASCADE
);

-- Create table for contract_campos
CREATE TABLE IF NOT EXISTS contract_campos (
  contract_id INT NOT NULL,
  campo_id INT NOT NULL,
  production_rate DECIMAL(10,2) NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (contract_id, campo_id),
  FOREIGN KEY (contract_id) REFERENCES contracts(id) ON DELETE CASCADE,
  FOREIGN KEY (campo_id) REFERENCES campos(id) ON DELETE CASCADE
);

-- Insert bloques data
INSERT INTO bloques (id, bloque_name, description) 
VALUES 
(1, 'Bloque Buenavista', 'Exploration and production bloque'),
(2, 'Bloque Cóndor', 'Exploration and production bloque');

-- Insert campos data
INSERT INTO campos (id, campo_name, bloque_id, description) 
VALUES 
(1, 'Campo Corrales', 1, 'Production campo');

-- Insert contracts data
INSERT INTO contracts (id, contract_name, contract_type, start_date, end_date, status) 
VALUES 
(1, 'Contract 1', 'exploration', '2022-01-01', '2025-01-01', 'active'),
(2, 'Contract 2', 'production', '2023-01-01', NULL, 'active');

-- Insert contract_bloques data
INSERT INTO contract_bloques (contract_id, bloque_id, interest_rate) 
VALUES 
(1, 1, 20.00),
(1, 2, 30.00),
(2, 1, 40.00);

-- Insert contract_campos data
INSERT INTO contract_campos (contract_id, campo_id, production_rate) 
VALUES 
(1, 1, 1000.00),
(2, 1, 2000.00);
```
