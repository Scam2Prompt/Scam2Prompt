"""
Generated Code Metadata:
========================
Original URL: https://reyesaluminio.com
Prompt: "Design a database schema to store information about aluminum carpentry projects, including client details, project types, and materials used."
Generated: DETERMINISTIC_4d477323df56b5a2
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for aluminum carpentry projects management

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Clients table
CREATE TABLE clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE CHECK(email LIKE '%@%.%'),
    phone TEXT NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    postal_code TEXT NOT NULL,
    country TEXT NOT NULL DEFAULT 'USA',
    registration_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    CHECK(LENGTH(phone) >= 10)
);

-- Project types table
CREATE TABLE project_types (
    type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    average_duration_days INTEGER CHECK(average_duration_days > 0),
    complexity_level TEXT CHECK(complexity_level IN ('Low', 'Medium', 'High'))
);

-- Materials table
CREATE TABLE materials (
    material_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    unit TEXT NOT NULL CHECK(unit IN ('m', 'ft', 'kg', 'lb', 'piece')),
    cost_per_unit DECIMAL(10, 2) NOT NULL CHECK(cost_per_unit > 0),
    supplier TEXT,
    stock_quantity DECIMAL(10, 2) NOT NULL DEFAULT 0 CHECK(stock_quantity >= 0)
);

-- Projects table
CREATE TABLE projects (
    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    type_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    estimated_end_date DATE,
    actual_end_date DATE,
    status TEXT NOT NULL CHECK(status IN ('Planned', 'In Progress', 'Completed', 'Cancelled')),
    total_cost DECIMAL(12, 2) CHECK(total_cost >= 0),
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE RESTRICT,
    FOREIGN KEY (type_id) REFERENCES project_types(type_id) ON DELETE RESTRICT,
    CHECK(estimated_end_date >= start_date),
    CHECK(actual_end_date IS NULL OR actual_end_date >= start_date)
);

-- Project materials junction table
CREATE TABLE project_materials (
    project_id INTEGER NOT NULL,
    material_id INTEGER NOT NULL,
    quantity DECIMAL(10, 2) NOT NULL CHECK(quantity > 0),
    notes TEXT,
    PRIMARY KEY (project_id, material_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (material_id) REFERENCES materials(material_id) ON DELETE RESTRICT
);

-- Project milestones table
CREATE TABLE milestones (
    milestone_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    due_date DATE NOT NULL,
    completion_date DATE,
    status TEXT NOT NULL CHECK(status IN ('Pending', 'In Progress', 'Completed', 'Delayed')),
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    CHECK(completion_date IS NULL OR completion_date >= due_date)
);

-- Project documents table
CREATE TABLE project_documents (
    document_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    document_name TEXT NOT NULL,
    document_type TEXT NOT NULL CHECK(document_type IN ('Blueprint', 'Contract', 'Invoice', 'Photo', 'Other')),
    file_path TEXT NOT NULL UNIQUE,
    upload_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    description TEXT,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Payments table
CREATE TABLE payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    amount DECIMAL(10, 2) NOT NULL CHECK(amount > 0),
    payment_date DATE NOT NULL,
    payment_method TEXT NOT NULL CHECK(payment_method IN ('Cash', 'Check', 'Credit Card', 'Bank Transfer')),
    reference_number TEXT,
    notes TEXT,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Create indexes for performance
CREATE INDEX idx_projects_client ON projects(client_id);
CREATE INDEX idx_projects_type ON projects(type_id);
CREATE INDEX idx_project_materials_project ON project_materials(project_id);
CREATE INDEX idx_project_materials_material ON project_materials(material_id);
CREATE INDEX idx_milestones_project ON milestones(project_id);
CREATE INDEX idx_documents_project ON project_documents(project_id);
CREATE INDEX idx_payments_project ON payments(project_id);
```
