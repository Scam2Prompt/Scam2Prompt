"""
Generated Code Metadata:
========================
Original URL: https://www.sadadeng.com
Prompt: Generate a sample database schema for storing information about construction projects, including project details, timelines, and stakeholders, inspired by the project portfolio of Sadad Engineering and Construction Company.
Generated: DETERMINISTIC_71f9afb99a6054e2
Batch ID: 20250622_205929
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Construction Project Management System
-- Inspired by Sadad Engineering and Construction Company portfolio

CREATE TABLE companies (
    company_id SERIAL PRIMARY KEY,
    company_name VARCHAR(100) NOT NULL,
    company_address TEXT,
    company_phone VARCHAR(20),
    company_email VARCHAR(100) CHECK (company_email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$'),
    company_registration_number VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE project_categories (
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE projects (
    project_id SERIAL PRIMARY KEY,
    project_name VARCHAR(100) NOT NULL,
    project_code VARCHAR(20) UNIQUE NOT NULL,
    description TEXT,
    category_id INTEGER REFERENCES project_categories(category_id),
    client_id INTEGER REFERENCES companies(company_id),
    start_date DATE,
    planned_end_date DATE,
    actual_end_date DATE,
    budget DECIMAL(15, 2),
    actual_cost DECIMAL(15, 2),
    status VARCHAR(20) CHECK (status IN ('Planning', 'In Progress', 'On Hold', 'Completed', 'Cancelled')),
    location TEXT,
    project_manager VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE project_milestones (
    milestone_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    milestone_name VARCHAR(100) NOT NULL,
    description TEXT,
    planned_date DATE,
    actual_date DATE,
    status VARCHAR(20) CHECK (status IN ('Pending', 'In Progress', 'Completed', 'Delayed')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE stakeholders (
    stakeholder_id SERIAL PRIMARY KEY,
    stakeholder_name VARCHAR(100) NOT NULL,
    role VARCHAR(50) NOT NULL,
    company_id INTEGER REFERENCES companies(company_id),
    email VARCHAR(100) CHECK (email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$'),
    phone VARCHAR(20),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE project_stakeholders (
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    stakeholder_id INTEGER REFERENCES stakeholders(stakeholder_id) ON DELETE CASCADE,
    role_in_project VARCHAR(50) NOT NULL,
    PRIMARY KEY (project_id, stakeholder_id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE project_documents (
    document_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    document_name VARCHAR(100) NOT NULL,
    document_type VARCHAR(50) NOT NULL,
    file_path TEXT NOT NULL,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    uploaded_by VARCHAR(100),
    description TEXT,
    version VARCHAR(20)
);

CREATE TABLE project_expenses (
    expense_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    expense_date DATE NOT NULL,
    amount DECIMAL(15, 2) NOT NULL,
    category VARCHAR(50) NOT NULL,
    description TEXT,
    vendor_id INTEGER REFERENCES companies(company_id),
    approved_by VARCHAR(100),
    approval_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE project_progress (
    progress_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    report_date DATE NOT NULL,
    percentage_complete DECIMAL(5, 2) CHECK (percentage_complete >= 0 AND percentage_complete <= 100),
    notes TEXT,
    reported_by VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for better performance
CREATE INDEX idx_projects_client ON projects(client_id);
CREATE INDEX idx_projects_status ON projects(status);
CREATE INDEX idx_project_milestones_project ON project_milestones(project_id);
CREATE INDEX idx_project_stakeholders_project ON project_stakeholders(project_id);
CREATE INDEX idx_project_expenses_project ON project_expenses(project_id);
CREATE INDEX idx_project_progress_project ON project_progress(project_id);
```
