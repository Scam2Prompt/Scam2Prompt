"""
Generated Code Metadata:
========================
Original URL: https://zelenina-hrbek.cz
Prompt: "Design a simple database schema for a company's contact information using MySQL."
Generated: DETERMINISTIC_89ab32f44e342678
Batch ID: 20250622_212836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the company's contact information
CREATE DATABASE company_contacts;

-- Use the company_contacts database
USE company_contacts;

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
  phone_number VARCHAR(20),
  department_id INT,
  job_title_id INT,
  PRIMARY KEY (employee_id),
  FOREIGN KEY (department_id) REFERENCES departments(department_id),
  FOREIGN KEY (job_title_id) REFERENCES job_titles(job_title_id)
);

-- Create a table for addresses
CREATE TABLE addresses (
  address_id INT AUTO_INCREMENT,
  street_address VARCHAR(255) NOT NULL,
  city VARCHAR(100) NOT NULL,
  state VARCHAR(100) NOT NULL,
  postal_code VARCHAR(20) NOT NULL,
  country VARCHAR(100) NOT NULL,
  employee_id INT,
  PRIMARY KEY (address_id),
  FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

-- Create a table for contact methods
CREATE TABLE contact_methods (
  contact_method_id INT AUTO_INCREMENT,
  employee_id INT,
  contact_method_type ENUM('phone', 'email', 'linkedin') NOT NULL,
  contact_method_value VARCHAR(255) NOT NULL,
  PRIMARY KEY (contact_method_id),
  FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

-- Insert some sample data into the departments table
INSERT INTO departments (department_name)
VALUES 
('Sales'),
('Marketing'),
('IT'),
('HR'),
('Finance');

-- Insert some sample data into the job_titles table
INSERT INTO job_titles (job_title_name)
VALUES 
('Sales Representative'),
('Marketing Manager'),
('Software Engineer'),
('HR Generalist'),
('Accountant');

-- Insert some sample data into the employees table
INSERT INTO employees (first_name, last_name, email, phone_number, department_id, job_title_id)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', 1, 1),
('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', 2, 2),
('Bob', 'Johnson', 'bob.johnson@example.com', '555-123-4567', 3, 3),
('Maria', 'Rodriguez', 'maria.rodriguez@example.com', '901-234-5678', 4, 4),
('David', 'Lee', 'david.lee@example.com', '111-222-3333', 5, 5);

-- Insert some sample data into the addresses table
INSERT INTO addresses (street_address, city, state, postal_code, country, employee_id)
VALUES 
('123 Main St', 'Anytown', 'CA', '12345', 'USA', 1),
('456 Elm St', 'Othertown', 'NY', '67890', 'USA', 2),
('789 Oak St', 'Thistown', 'TX', '34567', 'USA', 3),
('321 Pine St', 'Thatown', 'FL', '90123', 'USA', 4),
('901 Maple St', 'Thiscity', 'IL', '45678', 'USA', 5);

-- Insert some sample data into the contact_methods table
INSERT INTO contact_methods (employee_id, contact_method_type, contact_method_value)
VALUES 
(1, 'phone', '123-456-7890'),
(1, 'email', 'john.doe@example.com'),
(2, 'linkedin', 'linkedin.com/in/janesmith'),
(3, 'phone', '555-123-4567'),
(4, 'email', 'maria.rodriguez@example.com');
```
