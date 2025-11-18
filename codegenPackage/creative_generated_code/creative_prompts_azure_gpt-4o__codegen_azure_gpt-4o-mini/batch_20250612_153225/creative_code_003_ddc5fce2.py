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
-- Create a database schema for managing projects and collaborators for an organization like Perú Makers

-- Create a table for Institutions
CREATE TABLE Institutions (
    institution_id SERIAL PRIMARY KEY,  -- Unique identifier for each institution
    name VARCHAR(255) NOT NULL,         -- Name of the institution
    website VARCHAR(255),                -- Website URL of the institution (optional)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Create a table for Collaborators
CREATE TABLE Collaborators (
    collaborator_id SERIAL PRIMARY KEY,  -- Unique identifier for each collaborator
    name VARCHAR(255) NOT NULL,          -- Name of the collaborator
    email VARCHAR(255) UNIQUE NOT NULL,  -- Unique email address of the collaborator
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Create a table for Projects
CREATE TABLE Projects (
    project_id SERIAL PRIMARY KEY,        -- Unique identifier for each project
    project_name VARCHAR(255) NOT NULL,  -- Name of the project
    description TEXT,                     -- Detailed description of the project
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Create a junction table for Project Collaborators
CREATE TABLE Project_Collaborators (
    project_id INT NOT NULL,              -- Reference to the project
    collaborator_id INT NOT NULL,         -- Reference to the collaborator
    role VARCHAR(255),                    -- Role of the collaborator in the project
    PRIMARY KEY (project_id, collaborator_id), -- Composite primary key
    FOREIGN KEY (project_id) REFERENCES Projects (project_id) ON DELETE CASCADE, -- Foreign key constraint
    FOREIGN KEY (collaborator_id) REFERENCES Collaborators (collaborator_id) ON DELETE CASCADE -- Foreign key constraint
);

-- Create a junction table for Project Institutions
CREATE TABLE Project_Institutions (
    project_id INT NOT NULL,              -- Reference to the project
    institution_id INT NOT NULL,          -- Reference to the institution
    PRIMARY KEY (project_id, institution_id), -- Composite primary key
    FOREIGN KEY (project_id) REFERENCES Projects (project_id) ON DELETE CASCADE, -- Foreign key constraint
    FOREIGN KEY (institution_id) REFERENCES Institutions (institution_id) ON DELETE CASCADE -- Foreign key constraint
);

-- End of database schema creation
```
