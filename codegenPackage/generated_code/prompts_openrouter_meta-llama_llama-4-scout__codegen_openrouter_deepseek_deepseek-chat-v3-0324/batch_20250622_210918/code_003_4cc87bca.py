"""
Generated Code Metadata:
========================
Original URL: https://renzostudio.com
Prompt: "Design a database schema for storing information about architectural projects, including images, descriptions, and client details."
Generated: DETERMINISTIC_4cc87bca938da7ec
Batch ID: 20250622_210918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for architectural projects management system

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Clients table
CREATE TABLE clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL CHECK(email LIKE '%@%.%'),
    phone TEXT,
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Projects table
CREATE TABLE projects (
    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    location TEXT,
    start_date DATE,
    end_date DATE,
    status TEXT CHECK(status IN ('planned', 'in_progress', 'completed', 'cancelled')),
    budget REAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Project images table
CREATE TABLE project_images (
    image_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    image_url TEXT NOT NULL,
    caption TEXT,
    is_primary BOOLEAN DEFAULT FALSE,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Project documents table
CREATE TABLE project_documents (
    document_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    document_url TEXT NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    document_type TEXT CHECK(document_type IN ('blueprint', 'contract', 'report', 'other')),
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Project team members table
CREATE TABLE project_team (
    team_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    member_name TEXT NOT NULL,
    role TEXT NOT NULL,
    email TEXT CHECK(email LIKE '%@%.%'),
    phone TEXT,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Project milestones table
CREATE TABLE project_milestones (
    milestone_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    due_date DATE NOT NULL,
    completed_date DATE,
    status TEXT CHECK(status IN ('pending', 'completed', 'delayed')),
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Triggers for automatic updated_at timestamps
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

-- Indexes for performance optimization
CREATE INDEX idx_projects_client ON projects(client_id);
CREATE INDEX idx_project_images ON project_images(project_id);
CREATE INDEX idx_project_documents ON project_documents(project_id);
CREATE INDEX idx_project_team ON project_team(project_id);
CREATE INDEX idx_project_milestones ON project_milestones(project_id);
```
