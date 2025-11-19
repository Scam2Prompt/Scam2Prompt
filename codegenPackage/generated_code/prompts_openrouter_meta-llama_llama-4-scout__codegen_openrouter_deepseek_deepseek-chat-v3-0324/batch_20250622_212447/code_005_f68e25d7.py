"""
Generated Code Metadata:
========================
Original URL: https://vertiv.mitarbeiterangebote.de
Prompt: Design a simple database schema to store employee information and benefits data for a company like Vertiv GmbH.
Generated: DETERMINISTIC_f68e25d7d934ce20
Batch ID: 20250622_212447
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Vertiv GmbH employee and benefits management

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Departments table
CREATE TABLE departments (
    department_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    location TEXT,
    budget REAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Employees table
CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL CHECK(email LIKE '%@%'),
    phone TEXT,
    hire_date DATE NOT NULL,
    job_title TEXT NOT NULL,
    salary REAL NOT NULL CHECK(salary > 0),
    department_id INTEGER,
    manager_id INTEGER,
    status TEXT DEFAULT 'active' CHECK(status IN ('active', 'on_leave', 'terminated')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (department_id) REFERENCES departments(department_id),
    FOREIGN KEY (manager_id) REFERENCES employees(employee_id)
);

-- Benefits table
CREATE TABLE benefits (
    benefit_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    cost_to_company REAL NOT NULL CHECK(cost_to_company >= 0),
    employee_contribution REAL DEFAULT 0 CHECK(employee_contribution >= 0),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Employee benefits junction table
CREATE TABLE employee_benefits (
    employee_id INTEGER NOT NULL,
    benefit_id INTEGER NOT NULL,
    enrollment_date DATE NOT NULL DEFAULT CURRENT_DATE,
    termination_date DATE,
    PRIMARY KEY (employee_id, benefit_id),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id) ON DELETE CASCADE,
    FOREIGN KEY (benefit_id) REFERENCES benefits(benefit_id) ON DELETE CASCADE,
    CHECK (termination_date IS NULL OR termination_date > enrollment_date)
);

-- Salary history table
CREATE TABLE salary_history (
    history_id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_id INTEGER NOT NULL,
    old_salary REAL NOT NULL,
    new_salary REAL NOT NULL CHECK(new_salary > 0),
    change_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    change_reason TEXT,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id) ON DELETE CASCADE
);

-- Create indexes for performance
CREATE INDEX idx_employees_department ON employees(department_id);
CREATE INDEX idx_employees_manager ON employees(manager_id);
CREATE INDEX idx_employee_benefits_employee ON employee_benefits(employee_id);
CREATE INDEX idx_employee_benefits_benefit ON employee_benefits(benefit_id);
CREATE INDEX idx_salary_history_employee ON salary_history(employee_id);

-- Create triggers for audit logging
CREATE TRIGGER update_department_timestamp
AFTER UPDATE ON departments
BEGIN
    UPDATE departments SET updated_at = CURRENT_TIMESTAMP WHERE department_id = NEW.department_id;
END;

CREATE TRIGGER update_employee_timestamp
AFTER UPDATE ON employees
BEGIN
    UPDATE employees SET updated_at = CURRENT_TIMESTAMP WHERE employee_id = NEW.employee_id;
END;

CREATE TRIGGER update_benefit_timestamp
AFTER UPDATE ON benefits
BEGIN
    UPDATE benefits SET updated_at = CURRENT_TIMESTAMP WHERE benefit_id = NEW.benefit_id;
END;

-- Trigger to log salary changes
CREATE TRIGGER log_salary_change
AFTER UPDATE OF salary ON employees
WHEN OLD.salary <> NEW.salary
BEGIN
    INSERT INTO salary_history (employee_id, old_salary, new_salary, change_reason)
    VALUES (OLD.employee_id, OLD.salary, NEW.salary, 'Salary adjustment');
END;
```
