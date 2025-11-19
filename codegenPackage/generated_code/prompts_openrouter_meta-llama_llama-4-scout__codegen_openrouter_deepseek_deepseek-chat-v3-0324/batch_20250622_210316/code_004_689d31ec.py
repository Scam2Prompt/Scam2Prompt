"""
Generated Code Metadata:
========================
Original URL: https://doctoresjane.com
Prompt: "Design a database schema to store patient information and treatment plans for a dental clinic that practices integrative dentistry, including fields for tracking patient progress and outcomes."
Generated: DETERMINISTIC_689d31ece1d1214b
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for a dental clinic practicing integrative dentistry
-- Includes tables for patients, treatments, appointments, progress tracking, and outcomes

-- Create the database
CREATE DATABASE IF NOT EXISTS dental_clinic;
USE dental_clinic;

-- Patients table to store basic patient information
CREATE TABLE IF NOT EXISTS patients (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender ENUM('Male', 'Female', 'Other', 'Prefer not to say') NOT NULL,
    address VARCHAR(100),
    city VARCHAR(50),
    state VARCHAR(30),
    zip_code VARCHAR(20),
    phone VARCHAR(20) NOT NULL,
    email VARCHAR(100),
    emergency_contact_name VARCHAR(100),
    emergency_contact_phone VARCHAR(20),
    insurance_provider VARCHAR(50),
    insurance_policy_number VARCHAR(50),
    medical_history TEXT,
    dental_history TEXT,
    allergies TEXT,
    current_medications TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_email CHECK (email IS NULL OR email LIKE '%@%.%')
) ENGINE=InnoDB;

-- Dental staff table
CREATE TABLE IF NOT EXISTS staff (
    staff_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    role ENUM('Dentist', 'Hygienist', 'Assistant', 'Receptionist', 'Admin') NOT NULL,
    license_number VARCHAR(50),
    specialization VARCHAR(100),
    phone VARCHAR(20),
    email VARCHAR(100) NOT NULL,
    hire_date DATE NOT NULL,
    active BOOLEAN DEFAULT TRUE,
    CONSTRAINT chk_staff_email CHECK (email LIKE '%@%.%')
) ENGINE=InnoDB;

-- Treatment types table (integrative dentistry treatments)
CREATE TABLE IF NOT EXISTS treatment_types (
    treatment_type_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    category ENUM('Preventive', 'Restorative', 'Cosmetic', 'Periodontal', 'Orthodontic', 'Holistic', 'Other') NOT NULL,
    duration_minutes INT NOT NULL,
    standard_fee DECIMAL(10, 2) NOT NULL
) ENGINE=InnoDB;

-- Treatment plans table
CREATE TABLE IF NOT EXISTS treatment_plans (
    plan_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    created_by INT NOT NULL,
    date_created DATE NOT NULL,
    expected_completion_date DATE,
    status ENUM('Draft', 'Active', 'Completed', 'Cancelled') NOT NULL DEFAULT 'Draft',
    notes TEXT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (created_by) REFERENCES staff(staff_id) ON DELETE RESTRICT
) ENGINE=InnoDB;

-- Plan items (individual treatments within a plan)
CREATE TABLE IF NOT EXISTS plan_items (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    plan_id INT NOT NULL,
    treatment_type_id INT NOT NULL,
    tooth_number VARCHAR(10),
    surface VARCHAR(20),
    priority ENUM('High', 'Medium', 'Low') NOT NULL DEFAULT 'Medium',
    status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') NOT NULL DEFAULT 'Pending',
    notes TEXT,
    FOREIGN KEY (plan_id) REFERENCES treatment_plans(plan_id) ON DELETE CASCADE,
    FOREIGN KEY (treatment_type_id) REFERENCES treatment_types(treatment_type_id) ON DELETE RESTRICT
) ENGINE=InnoDB;

-- Appointments table
CREATE TABLE IF NOT EXISTS appointments (
    appointment_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    staff_id INT NOT NULL,
    treatment_type_id INT,
    plan_item_id INT,
    appointment_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    status ENUM('Scheduled', 'Completed', 'Cancelled', 'No Show') NOT NULL DEFAULT 'Scheduled',
    notes TEXT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (staff_id) REFERENCES staff(staff_id) ON DELETE RESTRICT,
    FOREIGN KEY (treatment_type_id) REFERENCES treatment_types(treatment_type_id) ON DELETE SET NULL,
    FOREIGN KEY (plan_item_id) REFERENCES plan_items(item_id) ON DELETE SET NULL,
    CONSTRAINT chk_appointment_time CHECK (end_time > start_time)
) ENGINE=InnoDB;

-- Treatment sessions table (actual performed treatments)
CREATE TABLE IF NOT EXISTS treatment_sessions (
    session_id INT AUTO_INCREMENT PRIMARY KEY,
    appointment_id INT NOT NULL,
    plan_item_id INT,
    treatment_type_id INT NOT NULL,
    performed_by INT NOT NULL,
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP NOT NULL,
    notes TEXT,
    materials_used TEXT,
    anesthesia_used VARCHAR(100),
    complications TEXT,
    FOREIGN KEY (appointment_id) REFERENCES appointments(appointment_id) ON DELETE CASCADE,
    FOREIGN KEY (plan_item_id) REFERENCES plan_items(item_id) ON DELETE SET NULL,
    FOREIGN KEY (treatment_type_id) REFERENCES treatment_types(treatment_type_id) ON DELETE RESTRICT,
    FOREIGN KEY (performed_by) REFERENCES staff(staff_id) ON DELETE RESTRICT,
    CONSTRAINT chk_session_time CHECK (end_time > start_time)
) ENGINE=InnoDB;

-- Patient progress tracking
CREATE TABLE IF NOT EXISTS patient_progress (
    progress_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    recorded_by INT NOT NULL,
    record_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    metric_type ENUM('Pain Level', 'Mobility', 'Bleeding', 'Sensitivity', 'Swelling', 'Other') NOT NULL,
    metric_value VARCHAR(50) NOT NULL,
    notes TEXT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (recorded_by) REFERENCES staff(staff_id) ON DELETE RESTRICT
) ENGINE=InnoDB;

-- Treatment outcomes
CREATE TABLE IF NOT EXISTS treatment_outcomes (
    outcome_id INT AUTO_INCREMENT PRIMARY KEY,
    session_id INT NOT NULL,
    patient_id INT NOT NULL,
    evaluated_by INT NOT NULL,
    evaluation_date DATE NOT NULL,
    success_rating ENUM('Excellent', 'Good', 'Fair', 'Poor') NOT NULL,
    patient_feedback TEXT,
    complications TEXT,
    follow_up_required BOOLEAN DEFAULT FALSE,
    follow_up_date DATE,
    notes TEXT,
    FOREIGN KEY (session_id) REFERENCES treatment_sessions(session_id) ON DELETE CASCADE,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (evaluated_by) REFERENCES staff(staff_id) ON DELETE RESTRICT
) ENGINE=InnoDB;

-- Patient documents (X-rays, scans, etc.)
CREATE TABLE IF NOT EXISTS patient_documents (
    document_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    uploaded_by INT NOT NULL,
    document_type ENUM('X-ray', 'Scan', 'Photo', 'Report', 'Consent Form', 'Other') NOT NULL,
    file_path VARCHAR(255) NOT NULL,
    description TEXT,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (uploaded_by) REFERENCES staff(staff_id) ON DELETE RESTRICT
) ENGINE=InnoDB;

-- Billing and payments
CREATE TABLE IF NOT EXISTS billing (
    bill_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    appointment_id INT,
    total_amount DECIMAL(10, 2) NOT NULL,
    insurance_covered DECIMAL(10, 2) DEFAULT 0,
    patient_balance DECIMAL(10, 2) NOT NULL,
    due_date DATE NOT NULL,
    status ENUM('Pending', 'Paid', 'Partially Paid', 'Overdue', 'Written Off') NOT NULL DEFAULT 'Pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (appointment_id) REFERENCES appointments(appointment_id) ON DELETE SET NULL
) ENGINE=InnoDB;

-- Payment records
CREATE TABLE IF NOT EXISTS payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    bill_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_method ENUM('Cash', 'Credit Card', 'Debit Card', 'Check', 'Insurance', 'Other') NOT NULL,
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    processed_by INT NOT NULL,
    notes TEXT,
    FOREIGN KEY (bill_id) REFERENCES billing(bill_id) ON DELETE CASCADE,
    FOREIGN KEY (processed_by) REFERENCES staff(staff_id) ON DELETE RESTRICT
) ENGINE=InnoDB;

-- Create indexes for better performance
CREATE INDEX idx_patient_name ON patients(last_name, first_name);
CREATE INDEX idx_appointment_date ON appointments(appointment_date, start_time);
CREATE INDEX idx_treatment_plan ON plan_items(plan_id,
