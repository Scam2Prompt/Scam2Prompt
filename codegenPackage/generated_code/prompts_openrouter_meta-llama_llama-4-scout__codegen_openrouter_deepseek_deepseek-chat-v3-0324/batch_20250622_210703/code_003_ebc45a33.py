"""
Generated Code Metadata:
========================
Original URL: https://fenceguys4u.com
Prompt: "Design a database schema to store information about customers, projects, and services offered by a fence, deck, and pergola installation company, including fields for customer satisfaction ratings and project completion dates."
Generated: DETERMINISTIC_ebc45a33555c8a23
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a fence, deck, and pergola installation company

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Customers table
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE CHECK(email LIKE '%@%.%'),
    phone TEXT NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    zip_code TEXT NOT NULL,
    date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    notes TEXT
);

-- Services table
CREATE TABLE services (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    service_name TEXT NOT NULL UNIQUE,
    description TEXT,
    base_price DECIMAL(10, 2) NOT NULL CHECK(base_price >= 0),
    estimated_duration_hours INTEGER CHECK(estimated_duration_hours > 0)
);

-- Projects table
CREATE TABLE projects (
    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    project_name TEXT NOT NULL,
    description TEXT,
    start_date DATE,
    completion_date DATE,
    status TEXT NOT NULL CHECK(status IN ('Pending', 'In Progress', 'Completed', 'Cancelled')),
    total_cost DECIMAL(10, 2) CHECK(total_cost >= 0),
    satisfaction_rating INTEGER CHECK(satisfaction_rating BETWEEN 1 AND 5),
    feedback TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
);

-- Project services junction table (many-to-many relationship)
CREATE TABLE project_services (
    project_service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL CHECK(quantity > 0),
    custom_price DECIMAL(10, 2) CHECK(custom_price >= 0),
    notes TEXT,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(service_id),
    UNIQUE(project_id, service_id)
);

-- Materials table
CREATE TABLE materials (
    material_id INTEGER PRIMARY KEY AUTOINCREMENT,
    material_name TEXT NOT NULL UNIQUE,
    description TEXT,
    unit_price DECIMAL(10, 2) NOT NULL CHECK(unit_price >= 0),
    unit_type TEXT NOT NULL
);

-- Project materials junction table
CREATE TABLE project_materials (
    project_material_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    material_id INTEGER NOT NULL,
    quantity DECIMAL(10, 2) NOT NULL CHECK(quantity > 0),
    notes TEXT,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (material_id) REFERENCES materials(material_id)
);

-- Employees table
CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE CHECK(email LIKE '%@%.%'),
    phone TEXT NOT NULL,
    position TEXT NOT NULL,
    hire_date DATE NOT NULL,
    hourly_rate DECIMAL(10, 2) CHECK(hourly_rate >= 0)
);

-- Project assignments table
CREATE TABLE project_assignments (
    assignment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    employee_id INTEGER NOT NULL,
    hours_worked DECIMAL(5, 2) CHECK(hours_worked >= 0),
    role TEXT NOT NULL,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

-- Create indexes for better performance
CREATE INDEX idx_projects_customer ON projects(customer_id);
CREATE INDEX idx_project_services_project ON project_services(project_id);
CREATE INDEX idx_project_services_service ON project_services(service_id);
CREATE INDEX idx_project_materials_project ON project_materials(project_id);
CREATE INDEX idx_project_assignments_project ON project_assignments(project_id);
CREATE INDEX idx_project_assignments_employee ON project_assignments(employee_id);
```
