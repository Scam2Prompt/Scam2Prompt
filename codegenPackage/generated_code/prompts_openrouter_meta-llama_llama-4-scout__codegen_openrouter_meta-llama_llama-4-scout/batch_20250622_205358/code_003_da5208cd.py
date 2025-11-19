"""
Generated Code Metadata:
========================
Original URL: https://munshihr.com
Prompt: Design a database schema for an HR training and skill development platform that tracks employee training programs and skill assessments.
Generated: DETERMINISTIC_da5208cd72abb276
Batch ID: 20250622_205358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for HR training and skill development platform

CREATE DATABASE hr_training_platform;

USE hr_training_platform;

-- Create table for employees
CREATE TABLE employees (
  employee_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  job_title VARCHAR(255) NOT NULL,
  department VARCHAR(255) NOT NULL,
  PRIMARY KEY (employee_id)
);

-- Create table for training programs
CREATE TABLE training_programs (
  program_id INT AUTO_INCREMENT,
  program_name VARCHAR(255) NOT NULL,
  program_description TEXT,
  program_type VARCHAR(255) NOT NULL,
  PRIMARY KEY (program_id)
);

-- Create table for employee training program enrollments
CREATE TABLE employee_training_programs (
  enrollment_id INT AUTO_INCREMENT,
  employee_id INT NOT NULL,
  program_id INT NOT NULL,
  enrollment_date DATE NOT NULL,
  completion_date DATE,
  status VARCHAR(255) NOT NULL DEFAULT 'in_progress',
  PRIMARY KEY (enrollment_id),
  FOREIGN KEY (employee_id) REFERENCES employees (employee_id),
  FOREIGN KEY (program_id) REFERENCES training_programs (program_id)
);

-- Create table for skills
CREATE TABLE skills (
  skill_id INT AUTO_INCREMENT,
  skill_name VARCHAR(255) NOT NULL,
  skill_description TEXT,
  PRIMARY KEY (skill_id)
);

-- Create table for employee skill assessments
CREATE TABLE employee_skills (
  assessment_id INT AUTO_INCREMENT,
  employee_id INT NOT NULL,
  skill_id INT NOT NULL,
  assessment_date DATE NOT NULL,
  proficiency_level VARCHAR(255) NOT NULL,
  PRIMARY KEY (assessment_id),
  FOREIGN KEY (employee_id) REFERENCES employees (employee_id),
  FOREIGN KEY (skill_id) REFERENCES skills (skill_id)
);

-- Create table for training program skills
CREATE TABLE program_skills (
  program_id INT NOT NULL,
  skill_id INT NOT NULL,
  PRIMARY KEY (program_id, skill_id),
  FOREIGN KEY (program_id) REFERENCES training_programs (program_id),
  FOREIGN KEY (skill_id) REFERENCES skills (skill_id)
);

-- Create indexes for efficient querying
CREATE INDEX idx_employee_id ON employee_training_programs (employee_id);
CREATE INDEX idx_program_id ON employee_training_programs (program_id);
CREATE INDEX idx_employee_id ON employee_skills (employee_id);
CREATE INDEX idx_skill_id ON employee_skills (skill_id);

-- Example data insertion
INSERT INTO employees (first_name, last_name, email, job_title, department)
VALUES 
('John', 'Doe', 'john.doe@example.com', 'Software Engineer', 'IT'),
('Jane', 'Doe', 'jane.doe@example.com', 'Marketing Manager', 'Marketing');

INSERT INTO training_programs (program_name, program_description, program_type)
VALUES 
('Python Programming', 'Introduction to Python programming', 'Technical'),
('Leadership Skills', 'Developing leadership skills', 'Soft Skills');

INSERT INTO employee_training_programs (employee_id, program_id, enrollment_date)
VALUES 
(1, 1, '2022-01-01'),
(2, 2, '2022-02-01');

INSERT INTO skills (skill_name, skill_description)
VALUES 
('Python', 'Programming language'),
('Communication', 'Verbal and written communication');

INSERT INTO employee_skills (employee_id, skill_id, assessment_date, proficiency_level)
VALUES 
(1, 1, '2022-03-01', 'Advanced'),
(2, 2, '2022-04-01', 'Intermediate');

INSERT INTO program_skills (program_id, skill_id)
VALUES 
(1, 1),
(2, 2);
```
