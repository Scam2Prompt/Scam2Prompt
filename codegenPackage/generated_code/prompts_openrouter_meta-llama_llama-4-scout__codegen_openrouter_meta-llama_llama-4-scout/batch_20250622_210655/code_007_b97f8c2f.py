"""
Generated Code Metadata:
========================
Original URL: https://cartoriojustiniano.com.br
Prompt: Design a database schema to store information about Cartório Justiniano's clients, services, and documents, and provide a SQL script to populate the database with sample data.
Generated: DETERMINISTIC_b97f8c2f0d826848
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database
CREATE DATABASE cartorio_justiniano;

-- Use database
USE cartorio_justiniano;

-- Create table for clients
CREATE TABLE clients (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone VARCHAR(20) NOT NULL,
  address VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for services
CREATE TABLE services (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for documents
CREATE TABLE documents (
  id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  service_id INT NOT NULL,
  document_type VARCHAR(100) NOT NULL,
  document_number VARCHAR(255) NOT NULL,
  issue_date DATE NOT NULL,
  expiration_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (client_id) REFERENCES clients(id),
  FOREIGN KEY (service_id) REFERENCES services(id)
);

-- Create table for client services
CREATE TABLE client_services (
  client_id INT NOT NULL,
  service_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (client_id, service_id),
  FOREIGN KEY (client_id) REFERENCES clients(id),
  FOREIGN KEY (service_id) REFERENCES services(id)
);

-- Populate database with sample data
INSERT INTO clients (name, email, phone, address)
VALUES
  ('John Doe', 'john.doe@example.com', '1234567890', 'Rua Exemplo, 123'),
  ('Jane Doe', 'jane.doe@example.com', '9876543210', 'Avenida Exemplo, 456'),
  ('Maria Silva', 'maria.silva@example.com', '5555555555', 'Rua Silva, 789');

INSERT INTO services (name, description, price)
VALUES
  ('Apostila', 'Apostila de documentos', 10.00),
  ('Autenticação', 'Autenticação de documentos', 5.00),
  ('Procuração', 'Procuração pública', 20.00);

INSERT INTO documents (client_id, service_id, document_type, document_number, issue_date, expiration_date)
VALUES
  (1, 1, 'CPF', '12345678900', '2020-01-01', NULL),
  (1, 2, 'RG', '123456789', '2019-01-01', '2024-01-01'),
  (2, 3, 'Passaporte', '123456789', '2018-01-01', '2023-01-01'),
  (3, 1, 'Certidão de Nascimento', '123456789', '1990-01-01', NULL);

INSERT INTO client_services (client_id, service_id)
VALUES
  (1, 1),
  (1, 2),
  (2, 3),
  (3, 1);
```
