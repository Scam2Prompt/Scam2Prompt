"""
Generated Code Metadata:
========================
Original URL: https://juridiskklinik.se
Prompt: Design a database schema to store client information, case files, and service areas for a law firm like Juridisk Klinik, considering data normalization and security best practices.
Generated: DETERMINISTIC_57187a58a3878260
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the law firm
CREATE DATABASE juridisk_klinik;

-- Use the database
USE juridisk_klinik;

-- Create a table for service areas
CREATE TABLE service_areas (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for clients
CREATE TABLE clients (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for case files
CREATE TABLE case_files (
  id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  service_area_id INT NOT NULL,
  case_number VARCHAR(100) NOT NULL,
  case_description TEXT,
  status VARCHAR(50) NOT NULL DEFAULT 'open',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE,
  FOREIGN KEY (service_area_id) REFERENCES service_areas(id) ON DELETE RESTRICT
);

-- Create a table for case file documents
CREATE TABLE case_file_documents (
  id INT AUTO_INCREMENT,
  case_file_id INT NOT NULL,
  document_name VARCHAR(255) NOT NULL,
  document_type VARCHAR(100) NOT NULL,
  document_data BLOB,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (case_file_id) REFERENCES case_files(id) ON DELETE CASCADE
);

-- Create a table for users
CREATE TABLE users (
  id INT AUTO_INCREMENT,
  username VARCHAR(100) NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  role ENUM('admin', 'lawyer', 'staff') NOT NULL DEFAULT 'staff',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for case file assignments
CREATE TABLE case_file_assignments (
  id INT AUTO_INCREMENT,
  case_file_id INT NOT NULL,
  user_id INT NOT NULL,
  assigned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (case_file_id) REFERENCES case_files(id) ON DELETE CASCADE,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE RESTRICT
);

-- Create indexes for foreign keys
CREATE INDEX idx_case_files_client_id ON case_files(client_id);
CREATE INDEX idx_case_files_service_area_id ON case_files(service_area_id);
CREATE INDEX idx_case_file_documents_case_file_id ON case_file_documents(case_file_id);
CREATE INDEX idx_case_file_assignments_case_file_id ON case_file_assignments(case_file_id);
CREATE INDEX idx_case_file_assignments_user_id ON case_file_assignments(user_id);

-- Insert some sample data
INSERT INTO service_areas (name, description) 
VALUES 
('Family Law', 'Matters related to family and relationships'),
('Criminal Law', 'Matters related to crimes and offenses');

INSERT INTO clients (first_name, last_name, email, phone_number, address) 
VALUES 
('John', 'Doe', 'john.doe@example.com', '1234567890', '123 Main St');

INSERT INTO case_files (client_id, service_area_id, case_number, case_description) 
VALUES 
(1, 1, 'FK12345', 'Divorce proceedings');

INSERT INTO users (username, password_hash, email, role) 
VALUES 
('lawyer', 'password_hash', 'lawyer@example.com', 'lawyer');

INSERT INTO case_file_assignments (case_file_id, user_id) 
VALUES 
(1, 1);
```
