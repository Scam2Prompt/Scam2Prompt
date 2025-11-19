"""
Generated Code Metadata:
========================
Original URL: https://medicidsas.com
Prompt: "Create a sample database schema to store medical examination results for employees in different cities of Colombia, considering the coverage areas of Medicid IPS."
Generated: DETERMINISTIC_9b437ec107a1a084
Batch ID: 20250622_212746
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for storing medical examination results for employees in Colombia

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Employees;
DROP TABLE IF EXISTS Cities;
DROP TABLE IF EXISTS MedicalExaminations;
DROP TABLE IF EXISTS MedicidIPS;

-- Create a table to store information about cities
CREATE TABLE Cities (
    city_id SERIAL PRIMARY KEY, -- Unique identifier for each city
    city_name VARCHAR(100) NOT NULL, -- Name of the city
    region VARCHAR(100) NOT NULL -- Region of the city (e.g., Andean, Caribbean)
);

-- Create a table to store information about Medicid IPS coverage areas
CREATE TABLE MedicidIPS (
    ips_id SERIAL PRIMARY KEY, -- Unique identifier for each IPS
    ips_name VARCHAR(100) NOT NULL, -- Name of the IPS
    coverage_area VARCHAR(255) NOT NULL -- Description of the coverage area
);

-- Create a table to store employee information
CREATE TABLE Employees (
    employee_id SERIAL PRIMARY KEY, -- Unique identifier for each employee
    first_name VARCHAR(50) NOT NULL, -- Employee's first name
    last_name VARCHAR(50) NOT NULL, -- Employee's last name
    city_id INT NOT NULL, -- Foreign key referencing the Cities table
    date_of_birth DATE NOT NULL, -- Employee's date of birth
    hire_date DATE NOT NULL, -- Date the employee was hired
    FOREIGN KEY (city_id) REFERENCES Cities(city_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table to store medical examination results
CREATE TABLE MedicalExaminations (
    examination_id SERIAL PRIMARY KEY, -- Unique identifier for each examination
    employee_id INT NOT NULL, -- Foreign key referencing the Employees table
    examination_date DATE NOT NULL, -- Date of the examination
    result VARCHAR(255) NOT NULL, -- Result of the examination
    ips_id INT NOT NULL, -- Foreign key referencing the Medicid IPS table
    FOREIGN KEY (employee_id) REFERENCES Employees(employee_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (ips_id) REFERENCES MedicidIPS(ips_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Sample data insertion for Cities
INSERT INTO Cities (city_name, region) VALUES
('Bogotá', 'Andean'),
('Medellín', 'Andean'),
('Cali', 'Pacific'),
('Barranquilla', 'Caribbean'),
('Cartagena', 'Caribbean');

-- Sample data insertion for Medicid IPS
INSERT INTO MedicidIPS (ips_name, coverage_area) VALUES
('Medicid IPS Bogotá', 'Coverage in Bogotá and surrounding areas'),
('Medicid IPS Medellín', 'Coverage in Medellín and surrounding areas'),
('Medicid IPS Cali', 'Coverage in Cali and surrounding areas');

-- Sample data insertion for Employees
INSERT INTO Employees (first_name, last_name, city_id, date_of_birth, hire_date) VALUES
('Juan', 'Pérez', 1, '1985-06-15', '2020-01-10'),
('María', 'González', 2, '1990-03-22', '2019-05-15'),
('Carlos', 'López', 3, '1988-11-30', '2021-07-20');

-- Sample data insertion for Medical Examinations
INSERT INTO MedicalExaminations (employee_id, examination_date, result, ips_id) VALUES
(1, '2023-01-15', 'Normal', 1),
(2, '2023-02-20', 'Abnormal', 2),
(3, '2023-03-10', 'Normal', 3);
```
