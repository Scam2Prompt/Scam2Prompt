"""
Generated Code Metadata:
========================
Original URL: https://uranpres.sk
Prompt: "Generate a sample database schema for storing information about construction projects, including underground construction, geological surveys, and client details, similar to what URANPRES, s.r.o. might use."
Generated: DETERMINISTIC_b4c184fb22988bf2
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for construction project management system
-- Similar to what URANPRES, s.r.o. might use

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Clients table
CREATE TABLE clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    postal_code TEXT NOT NULL,
    country TEXT DEFAULT 'Slovakia',
    contact_person TEXT,
    email TEXT CHECK(email LIKE '%@%.%'),
    phone TEXT,
    tax_id TEXT UNIQUE,
    registration_date DATE DEFAULT CURRENT_DATE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Projects table
CREATE TABLE projects (
    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    project_name TEXT NOT NULL,
    project_code TEXT UNIQUE,
    description TEXT,
    location TEXT NOT NULL,
    start_date DATE,
    end_date DATE,
    estimated_cost DECIMAL(12, 2),
    actual_cost DECIMAL(12, 2),
    status TEXT CHECK(status IN ('planned', 'active', 'on_hold', 'completed', 'cancelled')),
    project_manager TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE RESTRICT
);

-- Geological surveys table
CREATE TABLE geological_surveys (
    survey_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    survey_name TEXT NOT NULL,
    survey_date DATE NOT NULL,
    conducted_by TEXT NOT NULL,
    depth DECIMAL(8, 2),
    soil_type TEXT,
    rock_type TEXT,
    water_level DECIMAL(8, 2),
    stability_rating INTEGER CHECK(stability_rating BETWEEN 1 AND 10),
    report_file_path TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Underground construction table
CREATE TABLE underground_constructions (
    construction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    construction_type TEXT CHECK(construction_type IN ('tunnel', 'mine', 'basement', 'sewer', 'other')),
    name TEXT NOT NULL,
    start_depth DECIMAL(8, 2),
    end_depth DECIMAL(8, 2),
    length DECIMAL(10, 2),
    diameter DECIMAL(8, 2),
    material TEXT,
    construction_method TEXT,
    start_date DATE,
    end_date DATE,
    status TEXT CHECK(status IN ('planned', 'in_progress', 'completed', 'abandoned')),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Project documents table
CREATE TABLE project_documents (
    document_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    document_type TEXT CHECK(document_type IN ('contract', 'permit', 'report', 'drawing', 'photo', 'other')),
    title TEXT NOT NULL,
    description TEXT,
    file_path TEXT NOT NULL,
    upload_date DATE DEFAULT CURRENT_DATE,
    uploaded_by TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Project milestones table
CREATE TABLE project_milestones (
    milestone_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    due_date DATE NOT NULL,
    completion_date DATE,
    status TEXT CHECK(status IN ('pending', 'completed', 'delayed')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Triggers for automatic timestamps
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

CREATE TRIGGER update_survey_timestamp
AFTER UPDATE ON geological_surveys
FOR EACH ROW
BEGIN
    UPDATE geological_surveys SET updated_at = CURRENT_TIMESTAMP WHERE survey_id = OLD.survey_id;
END;

CREATE TRIGGER update_construction_timestamp
AFTER UPDATE ON underground_constructions
FOR EACH ROW
BEGIN
    UPDATE underground_constructions SET updated_at = CURRENT_TIMESTAMP WHERE construction_id = OLD.construction_id;
END;

CREATE TRIGGER update_milestone_timestamp
AFTER UPDATE ON project_milestones
FOR EACH ROW
BEGIN
    UPDATE project_milestones SET updated_at = CURRENT_TIMESTAMP WHERE milestone_id = OLD.milestone_id;
END;
```
