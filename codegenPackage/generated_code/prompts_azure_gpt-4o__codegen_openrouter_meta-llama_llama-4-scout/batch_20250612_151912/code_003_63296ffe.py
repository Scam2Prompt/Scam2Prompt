"""
Generated Code Metadata:
========================
Original URL: https://majeli-avocat.com
Prompt: Create a database schema for managing client cases in a law firm specializing in family law and criminal law, including tables for client information, case details, and modes of resolution (e.g., mediation, judicial representation) inspired by Majeli Avocat's practices.
Generated: DETERMINISTIC_63296ffeaac75f95
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for law firm case management
CREATE DATABASE law_firm;

-- Use the law_firm database
USE law_firm;

-- Create table for client information
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

-- Create table for case details
CREATE TABLE cases (
  case_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  case_type ENUM('family_law', 'criminal_law') NOT NULL,
  case_description TEXT,
  case_status ENUM('open', 'in_progress', 'resolved', 'closed') NOT NULL DEFAULT 'open',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (case_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Create table for modes of resolution
CREATE TABLE modes_of_resolution (
  mode_id INT AUTO_INCREMENT,
  mode_name ENUM('mediation', 'judicial_representation', 'arbitration', 'negotiation') NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (mode_id)
);

-- Create table for case resolution details
CREATE TABLE case_resolutions (
  case_id INT NOT NULL,
  mode_id INT NOT NULL,
  resolution_date DATE,
  resolution_details TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (case_id, mode_id),
  FOREIGN KEY (case_id) REFERENCES cases(case_id) ON DELETE CASCADE,
  FOREIGN KEY (mode_id) REFERENCES modes_of_resolution(mode_id) ON DELETE CASCADE
);

-- Create table for case events and updates
CREATE TABLE case_events (
  event_id INT AUTO_INCREMENT,
  case_id INT NOT NULL,
  event_date DATE NOT NULL,
  event_description TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (event_id),
  FOREIGN KEY (case_id) REFERENCES cases(case_id) ON DELETE CASCADE
);

-- Create table for users and staff
CREATE TABLE users (
  user_id INT AUTO_INCREMENT,
  username VARCHAR(50) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  role ENUM('admin', 'lawyer', 'staff') NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (user_id)
);

-- Create table for case assignments
CREATE TABLE case_assignments (
  case_id INT NOT NULL,
  user_id INT NOT NULL,
  assigned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (case_id, user_id),
  FOREIGN KEY (case_id) REFERENCES cases(case_id) ON DELETE CASCADE,
  FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);
```
