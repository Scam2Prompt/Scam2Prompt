"""
Generated Code Metadata:
========================
Original URL: https://uaeinterior.com
Prompt: Design a database schema for storing information about interior design projects, including project details, client information, and space planning, based on the services provided by Amazing Interior.
Generated: DETERMINISTIC_04782efdd28b7ed1
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Amazing Interior design projects

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Clients table
CREATE TABLE IF NOT EXISTS clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT NOT NULL,
    address TEXT,
    city TEXT,
    state TEXT,
    zip_code TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%.%')
);

-- Project types table
CREATE TABLE IF NOT EXISTS project_types (
    type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Projects table
CREATE TABLE IF NOT EXISTS projects (
    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    type_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    budget REAL,
    start_date DATE,
    estimated_end_date DATE,
    actual_end_date DATE,
    status TEXT NOT NULL DEFAULT 'planning' CHECK (status IN ('planning', 'in_progress', 'on_hold', 'completed', 'cancelled')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (type_id) REFERENCES project_types(type_id)
);

-- Spaces table
CREATE TABLE IF NOT EXISTS spaces (
    space_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    square_footage REAL NOT NULL,
    purpose TEXT,
    notes TEXT,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Furniture categories table
CREATE TABLE IF NOT EXISTS furniture_categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Furniture items table
CREATE TABLE IF NOT EXISTS furniture_items (
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    dimensions TEXT,
    material TEXT,
    color TEXT,
    FOREIGN KEY (category_id) REFERENCES furniture_categories(category_id)
);

-- Space furniture assignments
CREATE TABLE IF NOT EXISTS space_furniture (
    assignment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    space_id INTEGER NOT NULL,
    item_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 1,
    placement_notes TEXT,
    FOREIGN KEY (space_id) REFERENCES spaces(space_id) ON DELETE CASCADE,
    FOREIGN KEY (item_id) REFERENCES furniture_items(item_id)
);

-- Design styles table
CREATE TABLE IF NOT EXISTS design_styles (
    style_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Project styles mapping
CREATE TABLE IF NOT EXISTS project_styles (
    project_id INTEGER NOT NULL,
    style_id INTEGER NOT NULL,
    PRIMARY KEY (project_id, style_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (style_id) REFERENCES design_styles(style_id)
);

-- Materials table
CREATE TABLE IF NOT EXISTS materials (
    material_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    type TEXT NOT NULL,
    description TEXT,
    cost_per_unit REAL,
    unit_type TEXT
);

-- Project materials mapping
CREATE TABLE IF NOT EXISTS project_materials (
    project_id INTEGER NOT NULL,
    material_id INTEGER NOT NULL,
    quantity REAL NOT NULL,
    notes TEXT,
    PRIMARY KEY (project_id, material_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (material_id) REFERENCES materials(material_id)
);

-- Project notes table
CREATE TABLE IF NOT EXISTS project_notes (
    note_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Project documents table
CREATE TABLE IF NOT EXISTS project_documents (
    document_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    file_path TEXT NOT NULL,
    document_type TEXT NOT NULL,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Create indexes for performance
CREATE INDEX IF NOT EXISTS idx_projects_client ON projects(client_id);
CREATE INDEX IF NOT EXISTS idx_spaces_project ON spaces(project_id);
CREATE INDEX IF NOT EXISTS idx_space_furniture_space ON space_furniture(space_id);
CREATE INDEX IF NOT EXISTS idx_space_furniture_item ON space_furniture(item_id);
CREATE INDEX IF NOT EXISTS idx_project_styles_project ON project_styles(project_id);
CREATE INDEX IF NOT EXISTS idx_project_materials_project ON project_materials(project_id);

-- Triggers for updated_at timestamps
CREATE TRIGGER IF NOT EXISTS update_client_timestamp
AFTER UPDATE ON clients
FOR EACH ROW
BEGIN
    UPDATE clients SET updated_at = CURRENT_TIMESTAMP WHERE client_id = OLD.client_id;
END;

CREATE TRIGGER IF NOT EXISTS update_project_timestamp
AFTER UPDATE ON projects
FOR EACH ROW
BEGIN
    UPDATE projects SET updated_at = CURRENT_TIMESTAMP WHERE project_id = OLD.project_id;
END;

CREATE TRIGGER IF NOT EXISTS update_project_note_timestamp
AFTER UPDATE ON project_notes
FOR EACH ROW
BEGIN
    UPDATE project_notes SET updated_at = CURRENT_TIMESTAMP WHERE note_id = OLD.note_id;
END;
```
