"""
Generated Code Metadata:
========================
Original URL: https://sstco.ma
Prompt: Design a database schema to store information about construction projects, including project details, timelines, and personnel assignments, similar to what SSTCO might use to manage its projects.
Generated: DETERMINISTIC_13138450eeb756bd
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for construction project management

CREATE TABLE projects (
    project_id SERIAL PRIMARY KEY,
    project_name VARCHAR(100) NOT NULL,
    project_description TEXT,
    client_name VARCHAR(100) NOT NULL,
    client_contact VARCHAR(100),
    start_date DATE NOT NULL,
    estimated_end_date DATE,
    actual_end_date DATE,
    budget DECIMAL(15, 2),
    status VARCHAR(20) CHECK (status IN ('Planning', 'In Progress', 'On Hold', 'Completed', 'Cancelled')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE project_phases (
    phase_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    phase_name VARCHAR(50) NOT NULL,
    description TEXT,
    start_date DATE,
    end_date DATE,
    status VARCHAR(20) CHECK (status IN ('Not Started', 'In Progress', 'Completed', 'Delayed')),
    completion_percentage INTEGER DEFAULT 0 CHECK (completion_percentage BETWEEN 0 AND 100)
);

CREATE TABLE employees (
    employee_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    position VARCHAR(50),
    department VARCHAR(50),
    hire_date DATE,
    is_active BOOLEAN DEFAULT TRUE
);

CREATE TABLE project_assignments (
    assignment_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    employee_id INTEGER REFERENCES employees(employee_id) ON DELETE CASCADE,
    phase_id INTEGER REFERENCES project_phases(phase_id) ON DELETE SET NULL,
    role VARCHAR(50) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    hours_allocated INTEGER,
    status VARCHAR(20) DEFAULT 'Active' CHECK (status IN ('Active', 'Completed', 'Reassigned'))
);

CREATE TABLE project_documents (
    document_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    document_name VARCHAR(100) NOT NULL,
    document_type VARCHAR(50),
    file_path VARCHAR(255) NOT NULL,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    uploaded_by INTEGER REFERENCES employees(employee_id) ON DELETE SET NULL,
    description TEXT
);

CREATE TABLE project_milestones (
    milestone_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    milestone_name VARCHAR(100) NOT NULL,
    description TEXT,
    due_date DATE NOT NULL,
    completed_date DATE,
    status VARCHAR(20) DEFAULT 'Pending' CHECK (status IN ('Pending', 'Completed', 'Delayed'))
);

CREATE TABLE project_expenses (
    expense_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    expense_date DATE NOT NULL,
    category VARCHAR(50) NOT NULL,
    description TEXT,
    amount DECIMAL(10, 2) NOT NULL,
    approved_by INTEGER REFERENCES employees(employee_id) ON DELETE SET NULL,
    approval_date DATE,
    receipt_path VARCHAR(255)
);

CREATE TABLE project_comments (
    comment_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    employee_id INTEGER REFERENCES employees(employee_id) ON DELETE SET NULL,
    comment_text TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    parent_comment_id INTEGER REFERENCES project_comments(comment_id) ON DELETE CASCADE
);

-- Indexes for performance optimization
CREATE INDEX idx_project_status ON projects(status);
CREATE INDEX idx_project_phase_status ON project_phases(status);
CREATE INDEX idx_project_assignments ON project_assignments(project_id, employee_id);
CREATE INDEX idx_project_milestones ON project_milestones(project_id, status);
CREATE INDEX idx_project_expenses ON project_expenses(project_id, expense_date);

-- Triggers for automatic updated_at timestamps
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_project_timestamp
BEFORE UPDATE ON projects
FOR EACH ROW
EXECUTE FUNCTION update_timestamp();
```
