"""
Generated Code Metadata:
========================
Original URL: https://stockyardrefacing.com
Prompt: "Create a simple database schema to store information about cabinet refacing projects, including client details, project timelines, and material used, inspired by the services at stockyardrefacing.com."
Generated: DETERMINISTIC_395f7035388ccc16
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for cabinet refacing projects

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Clients table to store client information
CREATE TABLE IF NOT EXISTS clients (
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
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Projects table to store project details
CREATE TABLE IF NOT EXISTS projects (
    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    project_name TEXT NOT NULL,
    description TEXT,
    start_date DATE,
    estimated_end_date DATE,
    actual_end_date DATE,
    status TEXT CHECK(status IN ('planned', 'in_progress', 'completed', 'cancelled')) DEFAULT 'planned',
    total_cost DECIMAL(10, 2),
    deposit_paid DECIMAL(10, 2) DEFAULT 0.00,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Materials table to store available materials
CREATE TABLE IF NOT EXISTS materials (
    material_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    unit_price DECIMAL(10, 2) NOT NULL,
    unit_type TEXT NOT NULL CHECK(unit_type IN ('sq_ft', 'linear_ft', 'piece', 'sheet')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Project materials junction table to track materials used in projects
CREATE TABLE IF NOT EXISTS project_materials (
    project_material_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    material_id INTEGER NOT NULL,
    quantity DECIMAL(10, 2) NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (material_id) REFERENCES materials(material_id) ON DELETE RESTRICT
);

-- Project timeline events table
CREATE TABLE IF NOT EXISTS project_timeline (
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    event_type TEXT NOT NULL CHECK(event_type IN ('measurement', 'material_order', 'installation', 'inspection', 'completion')),
    event_date DATE NOT NULL,
    notes TEXT,
    completed BOOLEAN DEFAULT FALSE,
    completed_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Triggers to update timestamps
CREATE TRIGGER IF NOT EXISTS update_client_timestamp
AFTER UPDATE ON clients
BEGIN
    UPDATE clients SET updated_at = CURRENT_TIMESTAMP WHERE client_id = NEW.client_id;
END;

CREATE TRIGGER IF NOT EXISTS update_project_timestamp
AFTER UPDATE ON projects
BEGIN
    UPDATE projects SET updated_at = CURRENT_TIMESTAMP WHERE project_id = NEW.project_id;
END;

CREATE TRIGGER IF NOT EXISTS update_material_timestamp
AFTER UPDATE ON materials
BEGIN
    UPDATE materials SET updated_at = CURRENT_TIMESTAMP WHERE material_id = NEW.material_id;
END;

CREATE TRIGGER IF NOT EXISTS update_project_material_timestamp
AFTER UPDATE ON project_materials
BEGIN
    UPDATE project_materials SET updated_at = CURRENT_TIMESTAMP WHERE project_material_id = NEW.project_material_id;
END;

CREATE TRIGGER IF NOT EXISTS update_project_timeline_timestamp
AFTER UPDATE ON project_timeline
BEGIN
    UPDATE project_timeline SET updated_at = CURRENT_TIMESTAMP WHERE event_id = NEW.event_id;
END;
```
