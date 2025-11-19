"""
Generated Code Metadata:
========================
Original URL: https://westpoint-construction.co.uk
Prompt: "Design a database schema for a construction company's customer relationship management (CRM) system, including tables for clients, projects, and services offered, such as groundworks solutions and health and safety consulting."
Generated: DETERMINISTIC_6b66b303866727dd
Batch ID: 20250622_205955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Construction CRM System

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Clients table
CREATE TABLE clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT NOT NULL,
    contact_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT NOT NULL,
    address TEXT,
    city TEXT,
    postcode TEXT,
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    CHECK (email LIKE '%@%.%')
);

-- Services table
CREATE TABLE services (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    service_name TEXT NOT NULL UNIQUE,
    description TEXT,
    category TEXT NOT NULL,
    base_price DECIMAL(10, 2) NOT NULL,
    is_active BOOLEAN DEFAULT 1,
    CHECK (base_price >= 0)
);

-- Projects table
CREATE TABLE projects (
    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    project_name TEXT NOT NULL,
    description TEXT,
    start_date DATE,
    end_date DATE,
    status TEXT NOT NULL DEFAULT 'Pending',
    budget DECIMAL(10, 2),
    location TEXT,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    CHECK (end_date >= start_date OR end_date IS NULL),
    CHECK (budget >= 0 OR budget IS NULL)
);

-- Project services junction table
CREATE TABLE project_services (
    project_service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    quantity INTEGER DEFAULT 1,
    unit_price DECIMAL(10, 2) NOT NULL,
    notes TEXT,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(service_id),
    CHECK (quantity > 0),
    CHECK (unit_price >= 0)
);

-- Documents table
CREATE TABLE documents (
    document_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    document_name TEXT NOT NULL,
    document_type TEXT NOT NULL,
    file_path TEXT NOT NULL UNIQUE,
    upload_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Meetings table
CREATE TABLE meetings (
    meeting_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    project_id INTEGER,
    meeting_date DATETIME NOT NULL,
    location TEXT,
    notes TEXT,
    follow_up_required BOOLEAN DEFAULT 0,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE SET NULL
);

-- Indexes for performance
CREATE INDEX idx_clients_email ON clients(email);
CREATE INDEX idx_projects_client ON projects(client_id);
CREATE INDEX idx_projects_status ON projects(status);
CREATE INDEX idx_project_services_project ON project_services(project_id);
CREATE INDEX idx_project_services_service ON project_services(service_id);
CREATE INDEX idx_meetings_client ON meetings(client_id);
CREATE INDEX idx_meetings_project ON meetings(project_id);

-- Initial data for services
INSERT INTO services (service_name, description, category, base_price) VALUES
    ('Groundworks Solutions', 'Site preparation and foundation work', 'Construction', 5000.00),
    ('Health and Safety Consulting', 'Risk assessment and safety planning', 'Consulting', 1500.00),
    ('Project Management', 'Full project oversight and coordination', 'Management', 3000.00),
    ('Building Construction', 'Complete building services', 'Construction', 10000.00),
    ('Renovation Services', 'Building refurbishment and upgrades', 'Construction', 7500.00);
```
