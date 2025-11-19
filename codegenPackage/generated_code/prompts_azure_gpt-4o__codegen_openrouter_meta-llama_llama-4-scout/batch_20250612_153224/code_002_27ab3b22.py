"""
Generated Code Metadata:
========================
Original URL: https://munasimkullakita.org
Prompt: Create a database schema for storing information about beneficiaries of social programs, including fields for personal details, program participation, and reintegration status, inspired by Fundación Munasim Kullakita's initiatives.
Generated: DETERMINISTIC_27ab3b22b83065fd
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for social program beneficiaries

-- Create database
CREATE DATABASE social_programs;

-- Use database
USE social_programs;

-- Create table for beneficiaries' personal details
CREATE TABLE beneficiaries (
    id INT AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    date_of_birth DATE NOT NULL,
    national_id VARCHAR(20) UNIQUE NOT NULL,
    address VARCHAR(255),
    phone_number VARCHAR(20),
    email VARCHAR(100) UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

-- Create table for social programs
CREATE TABLE programs (
    id INT AUTO_INCREMENT,
    program_name VARCHAR(255) NOT NULL,
    program_description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

-- Create table for beneficiaries' program participation
CREATE TABLE beneficiary_programs (
    id INT AUTO_INCREMENT,
    beneficiary_id INT NOT NULL,
    program_id INT NOT NULL,
    enrollment_date DATE NOT NULL,
    exit_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (beneficiary_id) REFERENCES beneficiaries(id) ON DELETE CASCADE,
    FOREIGN KEY (program_id) REFERENCES programs(id) ON DELETE CASCADE,
    UNIQUE (beneficiary_id, program_id)
);

-- Create table for reintegration status
CREATE TABLE reintegration_status (
    id INT AUTO_INCREMENT,
    beneficiary_id INT NOT NULL,
    status VARCHAR(50) NOT NULL CHECK (status IN ('active', 'inactive', 'graduated', 'dropped_out')),
    status_date DATE NOT NULL,
    comments TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (beneficiary_id) REFERENCES beneficiaries(id) ON DELETE CASCADE
);

-- Create table for beneficiary documents
CREATE TABLE beneficiary_documents (
    id INT AUTO_INCREMENT,
    beneficiary_id INT NOT NULL,
    document_type VARCHAR(50) NOT NULL CHECK (document_type IN ('id', 'medical_certificate', 'proof_of_address')),
    document_number VARCHAR(100),
    document_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (beneficiary_id) REFERENCES beneficiaries(id) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_beneficiaries_national_id ON beneficiaries (national_id);
CREATE INDEX idx_beneficiary_programs_beneficiary_id ON beneficiary_programs (beneficiary_id);
CREATE INDEX idx_beneficiary_programs_program_id ON beneficiary_programs (program_id);
CREATE INDEX idx_reintegration_status_beneficiary_id ON reintegration_status (beneficiary_id);
```

```sql
-- Example usage:

-- Insert beneficiary
INSERT INTO beneficiaries (first_name, last_name, date_of_birth, national_id, address, phone_number, email)
VALUES ('John', 'Doe', '1990-01-01', '1234567890', '123 Main St', '1234567890', 'john.doe@example.com');

-- Insert program
INSERT INTO programs (program_name, program_description)
VALUES ('Job Training', 'Job training program for unemployed individuals');

-- Insert beneficiary program participation
INSERT INTO beneficiary_programs (beneficiary_id, program_id, enrollment_date)
VALUES (1, 1, '2022-01-01');

-- Insert reintegration status
INSERT INTO reintegration_status (beneficiary_id, status, status_date, comments)
VALUES (1, 'active', '2022-06-01', 'Beneficiary is actively participating in the program');

-- Query beneficiaries with program participation
SELECT b.*, p.program_name
FROM beneficiaries b
JOIN beneficiary_programs bp ON b.id = bp.beneficiary_id
JOIN programs p ON bp.program_id = p.id;
```
