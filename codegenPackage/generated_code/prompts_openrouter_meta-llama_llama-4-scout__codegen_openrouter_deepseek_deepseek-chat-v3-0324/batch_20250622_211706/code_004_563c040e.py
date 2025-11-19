"""
Generated Code Metadata:
========================
Original URL: https://kowlaung.go.th
Prompt: Design a database schema for storing information about local government projects and initiatives in Khao Luang Subdistrict, including tables for project details, funding, and responsible agencies.
Generated: DETERMINISTIC_563c040e62422d5b
Batch ID: 20250622_211706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Khao Luang Subdistrict projects and initiatives

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Table for storing government agencies
CREATE TABLE agencies (
    agency_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    contact_person TEXT,
    contact_phone TEXT,
    contact_email TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (contact_email LIKE '%@%')
);

-- Table for storing project categories
CREATE TABLE project_categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Table for storing project statuses
CREATE TABLE project_statuses (
    status_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Main table for storing project information
CREATE TABLE projects (
    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    category_id INTEGER NOT NULL,
    status_id INTEGER NOT NULL,
    start_date DATE,
    end_date DATE,
    location TEXT,
    latitude REAL,
    longitude REAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES project_categories(category_id),
    FOREIGN KEY (status_id) REFERENCES project_statuses(status_id),
    CHECK (end_date IS NULL OR end_date >= start_date)
);

-- Table for tracking project funding sources and amounts
CREATE TABLE project_funding (
    funding_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    source_name TEXT NOT NULL,
    amount DECIMAL(12, 2) NOT NULL,
    currency TEXT DEFAULT 'THB',
    funding_date DATE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    CHECK (amount > 0)
);

-- Junction table for projects and responsible agencies
CREATE TABLE project_agencies (
    project_id INTEGER NOT NULL,
    agency_id INTEGER NOT NULL,
    role TEXT NOT NULL,
    PRIMARY KEY (project_id, agency_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (agency_id) REFERENCES agencies(agency_id) ON DELETE CASCADE
);

-- Table for project milestones
CREATE TABLE project_milestones (
    milestone_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    target_date DATE,
    completion_date DATE,
    status TEXT CHECK(status IN ('planned', 'in_progress', 'completed', 'delayed')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Table for project documents (reports, plans, etc.)
CREATE TABLE project_documents (
    document_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    file_path TEXT NOT NULL,
    file_type TEXT,
    file_size INTEGER,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    uploaded_by TEXT,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Create indexes for better performance
CREATE INDEX idx_projects_category ON projects(category_id);
CREATE INDEX idx_projects_status ON projects(status_id);
CREATE INDEX idx_funding_project ON project_funding(project_id);
CREATE INDEX idx_milestones_project ON project_milestones(project_id);
CREATE INDEX idx_documents_project ON project_documents(project_id);

-- Trigger to update the updated_at timestamp when projects are modified
CREATE TRIGGER update_project_timestamp
AFTER UPDATE ON projects
BEGIN
    UPDATE projects SET updated_at = CURRENT_TIMESTAMP WHERE project_id = OLD.project_id;
END;

-- Trigger to update the updated_at timestamp when milestones are modified
CREATE TRIGGER update_milestone_timestamp
AFTER UPDATE ON project_milestones
BEGIN
    UPDATE project_milestones SET updated_at = CURRENT_TIMESTAMP WHERE milestone_id = OLD.milestone_id;
END;
```
