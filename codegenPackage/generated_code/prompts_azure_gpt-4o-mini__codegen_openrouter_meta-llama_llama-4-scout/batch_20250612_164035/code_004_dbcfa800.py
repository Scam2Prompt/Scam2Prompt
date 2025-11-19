"""
Generated Code Metadata:
========================
Original URL: https://sardagnapoeta.com.br
Prompt: Design a database schema for a law office that tracks cases involving "Prisão em Flagrante" and "Tribunal do Júri," ensuring compliance with legal standards.
Generated: DETERMINISTIC_dbcfa800041ccf33
Batch ID: 20250612_164035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for law office
CREATE DATABASE law_office;

-- Use law office database
USE law_office;

-- Create table for clients
CREATE TABLE clients (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  cpf VARCHAR(11) UNIQUE NOT NULL,
  rg VARCHAR(10) NOT NULL,
  address VARCHAR(255) NOT NULL,
  phone VARCHAR(20) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for lawyers
CREATE TABLE lawyers (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  oab VARCHAR(20) UNIQUE NOT NULL,
  phone VARCHAR(20) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for cases
CREATE TABLE cases (
  id INT AUTO_INCREMENT,
  case_type ENUM('Prisão em Flagrante', 'Tribunal do Júri') NOT NULL,
  client_id INT NOT NULL,
  lawyer_id INT NOT NULL,
  case_number VARCHAR(50) NOT NULL,
  case_status VARCHAR(50) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (client_id) REFERENCES clients(id),
  FOREIGN KEY (lawyer_id) REFERENCES lawyers(id)
);

-- Create table for hearings
CREATE TABLE hearings (
  id INT AUTO_INCREMENT,
  case_id INT NOT NULL,
  hearing_date DATE NOT NULL,
  hearing_time TIME NOT NULL,
  location VARCHAR(255) NOT NULL,
  outcome VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (case_id) REFERENCES cases(id)
);

-- Create table for documents
CREATE TABLE documents (
  id INT AUTO_INCREMENT,
  case_id INT NOT NULL,
  document_type VARCHAR(50) NOT NULL,
  document_date DATE NOT NULL,
  document_number VARCHAR(50) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (case_id) REFERENCES cases(id)
);

-- Create table for case history
CREATE TABLE case_history (
  id INT AUTO_INCREMENT,
  case_id INT NOT NULL,
  status VARCHAR(50) NOT NULL,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_by VARCHAR(255) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (case_id) REFERENCES cases(id)
);

-- Create indexes for foreign keys
CREATE INDEX idx_client_id ON cases (client_id);
CREATE INDEX idx_lawyer_id ON cases (lawyer_id);
CREATE INDEX idx_case_id ON hearings (case_id);
CREATE INDEX idx_case_id ON documents (case_id);
CREATE INDEX idx_case_id ON case_history (case_id);
```

```sql
-- example_data.sql

-- Insert example data into clients table
INSERT INTO clients (name, cpf, rg, address, phone, email)
VALUES
  ('John Doe', '12345678901', '1234567890', 'Rua Exemplo, 123', '(11) 12345-6789', 'john.doe@example.com'),
  ('Jane Doe', '98765432109', '9876543210', 'Avenida Exemplo, 456', '(11) 98765-4321', 'jane.doe@example.com');

-- Insert example data into lawyers table
INSERT INTO lawyers (name, oab, phone, email)
VALUES
  ('Lawyer 1', '123456', '(11) 12345-6789', 'lawyer1@example.com'),
  ('Lawyer 2', '987654', '(11) 98765-4321', 'lawyer2@example.com');

-- Insert example data into cases table
INSERT INTO cases (case_type, client_id, lawyer_id, case_number, case_status)
VALUES
  ('Prisão em Flagrante', 1, 1, '123/2022', 'Open'),
  ('Tribunal do Júri', 2, 2, '456/2022', 'Closed');

-- Insert example data into hearings table
INSERT INTO hearings (case_id, hearing_date, hearing_time, location, outcome)
VALUES
  (1, '2022-01-01', '10:00:00', 'Tribunal de Justiça', 'Pending'),
  (2, '2022-02-02', '14:00:00', 'Fórum', 'Closed');

-- Insert example data into documents table
INSERT INTO documents (case_id, document_type, document_date, document_number)
VALUES
  (1, 'Petição Inicial', '2022-01-01', '123456'),
  (2, 'Sentença', '2022-02-02', '987654');

-- Insert example data into case_history table
INSERT INTO case_history (case_id, status, updated_by)
VALUES
  (1, 'Open', 'Lawyer 1'),
  (2, 'Closed', 'Judge');
```
