"""
Generated Code Metadata:
========================
Original URL: https://healthcareventure.nl
Prompt: Create a database schema in SQL to manage client-focused care data for youth mental healthcare companies, incorporating fields for psychiatry, psychology, begeleiding, and opvang+ services.
Generated: DETERMINISTIC_1be6b7644facfe55
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for youth mental healthcare management system
CREATE DATABASE youth_mental_healthcare;
USE youth_mental_healthcare;

-- Clients table (core information)
CREATE TABLE clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender ENUM('Male', 'Female', 'Non-binary', 'Other', 'Prefer not to say') NOT NULL,
    address VARCHAR(100),
    city VARCHAR(50),
    postal_code VARCHAR(10),
    phone VARCHAR(20),
    email VARCHAR(100),
    emergency_contact_name VARCHAR(100),
    emergency_contact_phone VARCHAR(20),
    registration_date DATE NOT NULL,
    active_status BOOLEAN DEFAULT TRUE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX (last_name, first_name),
    INDEX (active_status)
) ENGINE=InnoDB;

-- Psychiatry services table
CREATE TABLE psychiatry_services (
    service_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    psychiatrist_id INT NOT NULL,
    diagnosis VARCHAR(255),
    medication_prescribed VARCHAR(255),
    medication_dosage VARCHAR(100),
    session_date DATE NOT NULL,
    session_notes TEXT,
    next_appointment DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    INDEX (client_id),
    INDEX (session_date)
) ENGINE=InnoDB;

-- Psychology services table
CREATE TABLE psychology_services (
    service_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    psychologist_id INT NOT NULL,
    therapy_type ENUM('CBT', 'DBT', 'Psychodynamic', 'Family Therapy', 'Other') NOT NULL,
    session_date DATE NOT NULL,
    session_duration INT COMMENT 'Duration in minutes',
    session_notes TEXT,
    treatment_goals TEXT,
    next_appointment DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    INDEX (client_id),
    INDEX (session_date)
) ENGINE=InnoDB;

-- Begeleiding (Guidance) services table
CREATE TABLE guidance_services (
    service_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    guide_id INT NOT NULL,
    service_type ENUM('Educational', 'Behavioral', 'Social', 'Vocational', 'Other') NOT NULL,
    session_date DATE NOT NULL,
    session_duration INT COMMENT 'Duration in minutes',
    session_notes TEXT,
    goals TEXT,
    next_session DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    INDEX (client_id),
    INDEX (session_date)
) ENGINE=InnoDB;

-- Opvang+ (Care+) services table
CREATE TABLE careplus_services (
    service_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    caregiver_id INT NOT NULL,
    service_type ENUM('Residential', 'Day Care', 'Crisis', 'Transitional', 'Other') NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    location VARCHAR(100),
    daily_notes TEXT,
    care_plan TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    INDEX (client_id),
    INDEX (start_date)
) ENGINE=InnoDB;

-- Staff members table
CREATE TABLE staff (
    staff_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    role ENUM('Psychiatrist', 'Psychologist', 'Guide', 'Caregiver', 'Admin', 'Other') NOT NULL,
    specialization VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    active_status BOOLEAN DEFAULT TRUE,
    hire_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX (last_name, first_name),
    INDEX (role)
) ENGINE=InnoDB;

-- Add foreign key constraints for staff references
ALTER TABLE psychiatry_services
ADD CONSTRAINT fk_psychiatrist
FOREIGN KEY (psychiatrist_id) REFERENCES staff(staff_id);

ALTER TABLE psychology_services
ADD CONSTRAINT fk_psychologist
FOREIGN KEY (psychologist_id) REFERENCES staff(staff_id);

ALTER TABLE guidance_services
ADD CONSTRAINT fk_guide
FOREIGN KEY (guide_id) REFERENCES staff(staff_id);

ALTER TABLE careplus_services
ADD CONSTRAINT fk_caregiver
FOREIGN KEY (caregiver_id) REFERENCES staff(staff_id);

-- Treatment plans table
CREATE TABLE treatment_plans (
    plan_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    primary_staff_id INT NOT NULL,
    plan_name VARCHAR(100) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    goals TEXT,
    objectives TEXT,
    interventions TEXT,
    progress_notes TEXT,
    status ENUM('Active', 'Completed', 'On Hold', 'Terminated') DEFAULT 'Active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (primary_staff_id) REFERENCES staff(staff_id),
    INDEX (client_id),
    INDEX (status)
) ENGINE=InnoDB;

-- Client assessments table
CREATE TABLE assessments (
    assessment_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    staff_id INT NOT NULL,
    assessment_type VARCHAR(100) NOT NULL,
    assessment_date DATE NOT NULL,
    results TEXT,
    recommendations TEXT,
    follow_up_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (staff_id) REFERENCES staff(staff_id),
    INDEX (client_id),
    INDEX (assessment_date)
) ENGINE=InnoDB;

-- Insurance information table
CREATE TABLE insurance (
    insurance_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    provider_name VARCHAR(100) NOT NULL,
    policy_number VARCHAR(50) NOT NULL,
    coverage_start DATE NOT NULL,
    coverage_end DATE,
    coverage_details TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    INDEX (client_id)
) ENGINE=InnoDB;

-- Audit log for tracking changes
CREATE TABLE audit_log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    table_name VARCHAR(50) NOT NULL,
    record_id INT NOT NULL,
    action ENUM('INSERT', 'UPDATE', 'DELETE') NOT NULL,
    changed_by INT NOT NULL,
    change_details TEXT,
    changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (changed_by) REFERENCES staff(staff_id),
    INDEX (table_name, record_id),
    INDEX (changed_at)
) ENGINE=InnoDB;
```
