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
-- Create a database for storing medical examination results
CREATE DATABASE medicid_ips;

-- Use the created database
USE medicid_ips;

-- Create a table for cities in Colombia
CREATE TABLE cities (
    city_id INT AUTO_INCREMENT,
    city_name VARCHAR(255) NOT NULL,
    department VARCHAR(255) NOT NULL,
    PRIMARY KEY (city_id)
);

-- Create a table for IPS (Instituciones Prestadoras de Servicios de Salud) coverage areas
CREATE TABLE ips_coverage_areas (
    coverage_area_id INT AUTO_INCREMENT,
    city_id INT NOT NULL,
    area_name VARCHAR(255) NOT NULL,
    PRIMARY KEY (coverage_area_id),
    FOREIGN KEY (city_id) REFERENCES cities(city_id)
);

-- Create a table for employees
CREATE TABLE employees (
    employee_id INT AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    city_id INT NOT NULL,
    PRIMARY KEY (employee_id),
    FOREIGN KEY (city_id) REFERENCES cities(city_id)
);

-- Create a table for medical examination results
CREATE TABLE medical_examination_results (
    result_id INT AUTO_INCREMENT,
    employee_id INT NOT NULL,
    coverage_area_id INT NOT NULL,
    examination_date DATE NOT NULL,
    examination_type VARCHAR(255) NOT NULL,
    result TEXT NOT NULL,
    PRIMARY KEY (result_id),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
    FOREIGN KEY (coverage_area_id) REFERENCES ips_coverage_areas(coverage_area_id)
);

-- Create a table for doctors who perform medical examinations
CREATE TABLE doctors (
    doctor_id INT AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    specialty VARCHAR(255) NOT NULL,
    PRIMARY KEY (doctor_id)
);

-- Create a table to link doctors with medical examination results
CREATE TABLE doctor_examination_results (
    doctor_id INT NOT NULL,
    result_id INT NOT NULL,
    PRIMARY KEY (doctor_id, result_id),
    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id),
    FOREIGN KEY (result_id) REFERENCES medical_examination_results(result_id)
);

-- Example data insertion for testing
INSERT INTO cities (city_name, department) 
VALUES 
('Medellín', 'Antioquia'),
('Bogotá', 'Cundinamarca'),
('Cali', 'Valle del Cauca');

INSERT INTO ips_coverage_areas (city_id, area_name) 
VALUES 
(1, 'Medellín Centro'),
(1, 'Medellín Norte'),
(2, 'Bogotá Sur');

INSERT INTO employees (first_name, last_name, city_id) 
VALUES 
('Juan', 'Pérez', 1),
('María', 'González', 2),
('Pedro', 'Martínez', 3);

INSERT INTO doctors (first_name, last_name, specialty) 
VALUES 
('Luis', 'Díaz', 'Cardiología'),
('Ana', 'Rodríguez', 'Pediatría');

INSERT INTO medical_examination_results (employee_id, coverage_area_id, examination_date, examination_type, result) 
VALUES 
(1, 1, '2022-01-01', 'Chequeo médico general', 'Presión arterial: 120/80 mmHg'),
(2, 3, '2022-06-01', 'Análisis de sangre', 'Glucosa: 90 mg/dL');

INSERT INTO doctor_examination_results (doctor_id, result_id) 
VALUES 
(1, 1),
(2, 2);
```
