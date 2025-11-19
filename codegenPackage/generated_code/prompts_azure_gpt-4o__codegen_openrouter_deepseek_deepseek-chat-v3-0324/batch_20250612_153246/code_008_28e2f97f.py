"""
Generated Code Metadata:
========================
Original URL: https://simho.in
Prompt: Create a database schema to store HR service details, including permanent staffing, temporary staffing, and training, based on the structure provided by SIMHO.
Generated: DETERMINISTIC_28e2f97f063c76b1
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for HR services management system
-- Includes tables for permanent staffing, temporary staffing, and training services

-- Create database
CREATE DATABASE IF NOT EXISTS hr_services_management;
USE hr_services_management;

-- Company table (stores client companies)
CREATE TABLE IF NOT EXISTS companies (
    company_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    industry VARCHAR(50),
    address TEXT,
    contact_person VARCHAR(100),
    contact_email VARCHAR(100),
    contact_phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY unique_company (name, contact_email)
) ENGINE=InnoDB;

-- Permanent Staffing table
CREATE TABLE IF NOT EXISTS permanent_staffing (
    staffing_id INT AUTO_INCREMENT PRIMARY KEY,
    company_id INT NOT NULL,
    position_title VARCHAR(100) NOT NULL,
    department VARCHAR(50),
    job_description TEXT,
    salary_range VARCHAR(50),
    experience_required VARCHAR(100),
    qualifications_required TEXT,
    status ENUM('open', 'filled', 'closed') DEFAULT 'open',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (company_id) REFERENCES companies(company_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Temporary Staffing table
CREATE TABLE IF NOT EXISTS temporary_staffing (
    temp_id INT AUTO_INCREMENT PRIMARY KEY,
    company_id INT NOT NULL,
    position_title VARCHAR(100) NOT NULL,
    department VARCHAR(50),
    job_description TEXT,
    hourly_rate DECIMAL(10,2),
    duration_weeks INT,
    start_date DATE,
    end_date DATE,
    status ENUM('active', 'completed', 'cancelled') DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (company_id) REFERENCES companies(company_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Training Programs table
CREATE TABLE IF NOT EXISTS training_programs (
    program_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    duration_hours INT,
    cost DECIMAL(10,2),
    trainer_name VARCHAR(100),
    max_participants INT,
    category VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Training Sessions table (specific instances of training programs)
CREATE TABLE IF NOT EXISTS training_sessions (
    session_id INT AUTO_INCREMENT PRIMARY KEY,
    program_id INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    location VARCHAR(100),
    status ENUM('scheduled', 'ongoing', 'completed', 'cancelled') DEFAULT 'scheduled',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (program_id) REFERENCES training_programs(program_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Company Training Enrollment table
CREATE TABLE IF NOT EXISTS company_training_enrollment (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    company_id INT NOT NULL,
    session_id INT NOT NULL,
    participants_count INT DEFAULT 1,
    enrollment_date DATE NOT NULL,
    payment_status ENUM('pending', 'paid', 'cancelled') DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (company_id) REFERENCES companies(company_id) ON DELETE CASCADE,
    FOREIGN KEY (session_id) REFERENCES training_sessions(session_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Candidates table (for both permanent and temporary positions)
CREATE TABLE IF NOT EXISTS candidates (
    candidate_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(20),
    resume_path VARCHAR(255),
    skills TEXT,
    experience_years INT,
    education_level VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Permanent Staffing Applications
CREATE TABLE IF NOT EXISTS permanent_applications (
    application_id INT AUTO_INCREMENT PRIMARY KEY,
    candidate_id INT NOT NULL,
    staffing_id INT NOT NULL,
    application_date DATE NOT NULL,
    status ENUM('submitted', 'reviewed', 'interviewed', 'offered', 'hired', 'rejected') DEFAULT 'submitted',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (candidate_id) REFERENCES candidates(candidate_id) ON DELETE CASCADE,
    FOREIGN KEY (staffing_id) REFERENCES permanent_staffing(staffing_id) ON DELETE CASCADE,
    UNIQUE KEY unique_application (candidate_id, staffing_id)
) ENGINE=InnoDB;

-- Temporary Staffing Assignments
CREATE TABLE IF NOT EXISTS temporary_assignments (
    assignment_id INT AUTO_INCREMENT PRIMARY KEY,
    candidate_id INT NOT NULL,
    temp_id INT NOT NULL,
    assignment_date DATE NOT NULL,
    end_date DATE,
    status ENUM('active', 'completed', 'terminated') DEFAULT 'active',
    performance_rating INT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (candidate_id) REFERENCES candidates(candidate_id) ON DELETE CASCADE,
    FOREIGN KEY (temp_id) REFERENCES temporary_staffing(temp_id) ON DELETE CASCADE,
    UNIQUE KEY unique_assignment (candidate_id, temp_id)
) ENGINE=InnoDB;

-- Training Participants (individuals attending training)
CREATE TABLE IF NOT EXISTS training_participants (
    participant_id INT AUTO_INCREMENT PRIMARY KEY,
    candidate_id INT,
    session_id INT NOT NULL,
    enrollment_id INT NOT NULL,
    attendance_status ENUM('registered', 'attended', 'no-show') DEFAULT 'registered',
    completion_status ENUM('in-progress', 'completed', 'failed') DEFAULT 'in-progress',
    evaluation_score INT,
    feedback TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (candidate_id) REFERENCES candidates(candidate_id) ON DELETE SET NULL,
    FOREIGN KEY (session_id) REFERENCES training_sessions(session_id) ON DELETE CASCADE,
    FOREIGN KEY (enrollment_id) REFERENCES company_training_enrollment(enrollment_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Invoices table for all services
CREATE TABLE IF NOT EXISTS invoices (
    invoice_id INT AUTO_INCREMENT PRIMARY KEY,
    company_id INT NOT NULL,
    service_type ENUM('permanent', 'temporary', 'training') NOT NULL,
    service_id INT NOT NULL, -- references staffing_id, temp_id, or enrollment_id based on service_type
    invoice_date DATE NOT NULL,
    due_date DATE NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    tax_amount DECIMAL(10,2) DEFAULT 0,
    total_amount DECIMAL(10,2) NOT NULL,
    status ENUM('draft', 'sent', 'paid', 'overdue', 'cancelled') DEFAULT 'draft',
    payment_date DATE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (company_id) REFERENCES companies(company_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Create indexes for performance optimization
CREATE INDEX idx_permanent_staffing_company ON permanent_staffing(company_id);
CREATE INDEX idx_temporary_staffing_company ON temporary_staffing(company_id);
CREATE INDEX idx_training_enrollment_company ON company_training_enrollment(company_id);
CREATE INDEX idx_training_enrollment_session ON company_training_enrollment(session_id);
CREATE INDEX idx_permanent_applications_candidate ON permanent_applications(candidate_id);
CREATE INDEX idx_permanent_applications_staffing ON permanent_applications(staffing_id);
CREATE INDEX idx_temporary_assignments_candidate ON temporary_assignments(candidate_id);
CREATE INDEX idx_temporary_assignments_temp ON temporary_assignments(temp_id);
CREATE INDEX idx_invoices_company ON invoices(company_id);
```
