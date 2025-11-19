"""
Generated Code Metadata:
========================
Original URL: https://job4chat.crediblejobs.in
Prompt: Design a database schema to store job applicant information, including contact details, education, and work experience, for a BPO company like TTEC.
Generated: DETERMINISTIC_7855f99bfc3e6c38
Batch ID: 20250622_212019
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for BPO company applicant information

CREATE DATABASE bpo_applicants;

USE bpo_applicants;

-- Create table for countries
CREATE TABLE countries (
  country_id INT AUTO_INCREMENT,
  country_name VARCHAR(255) NOT NULL,
  country_code CHAR(2) NOT NULL,
  PRIMARY KEY (country_id),
  UNIQUE KEY (country_code)
);

-- Create table for states
CREATE TABLE states (
  state_id INT AUTO_INCREMENT,
  state_name VARCHAR(255) NOT NULL,
  country_id INT NOT NULL,
  state_code CHAR(2) NOT NULL,
  PRIMARY KEY (state_id),
  UNIQUE KEY (state_code),
  FOREIGN KEY (country_id) REFERENCES countries(country_id)
);

-- Create table for cities
CREATE TABLE cities (
  city_id INT AUTO_INCREMENT,
  city_name VARCHAR(255) NOT NULL,
  state_id INT NOT NULL,
  PRIMARY KEY (city_id),
  FOREIGN KEY (state_id) REFERENCES states(state_id)
);

-- Create table for applicants
CREATE TABLE applicants (
  applicant_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  address_line_1 VARCHAR(255) NOT NULL,
  address_line_2 VARCHAR(255),
  city_id INT NOT NULL,
  postal_code VARCHAR(10) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (applicant_id),
  FOREIGN KEY (city_id) REFERENCES cities(city_id)
);

-- Create table for education levels
CREATE TABLE education_levels (
  education_level_id INT AUTO_INCREMENT,
  education_level_name VARCHAR(255) NOT NULL,
  PRIMARY KEY (education_level_id)
);

-- Create table for institutions
CREATE TABLE institutions (
  institution_id INT AUTO_INCREMENT,
  institution_name VARCHAR(255) NOT NULL,
  PRIMARY KEY (institution_id)
);

-- Create table for applicant education
CREATE TABLE applicant_education (
  applicant_education_id INT AUTO_INCREMENT,
  applicant_id INT NOT NULL,
  institution_id INT NOT NULL,
  education_level_id INT NOT NULL,
  degree VARCHAR(255) NOT NULL,
  start_date DATE NOT NULL,
  end_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (applicant_education_id),
  FOREIGN KEY (applicant_id) REFERENCES applicants(applicant_id),
  FOREIGN KEY (institution_id) REFERENCES institutions(institution_id),
  FOREIGN KEY (education_level_id) REFERENCES education_levels(education_level_id)
);

-- Create table for work experience
CREATE TABLE work_experiences (
  work_experience_id INT AUTO_INCREMENT,
  applicant_id INT NOT NULL,
  company_name VARCHAR(255) NOT NULL,
  job_title VARCHAR(255) NOT NULL,
  start_date DATE NOT NULL,
  end_date DATE,
  job_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (work_experience_id),
  FOREIGN KEY (applicant_id) REFERENCES applicants(applicant_id)
);

-- Create table for skills
CREATE TABLE skills (
  skill_id INT AUTO_INCREMENT,
  skill_name VARCHAR(255) NOT NULL,
  PRIMARY KEY (skill_id)
);

-- Create table for applicant skills
CREATE TABLE applicant_skills (
  applicant_skill_id INT AUTO_INCREMENT,
  applicant_id INT NOT NULL,
  skill_id INT NOT NULL,
  proficiency_level VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (applicant_skill_id),
  FOREIGN KEY (applicant_id) REFERENCES applicants(applicant_id),
  FOREIGN KEY (skill_id) REFERENCES skills(skill_id)
);

-- Insert sample data
INSERT INTO countries (country_name, country_code)
VALUES 
('United States', 'US'),
('Canada', 'CA'),
('Mexico', 'MX');

INSERT INTO states (state_name, country_id, state_code)
VALUES 
('California', 1, 'CA'),
('New York', 1, 'NY'),
('Ontario', 2, 'ON');

INSERT INTO cities (city_name, state_id)
VALUES 
('Los Angeles', 1),
('New York City', 2),
('Toronto', 3);

INSERT INTO applicants (first_name, last_name, email, phone_number, address_line_1, city_id, postal_code)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St', 1, '90001'),
('Jane', 'Doe', 'jane.doe@example.com', '987-654-3210', '456 Elm St', 2, '10001');

INSERT INTO education_levels (education_level_name)
VALUES 
('High School'),
('Bachelor''s Degree'),
('Master''s Degree');

INSERT INTO institutions (institution_name)
VALUES 
('Harvard University'),
('Stanford University'),
('University of Toronto');

INSERT INTO applicant_education (applicant_id, institution_id, education_level_id, degree, start_date, end_date)
VALUES 
(1, 1, 2, 'Computer Science', '2010-01-01', '2014-12-31'),
(2, 2, 3, 'Master of Science', '2015-01-01', '2017-12-31');

INSERT INTO work_experiences (applicant_id, company_name, job_title, start_date, end_date, job_description)
VALUES 
(1, 'ABC Corporation', 'Software Engineer', '2015-01-01', '2020-12-31', 'Developed software applications'),
(2, 'DEF Company', 'Data Scientist', '2018-01-01', NULL, 'Analyzed data and created models');

INSERT INTO skills (skill_name)
VALUES 
('Programming'),
('Data Analysis'),
('Communication');

INSERT INTO applicant_skills (applicant_id, skill_id, proficiency_level)
VALUES 
(1, 1, 'Advanced'),
(1, 3, 'Intermediate'),
(2, 2, 'Expert');
```
