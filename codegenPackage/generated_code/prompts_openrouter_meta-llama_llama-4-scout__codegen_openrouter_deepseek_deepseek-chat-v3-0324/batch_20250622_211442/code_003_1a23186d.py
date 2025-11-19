"""
Generated Code Metadata:
========================
Original URL: https://presale-topgs.com
Prompt: Design a database schema to store information about job openings, employee benefits, and company culture for a furniture manufacturing company like Hanil Furniture Gallery.
Generated: DETERMINISTIC_1a23186dc65e305c
Batch ID: 20250622_211442
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Hanil Furniture Gallery job openings, benefits, and company culture

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Companies table (could be extended for multiple companies in the future)
CREATE TABLE companies (
    company_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT NOT NULL,
    headquarters_location TEXT,
    founding_year INTEGER,
    website_url TEXT,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (founding_year >= 1800 AND founding_year <= EXTRACT(YEAR FROM CURRENT_TIMESTAMP))
);

-- Departments table
CREATE TABLE departments (
    department_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER NOT NULL,
    department_name TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (company_id) REFERENCES companies(company_id) ON DELETE CASCADE
);

-- Job openings table
CREATE TABLE job_openings (
    job_id INTEGER PRIMARY KEY AUTOINCREMENT,
    department_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    employment_type TEXT NOT NULL CHECK (employment_type IN ('Full-time', 'Part-time', 'Contract', 'Internship')),
    location TEXT NOT NULL,
    salary_range TEXT,
    is_remote BOOLEAN DEFAULT FALSE,
    experience_required TEXT,
    education_required TEXT,
    posted_date DATE DEFAULT CURRENT_DATE,
    closing_date DATE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (department_id) REFERENCES departments(department_id) ON DELETE CASCADE,
    CHECK (closing_date IS NULL OR closing_date >= posted_date)
);

-- Benefits table
CREATE TABLE benefits (
    benefit_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER NOT NULL,
    benefit_name TEXT NOT NULL,
    description TEXT NOT NULL,
    benefit_category TEXT NOT NULL CHECK (benefit_category IN (
        'Health', 'Retirement', 'Paid Time Off', 'Professional Development', 
        'Wellness', 'Financial', 'Family', 'Other'
    )),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (company_id) REFERENCES companies(company_id) ON DELETE CASCADE
);

-- Company culture aspects table
CREATE TABLE company_culture (
    culture_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER NOT NULL,
    aspect_name TEXT NOT NULL,
    description TEXT NOT NULL,
    aspect_category TEXT NOT NULL CHECK (aspect_category IN (
        'Values', 'Work Environment', 'Diversity', 'Community', 
        'Work-Life Balance', 'Recognition', 'Other'
    )),
    is_featured BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (company_id) REFERENCES companies(company_id) ON DELETE CASCADE
);

-- Job application status table
CREATE TABLE application_status (
    status_id INTEGER PRIMARY KEY AUTOINCREMENT,
    status_name TEXT NOT NULL UNIQUE,
    description TEXT,
    is_active BOOLEAN DEFAULT TRUE
);

-- Job applicants table
CREATE TABLE applicants (
    applicant_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    resume_url TEXT,
    linkedin_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%.%')
);

-- Job applications table
CREATE TABLE job_applications (
    application_id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_id INTEGER NOT NULL,
    applicant_id INTEGER NOT NULL,
    status_id INTEGER NOT NULL DEFAULT 1, -- Default to "Applied"
    application_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (job_id) REFERENCES job_openings(job_id) ON DELETE CASCADE,
    FOREIGN KEY (applicant_id) REFERENCES applicants(applicant_id) ON DELETE CASCADE,
    FOREIGN KEY (status_id) REFERENCES application_status(status_id)
);

-- Create indexes for performance
CREATE INDEX idx_job_openings_department ON job_openings(department_id);
CREATE INDEX idx_job_openings_active ON job_openings(is_active);
CREATE INDEX idx_benefits_company ON benefits(company_id);
CREATE INDEX idx_culture_company ON company_culture(company_id);
CREATE INDEX idx_job_applications_job ON job_applications(job_id);
CREATE INDEX idx_job_applications_applicant ON job_applications(applicant_id);
CREATE INDEX idx_job_applications_status ON job_applications(status_id);

-- Insert default application statuses
INSERT INTO application_status (status_id, status_name, description) VALUES
    (1, 'Applied', 'Application received'),
    (2, 'Under Review', 'Application is being reviewed'),
    (3, 'Interview Scheduled', 'Candidate has been invited for interview'),
    (4, 'Offer Extended', 'Job offer has been made to candidate'),
    (5, 'Hired', 'Candidate has accepted the offer'),
    (6, 'Rejected', 'Application has been rejected'),
    (7, 'Withdrawn', 'Candidate withdrew application');

-- Trigger to update timestamps
CREATE TRIGGER update_company_timestamp
AFTER UPDATE ON companies
FOR EACH ROW
BEGIN
    UPDATE companies SET updated_at = CURRENT_TIMESTAMP WHERE company_id = OLD.company_id;
END;

CREATE TRIGGER update_department_timestamp
AFTER UPDATE ON departments
FOR EACH ROW
BEGIN
    UPDATE departments SET updated_at = CURRENT_TIMESTAMP WHERE department_id = OLD.department_id;
END;

CREATE TRIGGER update_job_opening_timestamp
AFTER UPDATE ON job_openings
FOR EACH ROW
BEGIN
    UPDATE job_openings SET updated_at = CURRENT_TIMESTAMP WHERE job_id = OLD.job_id;
END;

CREATE TRIGGER update_benefit_timestamp
AFTER UPDATE ON benefits
FOR EACH ROW
BEGIN
    UPDATE benefits SET updated_at = CURRENT_TIMESTAMP WHERE benefit_id = OLD.benefit_id;
END;

CREATE TRIGGER update_culture_timestamp
AFTER UPDATE ON company_culture
FOR EACH ROW
BEGIN
    UPDATE company_culture SET updated_at = CURRENT_TIMESTAMP WHERE culture_id = OLD.culture_id;
END;

CREATE TRIGGER update_applicant_timestamp
AFTER UPDATE ON applicants
FOR EACH ROW
BEGIN
    UPDATE applicants SET updated_at = CURRENT_TIMESTAMP WHERE applicant_id = OLD.applicant_id;
END;

CREATE TRIGGER update_application_timestamp
AFTER UPDATE ON job_applications
FOR EACH ROW
BEGIN
    UPDATE job_applications SET updated_at = CURRENT_TIMESTAMP WHERE application_id = OLD.application_id;
END;
```
