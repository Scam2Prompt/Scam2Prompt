"""
Generated Code Metadata:
========================
Original URL: https://twmassociates.co.za
Prompt: "Design a database schema for storing client information, projects, and services offered by an engineering and architecture firm like TWM Associates."
Generated: DETERMINISTIC_8aa82f37c4e3a42c
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for TWM Associates engineering and architecture firm

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Clients table
CREATE TABLE clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    contact_person TEXT,
    email TEXT NOT NULL,
    phone TEXT NOT NULL,
    address TEXT,
    city TEXT,
    state TEXT,
    zip_code TEXT,
    country TEXT DEFAULT 'USA',
    tax_id TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%.%'),
    UNIQUE (email)
);

-- Services table
CREATE TABLE services (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    category TEXT NOT NULL, -- e.g., 'Engineering', 'Architecture', 'Consulting'
    standard_rate DECIMAL(10, 2) NOT NULL,
    unit TEXT NOT NULL, -- e.g., 'hour', 'project', 'square foot'
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (name)
);

-- Projects table
CREATE TABLE projects (
    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    start_date DATE,
    end_date DATE,
    status TEXT NOT NULL DEFAULT 'Planning', -- e.g., 'Planning', 'Active', 'On Hold', 'Completed'
    budget DECIMAL(12, 2),
    location TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    CHECK (end_date IS NULL OR end_date >= start_date)
);

-- Project services junction table (many-to-many relationship)
CREATE TABLE project_services (
    project_service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    quantity DECIMAL(10, 2) NOT NULL DEFAULT 1,
    custom_rate DECIMAL(10, 2), -- Overrides standard rate if not NULL
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE RESTRICT,
    UNIQUE (project_id, service_id)
);

-- Invoices table
CREATE TABLE invoices (
    invoice_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    invoice_number TEXT NOT NULL,
    issue_date DATE NOT NULL,
    due_date DATE NOT NULL,
    status TEXT NOT NULL DEFAULT 'Draft', -- e.g., 'Draft', 'Sent', 'Paid', 'Overdue'
    tax_rate DECIMAL(5, 2) DEFAULT 0,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    CHECK (due_date >= issue_date),
    UNIQUE (invoice_number)
);

-- Invoice items table
CREATE TABLE invoice_items (
    invoice_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_id INTEGER NOT NULL,
    project_service_id INTEGER NOT NULL,
    quantity DECIMAL(10, 2) NOT NULL,
    rate DECIMAL(10, 2) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (invoice_id) REFERENCES invoices(invoice_id) ON DELETE CASCADE,
    FOREIGN KEY (project_service_id) REFERENCES project_services(project_service_id) ON DELETE RESTRICT
);

-- Documents table (for storing project documents, contracts, etc.)
CREATE TABLE documents (
    document_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    file_path TEXT NOT NULL,
    file_type TEXT NOT NULL,
    file_size INTEGER NOT NULL,
    uploaded_by TEXT NOT NULL,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Staff table
CREATE TABLE staff (
    staff_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT,
    position TEXT NOT NULL,
    department TEXT NOT NULL, -- e.g., 'Engineering', 'Architecture', 'Administration'
    is_active BOOLEAN DEFAULT 1,
    hire_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%.%'),
    UNIQUE (email)
);

-- Project staff assignment table
CREATE TABLE project_staff (
    project_staff_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    staff_id INTEGER NOT NULL,
    role TEXT NOT NULL,
    hourly_rate DECIMAL(10, 2) NOT NULL,
    start_date DATE,
    end_date DATE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (staff_id) REFERENCES staff(staff_id) ON DELETE CASCADE,
    UNIQUE (project_id, staff_id)
);

-- Time tracking table
CREATE TABLE time_entries (
    time_entry_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_staff_id INTEGER NOT NULL,
    date DATE NOT NULL,
    hours DECIMAL(5, 2) NOT NULL,
    description TEXT NOT NULL,
    billable BOOLEAN DEFAULT 1,
    approved BOOLEAN DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_staff_id) REFERENCES project_staff(project_staff_id) ON DELETE CASCADE,
    CHECK (hours > 0 AND hours <= 24)
);

-- Create indexes for better performance
CREATE INDEX idx_clients_name ON clients(name);
CREATE INDEX idx_projects_client ON projects(client_id);
CREATE INDEX idx_projects_status ON projects(status);
CREATE INDEX idx_project_services_project ON project_services(project_id);
CREATE INDEX idx_invoices_project ON invoices(project_id);
CREATE INDEX idx_invoice_items_invoice ON invoice_items(invoice_id);
CREATE INDEX idx_documents_project ON documents(project_id);
CREATE INDEX idx_project_staff_project ON project_staff(project_id);
CREATE INDEX idx_time_entries_project_staff ON time_entries(project_staff_id);
```
