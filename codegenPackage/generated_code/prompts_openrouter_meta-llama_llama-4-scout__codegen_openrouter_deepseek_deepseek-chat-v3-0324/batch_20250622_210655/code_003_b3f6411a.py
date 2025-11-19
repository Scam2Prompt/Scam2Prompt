"""
Generated Code Metadata:
========================
Original URL: https://thedesignumbrella.in
Prompt: "Design a database schema for storing and managing projects, clients, and services for a design studio like The Design Umbrella, incorporating details such as project analysis, site study, and materials selection."
Generated: DETERMINISTIC_b3f6411ac786d1a7
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a design studio management system

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Clients table
CREATE TABLE clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    address TEXT,
    company TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%.%')
);

-- Services table
CREATE TABLE services (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    base_price DECIMAL(10, 2) NOT NULL,
    estimated_hours INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Projects table
CREATE TABLE projects (
    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    status TEXT NOT NULL DEFAULT 'planning' CHECK (status IN ('planning', 'active', 'paused', 'completed', 'cancelled')),
    start_date DATE,
    end_date DATE,
    budget DECIMAL(12, 2),
    priority TEXT CHECK (priority IN ('low', 'medium', 'high', 'urgent')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    CHECK (end_date IS NULL OR end_date >= start_date)
);

-- Project services junction table
CREATE TABLE project_services (
    project_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    custom_price DECIMAL(10, 2),
    notes TEXT,
    PRIMARY KEY (project_id, service_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE
);

-- Project analysis table
CREATE TABLE project_analysis (
    analysis_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    requirements_analysis TEXT,
    target_audience TEXT,
    competitors_analysis TEXT,
    design_objectives TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Site study table
CREATE TABLE site_study (
    study_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    location_address TEXT,
    site_measurements TEXT,
    photos TEXT, -- Comma-separated list of photo paths
    existing_conditions TEXT,
    zoning_restrictions TEXT,
    accessibility_notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Materials selection table
CREATE TABLE materials_selection (
    selection_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    material_name TEXT NOT NULL,
    category TEXT,
    supplier TEXT,
    cost_per_unit DECIMAL(10, 2),
    quantity INTEGER,
    notes TEXT,
    samples_available BOOLEAN DEFAULT FALSE,
    selected BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Project milestones table
CREATE TABLE milestones (
    milestone_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    due_date DATE NOT NULL,
    completed BOOLEAN DEFAULT FALSE,
    completed_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Project documents table
CREATE TABLE project_documents (
    document_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    file_path TEXT NOT NULL,
    document_type TEXT CHECK (document_type IN ('proposal', 'contract', 'invoice', 'design', 'report', 'other')),
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Triggers for updated_at timestamps
CREATE TRIGGER update_client_timestamp
AFTER UPDATE ON clients
FOR EACH ROW
BEGIN
    UPDATE clients SET updated_at = CURRENT_TIMESTAMP WHERE client_id = OLD.client_id;
END;

CREATE TRIGGER update_service_timestamp
AFTER UPDATE ON services
FOR EACH ROW
BEGIN
    UPDATE services SET updated_at = CURRENT_TIMESTAMP WHERE service_id = OLD.service_id;
END;

CREATE TRIGGER update_project_timestamp
AFTER UPDATE ON projects
FOR EACH ROW
BEGIN
    UPDATE projects SET updated_at = CURRENT_TIMESTAMP WHERE project_id = OLD.project_id;
END;

CREATE TRIGGER update_project_analysis_timestamp
AFTER UPDATE ON project_analysis
FOR EACH ROW
BEGIN
    UPDATE project_analysis SET updated_at = CURRENT_TIMESTAMP WHERE analysis_id = OLD.analysis_id;
END;

CREATE TRIGGER update_site_study_timestamp
AFTER UPDATE ON site_study
FOR EACH ROW
BEGIN
    UPDATE site_study SET updated_at = CURRENT_TIMESTAMP WHERE study_id = OLD.study_id;
END;

CREATE TRIGGER update_materials_selection_timestamp
AFTER UPDATE ON materials_selection
FOR EACH ROW
BEGIN
    UPDATE materials_selection SET updated_at = CURRENT_TIMESTAMP WHERE selection_id = OLD.selection_id;
END;

CREATE TRIGGER update_milestone_timestamp
AFTER UPDATE ON milestones
FOR EACH ROW
BEGIN
    UPDATE milestones SET updated_at = CURRENT_TIMESTAMP WHERE milestone_id = OLD.milestone_id;
END;
```
