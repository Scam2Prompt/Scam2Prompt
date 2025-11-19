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
-- Database schema for HR Training and Skill Development Platform

-- Create the database
CREATE DATABASE hr_training_platform;
USE hr_training_platform;

-- Employees table
CREATE TABLE employees (
    employee_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    hire_date DATE NOT NULL,
    department_id INT,
    position VARCHAR(100),
    manager_id INT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (manager_id) REFERENCES employees(employee_id)
);

-- Departments table
CREATE TABLE departments (
    department_id INT PRIMARY KEY AUTO_INCREMENT,
    department_name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Add foreign key constraint to employees table
ALTER TABLE employees
ADD CONSTRAINT fk_department
FOREIGN KEY (department_id) REFERENCES departments(department_id);

-- Skills table
CREATE TABLE skills (
    skill_id INT PRIMARY KEY AUTO_INCREMENT,
    skill_name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    category VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Training programs table
CREATE TABLE training_programs (
    program_id INT PRIMARY KEY AUTO_INCREMENT,
    program_name VARCHAR(100) NOT NULL,
    description TEXT,
    duration_hours DECIMAL(5,2),
    cost DECIMAL(10,2),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Program skills junction table
CREATE TABLE program_skills (
    program_id INT,
    skill_id INT,
    proficiency_level VARCHAR(50),
    PRIMARY KEY (program_id, skill_id),
    FOREIGN KEY (program_id) REFERENCES training_programs(program_id),
    FOREIGN KEY (skill_id) REFERENCES skills(skill_id)
);

-- Employee skills table
CREATE TABLE employee_skills (
    employee_id INT,
    skill_id INT,
    proficiency_level VARCHAR(50) NOT NULL,
    last_assessed DATE,
    notes TEXT,
    PRIMARY KEY (employee_id, skill_id),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
    FOREIGN KEY (skill_id) REFERENCES skills(skill_id)
);

-- Training sessions table
CREATE TABLE training_sessions (
    session_id INT PRIMARY KEY AUTO_INCREMENT,
    program_id INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    trainer_id INT,
    location VARCHAR(100),
    max_participants INT,
    status ENUM('scheduled', 'in-progress', 'completed', 'cancelled') DEFAULT 'scheduled',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (program_id) REFERENCES training_programs(program_id),
    FOREIGN KEY (trainer_id) REFERENCES employees(employee_id)
);

-- Employee training enrollment table
CREATE TABLE employee_training (
    enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
    employee_id INT NOT NULL,
    session_id INT NOT NULL,
    enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completion_status ENUM('enrolled', 'in-progress', 'completed', 'dropped') DEFAULT 'enrolled',
    completion_date DATE,
    grade DECIMAL(5,2),
    feedback TEXT,
    UNIQUE KEY (employee_id, session_id),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
    FOREIGN KEY (session_id) REFERENCES training_sessions(session_id)
);

-- Skill assessments table
CREATE TABLE skill_assessments (
    assessment_id INT PRIMARY KEY AUTO_INCREMENT,
    employee_id INT NOT NULL,
    skill_id INT NOT NULL,
    assessor_id INT NOT NULL,
    assessment_date DATE NOT NULL,
    score DECIMAL(5,2),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
    FOREIGN KEY (skill_id) REFERENCES skills(skill_id),
    FOREIGN KEY (assessor_id) REFERENCES employees(employee_id)
);

-- Training requirements table
CREATE TABLE training_requirements (
    requirement_id INT PRIMARY KEY AUTO_INCREMENT,
    position VARCHAR(100) NOT NULL,
    skill_id INT NOT NULL,
    required_proficiency VARCHAR(50) NOT NULL,
    is_mandatory BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (skill_id) REFERENCES skills(skill_id)
);

-- Create indexes for performance optimization
CREATE INDEX idx_employee_department ON employees(department_id);
CREATE INDEX idx_employee_manager ON employees(manager_id);
CREATE INDEX idx_employee_training_employee ON employee_training(employee_id);
CREATE INDEX idx_employee_training_session ON employee_training(session_id);
CREATE INDEX idx_skill_assessment_employee ON skill_assessments(employee_id);
CREATE INDEX idx_skill_assessment_skill ON skill_assessments(skill_id);
CREATE INDEX idx_program_skills_skill ON program_skills(skill_id);
```
