"""
Generated Code Metadata:
========================
Original URL: https://1marbleclassic.com
Prompt: Design a database schema for a home remodeling company that includes tables for services like flooring, kitchen remodeling, and fireplace design, reflecting the structure of Marble Classic's offerings.
Generated: DETERMINISTIC_f727ea031d8d43a0
Batch ID: 20250612_155531
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a home remodeling company (Marble Classic)

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Customers table
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    zip_code TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%.%')
);

-- Projects table
CREATE TABLE IF NOT EXISTS projects (
    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    project_name TEXT NOT NULL,
    description TEXT,
    start_date DATE,
    estimated_end_date DATE,
    actual_end_date DATE,
    status TEXT NOT NULL DEFAULT 'pending',
    budget REAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    CHECK (status IN ('pending', 'in_progress', 'completed', 'cancelled'))
);

-- Services table (parent table for all services)
CREATE TABLE IF NOT EXISTS services (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    service_name TEXT NOT NULL UNIQUE,
    description TEXT,
    base_price REAL NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Flooring services (specialization)
CREATE TABLE IF NOT EXISTS flooring_services (
    flooring_id INTEGER PRIMARY KEY AUTOINCREMENT,
    service_id INTEGER NOT NULL,
    flooring_type TEXT NOT NULL,
    material TEXT NOT NULL,
    area_coverage REAL NOT NULL,
    installation_type TEXT NOT NULL,
    FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE,
    CHECK (flooring_type IN ('hardwood', 'tile', 'laminate', 'vinyl', 'carpet')),
    CHECK (installation_type IN ('floating', 'glue_down', 'nail_down'))
);

-- Kitchen remodeling services (specialization)
CREATE TABLE IF NOT EXISTS kitchen_services (
    kitchen_id INTEGER PRIMARY KEY AUTOINCREMENT,
    service_id INTEGER NOT NULL,
    countertop_material TEXT NOT NULL,
    cabinet_style TEXT NOT NULL,
    backsplash_type TEXT,
    includes_appliances BOOLEAN DEFAULT FALSE,
    square_footage REAL NOT NULL,
    FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE
);

-- Fireplace design services (specialization)
CREATE TABLE IF NOT EXISTS fireplace_services (
    fireplace_id INTEGER PRIMARY KEY AUTOINCREMENT,
    service_id INTEGER NOT NULL,
    fireplace_type TEXT NOT NULL,
    material TEXT NOT NULL,
    heating_type TEXT NOT NULL,
    mantel_style TEXT,
    FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE,
    CHECK (fireplace_type IN ('wood_burning', 'gas', 'electric', 'ethanol')),
    CHECK (heating_type IN ('radiant', 'convection', 'fan_assisted'))
);

-- Project services (junction table for projects and services)
CREATE TABLE IF NOT EXISTS project_services (
    project_service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    quantity INTEGER DEFAULT 1,
    custom_price REAL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE
);

-- Materials inventory
CREATE TABLE IF NOT EXISTS materials (
    material_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    unit_type TEXT NOT NULL,
    cost_per_unit REAL NOT NULL,
    current_stock REAL NOT NULL DEFAULT 0,
    supplier TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (unit_type IN ('sq_ft', 'linear_ft', 'piece', 'box', 'gallon'))
);

-- Service materials (junction table for services and materials)
CREATE TABLE IF NOT EXISTS service_materials (
    service_material_id INTEGER PRIMARY KEY AUTOINCREMENT,
    service_id INTEGER NOT NULL,
    material_id INTEGER NOT NULL,
    quantity_required REAL NOT NULL,
    FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE,
    FOREIGN KEY (material_id) REFERENCES materials(material_id) ON DELETE CASCADE
);

-- Employees table
CREATE TABLE IF NOT EXISTS employees (
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT NOT NULL,
    hire_date DATE NOT NULL,
    position TEXT NOT NULL,
    hourly_rate REAL NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%.%')
);

-- Project assignments
CREATE TABLE IF NOT EXISTS project_assignments (
    assignment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    employee_id INTEGER NOT NULL,
    role TEXT NOT NULL,
    hours_worked REAL DEFAULT 0,
    start_date DATE,
    end_date DATE,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id) ON DELETE CASCADE
);

-- Triggers for updated_at timestamps
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

CREATE TRIGGER IF NOT EXISTS update_service_timestamp
AFTER UPDATE ON services
FOR EACH ROW
BEGIN
    UPDATE services SET updated_at = CURRENT_TIMESTAMP WHERE service_id = OLD.service_id;
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
