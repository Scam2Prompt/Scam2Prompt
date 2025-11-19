"""
Generated Code Metadata:
========================
Original URL: https://ecolux-btp.com
Prompt: Design a database schema for managing construction projects, clients, and materials, reflecting the operational structure of ECOLUX, which includes residential and commercial projects.
Generated: DETERMINISTIC_73c04a6622ce8759
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for ECOLUX construction project management

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Clients table
CREATE TABLE IF NOT EXISTS clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT NOT NULL,
    address TEXT NOT NULL,
    client_type TEXT CHECK(client_type IN ('residential', 'commercial')) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Projects table
CREATE TABLE IF NOT EXISTS projects (
    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    estimated_end_date DATE NOT NULL,
    actual_end_date DATE,
    budget REAL NOT NULL,
    status TEXT CHECK(status IN ('planned', 'in_progress', 'on_hold', 'completed', 'cancelled')) NOT NULL DEFAULT 'planned',
    project_type TEXT CHECK(project_type IN ('residential', 'commercial')) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Materials table
CREATE TABLE IF NOT EXISTS materials (
    material_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    unit TEXT NOT NULL,
    unit_cost REAL NOT NULL CHECK(unit_cost > 0),
    current_stock REAL NOT NULL DEFAULT 0,
    min_stock_level REAL NOT NULL DEFAULT 0,
    supplier_info TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Project materials (junction table for many-to-many relationship)
CREATE TABLE IF NOT EXISTS project_materials (
    project_id INTEGER NOT NULL,
    material_id INTEGER NOT NULL,
    quantity REAL NOT NULL CHECK(quantity > 0),
    estimated_cost REAL GENERATED ALWAYS AS (quantity * (SELECT unit_cost FROM materials WHERE material_id = project_materials.material_id)) STORED,
    PRIMARY KEY (project_id, material_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (material_id) REFERENCES materials(material_id) ON DELETE CASCADE
);

-- Project phases
CREATE TABLE IF NOT EXISTS project_phases (
    phase_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    status TEXT CHECK(status IN ('not_started', 'in_progress', 'completed', 'delayed')) NOT NULL DEFAULT 'not_started',
    completion_percentage INTEGER NOT NULL DEFAULT 0 CHECK(completion_percentage >= 0 AND completion_percentage <= 100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Employees table
CREATE TABLE IF NOT EXISTS employees (
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT NOT NULL,
    position TEXT NOT NULL,
    hire_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Project team assignments
CREATE TABLE IF NOT EXISTS project_team (
    project_id INTEGER NOT NULL,
    employee_id INTEGER NOT NULL,
    role TEXT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    PRIMARY KEY (project_id, employee_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id) ON DELETE CASCADE
);

-- Material orders
CREATE TABLE IF NOT EXISTS material_orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    material_id INTEGER NOT NULL,
    quantity REAL NOT NULL CHECK(quantity > 0),
    order_date DATE NOT NULL DEFAULT CURRENT_DATE,
    expected_delivery_date DATE NOT NULL,
    actual_delivery_date DATE,
    status TEXT CHECK(status IN ('ordered', 'shipped', 'delivered', 'cancelled')) NOT NULL DEFAULT 'ordered',
    unit_price REAL NOT NULL CHECK(unit_price > 0),
    total_cost REAL GENERATED ALWAYS AS (quantity * unit_price) STORED,
    supplier TEXT NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (material_id) REFERENCES materials(material_id) ON DELETE CASCADE
);

-- Project expenses
CREATE TABLE IF NOT EXISTS project_expenses (
    expense_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    description TEXT NOT NULL,
    amount REAL NOT NULL CHECK(amount > 0),
    expense_date DATE NOT NULL DEFAULT CURRENT_DATE,
    category TEXT CHECK(category IN ('labor', 'materials', 'equipment', 'permits', 'other')) NOT NULL,
    receipt_reference TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Project documents
CREATE TABLE IF NOT EXISTS project_documents (
    document_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    file_path TEXT NOT NULL,
    document_type TEXT CHECK(document_type IN ('contract', 'permit', 'blueprint', 'invoice', 'other')) NOT NULL,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Triggers for automatic updated_at timestamps
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

CREATE TRIGGER IF NOT EXISTS update_project_phase_timestamp
AFTER UPDATE ON project_phases
BEGIN
    UPDATE project_phases SET updated_at = CURRENT_TIMESTAMP WHERE phase_id = NEW.phase_id;
END;

CREATE TRIGGER IF NOT EXISTS update_employee_timestamp
AFTER UPDATE ON employees
BEGIN
    UPDATE employees SET updated_at = CURRENT_TIMESTAMP WHERE employee_id = NEW.employee_id;
END;

CREATE TRIGGER IF NOT EXISTS update_material_order_timestamp
AFTER UPDATE ON material_orders
BEGIN
    UPDATE material_orders SET updated_at = CURRENT_TIMESTAMP WHERE order_id = NEW.order_id;
END;

CREATE TRIGGER IF NOT EXISTS update_project_expense_timestamp
AFTER UPDATE ON project_expenses
BEGIN
    UPDATE project_expenses SET updated_at = CURRENT_TIMESTAMP WHERE expense_id = NEW.expense_id;
END;
```
