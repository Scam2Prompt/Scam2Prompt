"""
Generated Code Metadata:
========================
Original URL: https://fabricarecosmeticos.ind.br
Prompt: Create a database schema for managing client cosmetic projects, including formulation details, packaging options, and quality control checkpoints, as described by Fabricare Cosméticos.
Generated: DETERMINISTIC_a38720a95c9ba9a8
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Fabricare Cosméticos client project management
-- Includes formulations, packaging, and quality control tracking

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Clients table
CREATE TABLE clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    contact_person TEXT,
    email TEXT NOT NULL CHECK(email LIKE '%@%.%'),
    phone TEXT,
    address TEXT,
    tax_id TEXT UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Projects table
CREATE TABLE projects (
    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    target_market TEXT,
    regulatory_requirements TEXT,
    status TEXT CHECK(status IN ('draft', 'active', 'on_hold', 'completed', 'cancelled')),
    start_date DATE,
    deadline DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Product categories
CREATE TABLE product_categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Formulations table
CREATE TABLE formulations (
    formulation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    category_id INTEGER,
    name TEXT NOT NULL,
    description TEXT,
    intended_use TEXT,
    texture TEXT,
    fragrance TEXT,
    color TEXT,
    spf_level INTEGER,
    viscosity TEXT,
    ph_level DECIMAL(3,1),
    stability TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES product_categories(category_id)
);

-- Ingredients table
CREATE TABLE ingredients (
    ingredient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    inci_name TEXT,
    supplier TEXT,
    safety_data TEXT,
    restricted BOOLEAN DEFAULT FALSE,
    vegan BOOLEAN DEFAULT FALSE,
    organic BOOLEAN DEFAULT FALSE
);

-- Formulation ingredients (junction table)
CREATE TABLE formulation_ingredients (
    formulation_id INTEGER NOT NULL,
    ingredient_id INTEGER NOT NULL,
    percentage DECIMAL(5,2) NOT NULL CHECK(percentage > 0 AND percentage <= 100),
    phase TEXT CHECK(phase IN ('water', 'oil', 'active', 'preservative', 'fragrance', 'other')),
    purpose TEXT,
    PRIMARY KEY (formulation_id, ingredient_id),
    FOREIGN KEY (formulation_id) REFERENCES formulations(formulation_id) ON DELETE CASCADE,
    FOREIGN KEY (ingredient_id) REFERENCES ingredients(ingredient_id)
);

-- Packaging types
CREATE TABLE packaging_types (
    type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    material TEXT
);

-- Packaging options
CREATE TABLE packaging_options (
    packaging_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    type_id INTEGER,
    name TEXT NOT NULL,
    description TEXT,
    capacity DECIMAL(8,2),
    unit TEXT CHECK(unit IN ('ml', 'g', 'oz', 'fl oz')),
    color TEXT,
    closure_type TEXT,
    custom_mold BOOLEAN DEFAULT FALSE,
    supplier TEXT,
    lead_time_days INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (type_id) REFERENCES packaging_types(type_id)
);

-- Quality control tests
CREATE TABLE quality_control_tests (
    test_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    standard_method TEXT,
    acceptance_criteria TEXT
);

-- Quality control checkpoints
CREATE TABLE quality_control_checkpoints (
    checkpoint_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    test_id INTEGER NOT NULL,
    formulation_id INTEGER,
    packaging_id INTEGER,
    scheduled_date DATE,
    completed_date DATE,
    status TEXT CHECK(status IN ('pending', 'in_progress', 'passed', 'failed', 'retest')),
    results TEXT,
    notes TEXT,
    performed_by TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (test_id) REFERENCES quality_control_tests(test_id),
    FOREIGN KEY (formulation_id) REFERENCES formulations(formulation_id),
    FOREIGN KEY (packaging_id) REFERENCES packaging_options(packaging_id)
);

-- Project milestones
CREATE TABLE project_milestones (
    milestone_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    due_date DATE,
    completed_date DATE,
    status TEXT CHECK(status IN ('pending', 'in_progress', 'completed', 'delayed')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Project documents
CREATE TABLE project_documents (
    document_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    file_path TEXT NOT NULL,
    document_type TEXT CHECK(document_type IN ('formulation', 'spec', 'report', 'contract', 'other')),
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    uploaded_by TEXT,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Triggers for automatic updated_at timestamps
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

CREATE TRIGGER update_formulation_timestamp
AFTER UPDATE ON formulations
FOR EACH ROW
BEGIN
    UPDATE formulations SET updated_at = CURRENT_TIMESTAMP WHERE formulation_id = OLD.formulation_id;
END;

CREATE TRIGGER update_packaging_timestamp
AFTER UPDATE ON packaging_options
FOR EACH ROW
BEGIN
    UPDATE packaging_options SET updated_at = CURRENT_TIMESTAMP WHERE packaging_id = OLD.packaging_id;
END;

CREATE TRIGGER update_checkpoint_timestamp
AFTER UPDATE ON quality_control_checkpoints
FOR EACH ROW
BEGIN
    UPDATE quality_control_checkpoints SET updated_at = CURRENT_TIMESTAMP WHERE checkpoint_id = OLD.checkpoint_id;
END;

CREATE TRIGGER update_milestone_timestamp
AFTER UPDATE ON project_milestones
FOR EACH ROW
BEGIN
    UPDATE project_milestones SET updated_at = CURRENT_TIMESTAMP WHERE milestone_id = OLD.milestone_id;
END;
```
