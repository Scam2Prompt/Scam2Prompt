"""
Generated Code Metadata:
========================
Original URL: https://mandosecurity.com
Prompt: "Design a simple database schema to store information about security guards, their training, and deployment for a company like Mando Security."
Generated: DETERMINISTIC_914fe72fc33a9d1a
Batch ID: 20250622_205929
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for security guard management system

-- Create the database
CREATE DATABASE IF NOT EXISTS security_management;
USE security_management;

-- Guards table to store basic guard information
CREATE TABLE IF NOT EXISTS guards (
    guard_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender ENUM('Male', 'Female', 'Other') NOT NULL,
    contact_number VARCHAR(20) NOT NULL,
    email VARCHAR(100) UNIQUE,
    address TEXT NOT NULL,
    hire_date DATE NOT NULL,
    employment_status ENUM('Active', 'On Leave', 'Terminated') DEFAULT 'Active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_contact_number CHECK (contact_number REGEXP '^[0-9]{10,15}$'),
    CONSTRAINT chk_email CHECK (email IS NULL OR email REGEXP '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,4}$')
) ENGINE=InnoDB;

-- Training programs table
CREATE TABLE IF NOT EXISTS training_programs (
    program_id INT AUTO_INCREMENT PRIMARY KEY,
    program_name VARCHAR(100) NOT NULL,
    description TEXT,
    duration_hours INT NOT NULL,
    certification_required BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_duration CHECK (duration_hours > 0)
) ENGINE=InnoDB;

-- Guard training records (junction table)
CREATE TABLE IF NOT EXISTS guard_trainings (
    record_id INT AUTO_INCREMENT PRIMARY KEY,
    guard_id INT NOT NULL,
    program_id INT NOT NULL,
    completion_date DATE NOT NULL,
    expiry_date DATE,
    trainer_name VARCHAR(100),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (guard_id) REFERENCES guards(guard_id) ON DELETE CASCADE,
    FOREIGN KEY (program_id) REFERENCES training_programs(program_id) ON DELETE CASCADE,
    CONSTRAINT chk_dates CHECK (expiry_date IS NULL OR completion_date <= expiry_date)
) ENGINE=InnoDB;

-- Client sites table
CREATE TABLE IF NOT EXISTS client_sites (
    site_id INT AUTO_INCREMENT PRIMARY KEY,
    client_name VARCHAR(100) NOT NULL,
    site_name VARCHAR(100) NOT NULL,
    address TEXT NOT NULL,
    contact_person VARCHAR(100),
    contact_number VARCHAR(20),
    special_requirements TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_site_contact_number CHECK (contact_number IS NULL OR contact_number REGEXP '^[0-9]{10,15}$')
) ENGINE=InnoDB;

-- Shifts table
CREATE TABLE IF NOT EXISTS shifts (
    shift_id INT AUTO_INCREMENT PRIMARY KEY,
    site_id INT NOT NULL,
    shift_name VARCHAR(50) NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    required_guards INT NOT NULL DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (site_id) REFERENCES client_sites(site_id) ON DELETE CASCADE,
    CONSTRAINT chk_times CHECK (start_time < end_time),
    CONSTRAINT chk_guards CHECK (required_guards > 0)
) ENGINE=InnoDB;

-- Guard deployments (junction table)
CREATE TABLE IF NOT EXISTS deployments (
    deployment_id INT AUTO_INCREMENT PRIMARY KEY,
    guard_id INT NOT NULL,
    shift_id INT NOT NULL,
    deployment_date DATE NOT NULL,
    status ENUM('Scheduled', 'Completed', 'Cancelled', 'No Show') DEFAULT 'Scheduled',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (guard_id) REFERENCES guards(guard_id) ON DELETE CASCADE,
    FOREIGN KEY (shift_id) REFERENCES shifts(shift_id) ON DELETE CASCADE,
    UNIQUE KEY unique_deployment (guard_id, shift_id, deployment_date)
) ENGINE=InnoDB;

-- Equipment table
CREATE TABLE IF NOT EXISTS equipment (
    equipment_id INT AUTO_INCREMENT PRIMARY KEY,
    equipment_name VARCHAR(100) NOT NULL,
    description TEXT,
    quantity_available INT NOT NULL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_quantity CHECK (quantity_available >= 0)
) ENGINE=InnoDB;

-- Equipment assignments
CREATE TABLE IF NOT EXISTS equipment_assignments (
    assignment_id INT AUTO_INCREMENT PRIMARY KEY,
    deployment_id INT NOT NULL,
    equipment_id INT NOT NULL,
    quantity_assigned INT NOT NULL DEFAULT 1,
    return_date DATE,
    return_condition ENUM('Good', 'Damaged', 'Lost') DEFAULT 'Good',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (deployment_id) REFERENCES deployments(deployment_id) ON DELETE CASCADE,
    FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id) ON DELETE CASCADE,
    CONSTRAINT chk_assigned_quantity CHECK (quantity_assigned > 0)
) ENGINE=InnoDB;

-- Incident reports
CREATE TABLE IF NOT EXISTS incident_reports (
    report_id INT AUTO_INCREMENT PRIMARY KEY,
    deployment_id INT NOT NULL,
    incident_date DATETIME NOT NULL,
    incident_type VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    action_taken TEXT,
    reported_by VARCHAR(100) NOT NULL,
    severity ENUM('Low', 'Medium', 'High', 'Critical') NOT NULL,
    follow_up_required BOOLEAN DEFAULT FALSE,
    follow_up_notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (deployment_id) REFERENCES deployments(deployment_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Performance evaluations
CREATE TABLE IF NOT EXISTS performance_evaluations (
    evaluation_id INT AUTO_INCREMENT PRIMARY KEY,
    guard_id INT NOT NULL,
    evaluator_id INT NOT NULL,
    evaluation_date DATE NOT NULL,
    overall_rating DECIMAL(3,1) NOT NULL,
    punctuality_rating DECIMAL(3,1) NOT NULL,
    professionalism_rating DECIMAL(3,1) NOT NULL,
    knowledge_rating DECIMAL(3,1) NOT NULL,
    comments TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (guard_id) REFERENCES guards(guard_id) ON DELETE CASCADE,
    FOREIGN KEY (evaluator_id) REFERENCES guards(guard_id) ON DELETE CASCADE,
    CONSTRAINT chk_rating CHECK (
        overall_rating BETWEEN 1 AND 5 AND
        punctuality_rating BETWEEN 1 AND 5 AND
        professionalism_rating BETWEEN 1 AND 5 AND
        knowledge_rating BETWEEN 1 AND 5
    )
) ENGINE=InnoDB;
```
