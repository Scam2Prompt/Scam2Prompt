"""
Generated Code Metadata:
========================
Original URL: https://cristalesgraf.com
Prompt: Create a database schema to store customer inquiries and project details for a company specializing in processed glass and aluminum solutions, like CristalesGraf.
Generated: DETERMINISTIC_7d0918fb3d4da631
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for CristalesGraf customer inquiries and project management

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Customers table to store customer information
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT NOT NULL,
    company TEXT,
    address TEXT,
    city TEXT,
    state TEXT,
    postal_code TEXT,
    country TEXT DEFAULT 'Mexico',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%.%')
);

-- Inquiry categories table
CREATE TABLE IF NOT EXISTS inquiry_categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Inquiry status table
CREATE TABLE IF NOT EXISTS inquiry_status (
    status_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Customer inquiries table
CREATE TABLE IF NOT EXISTS inquiries (
    inquiry_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    status_id INTEGER NOT NULL DEFAULT 1,
    subject TEXT NOT NULL,
    message TEXT NOT NULL,
    priority INTEGER DEFAULT 2 CHECK (priority BETWEEN 1 AND 3),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES inquiry_categories(category_id),
    FOREIGN KEY (status_id) REFERENCES inquiry_status(status_id)
);

-- Project types table
CREATE TABLE IF NOT EXISTS project_types (
    type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Project status table
CREATE TABLE IF NOT EXISTS project_status (
    status_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Projects table
CREATE TABLE IF NOT EXISTS projects (
    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
    inquiry_id INTEGER,
    customer_id INTEGER NOT NULL,
    type_id INTEGER NOT NULL,
    status_id INTEGER NOT NULL DEFAULT 1,
    name TEXT NOT NULL,
    description TEXT,
    start_date DATE,
    estimated_end_date DATE,
    actual_end_date DATE,
    budget REAL CHECK (budget >= 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (inquiry_id) REFERENCES inquiries(inquiry_id) ON DELETE SET NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (type_id) REFERENCES project_types(type_id),
    FOREIGN KEY (status_id) REFERENCES project_status(status_id),
    CHECK (actual_end_date IS NULL OR actual_end_date >= start_date),
    CHECK (estimated_end_date >= start_date)
);

-- Materials table
CREATE TABLE IF NOT EXISTS materials (
    material_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    unit_price REAL NOT NULL CHECK (unit_price >= 0),
    unit_of_measure TEXT NOT NULL DEFAULT 'm2'
);

-- Project materials (junction table)
CREATE TABLE IF NOT EXISTS project_materials (
    project_id INTEGER NOT NULL,
    material_id INTEGER NOT NULL,
    quantity REAL NOT NULL CHECK (quantity > 0),
    notes TEXT,
    PRIMARY KEY (project_id, material_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (material_id) REFERENCES materials(material_id)
);

-- Project documents table
CREATE TABLE IF NOT EXISTS project_documents (
    document_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    file_path TEXT NOT NULL,
    file_type TEXT NOT NULL,
    file_size INTEGER NOT NULL CHECK (file_size > 0),
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Triggers for automatic updated_at timestamps
CREATE TRIGGER IF NOT EXISTS update_customer_timestamp
AFTER UPDATE ON customers
FOR EACH ROW
BEGIN
    UPDATE customers SET updated_at = CURRENT_TIMESTAMP WHERE customer_id = OLD.customer_id;
END;

CREATE TRIGGER IF NOT EXISTS update_inquiry_timestamp
AFTER UPDATE ON inquiries
FOR EACH ROW
BEGIN
    UPDATE inquiries SET updated_at = CURRENT_TIMESTAMP WHERE inquiry_id = OLD.inquiry_id;
END;

CREATE TRIGGER IF NOT EXISTS update_project_timestamp
AFTER UPDATE ON projects
FOR EACH ROW
BEGIN
    UPDATE projects SET updated_at = CURRENT_TIMESTAMP WHERE project_id = OLD.project_id;
END;

-- Initial data for lookup tables
INSERT OR IGNORE INTO inquiry_categories (name, description) VALUES 
    ('General Inquiry', 'General questions about products or services'),
    ('Quote Request', 'Request for a price quote'),
    ('Technical Support', 'Technical questions or issues'),
    ('Custom Project', 'Inquiry about a custom project');

INSERT OR IGNORE INTO inquiry_status (name, description) VALUES 
    ('New', 'New inquiry, not yet processed'),
    ('In Progress', 'Inquiry is being processed'),
    ('Waiting for Customer', 'Waiting for customer response'),
    ('Completed', 'Inquiry has been resolved'),
    ('Cancelled', 'Inquiry was cancelled');

INSERT OR IGNORE INTO project_types (name, description) VALUES 
    ('Glass Installation', 'Standard glass installation project'),
    ('Aluminum Structure', 'Aluminum framing and structure project'),
    ('Custom Glass Design', 'Custom glass design and fabrication'),
    ('Maintenance', 'Maintenance or repair project');

INSERT OR IGNORE INTO project_status (name, description) VALUES 
    ('Planning', 'Project is in planning phase'),
    ('In Progress', 'Project is currently being worked on'),
    ('On Hold', 'Project is temporarily on hold'),
    ('Completed', 'Project has been completed'),
    ('Cancelled', 'Project was cancelled');

INSERT OR IGNORE INTO materials (name, description, unit_price, unit_of_measure) VALUES
    ('Clear Float Glass', 'Standard clear float glass', 150.00, 'm2'),
    ('Tempered Glass', 'Safety tempered glass', 250.00, 'm2'),
    ('Laminated Glass', 'Safety laminated glass', 300.00, 'm2'),
    ('Aluminum Profile 6063', 'Standard aluminum profile', 120.00, 'meter'),
    ('Aluminum Profile 6061', 'Structural aluminum profile', 150.00, 'meter');
```
