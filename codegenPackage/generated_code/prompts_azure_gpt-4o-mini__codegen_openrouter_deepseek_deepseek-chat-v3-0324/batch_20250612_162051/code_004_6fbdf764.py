"""
Generated Code Metadata:
========================
Original URL: https://aluivars.com
Prompt: Design a database schema for storing customer projects and service requests for a carpentry business like Aluivars, focusing on iron and aluminum work.
Generated: DETERMINISTIC_6fbdf7642a5e5474
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a carpentry business (e.g., Aluivars) specializing in iron and aluminum work

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Customers table
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE,
    phone TEXT NOT NULL,
    address TEXT,
    city TEXT,
    state TEXT,
    zip_code TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%.%' OR email IS NULL),
    CHECK (LENGTH(phone) >= 10)
);

-- Projects table
CREATE TABLE IF NOT EXISTS projects (
    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    project_name TEXT NOT NULL,
    description TEXT,
    project_type TEXT CHECK(project_type IN ('iron', 'aluminum', 'mixed', 'other')),
    start_date DATE,
    estimated_end_date DATE,
    actual_end_date DATE,
    status TEXT CHECK(status IN ('pending', 'in_progress', 'completed', 'delivered', 'cancelled')),
    total_cost DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    CHECK (estimated_end_date >= start_date OR estimated_end_date IS NULL),
    CHECK (actual_end_date >= start_date OR actual_end_date IS NULL)
);

-- Service requests table
CREATE TABLE IF NOT EXISTS service_requests (
    request_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    project_id INTEGER,
    request_type TEXT CHECK(request_type IN ('repair', 'maintenance', 'custom_fabrication', 'consultation')),
    description TEXT NOT NULL,
    urgency TEXT CHECK(urgency IN ('low', 'medium', 'high', 'emergency')),
    status TEXT CHECK(status IN ('open', 'assigned', 'in_progress', 'completed', 'cancelled')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE SET NULL
);

-- Materials table
CREATE TABLE IF NOT EXISTS materials (
    material_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    material_type TEXT CHECK(material_type IN ('iron', 'aluminum', 'other')),
    unit TEXT CHECK(unit IN ('kg', 'm', 'piece', 'sheet')),
    cost_per_unit DECIMAL(10, 2) NOT NULL,
    current_stock DECIMAL(10, 2) DEFAULT 0,
    supplier_info TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (cost_per_unit > 0),
    CHECK (current_stock >= 0)
);

-- Project materials (junction table)
CREATE TABLE IF NOT EXISTS project_materials (
    project_id INTEGER NOT NULL,
    material_id INTEGER NOT NULL,
    quantity DECIMAL(10, 2) NOT NULL,
    notes TEXT,
    PRIMARY KEY (project_id, material_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (material_id) REFERENCES materials(material_id) ON DELETE CASCADE,
    CHECK (quantity > 0)
);

-- Employees table
CREATE TABLE IF NOT EXISTS employees (
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT NOT NULL,
    specialization TEXT CHECK(specialization IN ('ironwork', 'aluminum', 'both', 'other')),
    hire_date DATE NOT NULL,
    active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%.%'),
    CHECK (LENGTH(phone) >= 10)
);

-- Project assignments (junction table)
CREATE TABLE IF NOT EXISTS project_assignments (
    project_id INTEGER NOT NULL,
    employee_id INTEGER NOT NULL,
    role TEXT CHECK(role IN ('lead', 'assistant', 'supervisor', 'other')),
    hours_worked DECIMAL(5, 2) DEFAULT 0,
    PRIMARY KEY (project_id, employee_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id) ON DELETE CASCADE,
    CHECK (hours_worked >= 0)
);

-- Project milestones
CREATE TABLE IF NOT EXISTS project_milestones (
    milestone_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    due_date DATE NOT NULL,
    completed_date DATE,
    status TEXT CHECK(status IN ('pending', 'in_progress', 'completed', 'delayed')),
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    CHECK (completed_date >= due_date OR completed_date IS NULL)
);

-- Project documents
CREATE TABLE IF NOT EXISTS project_documents (
    document_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    document_type TEXT CHECK(document_type IN ('design', 'contract', 'invoice', 'photo', 'other')),
    file_path TEXT NOT NULL,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    description TEXT,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Triggers for automatic updated_at timestamps
CREATE TRIGGER IF NOT EXISTS update_customer_timestamp
AFTER UPDATE ON customers
FOR EACH ROW
BEGIN
    UPDATE customers SET updated_at = CURRENT_TIMESTAMP WHERE customer_id = OLD.customer_id;
END;

CREATE TRIGGER IF NOT EXISTS update_project_timestamp
AFTER UPDATE ON projects
FOR EACH ROW
BEGIN
    UPDATE projects SET updated_at = CURRENT_TIMESTAMP WHERE project_id = OLD.project_id;
END;

CREATE TRIGGER IF NOT EXISTS update_service_request_timestamp
AFTER UPDATE ON service_requests
FOR EACH ROW
BEGIN
    UPDATE service_requests SET updated_at = CURRENT_TIMESTAMP WHERE request_id = OLD.request_id;
END;

CREATE TRIGGER IF NOT EXISTS update_material_timestamp
AFTER UPDATE ON materials
FOR EACH ROW
BEGIN
    UPDATE materials SET updated_at = CURRENT_TIMESTAMP WHERE material_id = OLD.material_id;
END;

CREATE TRIGGER IF NOT EXISTS update_employee_timestamp
AFTER UPDATE ON employees
FOR EACH ROW
BEGIN
    UPDATE employees SET updated_at = CURRENT_TIMESTAMP WHERE employee_id = OLD.employee_id;
END;
```
