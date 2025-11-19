"""
Generated Code Metadata:
========================
Original URL: https://pconsultsa.com
Prompt: Design a simple database schema to store information about clients, projects, and outcomes for a consulting firm like PConsultsa.
Generated: DETERMINISTIC_164e27c73f1e33f9
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for PConsultsa consulting firm

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Clients table
CREATE TABLE clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT,
    address TEXT,
    industry TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%.%')
);

-- Projects table
CREATE TABLE projects (
    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    start_date DATE,
    end_date DATE,
    budget DECIMAL(10, 2),
    status TEXT CHECK(status IN ('planned', 'active', 'completed', 'cancelled')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    CHECK (end_date IS NULL OR end_date >= start_date)
);

-- Outcomes table
CREATE TABLE outcomes (
    outcome_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    description TEXT NOT NULL,
    impact TEXT CHECK(impact IN ('low', 'medium', 'high')),
    achieved BOOLEAN DEFAULT FALSE,
    achieved_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Team members table
CREATE TABLE team_members (
    member_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    role TEXT,
    hire_date DATE,
    CHECK (email LIKE '%@%.%')
);

-- Project assignments table
CREATE TABLE project_assignments (
    assignment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    member_id INTEGER NOT NULL,
    role TEXT NOT NULL,
    start_date DATE,
    end_date DATE,
    hours_allocated INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (member_id) REFERENCES team_members(member_id) ON DELETE CASCADE,
    UNIQUE (project_id, member_id),
    CHECK (end_date IS NULL OR end_date >= start_date)
);

-- Create triggers to update timestamps
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

CREATE TRIGGER update_outcome_timestamp
AFTER UPDATE ON outcomes
FOR EACH ROW
BEGIN
    UPDATE outcomes SET updated_at = CURRENT_TIMESTAMP WHERE outcome_id = OLD.outcome_id;
END;

CREATE TRIGGER update_assignment_timestamp
AFTER UPDATE ON project_assignments
FOR EACH ROW
BEGIN
    UPDATE project_assignments SET updated_at = CURRENT_TIMESTAMP WHERE assignment_id = OLD.assignment_id;
END;
```
