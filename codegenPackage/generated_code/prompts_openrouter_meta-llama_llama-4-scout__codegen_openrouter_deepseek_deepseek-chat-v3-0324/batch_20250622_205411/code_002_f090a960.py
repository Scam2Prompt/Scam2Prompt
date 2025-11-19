"""
Generated Code Metadata:
========================
Original URL: https://clickmartltd.com
Prompt: "Generate a sample database schema for a construction company's customer relationship management (CRM) system, incorporating details such as client testimonials, project types, and service offerings like those of Clickmart Ltd."
Generated: DETERMINISTIC_f090a96083a718dd
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a construction company CRM system

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Clients table
CREATE TABLE clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT NOT NULL,
    address TEXT,
    company_name TEXT,
    date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    notes TEXT
);

-- Project types table
CREATE TABLE project_types (
    project_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Services table
CREATE TABLE services (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    base_price DECIMAL(10, 2)
);

-- Projects table
CREATE TABLE projects (
    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    project_type_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    start_date DATE,
    end_date DATE,
    budget DECIMAL(12, 2),
    status TEXT CHECK(status IN ('planned', 'in_progress', 'completed', 'cancelled')),
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (project_type_id) REFERENCES project_types(project_type_id)
);

-- Project services junction table
CREATE TABLE project_services (
    project_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    quantity INTEGER DEFAULT 1,
    custom_price DECIMAL(10, 2),
    PRIMARY KEY (project_id, service_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(service_id)
);

-- Testimonials table
CREATE TABLE testimonials (
    testimonial_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    project_id INTEGER NOT NULL,
    content TEXT NOT NULL,
    rating INTEGER CHECK(rating BETWEEN 1 AND 5),
    date_posted TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_approved BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (client_id) REFERENCES clients(client_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
);

-- Employees table
CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT NOT NULL,
    position TEXT,
    hire_date DATE
);

-- Project assignments
CREATE TABLE project_assignments (
    assignment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    employee_id INTEGER NOT NULL,
    role TEXT NOT NULL,
    start_date DATE,
    end_date DATE,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id) ON DELETE CASCADE
);

-- Documents table
CREATE TABLE documents (
    document_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    file_path TEXT NOT NULL,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    document_type TEXT,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Create indexes for better performance
CREATE INDEX idx_projects_client ON projects(client_id);
CREATE INDEX idx_projects_type ON projects(project_type_id);
CREATE INDEX idx_testimonials_client ON testimonials(client_id);
CREATE INDEX idx_testimonials_project ON testimonials(project_id);
CREATE INDEX idx_project_assignments_project ON project_assignments(project_id);
CREATE INDEX idx_project_assignments_employee ON project_assignments(employee_id);
CREATE INDEX idx_documents_project ON documents(project_id);
```
