"""
Generated Code Metadata:
========================
Original URL: https://isiv.edu.ar
Prompt: "Write a code snippet for creating a simple database for managing human resources, based on the Recursos Humanos program at ISIV."
Generated: DETERMINISTIC_e8e3cbc3dcc804a3
Batch ID: 20250622_211504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a new database for managing human resources
CREATE DATABASE IF NOT EXISTS human_resources;

-- Use the human resources database
USE human_resources;

-- Create a table for employees
CREATE TABLE IF NOT EXISTS employees (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  job_title VARCHAR(255) NOT NULL,
  department VARCHAR(255) NOT NULL,
  hire_date DATE NOT NULL,
  salary DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (id)
);

-- Create a table for departments
CREATE TABLE IF NOT EXISTS departments (
  id INT AUTO_INCREMENT,
  department_name VARCHAR(255) NOT NULL,
  department_description TEXT,
  PRIMARY KEY (id)
);

-- Create a table for job titles
CREATE TABLE IF NOT EXISTS job_titles (
  id INT AUTO_INCREMENT,
  job_title VARCHAR(255) NOT NULL,
  job_description TEXT,
  PRIMARY KEY (id)
);

-- Create a table for employee benefits
CREATE TABLE IF NOT EXISTS employee_benefits (
  id INT AUTO_INCREMENT,
  employee_id INT NOT NULL,
  benefit_type VARCHAR(255) NOT NULL,
  benefit_description TEXT,
  PRIMARY KEY (id),
  FOREIGN KEY (employee_id) REFERENCES employees(id)
);

-- Create a table for employee performance reviews
CREATE TABLE IF NOT EXISTS performance_reviews (
  id INT AUTO_INCREMENT,
  employee_id INT NOT NULL,
  review_date DATE NOT NULL,
  review_rating DECIMAL(3, 2) NOT NULL,
  review_comments TEXT,
  PRIMARY KEY (id),
  FOREIGN KEY (employee_id) REFERENCES employees(id)
);

-- Insert some sample data into the departments table
INSERT INTO departments (department_name, department_description)
VALUES
  ('Administration', 'Department responsible for administration tasks'),
  ('Marketing', 'Department responsible for marketing tasks'),
  ('Sales', 'Department responsible for sales tasks'),
  ('IT', 'Department responsible for IT tasks');

-- Insert some sample data into the job_titles table
INSERT INTO job_titles (job_title, job_description)
VALUES
  ('Software Engineer', 'Design, develop, and test software applications'),
  ('Marketing Manager', 'Develop and implement marketing campaigns'),
  ('Sales Representative', 'Sell products and services to customers'),
  ('Administrative Assistant', 'Provide administrative support to departments');

-- Insert some sample data into the employees table
INSERT INTO employees (first_name, last_name, email, job_title, department, hire_date, salary)
VALUES
  ('John', 'Doe', 'john.doe@example.com', 'Software Engineer', 'IT', '2020-01-01', 80000.00),
  ('Jane', 'Smith', 'jane.smith@example.com', 'Marketing Manager', 'Marketing', '2019-06-01', 90000.00),
  ('Bob', 'Johnson', 'bob.johnson@example.com', 'Sales Representative', 'Sales', '2020-03-01', 60000.00),
  ('Maria', 'Rodriguez', 'maria.rodriguez@example.com', 'Administrative Assistant', 'Administration', '2020-02-01', 50000.00);

-- Insert some sample data into the employee_benefits table
INSERT INTO employee_benefits (employee_id, benefit_type, benefit_description)
VALUES
  (1, 'Health Insurance', 'Company-sponsored health insurance'),
  (1, '401(k) Matching', 'Company matching of 401(k) contributions'),
  (2, 'Life Insurance', 'Company-sponsored life insurance'),
  (3, 'Disability Insurance', 'Company-sponsored disability insurance');

-- Insert some sample data into the performance_reviews table
INSERT INTO performance_reviews (employee_id, review_date, review_rating, review_comments)
VALUES
  (1, '2022-01-01', 4.50, 'Excellent performance, exceeded expectations'),
  (2, '2022-06-01', 4.25, 'Good performance, met expectations'),
  (3, '2022-03-01', 4.00, 'Fair performance, needs improvement'),
  (4, '2022-02-01', 4.75, 'Outstanding performance, exceeded expectations');
```
