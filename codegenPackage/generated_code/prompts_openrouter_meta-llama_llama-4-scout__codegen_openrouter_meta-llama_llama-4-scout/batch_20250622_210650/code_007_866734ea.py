"""
Generated Code Metadata:
========================
Original URL: https://recruit-overseas.com
Prompt: Design a database schema to store information about job roles, candidates, and clients for a recruitment agency like Recruit Overseas.
Generated: DETERMINISTIC_866734eaf347fd2d
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for Recruit Overseas
CREATE DATABASE recruit_overseas;

-- Use the database
USE recruit_overseas;

-- Create table for job roles
CREATE TABLE job_roles (
    id INT AUTO_INCREMENT,
    role_name VARCHAR(255) NOT NULL,
    role_description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

-- Create table for clients
CREATE TABLE clients (
    id INT AUTO_INCREMENT,
    company_name VARCHAR(255) NOT NULL,
    contact_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(20),
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

-- Create table for candidates
CREATE TABLE candidates (
    id INT AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(20),
    address TEXT,
    cv TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

-- Create table for job postings
CREATE TABLE job_postings (
    id INT AUTO_INCREMENT,
    job_role_id INT NOT NULL,
    client_id INT NOT NULL,
    job_title VARCHAR(255) NOT NULL,
    job_description TEXT,
    location VARCHAR(255) NOT NULL,
    salary DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (job_role_id) REFERENCES job_roles(id) ON DELETE CASCADE,
    FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE
);

-- Create table for candidate applications
CREATE TABLE candidate_applications (
    id INT AUTO_INCREMENT,
    candidate_id INT NOT NULL,
    job_posting_id INT NOT NULL,
    application_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    application_status ENUM('pending', 'shortlisted', 'rejected', 'selected') DEFAULT 'pending',
    PRIMARY KEY (id),
    FOREIGN KEY (candidate_id) REFERENCES candidates(id) ON DELETE CASCADE,
    FOREIGN KEY (job_posting_id) REFERENCES job_postings(id) ON DELETE CASCADE,
    UNIQUE KEY (candidate_id, job_posting_id)
);

-- Create table for interviews
CREATE TABLE interviews (
    id INT AUTO_INCREMENT,
    candidate_application_id INT NOT NULL,
    interview_date DATE NOT NULL,
    interview_time TIME NOT NULL,
    interview_location VARCHAR(255) NOT NULL,
    interview_type ENUM('phone', 'video', 'in-person') NOT NULL,
    interview_status ENUM('scheduled', 'conducted', 'cancelled') NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (candidate_application_id) REFERENCES candidate_applications(id) ON DELETE CASCADE
);

-- Create table for feedback
CREATE TABLE feedback (
    id INT AUTO_INCREMENT,
    candidate_application_id INT NOT NULL,
    feedback_type ENUM('candidate', 'client') NOT NULL,
    feedback_text TEXT,
    rating TINYINT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (candidate_application_id) REFERENCES candidate_applications(id) ON DELETE CASCADE
);
```
