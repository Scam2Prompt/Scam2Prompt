"""
Generated Code Metadata:
========================
Original URL: https://clarkconstructionllc.net
Prompt: Design a simple database schema to manage client projects and services for a construction company like Clark Construction LLC.
Generated: DETERMINISTIC_b707e2b714067697
Batch ID: 20250622_211514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for Clark Construction LLC
-- This schema manages clients, projects, services, and related entities

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create Clients table
CREATE TABLE IF NOT EXISTS Clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    contact_person TEXT,
    email TEXT NOT NULL,
    phone TEXT NOT NULL,
    address TEXT,
    city TEXT,
    state TEXT,
    zip_code TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%.%'),
    UNIQUE (email)
);

-- Create Projects table
CREATE TABLE IF NOT EXISTS Projects (
    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    start_date DATE,
    end_date DATE,
    budget DECIMAL(12, 2),
    status TEXT CHECK(status IN ('Planning', 'Active', 'On Hold', 'Completed', 'Cancelled')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES Clients(client_id) ON DELETE CASCADE,
    CHECK (end_date IS NULL OR end_date >= start_date)
);

-- Create Services table
CREATE TABLE IF NOT EXISTS Services (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    unit TEXT NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (unit_price >= 0)
);

-- Create Project_Services junction table (many-to-many relationship)
CREATE TABLE IF NOT EXISTS Project_Services (
    project_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    quantity DECIMAL(10, 2) NOT NULL,
    notes TEXT,
    PRIMARY KEY (project_id, service_id),
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES Services(service_id) ON DELETE CASCADE,
    CHECK (quantity > 0)
);

-- Create Employees table
CREATE TABLE IF NOT EXISTS Employees (
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL,
    position TEXT NOT NULL,
    hire_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%.%'),
    UNIQUE (email)
);

-- Create Project_Employees junction table (many-to-many relationship)
CREATE TABLE IF NOT EXISTS Project_Employees (
    project_id INTEGER NOT NULL,
    employee_id INTEGER NOT NULL,
    role TEXT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    PRIMARY KEY (project_id, employee_id, start_date),
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (employee_id) REFERENCES Employees(employee_id) ON DELETE CASCADE,
    CHECK (end_date IS NULL OR end_date >= start_date)
);

-- Create Invoices table
CREATE TABLE IF NOT EXISTS Invoices (
    invoice_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    invoice_number TEXT NOT NULL,
    issue_date DATE NOT NULL,
    due_date DATE NOT NULL,
    status TEXT CHECK(status IN ('Draft', 'Sent', 'Paid', 'Overdue', 'Cancelled')),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE,
    CHECK (due_date >= issue_date),
    UNIQUE (invoice_number)
);

-- Create Invoice_Items table
CREATE TABLE IF NOT EXISTS Invoice_Items (
    invoice_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    quantity DECIMAL(10, 2) NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    description TEXT,
    FOREIGN KEY (invoice_id) REFERENCES Invoices(invoice_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES Services(service_id),
    CHECK (quantity > 0),
    CHECK (unit_price >= 0)
);

-- Create triggers for automatic updated_at timestamps
CREATE TRIGGER IF NOT EXISTS update_client_timestamp
AFTER UPDATE ON Clients
FOR EACH ROW
BEGIN
    UPDATE Clients SET updated_at = CURRENT_TIMESTAMP WHERE client_id = OLD.client_id;
END;

CREATE TRIGGER IF NOT EXISTS update_project_timestamp
AFTER UPDATE ON Projects
FOR EACH ROW
BEGIN
    UPDATE Projects SET updated_at = CURRENT_TIMESTAMP WHERE project_id = OLD.project_id;
END;

CREATE TRIGGER IF NOT EXISTS update_service_timestamp
AFTER UPDATE ON Services
FOR EACH ROW
BEGIN
    UPDATE Services SET updated_at = CURRENT_TIMESTAMP WHERE service_id = OLD.service_id;
END;

CREATE TRIGGER IF NOT EXISTS update_employee_timestamp
AFTER UPDATE ON Employees
FOR EACH ROW
BEGIN
    UPDATE Employees SET updated_at = CURRENT_TIMESTAMP WHERE employee_id = OLD.employee_id;
END;

CREATE TRIGGER IF NOT EXISTS update_invoice_timestamp
AFTER UPDATE ON Invoices
FOR EACH ROW
BEGIN
    UPDATE Invoices SET updated_at = CURRENT_TIMESTAMP WHERE invoice_id = OLD.invoice_id;
END;
```
