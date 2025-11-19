"""
Generated Code Metadata:
========================
Original URL: https://perumakers.org
Prompt: Create a database schema for managing projects and collaborators for an organization like Perú Makers, with fields for project name, description, collaborators, and institutional partners.
Generated: DETERMINISTIC_ddc5fce2960ceb7a
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing projects and collaborators for an organization like Perú Makers

-- Create a table for storing project information
CREATE TABLE Projects (
    project_id SERIAL PRIMARY KEY,          -- Unique identifier for each project
    project_name VARCHAR(255) NOT NULL,    -- Name of the project
    description TEXT,                       -- Description of the project
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the project was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the project was last updated
);

-- Create a table for storing collaborator information
CREATE TABLE Collaborators (
    collaborator_id SERIAL PRIMARY KEY,      -- Unique identifier for each collaborator
    name VARCHAR(255) NOT NULL,              -- Name of the collaborator
    email VARCHAR(255) UNIQUE NOT NULL,      -- Email of the collaborator (must be unique)
    role VARCHAR(100)                        -- Role of the collaborator in the project
);

-- Create a table for storing institutional partners
CREATE TABLE InstitutionalPartners (
    partner_id SERIAL PRIMARY KEY,           -- Unique identifier for each institutional partner
    partner_name VARCHAR(255) NOT NULL,      -- Name of the institutional partner
    contact_info TEXT                        -- Contact information for the partner
);

-- Create a junction table to manage the many-to-many relationship between projects and collaborators
CREATE TABLE ProjectCollaborators (
    project_id INT NOT NULL,                 -- Foreign key referencing Projects
    collaborator_id INT NOT NULL,            -- Foreign key referencing Collaborators
    PRIMARY KEY (project_id, collaborator_id), -- Composite primary key
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (collaborator_id) REFERENCES Collaborators(collaborator_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a junction table to manage the many-to-many relationship between projects and institutional partners
CREATE TABLE ProjectPartners (
    project_id INT NOT NULL,                 -- Foreign key referencing Projects
    partner_id INT NOT NULL,                 -- Foreign key referencing InstitutionalPartners
    PRIMARY KEY (project_id, partner_id),    -- Composite primary key
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (partner_id) REFERENCES InstitutionalPartners(partner_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes can be added for performance optimization if necessary
-- CREATE INDEX idx_project_name ON Projects(project_name);
-- CREATE INDEX idx_collaborator_email ON Collaborators(email);
-- CREATE INDEX idx_partner_name ON InstitutionalPartners(partner_name);
```
