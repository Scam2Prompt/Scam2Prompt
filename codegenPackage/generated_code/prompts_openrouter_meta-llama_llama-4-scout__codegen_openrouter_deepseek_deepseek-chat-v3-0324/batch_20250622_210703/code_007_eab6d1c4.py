"""
Generated Code Metadata:
========================
Original URL: https://citygardenmexico.com.mx
Prompt: "Design a database schema to store information about gardening projects, clients, and services offered by City Garden Mexico."
Generated: DETERMINISTIC_eab6d1c4d29078e7
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for City Garden Mexico gardening projects

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Clients table
CREATE TABLE clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL CHECK(email LIKE '%@%.%'),
    phone TEXT NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    postal_code TEXT NOT NULL,
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    notes TEXT
);

-- Services table
CREATE TABLE services (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT NOT NULL,
    base_price DECIMAL(10, 2) NOT NULL CHECK(base_price >= 0),
    duration_hours DECIMAL(5, 2) NOT NULL CHECK(duration_hours > 0),
    is_active BOOLEAN DEFAULT 1
);

-- Projects table
CREATE TABLE projects (
    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    start_date DATE,
    end_date DATE,
    status TEXT NOT NULL CHECK(status IN ('planned', 'in_progress', 'completed', 'cancelled')),
    total_budget DECIMAL(12, 2) CHECK(total_budget >= 0),
    location_address TEXT NOT NULL,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Project services junction table
CREATE TABLE project_services (
    project_service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL CHECK(quantity > 0),
    custom_price DECIMAL(10, 2) CHECK(custom_price >= 0),
    notes TEXT,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(service_id),
    UNIQUE (project_id, service_id)
);

-- Payments table
CREATE TABLE payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    amount DECIMAL(12, 2) NOT NULL CHECK(amount > 0),
    payment_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    payment_method TEXT NOT NULL CHECK(payment_method IN ('cash', 'credit_card', 'bank_transfer', 'check')),
    transaction_reference TEXT,
    notes TEXT,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Project notes table
CREATE TABLE project_notes (
    note_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    note_text TEXT NOT NULL,
    created_by TEXT NOT NULL,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Create indexes for better performance
CREATE INDEX idx_clients_email ON clients(email);
CREATE INDEX idx_projects_client ON projects(client_id);
CREATE INDEX idx_projects_status ON projects(status);
CREATE INDEX idx_project_services_project ON project_services(project_id);
CREATE INDEX idx_project_services_service ON project_services(service_id);
CREATE INDEX idx_payments_project ON payments(project_id);
CREATE INDEX idx_project_notes_project ON project_notes(project_id);
```
