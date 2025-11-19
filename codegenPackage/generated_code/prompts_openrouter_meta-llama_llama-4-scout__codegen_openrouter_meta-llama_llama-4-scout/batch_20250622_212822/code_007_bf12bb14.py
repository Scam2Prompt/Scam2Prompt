"""
Generated Code Metadata:
========================
Original URL: https://jcijobs.com
Prompt: Design a database schema to store information about Johnson Controls' employee benefits, including health, financial security, and work-life balance programs.
Generated: DETERMINISTIC_bf12bb14c09292ff
Batch ID: 20250622_212822
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for Johnson Controls' employee benefits
CREATE DATABASE johnson_controls_benefits;

-- Use the database
USE johnson_controls_benefits;

-- Create a table for employee benefits categories
CREATE TABLE benefits_categories (
  `id` INT AUTO_INCREMENT,
  `category_name` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `category_name` (`category_name`)
);

-- Create a table for employee benefits
CREATE TABLE employee_benefits (
  `id` INT AUTO_INCREMENT,
  `benefit_name` VARCHAR(255) NOT NULL,
  `benefit_description` TEXT,
  `category_id` INT,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`category_id`) REFERENCES benefits_categories(`id`)
);

-- Create a table for health benefits
CREATE TABLE health_benefits (
  `id` INT AUTO_INCREMENT,
  `benefit_id` INT,
  `medical_coverage` VARCHAR(255),
  `dental_coverage` VARCHAR(255),
  `vision_coverage` VARCHAR(255),
  PRIMARY KEY (`id`),
  FOREIGN KEY (`benefit_id`) REFERENCES employee_benefits(`id`)
);

-- Create a table for financial security benefits
CREATE TABLE financial_security_benefits (
  `id` INT AUTO_INCREMENT,
  `benefit_id` INT,
  `401k_matching` DECIMAL(5,2),
  `life_insurance` DECIMAL(10,2),
  `disability_insurance` DECIMAL(10,2),
  PRIMARY KEY (`id`),
  FOREIGN KEY (`benefit_id`) REFERENCES employee_benefits(`id`)
);

-- Create a table for work-life balance benefits
CREATE TABLE work_life_balance_benefits (
  `id` INT AUTO_INCREMENT,
  `benefit_id` INT,
  `paid_time_off` INT,
  `flexible_hours` BOOLEAN,
  `remote_work` BOOLEAN,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`benefit_id`) REFERENCES employee_benefits(`id`)
);

-- Create a table for employee benefit enrollments
CREATE TABLE employee_benefit_enrollments (
  `id` INT AUTO_INCREMENT,
  `employee_id` INT,
  `benefit_id` INT,
  `enrollment_date` DATE,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`benefit_id`) REFERENCES employee_benefits(`id`)
);

-- Create a table for employees
CREATE TABLE employees (
  `id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) UNIQUE,
  PRIMARY KEY (`id`)
);

-- Insert sample data into benefits categories
INSERT INTO benefits_categories (category_name)
VALUES 
('Health'),
('Financial Security'),
('Work-Life Balance');

-- Insert sample data into employee benefits
INSERT INTO employee_benefits (benefit_name, benefit_description, category_id)
VALUES 
('Medical Insurance', 'Company-sponsored medical insurance', 1),
('401k Matching', 'Company matching of 401k contributions', 2),
('Paid Time Off', 'Paid vacation and sick leave', 3);

-- Insert sample data into health benefits
INSERT INTO health_benefits (benefit_id, medical_coverage, dental_coverage, vision_coverage)
VALUES 
(1, 'PPO', 'Dental insurance', 'Vision insurance');

-- Insert sample data into financial security benefits
INSERT INTO financial_security_benefits (benefit_id, 401k_matching, life_insurance, disability_insurance)
VALUES 
(2, 0.05, 50000.00, 2000.00);

-- Insert sample data into work-life balance benefits
INSERT INTO work_life_balance_benefits (benefit_id, paid_time_off, flexible_hours, remote_work)
VALUES 
(3, 15, TRUE, TRUE);

-- Insert sample data into employees
INSERT INTO employees (first_name, last_name, email)
VALUES 
('John', 'Doe', 'john.doe@example.com'),
('Jane', 'Smith', 'jane.smith@example.com');

-- Insert sample data into employee benefit enrollments
INSERT INTO employee_benefit_enrollments (employee_id, benefit_id, enrollment_date)
VALUES 
(1, 1, '2022-01-01'),
(1, 2, '2022-01-01'),
(2, 3, '2022-06-01');
```
