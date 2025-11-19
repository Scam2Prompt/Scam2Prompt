"""
Generated Code Metadata:
========================
Original URL: https://strk.site
Prompt: Design a database schema for storing information about completed renovation projects, including client details, project scope, and costs, inspired by the project management approach mentioned on the STRK site.
Generated: DETERMINISTIC_abcc73e29fa08c44
Batch ID: 20250612_135324
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for renovation project management system

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Clients table to store client information
CREATE TABLE clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    zip_code TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%.%')
);

-- Project categories table
CREATE TABLE project_categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Projects table to store renovation project details
CREATE TABLE projects (
    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    estimated_cost DECIMAL(10, 2) NOT NULL,
    actual_cost DECIMAL(10, 2),
    status TEXT NOT NULL CHECK (status IN ('planned', 'in_progress', 'completed', 'on_hold', 'cancelled')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES project_categories(category_id),
    CHECK (end_date >= start_date),
    CHECK (actual_cost >= 0 OR actual_cost IS NULL),
    CHECK (estimated_cost > 0)
);

-- Project phases table
CREATE TABLE project_phases (
    phase_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    status TEXT NOT NULL CHECK (status IN ('not_started', 'in_progress', 'completed', 'delayed')),
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    CHECK (end_date >= start_date)
);

-- Materials table
CREATE TABLE materials (
    material_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    unit TEXT NOT NULL,
    unit_cost DECIMAL(10, 2) NOT NULL,
    CHECK (unit_cost > 0)
);

-- Project materials (junction table)
CREATE TABLE project_materials (
    project_material_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    material_id INTEGER NOT NULL,
    quantity DECIMAL(10, 2) NOT NULL,
    actual_cost DECIMAL(10, 2),
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (material_id) REFERENCES materials(material_id),
    CHECK (quantity > 0),
    CHECK (actual_cost >= 0 OR actual_cost IS NULL)
);

-- Labor table
CREATE TABLE labor_types (
    labor_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    hourly_rate DECIMAL(10, 2) NOT NULL,
    CHECK (hourly_rate > 0)
);

-- Project labor (junction table)
CREATE TABLE project_labor (
    project_labor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    labor_type_id INTEGER NOT NULL,
    hours_worked DECIMAL(10, 2) NOT NULL,
    actual_cost DECIMAL(10, 2),
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (labor_type_id) REFERENCES labor_types(labor_type_id),
    CHECK (hours_worked > 0),
    CHECK (actual_cost >= 0 OR actual_cost IS NULL)
);

-- Project documents table
CREATE TABLE project_documents (
    document_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    file_path TEXT NOT NULL,
    document_type TEXT NOT NULL CHECK (document_type IN ('contract', 'invoice', 'permit', 'design', 'photo', 'other')),
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Project notes table
CREATE TABLE project_notes (
    note_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Triggers for automatic timestamp updates
CREATE TRIGGER update_client_timestamp
AFTER UPDATE ON clients
FOR EACH ROW
BEGIN
    UPDATE clients SET updated_at = CURRENT_TIMESTAMP WHERE client_id = OLD.client_id;
END;

CREATE TRIGGER update_project_timestamp
AFTER UPDATE ON projects
FOR EACH ROW
BEGIN
    UPDATE projects SET updated_at = CURRENT_TIMESTAMP WHERE project_id = OLD.project_id;
END;

CREATE TRIGGER update_project_note_timestamp
AFTER UPDATE ON project_notes
FOR EACH ROW
BEGIN
    UPDATE project_notes SET updated_at = CURRENT_TIMESTAMP WHERE note_id = OLD.note_id;
END;
```
