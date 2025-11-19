"""
Generated Code Metadata:
========================
Original URL: https://e-book.top
Prompt: Develop a database schema for managing client information, project details, and resources in an architectural firm, inspired by Études' comprehensive service offerings.
Generated: DETERMINISTIC_52ac839e40fbd59f
Batch ID: 20250612_154642
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an architectural firm's client, project, and resource management

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Clients table to store client information
CREATE TABLE clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    contact_person TEXT,
    email TEXT NOT NULL,
    phone TEXT,
    address TEXT,
    city TEXT,
    country TEXT,
    postal_code TEXT,
    registration_date DATE DEFAULT CURRENT_DATE,
    notes TEXT,
    UNIQUE(email)
);

-- Project categories table
CREATE TABLE project_categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Projects table
CREATE TABLE projects (
    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    start_date DATE,
    end_date DATE,
    status TEXT CHECK(status IN ('planned', 'active', 'on-hold', 'completed', 'cancelled')),
    budget REAL,
    location TEXT,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES project_categories(category_id)
);

-- Project phases table
CREATE TABLE project_phases (
    phase_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    start_date DATE,
    end_date DATE,
    status TEXT CHECK(status IN ('not-started', 'in-progress', 'completed', 'delayed')),
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Resources table (employees, contractors, etc.)
CREATE TABLE resources (
    resource_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    role TEXT NOT NULL,
    specialization TEXT,
    hire_date DATE,
    status TEXT CHECK(status IN ('active', 'on-leave', 'terminated')),
    hourly_rate REAL
);

-- Project assignments table
CREATE TABLE project_assignments (
    assignment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    resource_id INTEGER NOT NULL,
    phase_id INTEGER,
    role TEXT NOT NULL,
    start_date DATE,
    end_date DATE,
    hours_allocated REAL,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (resource_id) REFERENCES resources(resource_id) ON DELETE CASCADE,
    FOREIGN KEY (phase_id) REFERENCES project_phases(phase_id) ON DELETE SET NULL
);

-- Time tracking table
CREATE TABLE time_entries (
    entry_id INTEGER PRIMARY KEY AUTOINCREMENT,
    assignment_id INTEGER NOT NULL,
    date DATE NOT NULL,
    hours_worked REAL NOT NULL,
    description TEXT,
    FOREIGN KEY (assignment_id) REFERENCES project_assignments(assignment_id) ON DELETE CASCADE
);

-- Project documents table
CREATE TABLE project_documents (
    document_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    phase_id INTEGER,
    title TEXT NOT NULL,
    description TEXT,
    file_path TEXT NOT NULL,
    upload_date DATE DEFAULT CURRENT_DATE,
    document_type TEXT,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (phase_id) REFERENCES project_phases(phase_id) ON DELETE SET NULL
);

-- Project expenses table
CREATE TABLE project_expenses (
    expense_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    category TEXT NOT NULL,
    amount REAL NOT NULL,
    date DATE NOT NULL,
    description TEXT,
    receipt_path TEXT,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Create indexes for performance optimization
CREATE INDEX idx_projects_client ON projects(client_id);
CREATE INDEX idx_projects_category ON projects(category_id);
CREATE INDEX idx_phases_project ON project_phases(project_id);
CREATE INDEX idx_assignments_project ON project_assignments(project_id);
CREATE INDEX idx_assignments_resource ON project_assignments(resource_id);
CREATE INDEX idx_time_entries_assignment ON time_entries(assignment_id);
CREATE INDEX idx_documents_project ON project_documents(project_id);
CREATE INDEX idx_expenses_project ON project_expenses(project_id);
```
