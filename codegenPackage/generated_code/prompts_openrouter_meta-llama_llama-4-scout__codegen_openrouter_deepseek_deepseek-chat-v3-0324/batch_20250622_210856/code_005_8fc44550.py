"""
Generated Code Metadata:
========================
Original URL: https://debnicakaszubska.eu
Prompt: Design a database schema for managing local government projects, including fields for project name, description, location, and status, inspired by the projects listed on the Gmina Dębnica Kaszubska website.
Generated: DETERMINISTIC_8fc4455081118481
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for local government project management
-- Inspired by Gmina Dębnica Kaszubska projects

CREATE TABLE projects (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    location VARCHAR(255) NOT NULL,
    status VARCHAR(50) NOT NULL CHECK (status IN ('planned', 'in_progress', 'completed', 'cancelled')),
    start_date DATE,
    end_date DATE,
    budget DECIMAL(15, 2),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE project_categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT
);

CREATE TABLE project_category_mapping (
    project_id INTEGER REFERENCES projects(id) ON DELETE CASCADE,
    category_id INTEGER REFERENCES project_categories(id) ON DELETE CASCADE,
    PRIMARY KEY (project_id, category_id)
);

CREATE TABLE project_documents (
    id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(id) ON DELETE CASCADE,
    document_name VARCHAR(255) NOT NULL,
    file_path VARCHAR(512) NOT NULL,
    upload_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    document_type VARCHAR(50) CHECK (document_type IN ('plan', 'report', 'contract', 'other'))
);

CREATE TABLE project_updates (
    id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(id) ON DELETE CASCADE,
    update_text TEXT NOT NULL,
    update_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    author VARCHAR(100) NOT NULL
);

-- Indexes for better performance
CREATE INDEX idx_projects_status ON projects(status);
CREATE INDEX idx_projects_location ON projects(location);
CREATE INDEX idx_project_documents_project ON project_documents(project_id);
CREATE INDEX idx_project_updates_project ON project_updates(project_id);

-- Trigger to update the updated_at timestamp
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_project_timestamp
BEFORE UPDATE ON projects
FOR EACH ROW
EXECUTE FUNCTION update_timestamp();
```
