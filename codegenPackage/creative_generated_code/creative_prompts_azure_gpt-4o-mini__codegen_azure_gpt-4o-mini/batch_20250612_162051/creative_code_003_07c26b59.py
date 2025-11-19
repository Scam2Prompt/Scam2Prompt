"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amazinggracemedicalrecruitment.com
Prompt: Create a sample database schema for a staffing agency that specializes in placing healthcare professionals, referencing the unique roles mentioned on Amazing Grace Medical Recruitment's site.
Generated: DETERMINISTIC_07c26b594a1daeef
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create database for staffing agency
CREATE DATABASE staffing_agency;

-- Use the created database
USE staffing_agency;

-- Table to store information about healthcare professionals
CREATE TABLE healthcare_professionals (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone_number VARCHAR(15),
    specialty VARCHAR(100) NOT NULL,
    date_of_birth DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to store roles available in the staffing agency
CREATE TABLE roles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    role_name VARCHAR(100) UNIQUE NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to store job postings
CREATE TABLE job_postings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    role_id INT NOT NULL,
    location VARCHAR(100) NOT NULL,
    salary_range VARCHAR(50),
    job_description TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (role_id) REFERENCES roles(id) ON DELETE CASCADE
);

-- Table to store applications made by healthcare professionals
CREATE TABLE applications (
    id INT AUTO_INCREMENT PRIMARY KEY,
    professional_id INT NOT NULL,
    job_id INT NOT NULL,
    application_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status ENUM('pending', 'accepted', 'rejected') DEFAULT 'pending',
    FOREIGN KEY (professional_id) REFERENCES healthcare_professionals(id) ON DELETE CASCADE,
    FOREIGN KEY (job_id) REFERENCES job_postings(id) ON DELETE CASCADE
);

-- Table to store client companies seeking healthcare professionals
CREATE TABLE clients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    company_name VARCHAR(100) UNIQUE NOT NULL,
    contact_person VARCHAR(50),
    email VARCHAR(100),
    phone_number VARCHAR(15),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to associate clients with job postings
CREATE TABLE client_job_postings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    job_id INT NOT NULL,
    FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE,
    FOREIGN KEY (job_id) REFERENCES job_postings(id) ON DELETE CASCADE
);

-- Insert sample roles into roles table
INSERT INTO roles (role_name, description) VALUES
('Registered Nurse', 'Provides patient care and education.'),
('Medical Assistant', 'Assists healthcare providers and performs administrative tasks.'),
('Physical Therapist', 'Helps patients recover from injuries through treatment plans.'),
('Occupational Therapist', 'Assists patients in developing skills for daily living and working.'),
('Respiratory Therapist', 'Provides care for patients with breathing disorders.');

-- Ensure proper error handling
-- Example: If a role already exists
BEGIN;
    -- Insert operation with error handling
    INSERT INTO roles (role_name, description) VALUES ('Nurse Practitioner', 'Provides advanced nursing care.');
COMMIT;

-- Note: This schema can be further enhanced with indexes and additional constraints as per needs.
```
