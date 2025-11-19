"""
Generated Code Metadata:
========================
Original URL: https://www.mooveweb.com
Prompt: Create a SQL database schema for managing client relationships and projects for a digital marketing agency like moOve, including tables for clients, projects, and services offered.
Generated: DETERMINISTIC_90b9b5e7e7fb380e
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for Digital Marketing Agency Client Relationship Management

-- Clients table to store client information
CREATE TABLE clients (
    client_id INT PRIMARY KEY AUTO_INCREMENT,
    company_name VARCHAR(100) NOT NULL,
    contact_person VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(20) NOT NULL,
    address TEXT,
    industry VARCHAR(50),
    date_added DATE NOT NULL DEFAULT CURRENT_DATE,
    status ENUM('active', 'inactive', 'prospective') NOT NULL DEFAULT 'prospective',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_email CHECK (email LIKE '%@%.%')
);

-- Services offered by the agency
CREATE TABLE services (
    service_id INT PRIMARY KEY AUTO_INCREMENT,
    service_name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    base_price DECIMAL(10, 2) NOT NULL,
    category ENUM('SEO', 'PPC', 'Social Media', 'Content', 'Web Design', 'Other') NOT NULL,
    active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Projects table to track client projects
CREATE TABLE projects (
    project_id INT PRIMARY KEY AUTO_INCREMENT,
    client_id INT NOT NULL,
    project_name VARCHAR(100) NOT NULL,
    description TEXT,
    start_date DATE,
    end_date DATE,
    budget DECIMAL(12, 2),
    status ENUM('planning', 'active', 'paused', 'completed', 'cancelled') NOT NULL DEFAULT 'planning',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    CONSTRAINT chk_dates CHECK (end_date IS NULL OR start_date <= end_date)
);

-- Junction table for projects and services (many-to-many relationship)
CREATE TABLE project_services (
    project_id INT NOT NULL,
    service_id INT NOT NULL,
    custom_price DECIMAL(10, 2),
    notes TEXT,
    assigned_to VARCHAR(100),
    status ENUM('not_started', 'in_progress', 'completed', 'delayed') NOT NULL DEFAULT 'not_started',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (project_id, service_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE
);

-- Invoices table for billing clients
CREATE TABLE invoices (
    invoice_id INT PRIMARY KEY AUTO_INCREMENT,
    project_id INT NOT NULL,
    invoice_number VARCHAR(20) NOT NULL UNIQUE,
    issue_date DATE NOT NULL,
    due_date DATE NOT NULL,
    amount DECIMAL(12, 2) NOT NULL,
    tax_amount DECIMAL(12, 2) NOT NULL DEFAULT 0,
    status ENUM('draft', 'sent', 'paid', 'overdue', 'cancelled') NOT NULL DEFAULT 'draft',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    CONSTRAINT chk_invoice_dates CHECK (due_date >= issue_date)
);

-- Payments received from clients
CREATE TABLE payments (
    payment_id INT PRIMARY KEY AUTO_INCREMENT,
    invoice_id INT NOT NULL,
    amount DECIMAL(12, 2) NOT NULL,
    payment_date DATE NOT NULL,
    payment_method ENUM('credit_card', 'bank_transfer', 'check', 'cash', 'other') NOT NULL,
    reference_number VARCHAR(50),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (invoice_id) REFERENCES invoices(invoice_id) ON DELETE CASCADE
);

-- Client communication log
CREATE TABLE communications (
    communication_id INT PRIMARY KEY AUTO_INCREMENT,
    client_id INT NOT NULL,
    project_id INT,
    contact_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    contact_method ENUM('email', 'phone', 'meeting', 'other') NOT NULL,
    subject VARCHAR(100) NOT NULL,
    notes TEXT NOT NULL,
    follow_up_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE SET NULL
);

-- Indexes for performance optimization
CREATE INDEX idx_client_status ON clients(status);
CREATE INDEX idx_project_status ON projects(status);
CREATE INDEX idx_invoice_status ON invoices(status);
CREATE INDEX idx_project_client ON projects(client_id);
CREATE INDEX idx_communication_client ON communications(client_id);
```
