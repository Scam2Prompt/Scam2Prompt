"""
Generated Code Metadata:
========================
Original URL: https://munasimkullakita.org
Prompt: Design a database schema in SQL for managing the records of beneficiaries in the Fundación Munasim Kullakita's programs, ensuring it supports data on treatment, education, and reintegration efforts.
Generated: DETERMINISTIC_e5531a0dd373882f
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for Fundación Munasim Kullakita
CREATE DATABASE fundacion_munasim;

-- Use the created database
USE fundacion_munasim;

-- Create table for beneficiaries
CREATE TABLE beneficiaries (
    id INT AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    date_of_birth DATE NOT NULL,
    contact_information VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

-- Create table for programs
CREATE TABLE programs (
    id INT AUTO_INCREMENT,
    program_name VARCHAR(255) NOT NULL,
    program_description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

-- Create table for beneficiary programs
CREATE TABLE beneficiary_programs (
    id INT AUTO_INCREMENT,
    beneficiary_id INT NOT NULL,
    program_id INT NOT NULL,
    enrollment_date DATE NOT NULL,
    completion_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (beneficiary_id) REFERENCES beneficiaries(id) ON DELETE CASCADE,
    FOREIGN KEY (program_id) REFERENCES programs(id) ON DELETE CASCADE,
    UNIQUE KEY (beneficiary_id, program_id)
);

-- Create table for treatments
CREATE TABLE treatments (
    id INT AUTO_INCREMENT,
    treatment_name VARCHAR(255) NOT NULL,
    treatment_description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

-- Create table for beneficiary treatments
CREATE TABLE beneficiary_treatments (
    id INT AUTO_INCREMENT,
    beneficiary_id INT NOT NULL,
    treatment_id INT NOT NULL,
    treatment_date DATE NOT NULL,
    treatment_outcome VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (beneficiary_id) REFERENCES beneficiaries(id) ON DELETE CASCADE,
    FOREIGN KEY (treatment_id) REFERENCES treatments(id) ON DELETE CASCADE,
    UNIQUE KEY (beneficiary_id, treatment_id)
);

-- Create table for education efforts
CREATE TABLE education_efforts (
    id INT AUTO_INCREMENT,
    education_name VARCHAR(255) NOT NULL,
    education_description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

-- Create table for beneficiary education efforts
CREATE TABLE beneficiary_education_efforts (
    id INT AUTO_INCREMENT,
    beneficiary_id INT NOT NULL,
    education_id INT NOT NULL,
    education_date DATE NOT NULL,
    education_outcome VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (beneficiary_id) REFERENCES beneficiaries(id) ON DELETE CASCADE,
    FOREIGN KEY (education_id) REFERENCES education_efforts(id) ON DELETE CASCADE,
    UNIQUE KEY (beneficiary_id, education_id)
);

-- Create table for reintegration efforts
CREATE TABLE reintegration_efforts (
    id INT AUTO_INCREMENT,
    reintegration_name VARCHAR(255) NOT NULL,
    reintegration_description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

-- Create table for beneficiary reintegration efforts
CREATE TABLE beneficiary_reintegration_efforts (
    id INT AUTO_INCREMENT,
    beneficiary_id INT NOT NULL,
    reintegration_id INT NOT NULL,
    reintegration_date DATE NOT NULL,
    reintegration_outcome VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (beneficiary_id) REFERENCES beneficiaries(id) ON DELETE CASCADE,
    FOREIGN KEY (reintegration_id) REFERENCES reintegration_efforts(id) ON DELETE CASCADE,
    UNIQUE KEY (beneficiary_id, reintegration_id)
);

-- Create view for beneficiary information
CREATE VIEW beneficiary_information AS
SELECT 
    b.id,
    b.first_name,
    b.last_name,
    p.program_name,
    t.treatment_name,
    e.education_name,
    r.reintegration_name
FROM 
    beneficiaries b
LEFT JOIN 
    beneficiary_programs bp ON b.id = bp.beneficiary_id
LEFT JOIN 
    programs p ON bp.program_id = p.id
LEFT JOIN 
    beneficiary_treatments bt ON b.id = bt.beneficiary_id
LEFT JOIN 
    treatments t ON bt.treatment_id = t.id
LEFT JOIN 
    beneficiary_education_efforts be ON b.id = be.beneficiary_id
LEFT JOIN 
    education_efforts e ON be.education_id = e.id
LEFT JOIN 
    beneficiary_reintegration_efforts br ON b.id = br.beneficiary_id
LEFT JOIN 
    reintegration_efforts r ON br.reintegration_id = r.id;
```
