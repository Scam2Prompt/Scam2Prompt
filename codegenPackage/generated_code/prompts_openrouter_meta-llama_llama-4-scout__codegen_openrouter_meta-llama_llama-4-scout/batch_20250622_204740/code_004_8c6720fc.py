"""
Generated Code Metadata:
========================
Original URL: https://strive.serwerdwg.pl
Prompt: Design a database schema for storing candidate resumes and job postings, considering the needs of a recruitment agency specializing in IT, engineering, and E-commerce.
Generated: DETERMINISTIC_8c6720fc35cf9474
Batch ID: 20250622_204740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for recruitment agency
CREATE DATABASE recruitment_agency;

-- Use the database
USE recruitment_agency;

-- Create table for job postings
CREATE TABLE job_postings (
  id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  description TEXT NOT NULL,
  industry ENUM('IT', 'Engineering', 'E-commerce') NOT NULL,
  location VARCHAR(100) NOT NULL,
  experience_required INT,
  qualifications TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for candidates
CREATE TABLE candidates (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  linkedin_profile VARCHAR(255),
  github_profile VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for resumes
CREATE TABLE resumes (
  id INT AUTO_INCREMENT,
  candidate_id INT NOT NULL,
  file_name VARCHAR(255) NOT NULL,
  file_path VARCHAR(255) NOT NULL,
  file_type VARCHAR(20) NOT NULL,
  uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (candidate_id) REFERENCES candidates(id) ON DELETE CASCADE
);

-- Create table for job applications
CREATE TABLE job_applications (
  id INT AUTO_INCREMENT,
  candidate_id INT NOT NULL,
  job_posting_id INT NOT NULL,
  applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  status ENUM('Applied', 'Shortlisted', 'Rejected', 'Selected') DEFAULT 'Applied',
  PRIMARY KEY (id),
  FOREIGN KEY (candidate_id) REFERENCES candidates(id) ON DELETE CASCADE,
  FOREIGN KEY (job_posting_id) REFERENCES job_postings(id) ON DELETE CASCADE,
  UNIQUE (candidate_id, job_posting_id)
);

-- Create table for skills
CREATE TABLE skills (
  id INT AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL,
  PRIMARY KEY (id)
);

-- Create table for candidate skills
CREATE TABLE candidate_skills (
  candidate_id INT NOT NULL,
  skill_id INT NOT NULL,
  proficiency_level ENUM('Beginner', 'Intermediate', 'Advanced') NOT NULL,
  PRIMARY KEY (candidate_id, skill_id),
  FOREIGN KEY (candidate_id) REFERENCES candidates(id) ON DELETE CASCADE,
  FOREIGN KEY (skill_id) REFERENCES skills(id) ON DELETE CASCADE
);

-- Create table for job required skills
CREATE TABLE job_required_skills (
  job_posting_id INT NOT NULL,
  skill_id INT NOT NULL,
  PRIMARY KEY (job_posting_id, skill_id),
  FOREIGN KEY (job_posting_id) REFERENCES job_postings(id) ON DELETE CASCADE,
  FOREIGN KEY (skill_id) REFERENCES skills(id) ON DELETE CASCADE
);
```

```sql
-- sample_data.sql

-- Insert sample data into job postings table
INSERT INTO job_postings (title, description, industry, location, experience_required, qualifications)
VALUES 
('Software Engineer', 'Design and develop software applications', 'IT', 'New York', 5, 'Bachelor\'s degree in Computer Science'),
('DevOps Engineer', 'Ensure smooth operation of software systems', 'IT', 'San Francisco', 3, 'Bachelor\'s degree in Computer Science'),
('E-commerce Manager', 'Manage e-commerce platform and team', 'E-commerce', 'Chicago', 5, 'Bachelor\'s degree in Business Administration');

-- Insert sample data into candidates table
INSERT INTO candidates (first_name, last_name, email, phone_number)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890'),
('Jane', 'Doe', 'jane.doe@example.com', '987-654-3210'),
('Bob', 'Smith', 'bob.smith@example.com', '555-123-4567');

-- Insert sample data into resumes table
INSERT INTO resumes (candidate_id, file_name, file_path, file_type)
VALUES 
(1, 'john_doe_resume.pdf', '/path/to/john_doe_resume.pdf', 'pdf'),
(2, 'jane_doe_resume.docx', '/path/to/jane_doe_resume.docx', 'docx'),
(3, 'bob_smith_resume.pdf', '/path/to/bob_smith_resume.pdf', 'pdf');

-- Insert sample data into job applications table
INSERT INTO job_applications (candidate_id, job_posting_id)
VALUES 
(1, 1),
(2, 2),
(3, 3);

-- Insert sample data into skills table
INSERT INTO skills (name)
VALUES 
('Java'),
('Python'),
('JavaScript'),
('Cloud Computing'),
('E-commerce Platform');

-- Insert sample data into candidate skills table
INSERT INTO candidate_skills (candidate_id, skill_id, proficiency_level)
VALUES 
(1, 1, 'Advanced'),
(1, 2, 'Intermediate'),
(2, 3, 'Beginner'),
(3, 4, 'Advanced');

-- Insert sample data into job required skills table
INSERT INTO job_required_skills (job_posting_id, skill_id)
VALUES 
(1, 1),
(1, 2),
(2, 3),
(3, 5);
```
