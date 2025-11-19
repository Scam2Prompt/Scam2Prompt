"""
Generated Code Metadata:
========================
Original URL: https://highvaluestaffing.com
Prompt: Create a database schema for managing candidate profiles and job postings, focusing on features like "certified methods" and "quality standards" mentioned on High Value Staffing's website.
Generated: DETERMINISTIC_a857d73be86228f4
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for candidate profiles and job postings

-- Create database
CREATE DATABASE staffing_database;

-- Use database
USE staffing_database;

-- Create table for candidate profiles
CREATE TABLE candidates (
    id INT AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(20),
    address VARCHAR(255),
    certified_methods VARCHAR(255),
    quality_standards VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

-- Create table for job postings
CREATE TABLE job_postings (
    id INT AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    certified_methods VARCHAR(255),
    quality_standards VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

-- Create table for candidate skills
CREATE TABLE candidate_skills (
    id INT AUTO_INCREMENT,
    candidate_id INT NOT NULL,
    skill VARCHAR(255) NOT NULL,
    experience_level VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (candidate_id) REFERENCES candidates(id) ON DELETE CASCADE
);

-- Create table for job requirements
CREATE TABLE job_requirements (
    id INT AUTO_INCREMENT,
    job_posting_id INT NOT NULL,
    requirement VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (job_posting_id) REFERENCES job_postings(id) ON DELETE CASCADE
);

-- Create table for candidate job applications
CREATE TABLE candidate_applications (
    id INT AUTO_INCREMENT,
    candidate_id INT NOT NULL,
    job_posting_id INT NOT NULL,
    application_date DATE NOT NULL,
    status VARCHAR(255) NOT NULL DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (candidate_id) REFERENCES candidates(id) ON DELETE CASCADE,
    FOREIGN KEY (job_posting_id) REFERENCES job_postings(id) ON DELETE CASCADE,
    UNIQUE KEY (candidate_id, job_posting_id)
);

-- Create indexes for efficient querying
CREATE INDEX idx_candidates_email ON candidates(email);
CREATE INDEX idx_job_postings_title ON job_postings(title);
CREATE INDEX idx_candidate_skills_candidate_id ON candidate_skills(candidate_id);
CREATE INDEX idx_job_requirements_job_posting_id ON job_requirements(job_posting_id);
CREATE INDEX idx_candidate_applications_candidate_id ON candidate_applications(candidate_id);
CREATE INDEX idx_candidate_applications_job_posting_id ON candidate_applications(job_posting_id);
```

```sql
-- Example stored procedures for common operations

DELIMITER //

CREATE PROCEDURE create_candidate(
    IN p_first_name VARCHAR(255),
    IN p_last_name VARCHAR(255),
    IN p_email VARCHAR(255),
    IN p_phone_number VARCHAR(20),
    IN p_address VARCHAR(255),
    IN p_certified_methods VARCHAR(255),
    IN p_quality_standards VARCHAR(255)
)
BEGIN
    INSERT INTO candidates (first_name, last_name, email, phone_number, address, certified_methods, quality_standards)
    VALUES (p_first_name, p_last_name, p_email, p_phone_number, p_address, p_certified_methods, p_quality_standards);
END //

CREATE PROCEDURE create_job_posting(
    IN p_title VARCHAR(255),
    IN p_description TEXT,
    IN p_certified_methods VARCHAR(255),
    IN p_quality_standards VARCHAR(255)
)
BEGIN
    INSERT INTO job_postings (title, description, certified_methods, quality_standards)
    VALUES (p_title, p_description, p_certified_methods, p_quality_standards);
END //

DELIMITER ;
```

```sql
-- Example usage:

-- Create a new candidate
CALL create_candidate('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St', 'Agile', 'ISO 9001');

-- Create a new job posting
CALL create_job_posting('Software Engineer', 'Design and develop software applications', 'Scrum', 'CMMI');

-- Retrieve all candidates with their skills
SELECT c.*, cs.skill, cs.experience_level
FROM candidates c
JOIN candidate_skills cs ON c.id = cs.candidate_id;

-- Retrieve all job postings with their requirements
SELECT jp.*, jr.requirement
FROM job_postings jp
JOIN job_requirements jr ON jp.id = jr.job_posting_id;
```
