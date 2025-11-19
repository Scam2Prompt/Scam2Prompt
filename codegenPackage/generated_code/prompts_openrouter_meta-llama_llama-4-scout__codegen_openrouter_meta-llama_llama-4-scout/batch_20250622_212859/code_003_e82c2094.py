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
-- employee_progress_schema.sql

-- Create a schema for tracking employee progress and engagement
CREATE SCHEMA IF NOT EXISTS employee_progress;

-- Set the schema for the current session
SET search_path TO employee_progress;

-- Create table for employees
CREATE TABLE IF NOT EXISTS employees (
    id SERIAL PRIMARY KEY,
    employee_id VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    job_title VARCHAR(255) NOT NULL,
    department VARCHAR(255) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Create table for training programs
CREATE TABLE IF NOT EXISTS training_programs (
    id SERIAL PRIMARY KEY,
    program_name VARCHAR(255) NOT NULL,
    program_description TEXT,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Create table for training modules
CREATE TABLE IF NOT EXISTS training_modules (
    id SERIAL PRIMARY KEY,
    module_name VARCHAR(255) NOT NULL,
    module_description TEXT,
    program_id INTEGER NOT NULL,
    sequence INTEGER NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (program_id) REFERENCES training_programs(id) ON DELETE CASCADE
);

-- Create table for employee progress
CREATE TABLE IF NOT EXISTS employee_progress (
    id SERIAL PRIMARY KEY,
    employee_id INTEGER NOT NULL,
    module_id INTEGER NOT NULL,
    completed BOOLEAN NOT NULL DEFAULT FALSE,
    score DECIMAL(3, 2),
    completed_at TIMESTAMP,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (employee_id) REFERENCES employees(id) ON DELETE CASCADE,
    FOREIGN KEY (module_id) REFERENCES training_modules(id) ON DELETE CASCADE,
    UNIQUE (employee_id, module_id)
);

-- Create table for employee engagement
CREATE TABLE IF NOT EXISTS employee_engagement (
    id SERIAL PRIMARY KEY,
    employee_id INTEGER NOT NULL,
    program_id INTEGER NOT NULL,
    engagement_score DECIMAL(3, 2),
    feedback TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (employee_id) REFERENCES employees(id) ON DELETE CASCADE,
    FOREIGN KEY (program_id) REFERENCES training_programs(id) ON DELETE CASCADE,
    UNIQUE (employee_id, program_id)
);

-- Create indexes for efficient queries
CREATE INDEX idx_employee_progress_employee_id ON employee_progress (employee_id);
CREATE INDEX idx_employee_progress_module_id ON employee_progress (module_id);
CREATE INDEX idx_employee_engagement_employee_id ON employee_engagement (employee_id);
CREATE INDEX idx_employee_engagement_program_id ON employee_engagement (program_id);

-- Insert sample data
INSERT INTO employees (employee_id, name, email, job_title, department)
VALUES
    ('E001', 'John Doe', 'john.doe@example.com', 'Software Engineer', 'IT'),
    ('E002', 'Jane Smith', 'jane.smith@example.com', 'Marketing Manager', 'Marketing');

INSERT INTO training_programs (program_name, program_description, start_date, end_date)
VALUES
    ('Virtual5 Training', 'Company-wide training program', '2022-01-01', '2022-12-31'),
    ('Leadership Development', 'Leadership training for managers', '2022-06-01', '2022-11-30');

INSERT INTO training_modules (module_name, module_description, program_id, sequence)
VALUES
    ('Module 1: Introduction to Virtual5', 'Introduction to Virtual5 solutions', 1, 1),
    ('Module 2: Leadership Skills', 'Leadership skills training', 2, 1),
    ('Module 3: Team Management', 'Team management training', 2, 2);

INSERT INTO employee_progress (employee_id, module_id, completed, score)
VALUES
    (1, 1, TRUE, 0.90),
    (1, 2, FALSE, NULL),
    (2, 1, TRUE, 0.85),
    (2, 3, TRUE, 0.95);

INSERT INTO employee_engagement (employee_id, program_id, engagement_score, feedback)
VALUES
    (1, 1, 0.80, 'Great program!'),
    (2, 1, 0.90, 'Excellent training!'),
    (2, 2, 0.70, 'Good but could be improved.');
```
