"""
Generated Code Metadata:
========================
Original URL: https://aveaorg.com
Prompt: Develop a database schema for managing vocational education certifications, including fields for program type, completion status, and issuing authority, based on the AVEA certificate system.
Generated: DETERMINISTIC_2eb8e53732903eb5
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for managing vocational education certifications

-- Define the database
CREATE DATABASE IF NOT EXISTS aveacertificates;

-- Use the database
USE aveacertificates;

-- Create a table for program types
CREATE TABLE IF NOT EXISTS program_types (
  `id` INT AUTO_INCREMENT,
  `program_type` VARCHAR(255) NOT NULL COMMENT 'Type of vocational education program (e.g. apprenticeship, diploma, certificate)',
  `description` TEXT COMMENT 'Description of the program type',
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `program_type` (`program_type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Create a table for issuing authorities
CREATE TABLE IF NOT EXISTS issuing_authorities (
  `id` INT AUTO_INCREMENT,
  `authority_name` VARCHAR(255) NOT NULL COMMENT 'Name of the issuing authority (e.g. government agency, educational institution)',
  `authority_code` VARCHAR(50) NOT NULL COMMENT 'Unique code for the issuing authority',
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `authority_code` (`authority_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Create a table for vocational education certifications
CREATE TABLE IF NOT EXISTS certifications (
  `id` INT AUTO_INCREMENT,
  `program_type_id` INT NOT NULL COMMENT 'Foreign key referencing the program_types table',
  `issuing_authority_id` INT NOT NULL COMMENT 'Foreign key referencing the issuing_authorities table',
  `certificate_number` VARCHAR(255) NOT NULL COMMENT 'Unique certificate number',
  `completion_status` ENUM('pending', 'completed', 'revoked') NOT NULL DEFAULT 'pending' COMMENT 'Status of the certification (pending, completed, or revoked)',
  `issue_date` DATE COMMENT 'Date the certificate was issued',
  `expiration_date` DATE COMMENT 'Date the certificate expires',
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `certificate_number` (`certificate_number`),
  KEY `program_type_id` (`program_type_id`),
  KEY `issuing_authority_id` (`issuing_authority_id`),
  CONSTRAINT `certifications_ibfk1` FOREIGN KEY (`program_type_id`) REFERENCES `program_types` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `certifications_ibfk2` FOREIGN KEY (`issuing_authority_id`) REFERENCES `issuing_authorities` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Create a table for certification issuance history
CREATE TABLE IF NOT EXISTS certification_history (
  `id` INT AUTO_INCREMENT,
  `certification_id` INT NOT NULL COMMENT 'Foreign key referencing the certifications table',
  `status` ENUM('issued', 'revoked') NOT NULL COMMENT 'Status of the certification issuance (issued or revoked)',
  `update_date` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Date the certification status was updated',
  `updated_by` VARCHAR(255) NOT NULL COMMENT 'User or system that updated the certification status',
  PRIMARY KEY (`id`),
  KEY `certification_id` (`certification_id`),
  CONSTRAINT `certification_history_ibfk1` FOREIGN KEY (`certification_id`) REFERENCES `certifications` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Insert sample data into program_types table
INSERT INTO program_types (program_type, description) VALUES
  ('Apprenticeship', 'A work-based training program that combines on-the-job training with related classroom instruction'),
  ('Diploma', 'A diploma program that provides specialized training in a specific field or industry'),
  ('Certificate', 'A certificate program that provides foundational training in a specific skill or area');

-- Insert sample data into issuing_authorities table
INSERT INTO issuing_authorities (authority_name, authority_code) VALUES
  ('Government Agency', 'GA-001'),
  ('Educational Institution', 'EI-001'),
  ('Certification Body', 'CB-001');

-- Insert sample data into certifications table
INSERT INTO certifications (program_type_id, issuing_authority_id, certificate_number, completion_status, issue_date, expiration_date) VALUES
  (1, 1, 'CERT-001', 'completed', '2020-01-01', '2025-01-01'),
  (2, 2, 'CERT-002', 'pending', NULL, NULL),
  (3, 3, 'CERT-003', 'revoked', '2019-01-01', NULL);
```
