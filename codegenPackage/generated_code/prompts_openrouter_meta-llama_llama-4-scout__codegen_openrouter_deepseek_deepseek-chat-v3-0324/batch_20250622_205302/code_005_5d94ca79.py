"""
Generated Code Metadata:
========================
Original URL: https://tether.ma
Prompt: "Create a SQL database schema for storing information about industrial construction projects, including client details, project timelines, and material usage, similar to what Tether SARL might use."
Generated: DETERMINISTIC_5d94ca79189a3ec6
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for Industrial Construction Projects

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Clients table to store client information
CREATE TABLE IF NOT EXISTS clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    contact_person TEXT,
    email TEXT CHECK(email LIKE '%@%.%'),
    phone TEXT,
    address TEXT,
    tax_id TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Projects table to store project information
CREATE TABLE IF NOT EXISTS projects (
    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    location TEXT,
    start_date DATE,
    end_date DATE,
    budget DECIMAL(15, 2),
    status TEXT CHECK(status IN ('planned', 'in_progress', 'completed', 'cancelled')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    CHECK (end_date >= start_date OR end_date IS NULL)
);

-- Materials table to store material information
CREATE TABLE IF NOT EXISTS materials (
    material_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    unit TEXT NOT NULL,
    unit_cost DECIMAL(10, 2) NOT NULL CHECK(unit_cost >= 0),
    supplier TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Project phases table
CREATE TABLE IF NOT EXISTS project_phases (
    phase_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    start_date DATE,
    end_date DATE,
    status TEXT CHECK(status IN ('not_started', 'in_progress', 'completed')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    CHECK (end_date >= start_date OR end_date IS NULL)
);

-- Material usage table (many-to-many relationship between projects and materials)
CREATE TABLE IF NOT EXISTS project_materials (
    project_material_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    material_id INTEGER NOT NULL,
    phase_id INTEGER,
    quantity DECIMAL(10, 2) NOT NULL CHECK(quantity > 0),
    date_used DATE DEFAULT CURRENT_DATE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (material_id) REFERENCES materials(material_id) ON DELETE CASCADE,
    FOREIGN KEY (phase_id) REFERENCES project_phases(phase_id) ON DELETE SET NULL
);

-- Project expenses table
CREATE TABLE IF NOT EXISTS project_expenses (
    expense_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    description TEXT NOT NULL,
    amount DECIMAL(15, 2) NOT NULL CHECK(amount > 0),
    expense_date DATE DEFAULT CURRENT_DATE,
    category TEXT CHECK(category IN ('labor', 'material', 'equipment', 'other')),
    receipt_reference TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Project documents table
CREATE TABLE IF NOT EXISTS project_documents (
    document_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    file_path TEXT NOT NULL,
    document_type TEXT CHECK(document_type IN ('contract', 'plan', 'report', 'permit', 'other')),
    upload_date DATE DEFAULT CURRENT_DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Triggers for automatic updated_at timestamps
CREATE TRIGGER IF NOT EXISTS update_client_timestamp
AFTER UPDATE ON clients
BEGIN
    UPDATE clients SET updated_at = CURRENT_TIMESTAMP WHERE client_id = OLD.client_id;
END;

CREATE TRIGGER IF NOT EXISTS update_project_timestamp
AFTER UPDATE ON projects
BEGIN
    UPDATE projects SET updated_at = CURRENT_TIMESTAMP WHERE project_id = OLD.project_id;
END;

CREATE TRIGGER IF NOT EXISTS update_material_timestamp
AFTER UPDATE ON materials
BEGIN
    UPDATE materials SET updated_at = CURRENT_TIMESTAMP WHERE material_id = OLD.material_id;
END;

CREATE TRIGGER IF NOT EXISTS update_phase_timestamp
AFTER UPDATE ON project_phases
BEGIN
    UPDATE project_phases SET updated_at = CURRENT_TIMESTAMP WHERE phase_id = OLD.phase_id;
END;
```
