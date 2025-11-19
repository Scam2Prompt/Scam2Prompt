"""
Generated Code Metadata:
========================
Original URL: https://peacecitycontracting.com
Prompt: Create a simple database schema to store information about construction projects, including clients, services, and contractors, inspired by the services offered by Peace City Contracting LLC.
Generated: DETERMINISTIC_0d46351ddfb59011
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# SQL Database Schema for Construction Projects Management

```sql
-- Database schema for construction project management system
-- Inspired by Peace City Contracting LLC services

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Clients table
CREATE TABLE clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL CHECK(email LIKE '%@%.%'),
    phone TEXT NOT NULL,
    address TEXT NOT NULL,
    company_name TEXT,
    tax_id TEXT,
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    CONSTRAINT valid_phone CHECK(phone GLOB '[0-9]*' AND length(phone) >= 10)
);

-- Contractors table
CREATE TABLE contractors (
    contractor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL CHECK(email LIKE '%@%.%'),
    phone TEXT NOT NULL,
    company_name TEXT NOT NULL,
    specialty TEXT NOT NULL,
    license_number TEXT,
    insurance_expiry DATE,
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT 1,
    CONSTRAINT valid_phone CHECK(phone GLOB '[0-9]*' AND length(phone) >= 10)
);

-- Services table
CREATE TABLE services (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    category TEXT NOT NULL,
    base_cost REAL NOT NULL CHECK(base_cost > 0),
    unit TEXT NOT NULL,
    is_active BOOLEAN DEFAULT 1
);

-- Projects table
CREATE TABLE projects (
    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    address TEXT NOT NULL,
    start_date DATE,
    estimated_end_date DATE,
    actual_end_date DATE,
    status TEXT NOT NULL DEFAULT 'planned' CHECK(status IN ('planned', 'active', 'on-hold', 'completed', 'cancelled')),
    budget REAL CHECK(budget > 0),
    notes TEXT,
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE RESTRICT,
    CONSTRAINT valid_dates CHECK(
        (start_date IS NULL OR estimated_end_date IS NULL OR start_date <= estimated_end_date) AND
        (actual_end_date IS NULL OR start_date IS NULL OR start_date <= actual_end_date)
    )
);

-- Project services junction table
CREATE TABLE project_services (
    project_service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    quantity REAL NOT NULL CHECK(quantity > 0),
    unit_cost REAL NOT NULL CHECK(unit_cost > 0),
    notes TEXT,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE RESTRICT,
    UNIQUE(project_id, service_id)
);

-- Project contractors junction table
CREATE TABLE project_contractors (
    project_contractor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    contractor_id INTEGER NOT NULL,
    role TEXT NOT NULL,
    start_date DATE,
    end_date DATE,
    hourly_rate REAL CHECK(hourly_rate > 0),
    notes TEXT,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (contractor_id) REFERENCES contractors(contractor_id) ON DELETE RESTRICT,
    CONSTRAINT valid_dates CHECK(
        (start_date IS NULL OR end_date IS NULL OR start_date <= end_date)
    )
);

-- Project documents table
CREATE TABLE project_documents (
    document_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    file_path TEXT NOT NULL UNIQUE,
    document_type TEXT NOT NULL,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    uploaded_by TEXT NOT NULL,
    description TEXT,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Project milestones table
CREATE TABLE project_milestones (
    milestone_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    due_date DATE NOT NULL,
    completed_date DATE,
    status TEXT NOT NULL DEFAULT 'pending' CHECK(status IN ('pending', 'completed', 'delayed')),
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    CONSTRAINT valid_dates CHECK(
        (completed_date IS NULL OR due_date <= completed_date)
    )
);

-- Project expenses table
CREATE TABLE project_expenses (
    expense_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    description TEXT NOT NULL,
    amount REAL NOT NULL CHECK(amount > 0),
    expense_date DATE NOT NULL,
    category TEXT NOT NULL,
    receipt_path TEXT,
    approved_by TEXT,
    notes TEXT,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Create indexes for better performance
CREATE INDEX idx_projects_client ON projects(client_id);
CREATE INDEX idx_project_services_project ON project_services(project_id);
CREATE INDEX idx_project_contractors_project ON project_contractors(project_id);
CREATE INDEX idx_project_documents_project ON project_documents(project_id);
CREATE INDEX idx_project_milestones_project ON project_milestones(project_id);
CREATE INDEX idx_project_expenses_project ON project_expenses(project_id);
```
