"""
Generated Code Metadata:
========================
Original URL: https://twmassociates.co.za
Prompt: Create a database schema in SQL to manage client information, project details, and consulting costs for an architectural firm like TWM Associates.
Generated: DETERMINISTIC_06c794114f408b2d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for TWM Associates architectural firm
-- Manages clients, projects, and consulting costs

-- Create database (commented out as this is typically environment-specific)
-- CREATE DATABASE twm_associates;
-- USE twm_associates;

-- Clients table stores information about architectural firm's clients
CREATE TABLE clients (
    client_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    contact_person VARCHAR(100),
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    address VARCHAR(255),
    city VARCHAR(50),
    state VARCHAR(50),
    zip_code VARCHAR(20),
    country VARCHAR(50) DEFAULT 'USA',
    tax_id VARCHAR(50),
    date_added DATETIME DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    CONSTRAINT email_unique UNIQUE (email),
    CONSTRAINT phone_unique UNIQUE (phone)
) ENGINE=InnoDB;

-- Project types table (categorization of projects)
CREATE TABLE project_types (
    type_id INT PRIMARY KEY AUTO_INCREMENT,
    type_name VARCHAR(50) NOT NULL,
    description TEXT,
    CONSTRAINT type_name_unique UNIQUE (type_name)
) ENGINE=InnoDB;

-- Projects table stores information about architectural projects
CREATE TABLE projects (
    project_id INT PRIMARY KEY AUTO_INCREMENT,
    client_id INT NOT NULL,
    type_id INT,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    start_date DATE,
    estimated_end_date DATE,
    actual_end_date DATE,
    status ENUM('planned', 'active', 'on-hold', 'completed', 'cancelled') DEFAULT 'planned',
    budget DECIMAL(15, 2),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (type_id) REFERENCES project_types(type_id) ON DELETE SET NULL
) ENGINE=InnoDB;

-- Team members (architects, designers, etc.)
CREATE TABLE team_members (
    member_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    role VARCHAR(50) NOT NULL,
    hourly_rate DECIMAL(10, 2) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    hire_date DATE NOT NULL,
    termination_date DATE,
    CONSTRAINT team_email_unique UNIQUE (email)
) ENGINE=InnoDB;

-- Project assignments (which team members work on which projects)
CREATE TABLE project_assignments (
    assignment_id INT PRIMARY KEY AUTO_INCREMENT,
    project_id INT NOT NULL,
    member_id INT NOT NULL,
    role VARCHAR(50) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    hourly_rate DECIMAL(10, 2) NOT NULL,
    notes TEXT,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (member_id) REFERENCES team_members(member_id) ON DELETE CASCADE,
    CONSTRAINT unique_assignment UNIQUE (project_id, member_id, start_date)
) ENGINE=InnoDB;

-- Time tracking for billable hours
CREATE TABLE time_entries (
    entry_id INT PRIMARY KEY AUTO_INCREMENT,
    assignment_id INT NOT NULL,
    entry_date DATE NOT NULL,
    hours DECIMAL(5, 2) NOT NULL,
    description TEXT,
    is_billable BOOLEAN DEFAULT TRUE,
    billing_status ENUM('unbilled', 'billed', 'paid') DEFAULT 'unbilled',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (assignment_id) REFERENCES project_assignments(assignment_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Expenses related to projects
CREATE TABLE project_expenses (
    expense_id INT PRIMARY KEY AUTO_INCREMENT,
    project_id INT NOT NULL,
    category VARCHAR(50) NOT NULL,
    description TEXT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    expense_date DATE NOT NULL,
    receipt_reference VARCHAR(100),
    is_billable BOOLEAN DEFAULT TRUE,
    billing_status ENUM('unbilled', 'billed', 'paid') DEFAULT 'unbilled',
    added_by INT,
    added_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (added_by) REFERENCES team_members(member_id) ON DELETE SET NULL
) ENGINE=InnoDB;

-- Invoices sent to clients
CREATE TABLE invoices (
    invoice_id INT PRIMARY KEY AUTO_INCREMENT,
    project_id INT NOT NULL,
    invoice_number VARCHAR(50) NOT NULL,
    issue_date DATE NOT NULL,
    due_date DATE NOT NULL,
    status ENUM('draft', 'sent', 'paid', 'overdue', 'cancelled') DEFAULT 'draft',
    subtotal DECIMAL(12, 2) NOT NULL,
    tax_amount DECIMAL(12, 2) DEFAULT 0,
    total_amount DECIMAL(12, 2) NOT NULL,
    notes TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    CONSTRAINT invoice_number_unique UNIQUE (invoice_number)
) ENGINE=InnoDB;

-- Invoice line items (connects time entries and expenses to invoices)
CREATE TABLE invoice_items (
    item_id INT PRIMARY KEY AUTO_INCREMENT,
    invoice_id INT NOT NULL,
    item_type ENUM('time', 'expense') NOT NULL,
    time_entry_id INT,
    expense_id INT,
    description TEXT NOT NULL,
    quantity DECIMAL(10, 2) NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    amount DECIMAL(12, 2) NOT NULL,
    FOREIGN KEY (invoice_id) REFERENCES invoices(invoice_id) ON DELETE CASCADE,
    FOREIGN KEY (time_entry_id) REFERENCES time_entries(entry_id) ON DELETE SET NULL,
    FOREIGN KEY (expense_id) REFERENCES project_expenses(expense_id) ON DELETE SET NULL,
    CONSTRAINT chk_item_reference CHECK (
        (item_type = 'time' AND time_entry_id IS NOT NULL) OR
        (item_type = 'expense' AND expense_id IS NOT NULL)
    )
) ENGINE=InnoDB;

-- Payments received from clients
CREATE TABLE payments (
    payment_id INT PRIMARY KEY AUTO_INCREMENT,
    invoice_id INT NOT NULL,
    amount DECIMAL(12, 2) NOT NULL,
    payment_date DATE NOT NULL,
    payment_method ENUM('check', 'credit_card', 'bank_transfer', 'cash') NOT NULL,
    reference_number VARCHAR(50),
    notes TEXT,
    recorded_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    recorded_by INT,
    FOREIGN KEY (invoice_id) REFERENCES invoices(invoice_id) ON DELETE CASCADE,
    FOREIGN KEY (recorded_by) REFERENCES team_members(member_id) ON DELETE SET NULL
) ENGINE=InnoDB;

-- Document storage for projects
CREATE TABLE project_documents (
    document_id INT PRIMARY KEY AUTO_INCREMENT,
    project_id INT NOT NULL,
    document_name VARCHAR(255) NOT NULL,
    document_type VARCHAR(50) NOT NULL,
    file_path VARCHAR(255) NOT NULL,
    file_size INT NOT NULL,
    uploaded_by INT NOT NULL,
    upload_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    description TEXT,
    version VARCHAR(20),
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (uploaded_by) REFERENCES team_members(member_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Create indexes for performance
CREATE INDEX idx_projects_client ON projects(client_id);
CREATE INDEX idx_projects_status ON projects(status);
CREATE INDEX idx_time_entries_assignment ON time_entries(assignment_id);
CREATE INDEX idx_time_entries_billing_status ON time_entries(billing_status);
CREATE INDEX idx_invoices_project ON invoices(project_id);
CREATE INDEX idx_invoices_status ON invoices(status);
```
