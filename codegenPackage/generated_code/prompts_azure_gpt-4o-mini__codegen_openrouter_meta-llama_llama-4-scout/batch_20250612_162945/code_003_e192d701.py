"""
Generated Code Metadata:
========================
Original URL: https://azarlegal.com
Prompt: Create a sample database schema for storing client information and case details for a law firm like AZAR & Associates, focusing on corporate and real estate law.
Generated: DETERMINISTIC_e192d70186bb480f
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for the law firm
CREATE DATABASE azar_associates;

-- Use the database
USE azar_associates;

-- Create a table for clients
CREATE TABLE clients (
  client_id INT AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (client_id)
);

-- Create a table for case types
CREATE TABLE case_types (
  case_type_id INT AUTO_INCREMENT,
  case_type_name VARCHAR(50) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (case_type_id)
);

-- Create a table for cases
CREATE TABLE cases (
  case_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  case_type_id INT NOT NULL,
  case_number VARCHAR(50) UNIQUE NOT NULL,
  case_name VARCHAR(255) NOT NULL,
  description TEXT,
  status VARCHAR(50) NOT NULL DEFAULT 'Open',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (case_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
  FOREIGN KEY (case_type_id) REFERENCES case_types(case_type_id) ON DELETE RESTRICT
);

-- Create a table for case documents
CREATE TABLE case_documents (
  document_id INT AUTO_INCREMENT,
  case_id INT NOT NULL,
  document_name VARCHAR(255) NOT NULL,
  document_type VARCHAR(50) NOT NULL,
  document_url VARCHAR(255) NOT NULL,
  uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (document_id),
  FOREIGN KEY (case_id) REFERENCES cases(case_id) ON DELETE CASCADE
);

-- Create a table for case events
CREATE TABLE case_events (
  event_id INT AUTO_INCREMENT,
  case_id INT NOT NULL,
  event_type VARCHAR(50) NOT NULL,
  event_date DATE NOT NULL,
  event_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (event_id),
  FOREIGN KEY (case_id) REFERENCES cases(case_id) ON DELETE CASCADE
);

-- Create a table for users
CREATE TABLE users (
  user_id INT AUTO_INCREMENT,
  username VARCHAR(50) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  role VARCHAR(50) NOT NULL CHECK (role IN ('admin', 'lawyer', 'staff')),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (user_id)
);

-- Create a table for user assignments
CREATE TABLE user_assignments (
  assignment_id INT AUTO_INCREMENT,
  case_id INT NOT NULL,
  user_id INT NOT NULL,
  assigned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (assignment_id),
  FOREIGN KEY (case_id) REFERENCES cases(case_id) ON DELETE CASCADE,
  FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE RESTRICT
);
```
