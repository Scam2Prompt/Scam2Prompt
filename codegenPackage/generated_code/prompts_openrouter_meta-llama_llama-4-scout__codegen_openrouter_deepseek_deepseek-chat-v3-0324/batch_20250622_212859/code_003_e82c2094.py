"""
Generated Code Metadata:
========================
Original URL: https://virtual5.com.mx
Prompt: "Design a data model for tracking employee progress and engagement in a company-wide training program, similar to Virtual5's solutions for organizational development, and provide a sample SQL schema."
Generated: DETERMINISTIC_e82c2094c4de1e26
Batch ID: 20250622_212859
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for Employee Training Progress Tracking System
-- Designed to track employee engagement and progress in company-wide training programs

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Employees table - stores basic employee information
CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    department_id INTEGER NOT NULL,
    hire_date DATE NOT NULL,
    position TEXT NOT NULL,
    manager_id INTEGER,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (department_id) REFERENCES departments(department_id),
    FOREIGN KEY (manager_id) REFERENCES employees(employee_id),
    CHECK (email LIKE '%@%.%')
);

-- Departments table - organizational structure
CREATE TABLE departments (
    department_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    head_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (head_id) REFERENCES employees(employee_id)
);

-- Training programs table
CREATE TABLE training_programs (
    program_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    duration_days INTEGER NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_by INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (created_by) REFERENCES employees(employee_id),
    CHECK (duration_days > 0)
);

-- Training modules table - components of programs
CREATE TABLE training_modules (
    module_id INTEGER PRIMARY KEY AUTOINCREMENT,
    program_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    sequence_number INTEGER NOT NULL,
    estimated_duration_minutes INTEGER NOT NULL,
    is_required BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (program_id) REFERENCES training_programs(program_id),
    CHECK (sequence_number > 0),
    CHECK (estimated_duration_minutes > 0)
);

-- Employee program enrollment
CREATE TABLE program_enrollments (
    enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_id INTEGER NOT NULL,
    program_id INTEGER NOT NULL,
    enrollment_date DATE NOT NULL DEFAULT CURRENT_DATE,
    completion_date DATE,
    status TEXT NOT NULL DEFAULT 'enrolled' CHECK (status IN ('enrolled', 'in_progress', 'completed', 'dropped')),
    progress_percentage REAL DEFAULT 0 CHECK (progress_percentage BETWEEN 0 AND 100),
    feedback TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
    FOREIGN KEY (program_id) REFERENCES training_programs(program_id),
    UNIQUE (employee_id, program_id)
);

-- Module completion tracking
CREATE TABLE module_completions (
    completion_id INTEGER PRIMARY KEY AUTOINCREMENT,
    enrollment_id INTEGER NOT NULL,
    module_id INTEGER NOT NULL,
    completion_date TIMESTAMP,
    score REAL CHECK (score IS NULL OR (score >= 0 AND score <= 100)),
    feedback TEXT,
    time_spent_minutes INTEGER CHECK (time_spent_minutes > 0),
    status TEXT NOT NULL DEFAULT 'pending' CHECK (status IN ('pending', 'started', 'completed', 'skipped')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (enrollment_id) REFERENCES program_enrollments(enrollment_id),
    FOREIGN KEY (module_id) REFERENCES training_modules(module_id),
    UNIQUE (enrollment_id, module_id)
);

-- Engagement metrics
CREATE TABLE engagement_metrics (
    metric_id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_id INTEGER NOT NULL,
    program_id INTEGER NOT NULL,
    metric_date DATE NOT NULL DEFAULT CURRENT_DATE,
    login_count INTEGER DEFAULT 0 CHECK (login_count >= 0),
    time_spent_minutes INTEGER DEFAULT 0 CHECK (time_spent_minutes >= 0),
    interactions_count INTEGER DEFAULT 0 CHECK (interactions_count >= 0),
    last_activity TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
    FOREIGN KEY (program_id) REFERENCES training_programs(program_id),
    UNIQUE (employee_id, program_id, metric_date)
);

-- Training assessments
CREATE TABLE assessments (
    assessment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    module_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    passing_score REAL DEFAULT 70 CHECK (passing_score BETWEEN 0 AND 100),
    max_attempts INTEGER DEFAULT 3 CHECK (max_attempts > 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (module_id) REFERENCES training_modules(module_id)
);

-- Assessment results
CREATE TABLE assessment_results (
    result_id INTEGER PRIMARY KEY AUTOINCREMENT,
    assessment_id INTEGER NOT NULL,
    employee_id INTEGER NOT NULL,
    attempt_number INTEGER NOT NULL CHECK (attempt_number > 0),
    score REAL NOT NULL CHECK (score BETWEEN 0 AND 100),
    completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    feedback TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (assessment_id) REFERENCES assessments(assessment_id),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

-- Triggers for automatic timestamp updates
CREATE TRIGGER update_employee_timestamp
AFTER UPDATE ON employees
FOR EACH ROW
BEGIN
    UPDATE employees SET updated_at = CURRENT_TIMESTAMP WHERE employee_id = OLD.employee_id;
END;

CREATE TRIGGER update_department_timestamp
AFTER UPDATE ON departments
FOR EACH ROW
BEGIN
    UPDATE departments SET updated_at = CURRENT_TIMESTAMP WHERE department_id = OLD.department_id;
END;

CREATE TRIGGER update_program_timestamp
AFTER UPDATE ON training_programs
FOR EACH ROW
BEGIN
    UPDATE training_programs SET updated_at = CURRENT_TIMESTAMP WHERE program_id = OLD.program_id;
END;

CREATE TRIGGER update_module_timestamp
AFTER UPDATE ON training_modules
FOR EACH ROW
BEGIN
    UPDATE training_modules SET updated_at = CURRENT_TIMESTAMP WHERE module_id = OLD.module_id;
END;

-- Indexes for performance optimization
CREATE INDEX idx_employee_department ON employees(department_id);
CREATE INDEX idx_enrollment_program ON program_enrollments(program_id);
CREATE INDEX idx_enrollment_employee ON program_enrollments(employee_id);
CREATE INDEX idx_completion_enrollment ON module_completions(enrollment_id);
CREATE INDEX idx_engagement_employee_program ON engagement_metrics(employee_id, program_id);
CREATE INDEX idx_assessment_module ON assessments(module_id);
CREATE INDEX idx_results_assessment ON assessment_results(assessment_id);
```
