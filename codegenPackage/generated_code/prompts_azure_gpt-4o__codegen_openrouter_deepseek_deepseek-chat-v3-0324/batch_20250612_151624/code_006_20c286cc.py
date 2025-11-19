"""
Generated Code Metadata:
========================
Original URL: https://unitedcabinetry.com.au
Prompt: Create a database schema in SQL to store cabinetry project details, including design specifications, trades coordination, and after-sales support, inspired by United Cabinetry's workflow.
Generated: DETERMINISTIC_20c286cc776ecfa9
Batch ID: 20250612_151624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for cabinetry project management system
-- Inspired by United Cabinetry's workflow

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create tables

-- Clients table
CREATE TABLE clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT NOT NULL,
    address TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Projects table
CREATE TABLE projects (
    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    project_name TEXT NOT NULL,
    description TEXT,
    start_date DATE,
    estimated_completion_date DATE,
    actual_completion_date DATE,
    status TEXT CHECK(status IN ('pending', 'in_progress', 'completed', 'delivered', 'warranty')) DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Design specifications table
CREATE TABLE design_specifications (
    spec_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    room_type TEXT NOT NULL,
    cabinet_style TEXT NOT NULL,
    material TEXT NOT NULL,
    color TEXT NOT NULL,
    hardware_type TEXT,
    countertop_material TEXT,
    drawings_url TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Trades coordination table
CREATE TABLE trades (
    trade_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    trade_type TEXT NOT NULL CHECK(trade_type IN ('carpentry', 'electrical', 'plumbing', 'painting', 'countertop', 'other')),
    contractor_name TEXT NOT NULL,
    contact_info TEXT NOT NULL,
    scheduled_date DATE,
    completed_date DATE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Project milestones table
CREATE TABLE milestones (
    milestone_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    target_date DATE NOT NULL,
    completed_date DATE,
    status TEXT CHECK(status IN ('pending', 'in_progress', 'completed', 'delayed')) DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- After-sales support table
CREATE TABLE after_sales_support (
    support_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    issue_type TEXT NOT NULL CHECK(issue_type IN ('warranty', 'repair', 'adjustment', 'other')),
    description TEXT NOT NULL,
    reported_date DATE NOT NULL DEFAULT CURRENT_DATE,
    resolved_date DATE,
    status TEXT CHECK(status IN ('open', 'in_progress', 'resolved', 'closed')) DEFAULT 'open',
    resolution_notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Project documents table
CREATE TABLE project_documents (
    document_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    document_type TEXT NOT NULL CHECK(document_type IN ('contract', 'invoice', 'design', 'permit', 'other')),
    file_name TEXT NOT NULL,
    file_path TEXT NOT NULL,
    upload_date DATE NOT NULL DEFAULT CURRENT_DATE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Create indexes for better performance
CREATE INDEX idx_projects_client_id ON projects(client_id);
CREATE INDEX idx_design_specs_project_id ON design_specifications(project_id);
CREATE INDEX idx_trades_project_id ON trades(project_id);
CREATE INDEX idx_milestones_project_id ON milestones(project_id);
CREATE INDEX idx_support_project_id ON after_sales_support(project_id);
CREATE INDEX idx_documents_project_id ON project_documents(project_id);

-- Create triggers for automatic updated_at timestamps
CREATE TRIGGER update_client_timestamp
AFTER UPDATE ON clients
FOR EACH ROW
BEGIN
    UPDATE clients SET updated_at = CURRENT_TIMESTAMP WHERE client_id = OLD.client_id;
END;

CREATE TRIGGER update_project_timestamp
AFTER UPDATE ON projects
FOR EACH ROW
BEGIN
    UPDATE projects SET updated_at = CURRENT_TIMESTAMP WHERE project_id = OLD.project_id;
END;

CREATE TRIGGER update_design_spec_timestamp
AFTER UPDATE ON design_specifications
FOR EACH ROW
BEGIN
    UPDATE design_specifications SET updated_at = CURRENT_TIMESTAMP WHERE spec_id = OLD.spec_id;
END;

CREATE TRIGGER update_trade_timestamp
AFTER UPDATE ON trades
FOR EACH ROW
BEGIN
    UPDATE trades SET updated_at = CURRENT_TIMESTAMP WHERE trade_id = OLD.trade_id;
END;

CREATE TRIGGER update_milestone_timestamp
AFTER UPDATE ON milestones
FOR EACH ROW
BEGIN
    UPDATE milestones SET updated_at = CURRENT_TIMESTAMP WHERE milestone_id = OLD.milestone_id;
END;

CREATE TRIGGER update_support_timestamp
AFTER UPDATE ON after_sales_support
FOR EACH ROW
BEGIN
    UPDATE after_sales_support SET updated_at = CURRENT_TIMESTAMP WHERE support_id = OLD.support_id;
END;
```
