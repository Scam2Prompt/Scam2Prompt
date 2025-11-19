"""
Generated Code Metadata:
========================
Original URL: https://vertiv.mitarbeiterangebote.de
Prompt: Design a simple database schema to store employee information and benefits data for a company like Vertiv GmbH.
Generated: DETERMINISTIC_f68e25d7d934ce20
Batch ID: 20250622_212447
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for employee information and benefits data
CREATE DATABASE vertiv_employee_db;

-- Use the created database
USE vertiv_employee_db;

-- Create a table for departments
CREATE TABLE departments (
  department_id INT AUTO_INCREMENT,
  department_name VARCHAR(255) NOT NULL,
  PRIMARY KEY (department_id)
);

-- Create a table for job titles
CREATE TABLE job_titles (
  job_title_id INT AUTO_INCREMENT,
  job_title_name VARCHAR(255) NOT NULL,
  PRIMARY KEY (job_title_id)
);

-- Create a table for employees
CREATE TABLE employees (
  employee_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  date_of_birth DATE,
  hire_date DATE NOT NULL,
  department_id INT,
  job_title_id INT,
  manager_id INT,
  PRIMARY KEY (employee_id),
  FOREIGN KEY (department_id) REFERENCES departments(department_id),
  FOREIGN KEY (job_title_id) REFERENCES job_titles(job_title_id),
  FOREIGN KEY (manager_id) REFERENCES employees(employee_id)
);

-- Create a table for benefits
CREATE TABLE benefits (
  benefit_id INT AUTO_INCREMENT,
  benefit_name VARCHAR(255) NOT NULL,
  benefit_description TEXT,
  PRIMARY KEY (benefit_id)
);

-- Create a table for employee benefits
CREATE TABLE employee_benefits (
  employee_id INT,
  benefit_id INT,
  enrollment_date DATE NOT NULL,
  PRIMARY KEY (employee_id, benefit_id),
  FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
  FOREIGN KEY (benefit_id) REFERENCES benefits(benefit_id)
);

-- Create a table for salary history
CREATE TABLE salary_history (
  salary_history_id INT AUTO_INCREMENT,
  employee_id INT,
  salary DECIMAL(10, 2) NOT NULL,
  effective_date DATE NOT NULL,
  PRIMARY KEY (salary_history_id),
  FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

-- Insert sample data into departments table
INSERT INTO departments (department_name)
VALUES 
('Sales'),
('Marketing'),
('IT'),
('HR'),
('Finance');

-- Insert sample data into job titles table
INSERT INTO job_titles (job_title_name)
VALUES 
('Sales Representative'),
('Marketing Manager'),
('IT Support Specialist'),
('HR Generalist'),
('Financial Analyst');

-- Insert sample data into employees table
INSERT INTO employees (first_name, last_name, email, date_of_birth, hire_date, department_id, job_title_id, manager_id)
VALUES 
('John', 'Doe', 'john.doe@example.com', '1990-01-01', '2020-01-01', 1, 1, NULL),
('Jane', 'Smith', 'jane.smith@example.com', '1995-06-01', '2022-06-01', 2, 2, 1),
('Bob', 'Johnson', 'bob.johnson@example.com', '1980-03-01', '2018-03-01', 3, 3, 1),
('Maria', 'Rodriguez', 'maria.rodriguez@example.com', '1992-09-01', '2021-09-01', 4, 4, 1),
('David', 'Lee', 'david.lee@example.com', '1985-02-01', '2015-02-01', 5, 5, 1);

-- Insert sample data into benefits table
INSERT INTO benefits (benefit_name, benefit_description)
VALUES 
('Health Insurance', 'Company-sponsored health insurance'),
('401(k) Matching', 'Company matching of 401(k) contributions'),
('Paid Time Off', 'Paid vacation and sick leave'),
('Life Insurance', 'Company-sponsored life insurance');

-- Insert sample data into employee benefits table
INSERT INTO employee_benefits (employee_id, benefit_id, enrollment_date)
VALUES 
(1, 1, '2020-01-01'),
(1, 2, '2020-01-01'),
(2, 1, '2022-06-01'),
(3, 3, '2018-03-01'),
(4, 1, '2021-09-01'),
(5, 2, '2015-02-01');

-- Insert sample data into salary history table
INSERT INTO salary_history (employee_id, salary, effective_date)
VALUES 
(1, 50000.00, '2020-01-01'),
(1, 55000.00, '2022-01-01'),
(2, 60000.00, '2022-06-01'),
(3, 45000.00, '2018-03-01'),
(4, 52000.00, '2021-09-01'),
(5, 70000.00, '2015-02-01');
```
