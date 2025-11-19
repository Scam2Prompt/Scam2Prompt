"""
Generated Code Metadata:
========================
Original URL: https://perezbernalte.com
Prompt: Based on the information provided about Pérez Bernalte Abogados' services in criminal law, civil law, and administrative law, create a simple database schema to organize client cases by legal area.
Generated: DETERMINISTIC_8d792c79b601b30d
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

-- Create a database for Pérez Bernalte Abogados
CREATE DATABASE perez_bernalt_abogados;

-- Use the database
USE perez_bernalt_abogados;

-- Create a table for clients
CREATE TABLE clients (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for legal areas
CREATE TABLE legal_areas (
  id INT AUTO_INCREMENT,
  name ENUM('criminal', 'civil', 'administrative') NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for cases
CREATE TABLE cases (
  id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  legal_area_id INT NOT NULL,
  case_number VARCHAR(50) NOT NULL,
  case_description TEXT,
  status ENUM('open', 'in_progress', 'closed') NOT NULL DEFAULT 'open',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE,
  FOREIGN KEY (legal_area_id) REFERENCES legal_areas(id) ON DELETE CASCADE
);

-- Create a table for case updates
CREATE TABLE case_updates (
  id INT AUTO_INCREMENT,
  case_id INT NOT NULL,
  update_description TEXT NOT NULL,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (case_id) REFERENCES cases(id) ON DELETE CASCADE
);

-- Insert some sample data
INSERT INTO clients (name, email, phone_number, address)
VALUES
  ('John Doe', 'john.doe@example.com', '123-456-7890', '123 Main St'),
  ('Jane Smith', 'jane.smith@example.com', '987-654-3210', '456 Elm St');

INSERT INTO legal_areas (name, description)
VALUES
  ('criminal', 'Criminal law services'),
  ('civil', 'Civil law services'),
  ('administrative', 'Administrative law services');

INSERT INTO cases (client_id, legal_area_id, case_number, case_description)
VALUES
  (1, 1, 'CR-001', 'Client charged with a crime'),
  (2, 2, 'CI-001', 'Client involved in a civil dispute');

INSERT INTO case_updates (case_id, update_description)
VALUES
  (1, 'Initial consultation completed'),
  (2, 'Filed a complaint');
```
