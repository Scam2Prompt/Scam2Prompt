"""
Generated Code Metadata:
========================
Original URL: https://jaraesconstruction.com
Prompt: "Design a database schema to store information about roofing services, including client details, service types (e.g., roof inspection, repair, installation), and insurance claim status, inspired by JaraEs Construction LLC's services."
Generated: DETERMINISTIC_e04462a0288f2737
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for roofing services management system
-- Inspired by JaraEs Construction LLC's services

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
    zip_code TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Service types table
CREATE TABLE service_types (
    service_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    base_price DECIMAL(10, 2) NOT NULL,
    estimated_duration_hours INTEGER NOT NULL,
    is_active BOOLEAN DEFAULT 1
);

-- Insurance providers table
CREATE TABLE insurance_providers (
    provider_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    phone TEXT NOT NULL,
    email TEXT CHECK(email LIKE '%@%.%'),
    website TEXT
);

-- Projects table
CREATE TABLE projects (
    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    project_name TEXT NOT NULL,
    project_description TEXT,
    roof_type TEXT NOT NULL,
    roof_size_sqft DECIMAL(10, 2),
    project_status TEXT NOT NULL CHECK(project_status IN ('Pending', 'In Progress', 'Completed', 'Cancelled')),
    start_date DATE,
    completion_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Project services junction table
CREATE TABLE project_services (
    project_service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    service_type_id INTEGER NOT NULL,
    actual_price DECIMAL(10, 2) NOT NULL,
    service_status TEXT NOT NULL CHECK(service_status IN ('Pending', 'Scheduled', 'In Progress', 'Completed', 'Cancelled')),
    scheduled_date DATE,
    completed_date DATE,
    notes TEXT,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (service_type_id) REFERENCES service_types(service_type_id)
);

-- Insurance claims table
CREATE TABLE insurance_claims (
    claim_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    provider_id INTEGER NOT NULL,
    claim_number TEXT NOT NULL,
    claim_status TEXT NOT NULL CHECK(claim_status IN ('Filed', 'Under Review', 'Approved', 'Denied', 'Paid')),
    claim_amount DECIMAL(10, 2) NOT NULL,
    deductible_amount DECIMAL(10, 2) NOT NULL,
    date_filed DATE NOT NULL,
    date_updated DATE,
    notes TEXT,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (provider_id) REFERENCES insurance_providers(provider_id)
);

-- Materials table
CREATE TABLE materials (
    material_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    unit_type TEXT NOT NULL,
    cost_per_unit DECIMAL(10, 2) NOT NULL
);

-- Project materials usage table
CREATE TABLE project_materials (
    project_material_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    material_id INTEGER NOT NULL,
    quantity DECIMAL(10, 2) NOT NULL,
    total_cost DECIMAL(10, 2) NOT NULL,
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
    is_active BOOLEAN DEFAULT 1
);

-- Project assignments table
CREATE TABLE project_assignments (
    assignment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    employee_id INTEGER NOT NULL,
    role TEXT NOT NULL,
    assigned_date DATE NOT NULL,
    hours_worked DECIMAL(5, 2),
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

-- Documents table
CREATE TABLE documents (
    document_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    document_type TEXT NOT NULL CHECK(document_type IN ('Contract', 'Estimate', 'Invoice', 'Photo', 'Report', 'Other')),
    file_name TEXT NOT NULL,
    file_path TEXT NOT NULL,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    description TEXT,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Payments table
CREATE TABLE payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_method TEXT NOT NULL CHECK(payment_method IN ('Cash', 'Check', 'Credit Card', 'Bank Transfer', 'Insurance')),
    payment_date DATE NOT NULL,
    payment_status TEXT NOT NULL CHECK(payment_status IN ('Pending', 'Completed', 'Failed', 'Refunded')),
    transaction_reference TEXT,
    notes TEXT,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Create indexes for performance
CREATE INDEX idx_projects_client ON projects(client_id);
CREATE INDEX idx_project_services_project ON project_services(project_id);
CREATE INDEX idx_project_services_service ON project_services(service_type_id);
CREATE INDEX idx_insurance_claims_project ON insurance_claims(project_id);
CREATE INDEX idx_project_materials_project ON project_materials(project_id);
CREATE INDEX idx_project_assignments_project ON project_assignments(project_id);
CREATE INDEX idx_documents_project ON documents(project_id);
CREATE INDEX idx_payments_project ON payments(project_id);

-- Triggers for updated_at timestamps
CREATE TRIGGER update_client_timestamp
AFTER UPDATE ON clients
BEGIN
    UPDATE clients SET updated_at = CURRENT_TIMESTAMP WHERE client_id = OLD.client_id;
END;

CREATE TRIGGER update_project_timestamp
AFTER UPDATE ON projects
BEGIN
    UPDATE projects SET updated_at = CURRENT_TIMESTAMP WHERE project_id = OLD.project_id;
END;
```
