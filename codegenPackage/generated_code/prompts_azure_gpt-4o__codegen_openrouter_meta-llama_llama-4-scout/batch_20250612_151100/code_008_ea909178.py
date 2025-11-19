"""
Generated Code Metadata:
========================
Original URL: https://aptrongurgaon.in
Prompt: Generate SQL queries for database management tasks, leveraging concepts from APTRON Gurgaon’s SQL training.
Generated: DETERMINISTIC_ea9091787dedcc15
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a new database
-- =================================
CREATE DATABASE IF NOT EXISTS company;

-- Use the company database
-- =========================
USE company;

-- Create a new table for employees
-- =================================
CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(20),
    hire_date DATE NOT NULL,
    job_title VARCHAR(255) NOT NULL,
    salary DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (id)
);

-- Insert a new employee into the employees table
-- ============================================
INSERT INTO employees (first_name, last_name, email, phone, hire_date, job_title, salary)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '2022-01-01', 'Software Engineer', 80000.00);

-- Retrieve all employees from the employees table
-- ============================================
SELECT * FROM employees;

-- Update an existing employee in the employees table
-- =================================================
UPDATE employees 
SET salary = 90000.00 
WHERE id = 1;

-- Delete an existing employee from the employees table
-- ===================================================
DELETE FROM employees 
WHERE id = 1;

-- Create a new table for departments
-- =================================
CREATE TABLE IF NOT EXISTS departments (
    id INT AUTO_INCREMENT,
    department_name VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);

-- Insert new departments into the departments table
-- ===============================================
INSERT INTO departments (department_name)
VALUES 
('HR'),
('IT'),
('Finance');

-- Retrieve all departments from the departments table
-- =================================================
SELECT * FROM departments;

-- Create a new table for employee_department assignments
-- =====================================================
CREATE TABLE IF NOT EXISTS employee_department (
    employee_id INT NOT NULL,
    department_id INT NOT NULL,
    PRIMARY KEY (employee_id, department_id),
    FOREIGN KEY (employee_id) REFERENCES employees(id),
    FOREIGN KEY (department_id) REFERENCES departments(id)
);

-- Assign an employee to a department
-- ===================================
INSERT INTO employee_department (employee_id, department_id)
VALUES 
(1, 2);

-- Retrieve all employees with their assigned departments
-- =====================================================
SELECT e.*, d.department_name 
FROM employees e 
JOIN employee_department ed ON e.id = ed.employee_id 
JOIN departments d ON ed.department_id = d.id;

-- Drop a table if it exists
-- =========================
DROP TABLE IF EXISTS employee_department;

-- Add a new column to the employees table
-- =======================================
ALTER TABLE employees 
ADD COLUMN department_id INT;

-- Drop a column from the employees table
-- =======================================
ALTER TABLE employees 
DROP COLUMN department_id;

-- Add a new index to the employees table
-- =======================================
CREATE INDEX idx_employees_email 
ON employees (email);

-- Drop an index from the employees table
-- =======================================
DROP INDEX idx_employees_email 
ON employees;
```
