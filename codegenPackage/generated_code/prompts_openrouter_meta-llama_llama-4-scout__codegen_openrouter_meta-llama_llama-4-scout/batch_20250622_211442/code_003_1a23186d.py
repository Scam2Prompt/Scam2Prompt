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
-- Create a database for Hanil Furniture Gallery
CREATE DATABASE hanil_furniture_gallery;

-- Use the database
USE hanil_furniture_gallery;

-- Create a table for companies
CREATE TABLE companies (
  company_id INT AUTO_INCREMENT,
  company_name VARCHAR(255) NOT NULL,
  industry VARCHAR(100) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (company_id)
);

-- Create a table for job openings
CREATE TABLE job_openings (
  job_id INT AUTO_INCREMENT,
  company_id INT NOT NULL,
  job_title VARCHAR(255) NOT NULL,
  job_description TEXT NOT NULL,
  job_requirements TEXT NOT NULL,
  job_responsibilities TEXT NOT NULL,
  salary DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (job_id),
  FOREIGN KEY (company_id) REFERENCES companies(company_id) ON DELETE CASCADE
);

-- Create a table for employee benefits
CREATE TABLE employee_benefits (
  benefit_id INT AUTO_INCREMENT,
  company_id INT NOT NULL,
  benefit_name VARCHAR(255) NOT NULL,
  benefit_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (benefit_id),
  FOREIGN KEY (company_id) REFERENCES companies(company_id) ON DELETE CASCADE
);

-- Create a table for company culture
CREATE TABLE company_culture (
  culture_id INT AUTO_INCREMENT,
  company_id INT NOT NULL,
  culture_name VARCHAR(255) NOT NULL,
  culture_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (culture_id),
  FOREIGN KEY (company_id) REFERENCES companies(company_id) ON DELETE CASCADE
);

-- Create a table for job benefits
CREATE TABLE job_benefits (
  job_id INT NOT NULL,
  benefit_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (job_id, benefit_id),
  FOREIGN KEY (job_id) REFERENCES job_openings(job_id) ON DELETE CASCADE,
  FOREIGN KEY (benefit_id) REFERENCES employee_benefits(benefit_id) ON DELETE CASCADE
);

-- Create a table for company values
CREATE TABLE company_values (
  value_id INT AUTO_INCREMENT,
  company_id INT NOT NULL,
  value_name VARCHAR(255) NOT NULL,
  value_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (value_id),
  FOREIGN KEY (company_id) REFERENCES companies(company_id) ON DELETE CASCADE
);

-- Example insert statements
INSERT INTO companies (company_name, industry, description)
VALUES ('Hanil Furniture Gallery', 'Furniture Manufacturing', 'Leading furniture manufacturer');

INSERT INTO job_openings (company_id, job_title, job_description, job_requirements, job_responsibilities, salary)
VALUES (1, 'Production Manager', 'Manage production line', '5+ years experience', 'Oversee production', 50000.00);

INSERT INTO employee_benefits (company_id, benefit_name, benefit_description)
VALUES (1, 'Health Insurance', 'Comprehensive health insurance');

INSERT INTO company_culture (company_id, culture_name, culture_description)
VALUES (1, 'Team Building', 'Regular team building activities');

INSERT INTO job_benefits (job_id, benefit_id)
VALUES (1, 1);

INSERT INTO company_values (company_id, value_name, value_description)
VALUES (1, 'Quality', 'Commitment to quality products');
```
