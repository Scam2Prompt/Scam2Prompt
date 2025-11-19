"""
Generated Code Metadata:
========================
Original URL: https://accuratehire.co.in
Prompt: "Design a database schema to store information about job seekers, job openings, and recruitment services, inspired by Accurate Hire's approach to connecting people with opportunities."
Generated: DETERMINISTIC_44efd6ecd7c667f1
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database
CREATE DATABASE recruitment_services;

-- Use database
USE recruitment_services;

-- Create table for job seekers
CREATE TABLE job_seekers (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  resume TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for job openings
CREATE TABLE job_openings (
  id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  description TEXT NOT NULL,
  company_name VARCHAR(255) NOT NULL,
  company_description TEXT,
  location VARCHAR(255) NOT NULL,
  salary DECIMAL(10, 2),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for recruitment services
CREATE TABLE recruitment_services (
  id INT AUTO_INCREMENT,
  service_name VARCHAR(255) NOT NULL,
  service_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for job seeker skills
CREATE TABLE job_seeker_skills (
  id INT AUTO_INCREMENT,
  job_seeker_id INT NOT NULL,
  skill VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (job_seeker_id) REFERENCES job_seekers(id) ON DELETE CASCADE
);

-- Create table for job opening requirements
CREATE TABLE job_opening_requirements (
  id INT AUTO_INCREMENT,
  job_opening_id INT NOT NULL,
  requirement VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (job_opening_id) REFERENCES job_openings(id) ON DELETE CASCADE
);

-- Create table for job applications
CREATE TABLE job_applications (
  id INT AUTO_INCREMENT,
  job_seeker_id INT NOT NULL,
  job_opening_id INT NOT NULL,
  application_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  status VARCHAR(50) NOT NULL DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (job_seeker_id) REFERENCES job_seekers(id) ON DELETE CASCADE,
  FOREIGN KEY (job_opening_id) REFERENCES job_openings(id) ON DELETE CASCADE,
  CHECK (status IN ('pending', 'interviewing', 'rejected', 'hired'))
);

-- Create table for service providers
CREATE TABLE service_providers (
  id INT AUTO_INCREMENT,
  service_id INT NOT NULL,
  provider_name VARCHAR(255) NOT NULL,
  provider_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (service_id) REFERENCES recruitment_services(id) ON DELETE CASCADE
);

-- Create table for job seeker service subscriptions
CREATE TABLE job_seeker_service_subscriptions (
  id INT AUTO_INCREMENT,
  job_seeker_id INT NOT NULL,
  service_id INT NOT NULL,
  subscription_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (job_seeker_id) REFERENCES job_seekers(id) ON DELETE CASCADE,
  FOREIGN KEY (service_id) REFERENCES recruitment_services(id) ON DELETE CASCADE
);

-- Create indexes for foreign keys
CREATE INDEX idx_job_seeker_skills_job_seeker_id ON job_seeker_skills (job_seeker_id);
CREATE INDEX idx_job_opening_requirements_job_opening_id ON job_opening_requirements (job_opening_id);
CREATE INDEX idx_job_applications_job_seeker_id ON job_applications (job_seeker_id);
CREATE INDEX idx_job_applications_job_opening_id ON job_applications (job_opening_id);
CREATE INDEX idx_service_providers_service_id ON service_providers (service_id);
CREATE INDEX idx_job_seeker_service_subscriptions_job_seeker_id ON job_seeker_service_subscriptions (job_seeker_id);
CREATE INDEX idx_job_seeker_service_subscriptions_service_id ON job_seeker_service_subscriptions (service_id);
```

```sql
-- data.sql

-- Insert sample data into job seekers table
INSERT INTO job_seekers (first_name, last_name, email, phone_number, address, resume)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St', 'Sample resume'),
('Jane', 'Doe', 'jane.doe@example.com', '987-654-3210', '456 Elm St', 'Sample resume');

-- Insert sample data into job openings table
INSERT INTO job_openings (title, description, company_name, company_description, location, salary)
VALUES 
('Software Engineer', 'Design and develop software applications', 'ABC Corporation', 'Leading technology company', 'New York, NY', 100000.00),
('Data Scientist', 'Analyze and interpret complex data', 'DEF Company', 'Data analytics firm', 'San Francisco, CA', 120000.00);

-- Insert sample data into recruitment services table
INSERT INTO recruitment_services (service_name, service_description)
VALUES 
('Resume Building', 'Professional resume writing services'),
('Interview Coaching', 'Personalized interview coaching');

-- Insert sample data into job seeker skills table
INSERT INTO job_seeker_skills (job_seeker_id, skill)
VALUES 
(1, 'Java'),
(1, 'Python'),
(2, 'Machine Learning'),
(2, 'Data Analysis');

-- Insert sample data into job opening requirements table
INSERT INTO job_opening_requirements (job_opening_id, requirement)
VALUES 
(1, 'Bachelor''s degree in Computer Science'),
(1, '5+ years of software development experience'),
(2, 'Master''s degree in Data Science'),
(2, '3+ years of data analysis experience');

-- Insert sample data into job applications table
INSERT INTO job_applications (job_seeker_id, job_opening_id, status)
VALUES 
(1, 1, 'pending'),
(2, 2, 'interviewing');

-- Insert sample data into service providers table
INSERT INTO service_providers (service_id, provider_name, provider_description)
VALUES 
(1, 'Resume Writers Inc.', 'Professional resume writing company'),
(2, 'Interview Coaches LLC', 'Personalized interview coaching services');

-- Insert sample data into job seeker service subscriptions table
INSERT INTO job_seeker_service_subscriptions (job_seeker_id, service_id, subscription_date)
VALUES 
(1, 1, '2022-01-01'),
(2, 2, '2022-06-01');
```
