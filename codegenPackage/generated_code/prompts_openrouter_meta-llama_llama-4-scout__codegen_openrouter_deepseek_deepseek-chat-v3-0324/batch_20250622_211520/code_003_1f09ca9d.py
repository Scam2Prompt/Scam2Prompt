"""
Generated Code Metadata:
========================
Original URL: https://meezaninteriorsolutions.com
Prompt: "Design a database schema for storing information about interior design projects, including details about project types (residential, commercial, etc.), client information, and project awards, similar to Meezan Interior Solutions' project management needs."
Generated: DETERMINISTIC_1f09ca9d8582438c
Batch ID: 20250622_211520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Interior Design Project Management System
-- Designed for Meezan Interior Solutions-like project management needs

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create table for project types
CREATE TABLE IF NOT EXISTS project_types (
    type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    type_name TEXT NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create table for clients
CREATE TABLE IF NOT EXISTS clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE CHECK(email LIKE '%@%.%'),
    phone TEXT NOT NULL,
    address TEXT,
    company_name TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create table for project status
CREATE TABLE IF NOT EXISTS project_status (
    status_id INTEGER PRIMARY KEY AUTOINCREMENT,
    status_name TEXT NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create table for awards
CREATE TABLE IF NOT EXISTS awards (
    award_id INTEGER PRIMARY KEY AUTOINCREMENT,
    award_name TEXT NOT NULL,
    awarding_body TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create main projects table
CREATE TABLE IF NOT EXISTS projects (
    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_name TEXT NOT NULL,
    description TEXT,
    type_id INTEGER NOT NULL,
    client_id INTEGER NOT NULL,
    status_id INTEGER NOT NULL,
    start_date DATE,
    end_date DATE,
    budget DECIMAL(12, 2) CHECK(budget >= 0),
    square_footage INTEGER CHECK(square_footage > 0),
    location TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (type_id) REFERENCES project_types(type_id),
    FOREIGN KEY (client_id) REFERENCES clients(client_id),
    FOREIGN KEY (status_id) REFERENCES project_status(status_id),
    CHECK (end_date IS NULL OR end_date >= start_date)
);

-- Create junction table for project awards
CREATE TABLE IF NOT EXISTS project_awards (
    project_id INTEGER NOT NULL,
    award_id INTEGER NOT NULL,
    date_awarded DATE NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (project_id, award_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id),
    FOREIGN KEY (award_id) REFERENCES awards(award_id)
);

-- Create table for project milestones
CREATE TABLE IF NOT EXISTS milestones (
    milestone_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    milestone_name TEXT NOT NULL,
    description TEXT,
    due_date DATE NOT NULL,
    completed BOOLEAN DEFAULT FALSE,
    completion_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id),
    CHECK (completion_date IS NULL OR completion_date >= created_at)
);

-- Create table for project documents
CREATE TABLE IF NOT EXISTS project_documents (
    document_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    document_name TEXT NOT NULL,
    document_type TEXT NOT NULL,
    file_path TEXT NOT NULL,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    description TEXT,
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
);

-- Create indexes for performance
CREATE INDEX IF NOT EXISTS idx_projects_client ON projects(client_id);
CREATE INDEX IF NOT EXISTS idx_projects_type ON projects(type_id);
CREATE INDEX IF NOT EXISTS idx_projects_status ON projects(status_id);
CREATE INDEX IF NOT EXISTS idx_milestones_project ON milestones(project_id);
CREATE INDEX IF NOT EXISTS idx_project_awards_project ON project_awards(project_id);
CREATE INDEX IF NOT EXISTS idx_project_documents_project ON project_documents(project_id);

-- Create triggers for updated_at timestamps
CREATE TRIGGER IF NOT EXISTS update_project_types_timestamp
AFTER UPDATE ON project_types
BEGIN
    UPDATE project_types SET updated_at = CURRENT_TIMESTAMP WHERE type_id = NEW.type_id;
END;

CREATE TRIGGER IF NOT EXISTS update_clients_timestamp
AFTER UPDATE ON clients
BEGIN
    UPDATE clients SET updated_at = CURRENT_TIMESTAMP WHERE client_id = NEW.client_id;
END;

CREATE TRIGGER IF NOT EXISTS update_project_status_timestamp
AFTER UPDATE ON project_status
BEGIN
    UPDATE project_status SET updated_at = CURRENT_TIMESTAMP WHERE status_id = NEW.status_id;
END;

CREATE TRIGGER IF NOT EXISTS update_awards_timestamp
AFTER UPDATE ON awards
BEGIN
    UPDATE awards SET updated_at = CURRENT_TIMESTAMP WHERE award_id = NEW.award_id;
END;

CREATE TRIGGER IF NOT EXISTS update_projects_timestamp
AFTER UPDATE ON projects
BEGIN
    UPDATE projects SET updated_at = CURRENT_TIMESTAMP WHERE project_id = NEW.project_id;
END;

CREATE TRIGGER IF NOT EXISTS update_milestones_timestamp
AFTER UPDATE ON milestones
BEGIN
    UPDATE milestones SET updated_at = CURRENT_TIMESTAMP WHERE milestone_id = NEW.milestone_id;
END;
```
