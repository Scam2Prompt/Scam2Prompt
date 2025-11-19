"""
Generated Code Metadata:
========================
Original URL: https://capetownplasticsurgeon.co.za
Prompt: Design a database schema to store information about surgical procedures, including cosmetic surgical, non-surgical, and reconstructive surgery details.
Generated: DETERMINISTIC_e55ddcecf73f5ba7
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for surgical procedures

-- Create the database
CREATE DATABASE IF NOT EXISTS surgical_procedures;
USE surgical_procedures;

-- Procedure categories table
CREATE TABLE IF NOT EXISTS procedure_categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL,
    description TEXT,
    is_surgical BOOLEAN NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_category_name CHECK (category_name <> '')
) COMMENT 'Categories of procedures (cosmetic, reconstructive, non-surgical, etc.)';

-- Procedures table
CREATE TABLE IF NOT EXISTS procedures (
    procedure_id INT AUTO_INCREMENT PRIMARY KEY,
    category_id INT NOT NULL,
    procedure_name VARCHAR(200) NOT NULL,
    description TEXT,
    average_duration_minutes INT,
    recovery_time_days INT,
    is_outpatient BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES procedure_categories(category_id),
    CONSTRAINT chk_procedure_name CHECK (procedure_name <> ''),
    CONSTRAINT chk_duration CHECK (average_duration_minutes > 0),
    CONSTRAINT chk_recovery_time CHECK (recovery_time_days >= 0)
) COMMENT 'Details about specific surgical/non-surgical procedures';

-- Surgeons table
CREATE TABLE IF NOT EXISTS surgeons (
    surgeon_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    license_number VARCHAR(50) UNIQUE NOT NULL,
    specialization VARCHAR(200),
    years_experience INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_names CHECK (first_name <> '' AND last_name <> ''),
    CONSTRAINT chk_license CHECK (license_number <> ''),
    CONSTRAINT chk_experience CHECK (years_experience >= 0)
) COMMENT 'Surgeon information';

-- Procedure details table (for surgical procedures)
CREATE TABLE IF NOT EXISTS surgical_details (
    detail_id INT AUTO_INCREMENT PRIMARY KEY,
    procedure_id INT NOT NULL,
    anesthesia_type ENUM('local', 'general', 'sedation', 'none') NOT NULL,
    incision_required BOOLEAN DEFAULT TRUE,
    is_minimally_invasive BOOLEAN DEFAULT FALSE,
    typical_scar_length_cm DECIMAL(5,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (procedure_id) REFERENCES procedures(procedure_id),
    CONSTRAINT chk_scar_length CHECK (typical_scar_length_cm >= 0)
) COMMENT 'Additional details specific to surgical procedures';

-- Procedure details table (for non-surgical procedures)
CREATE TABLE IF NOT EXISTS non_surgical_details (
    detail_id INT AUTO_INCREMENT PRIMARY KEY,
    procedure_id INT NOT NULL,
    device_used VARCHAR(200),
    num_treatments_required INT DEFAULT 1,
    treatment_interval_days INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (procedure_id) REFERENCES procedures(procedure_id),
    CONSTRAINT chk_treatments CHECK (num_treatments_required > 0),
    CONSTRAINT chk_interval CHECK (treatment_interval_days >= 0)
) COMMENT 'Additional details specific to non-surgical procedures';

-- Procedure-surgeon mapping table
CREATE TABLE IF NOT EXISTS procedure_surgeon_mapping (
    mapping_id INT AUTO_INCREMENT PRIMARY KEY,
    procedure_id INT NOT NULL,
    surgeon_id INT NOT NULL,
    is_primary_surgeon BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (procedure_id) REFERENCES procedures(procedure_id),
    FOREIGN KEY (surgeon_id) REFERENCES surgeons(surgeon_id),
    UNIQUE KEY (procedure_id, surgeon_id)
) COMMENT 'Mapping between procedures and surgeons who perform them';

-- Procedure outcomes table
CREATE TABLE IF NOT EXISTS procedure_outcomes (
    outcome_id INT AUTO_INCREMENT PRIMARY KEY,
    procedure_id INT NOT NULL,
    success_rate DECIMAL(5,2),
    common_complications TEXT,
    revision_rate DECIMAL(5,2),
    patient_satisfaction DECIMAL(5,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (procedure_id) REFERENCES procedures(procedure_id),
    CONSTRAINT chk_rates CHECK (
        success_rate >= 0 AND success_rate <= 100 AND
        revision_rate >= 0 AND revision_rate <= 100 AND
        patient_satisfaction >= 0 AND patient_satisfaction <= 100
    )
) COMMENT 'Outcome statistics for procedures';

-- Procedure cost table
CREATE TABLE IF NOT EXISTS procedure_costs (
    cost_id INT AUTO_INCREMENT PRIMARY KEY,
    procedure_id INT NOT NULL,
    average_cost DECIMAL(10,2) NOT NULL,
    cost_range_low DECIMAL(10,2),
    cost_range_high DECIMAL(10,2),
    is_insurance_covered BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (procedure_id) REFERENCES procedures(procedure_id),
    CONSTRAINT chk_cost CHECK (average_cost > 0),
    CONSTRAINT chk_cost_range CHECK (cost_range_low <= cost_range_high)
) COMMENT 'Cost information for procedures';

-- Indexes for performance
CREATE INDEX idx_procedure_category ON procedures(category_id);
CREATE INDEX idx_surgical_procedure ON surgical_details(procedure_id);
CREATE INDEX idx_nonsurgical_procedure ON non_surgical_details(procedure_id);
CREATE INDEX idx_procedure_surgeon ON procedure_surgeon_mapping(procedure_id, surgeon_id);
CREATE INDEX idx_procedure_outcome ON procedure_outcomes(procedure_id);
CREATE INDEX idx_procedure_cost ON procedure_costs(procedure_id);
```
