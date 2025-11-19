"""
Generated Code Metadata:
========================
Original URL: https://drcarloscastillo.com
Prompt: Generate a sample database schema for storing information about orthopedic surgical procedures, including tables for patients, surgeons, and procedure types, with a focus on foot and ankle surgeries.
Generated: DETERMINISTIC_ad18a1f0f6dd81ea
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for orthopedic surgical procedures (foot and ankle focus)

-- Patients table
CREATE TABLE patients (
    patient_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender ENUM('Male', 'Female', 'Other') NOT NULL,
    contact_number VARCHAR(20),
    email VARCHAR(100),
    address TEXT,
    insurance_provider VARCHAR(100),
    insurance_policy_number VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX (last_name, first_name)
) ENGINE=InnoDB;

-- Surgeons table
CREATE TABLE surgeons (
    surgeon_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    license_number VARCHAR(50) NOT NULL UNIQUE,
    specialization VARCHAR(100) NOT NULL,
    contact_number VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL,
    hospital_affiliation VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX (last_name, first_name)
) ENGINE=InnoDB;

-- Procedure types table (focus on foot and ankle)
CREATE TABLE procedure_types (
    procedure_type_id INT PRIMARY KEY AUTO_INCREMENT,
    procedure_code VARCHAR(20) NOT NULL UNIQUE,
    procedure_name VARCHAR(100) NOT NULL,
    description TEXT,
    category ENUM('Foot', 'Ankle', 'Combined') NOT NULL,
    typical_duration_minutes INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX (procedure_name),
    INDEX (category)
) ENGINE=InnoDB;

-- Surgical procedures table
CREATE TABLE surgical_procedures (
    procedure_id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT NOT NULL,
    surgeon_id INT NOT NULL,
    procedure_type_id INT NOT NULL,
    procedure_date DATETIME NOT NULL,
    anesthesia_type ENUM('General', 'Local', 'Regional', 'Sedation') NOT NULL,
    facility_name VARCHAR(100) NOT NULL,
    room_number VARCHAR(20),
    notes TEXT,
    complications TEXT,
    follow_up_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE RESTRICT,
    FOREIGN KEY (surgeon_id) REFERENCES surgeons(surgeon_id) ON DELETE RESTRICT,
    FOREIGN KEY (procedure_type_id) REFERENCES procedure_types(procedure_type_id) ON DELETE RESTRICT,
    INDEX (procedure_date),
    INDEX (patient_id),
    INDEX (surgeon_id)
) ENGINE=InnoDB;

-- Pre-operative assessments table
CREATE TABLE pre_op_assessments (
    assessment_id INT PRIMARY KEY AUTO_INCREMENT,
    procedure_id INT NOT NULL,
    assessment_date DATETIME NOT NULL,
    blood_pressure VARCHAR(20),
    heart_rate INT,
    temperature DECIMAL(5,2),
    oxygen_saturation DECIMAL(5,2),
    allergies TEXT,
    medications TEXT,
    npo_status BOOLEAN DEFAULT FALSE,
    consent_signed BOOLEAN DEFAULT FALSE,
    lab_results TEXT,
    imaging_results TEXT,
    assessment_notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (procedure_id) REFERENCES surgical_procedures(procedure_id) ON DELETE CASCADE,
    INDEX (procedure_id)
) ENGINE=InnoDB;

-- Post-operative outcomes table
CREATE TABLE post_op_outcomes (
    outcome_id INT PRIMARY KEY AUTO_INCREMENT,
    procedure_id INT NOT NULL,
    assessment_date DATETIME NOT NULL,
    pain_level ENUM('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'),
    wound_condition ENUM('Normal', 'Infected', 'Dehisced', 'Necrotic') NOT NULL,
    mobility_level ENUM('Non-weight bearing', 'Partial weight bearing', 'Full weight bearing') NOT NULL,
    complications TEXT,
    prescribed_medications TEXT,
    follow_up_instructions TEXT,
    next_appointment_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (procedure_id) REFERENCES surgical_procedures(procedure_id) ON DELETE CASCADE,
    INDEX (procedure_id)
) ENGINE=InnoDB;

-- Procedure-specific implants table
CREATE TABLE procedure_implants (
    implant_id INT PRIMARY KEY AUTO_INCREMENT,
    procedure_id INT NOT NULL,
    implant_type ENUM('Screw', 'Plate', 'Pin', 'Anchor', 'Prosthesis', 'Other') NOT NULL,
    implant_size VARCHAR(50),
    implant_material ENUM('Titanium', 'Stainless Steel', 'PEEK', 'Other') NOT NULL,
    manufacturer VARCHAR(100),
    catalog_number VARCHAR(50),
    serial_number VARCHAR(50),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (procedure_id) REFERENCES surgical_procedures(procedure_id) ON DELETE CASCADE,
    INDEX (procedure_id)
) ENGINE=InnoDB;
```
