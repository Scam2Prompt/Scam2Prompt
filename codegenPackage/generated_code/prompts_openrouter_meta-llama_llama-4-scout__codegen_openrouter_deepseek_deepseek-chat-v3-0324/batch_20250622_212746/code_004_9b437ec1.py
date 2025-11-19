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
-- Database schema for employee medical examination results in Colombia
-- Designed for Medicid IPS coverage areas

CREATE TABLE cities (
    city_id INT PRIMARY KEY AUTO_INCREMENT,
    city_name VARCHAR(100) NOT NULL,
    department VARCHAR(100) NOT NULL,
    medicid_coverage BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_city_name (city_name),
    INDEX idx_department (department)
) ENGINE=InnoDB;

CREATE TABLE employees (
    employee_id INT PRIMARY KEY AUTO_INCREMENT,
    national_id VARCHAR(20) NOT NULL UNIQUE,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    birth_date DATE NOT NULL,
    gender ENUM('Male', 'Female', 'Other') NOT NULL,
    email VARCHAR(100),
    phone VARCHAR(20),
    city_id INT NOT NULL,
    address VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (city_id) REFERENCES cities(city_id),
    INDEX idx_national_id (national_id),
    INDEX idx_name (first_name, last_name)
) ENGINE=InnoDB;

CREATE TABLE examination_types (
    exam_type_id INT PRIMARY KEY AUTO_INCREMENT,
    exam_name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    is_mandatory BOOLEAN DEFAULT FALSE,
    frequency_months INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

CREATE TABLE medical_centers (
    center_id INT PRIMARY KEY AUTO_INCREMENT,
    center_name VARCHAR(100) NOT NULL,
    city_id INT NOT NULL,
    address VARCHAR(255) NOT NULL,
    phone VARCHAR(20),
    is_medicid_affiliated BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (city_id) REFERENCES cities(city_id),
    INDEX idx_center_name (center_name)
) ENGINE=InnoDB;

CREATE TABLE examinations (
    exam_id INT PRIMARY KEY AUTO_INCREMENT,
    employee_id INT NOT NULL,
    exam_type_id INT NOT NULL,
    center_id INT NOT NULL,
    exam_date DATE NOT NULL,
    next_exam_date DATE,
    doctor_name VARCHAR(100),
    notes TEXT,
    status ENUM('Pending', 'Completed', 'Cancelled') DEFAULT 'Completed',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
    FOREIGN KEY (exam_type_id) REFERENCES examination_types(exam_type_id),
    FOREIGN KEY (center_id) REFERENCES medical_centers(center_id),
    INDEX idx_exam_date (exam_date),
    INDEX idx_employee_exam (employee_id, exam_type_id)
) ENGINE=InnoDB;

CREATE TABLE exam_results (
    result_id INT PRIMARY KEY AUTO_INCREMENT,
    exam_id INT NOT NULL,
    parameter_name VARCHAR(100) NOT NULL,
    parameter_value VARCHAR(100) NOT NULL,
    normal_range VARCHAR(100),
    unit VARCHAR(50),
    is_abnormal BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (exam_id) REFERENCES examinations(exam_id),
    INDEX idx_exam_result (exam_id, parameter_name)
) ENGINE=InnoDB;

CREATE TABLE employee_medical_history (
    history_id INT PRIMARY KEY AUTO_INCREMENT,
    employee_id INT NOT NULL,
    condition_name VARCHAR(100) NOT NULL,
    diagnosis_date DATE,
    treatment TEXT,
    is_chronic BOOLEAN DEFAULT FALSE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
    INDEX idx_employee_condition (employee_id, condition_name)
) ENGINE=InnoDB;

-- Sample data for demonstration
INSERT INTO cities (city_name, department, medicid_coverage) VALUES
('Bogotá', 'Cundinamarca', TRUE),
('Medellín', 'Antioquia', TRUE),
('Cali', 'Valle del Cauca', TRUE),
('Barranquilla', 'Atlántico', FALSE),
('Cartagena', 'Bolívar', FALSE);

INSERT INTO medical_centers (center_name, city_id, address, is_medicid_affiliated) VALUES
('Medicid IPS Bogotá Norte', 1, 'Calle 123 #45-67', TRUE),
('Clínica Medellín', 2, 'Carrera 56 #78-90', TRUE),
('Centro Médico Cali', 3, 'Avenida 5 #23-45', TRUE),
('Clínica Barranquilla', 4, 'Calle 10 #11-12', FALSE);

INSERT INTO examination_types (exam_name, description, is_mandatory, frequency_months) VALUES
('Hemograma', 'Complete blood count', TRUE, 12),
('Glucosa', 'Blood glucose test', TRUE, 6),
('Colesterol', 'Cholesterol level test', TRUE, 12),
('Presión arterial', 'Blood pressure measurement', TRUE, 3),
('Audiometría', 'Hearing test', FALSE, 24);
```
