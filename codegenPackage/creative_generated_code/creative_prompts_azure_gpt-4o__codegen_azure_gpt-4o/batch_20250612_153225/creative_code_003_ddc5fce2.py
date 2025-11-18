"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perumakers.org
Prompt: Create a database schema for managing projects and collaborators for an organization like Perú Makers, with fields for project name, description, collaborators, and institutional partners.
Generated: DETERMINISTIC_ddc5fce2960ceb7a
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing projects and collaborators for an organization like Perú Makers

-- Table: projects
-- Purpose: Stores information about projects
CREATE TABLE projects (
    project_id SERIAL PRIMARY KEY,         -- Unique identifier for each project
    project_name VARCHAR(255) NOT NULL,   -- Name of the project
    description TEXT,                     -- Detailed description of the project
    created_at TIMESTAMP DEFAULT NOW(),   -- Timestamp when the project was created
    updated_at TIMESTAMP DEFAULT NOW()    -- Timestamp for the last update of the project
);

-- Table: collaborators
-- Purpose: Stores information about individual collaborators
CREATE TABLE collaborators (
    collaborator_id SERIAL PRIMARY KEY,   -- Unique identifier for each collaborator
    full_name VARCHAR(255) NOT NULL,      -- Full name of the collaborator
    email VARCHAR(255) UNIQUE NOT NULL,   -- Email address of the collaborator
    role VARCHAR(255),                    -- Role of the collaborator in the project
    created_at TIMESTAMP DEFAULT NOW(),   -- Timestamp when the collaborator was added
    updated_at TIMESTAMP DEFAULT NOW()    -- Timestamp for the last update of the collaborator
);

-- Table: institutional_partners
-- Purpose: Stores information about institutional partners
CREATE TABLE institutional_partners (
    partner_id SERIAL PRIMARY KEY,        -- Unique identifier for each institutional partner
    name VARCHAR(255) NOT NULL,           -- Name of the institution
    contact_email VARCHAR(255) UNIQUE,   -- Contact email of the institution
    website_url VARCHAR(255),             -- Website of the institution
    created_at TIMESTAMP DEFAULT NOW(),   -- Timestamp when the partner was added
    updated_at TIMESTAMP DEFAULT NOW()    -- Timestamp for the last update of the partner
);

-- Table: project_collaborators
-- Purpose: Links projects to collaborators
CREATE TABLE project_collaborators (
    project_id INT NOT NULL REFERENCES projects(project_id) ON DELETE CASCADE, -- Foreign key to projects table
    collaborator_id INT NOT NULL REFERENCES collaborators(collaborator_id) ON DELETE CASCADE, -- Foreign key to collaborators table
    PRIMARY KEY (project_id, collaborator_id),                                  -- Composite primary key
    assigned_at TIMESTAMP DEFAULT NOW()                                        -- Timestamp when the collaborator was assigned to the project
);

-- Table: project_partners
-- Purpose: Links projects to institutional partners
CREATE TABLE project_partners (
    project_id INT NOT NULL REFERENCES projects(project_id) ON DELETE CASCADE, -- Foreign key to projects table
    partner_id INT NOT NULL REFERENCES institutional_partners(partner_id) ON DELETE CASCADE, -- Foreign key to institutional partners table
    PRIMARY KEY (project_id, partner_id),                                      -- Composite primary key
    added_at TIMESTAMP DEFAULT NOW()                                           -- Timestamp when the partner was added to the project
);

-- Adding a trigger to update the `updated_at` field on projects table
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Apply the trigger to automatically update the `updated_at` field
CREATE TRIGGER update_projects_timestamp
BEFORE UPDATE ON projects
FOR EACH ROW
EXECUTE FUNCTION update_timestamp();

-- Adding a trigger to update the `updated_at` field on collaborators table
CREATE TRIGGER update_collaborators_timestamp
BEFORE UPDATE ON collaborators
FOR EACH ROW
EXECUTE FUNCTION update_timestamp();

-- Adding a trigger to update the `updated_at` field on institutional_partners table
CREATE TRIGGER update_partners_timestamp
BEFORE UPDATE ON institutional_partners
FOR EACH ROW
EXECUTE FUNCTION update_timestamp();
```
