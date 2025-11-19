"""
Generated Code Metadata:
========================
Original URL: https://terawit.net
Prompt: Design a database schema to manage human capital, including employee data, performance metrics, and training records, using a relational database management system.
Generated: DETERMINISTIC_19ff49e2b4a66081
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Human Capital Management System

-- Create the database
CREATE DATABASE IF NOT EXISTS human_capital_management;
USE human_capital_management;

-- Employees table
CREATE TABLE employees (
    employee_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    hire_date DATE NOT NULL,
    job_title VARCHAR(100) NOT NULL,
    department_id INT,
    manager_id INT,
    salary DECIMAL(10, 2) NOT NULL,
    status ENUM('active', 'on_leave', 'terminated') DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (department_id) REFERENCES departments(department_id),
    FOREIGN KEY (manager_id) REFERENCES employees(employee_id)
) ENGINE=InnoDB;

-- Departments table
CREATE TABLE departments (
    department_id INT PRIMARY KEY AUTO_INCREMENT,
    department_name VARCHAR(100) NOT NULL,
    location VARCHAR(100),
    manager_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (manager_id) REFERENCES employees(employee_id)
) ENGINE=InnoDB;

-- Performance reviews table
CREATE TABLE performance_reviews (
    review_id INT PRIMARY KEY AUTO_INCREMENT,
    employee_id INT NOT NULL,
    reviewer_id INT NOT NULL,
    review_date DATE NOT NULL,
    performance_score DECIMAL(3, 2) NOT NULL,
    comments TEXT,
    goals TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
    FOREIGN KEY (reviewer_id) REFERENCES employees(employee_id),
    CHECK (performance_score >= 0 AND performance_score <= 5)
) ENGINE=InnoDB;

-- Training programs table
CREATE TABLE training_programs (
    program_id INT PRIMARY KEY AUTO_INCREMENT,
    program_name VARCHAR(100) NOT NULL,
    description TEXT,
    duration_hours INT NOT NULL,
    provider VARCHAR(100),
    cost DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Employee training records
CREATE TABLE employee_training (
    record_id INT PRIMARY KEY AUTO_INCREMENT,
    employee_id INT NOT NULL,
    program_id INT NOT NULL,
    completion_date DATE NOT NULL,
    status ENUM('registered', 'in_progress', 'completed', 'failed') DEFAULT 'registered',
    score DECIMAL(5, 2),
    certificate_id VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
    FOREIGN KEY (program_id) REFERENCES training_programs(program_id)
) ENGINE=InnoDB;

-- Skills table
CREATE TABLE skills (
    skill_id INT PRIMARY KEY AUTO_INCREMENT,
    skill_name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Employee skills mapping
CREATE TABLE employee_skills (
    employee_skill_id INT PRIMARY KEY AUTO_INCREMENT,
    employee_id INT NOT NULL,
    skill_id INT NOT NULL,
    proficiency_level ENUM('beginner', 'intermediate', 'advanced', 'expert') NOT NULL,
    verified BOOLEAN DEFAULT FALSE,
    verified_by INT,
    verified_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
    FOREIGN KEY (skill_id) REFERENCES skills(skill_id),
    FOREIGN KEY (verified_by) REFERENCES employees(employee_id),
    UNIQUE KEY unique_employee_skill (employee_id, skill_id)
) ENGINE=InnoDB;

-- Compensation history
CREATE TABLE compensation_history (
    compensation_id INT PRIMARY KEY AUTO_INCREMENT,
    employee_id INT NOT NULL,
    change_date DATE NOT NULL,
    old_salary DECIMAL(10, 2),
    new_salary DECIMAL(10, 2) NOT NULL,
    change_reason VARCHAR(255),
    approved_by INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
    FOREIGN KEY (approved_by) REFERENCES employees(employee_id)
) ENGINE=InnoDB;

-- Leave records
CREATE TABLE leave_records (
    leave_id INT PRIMARY KEY AUTO_INCREMENT,
    employee_id INT NOT NULL,
    leave_type ENUM('vacation', 'sick', 'maternity', 'paternity', 'unpaid', 'other') NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    status ENUM('pending', 'approved', 'rejected', 'cancelled') DEFAULT 'pending',
    reason TEXT,
    approved_by INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
    FOREIGN KEY (approved_by) REFERENCES employees(employee_id),
    CHECK (end_date >= start_date)
) ENGINE=InnoDB;

-- Create indexes for performance optimization
CREATE INDEX idx_employee_department ON employees(department_id);
CREATE INDEX idx_employee_manager ON employees(manager_id);
CREATE INDEX idx_performance_employee ON performance_reviews(employee_id);
CREATE INDEX idx_training_employee ON employee_training(employee_id);
CREATE INDEX idx_skills_employee ON employee_skills(employee_id);
CREATE INDEX idx_compensation_employee ON compensation_history(employee_id);
CREATE INDEX idx_leave_employee ON leave_records(employee_id);
```
