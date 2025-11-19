"""
Generated Code Metadata:
========================
Original URL: https://taiko-t.com
Prompt: Generate a SQL database schema to store information about construction projects, including project type (e.g., pole construction, electrical and civil engineering), location, and project status, for a company like 株式会社タイコーテクノ.
Generated: DETERMINISTIC_82e85303a5f33780
Batch ID: 20250622_205156
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for Construction Projects

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS ProjectStatus;
DROP TABLE IF EXISTS ProjectType;
DROP TABLE IF EXISTS ConstructionProject;

-- Table to store different types of construction projects
CREATE TABLE ProjectType (
    id SERIAL PRIMARY KEY, -- Unique identifier for each project type
    name VARCHAR(100) NOT NULL UNIQUE, -- Name of the project type (e.g., pole construction)
    description TEXT -- Description of the project type
);

-- Table to store different statuses of projects
CREATE TABLE ProjectStatus (
    id SERIAL PRIMARY KEY, -- Unique identifier for each project status
    name VARCHAR(100) NOT NULL UNIQUE, -- Name of the project status (e.g., ongoing, completed)
    description TEXT -- Description of the project status
);

-- Table to store information about construction projects
CREATE TABLE ConstructionProject (
    id SERIAL PRIMARY KEY, -- Unique identifier for each construction project
    name VARCHAR(255) NOT NULL, -- Name of the construction project
    project_type_id INT NOT NULL, -- Foreign key referencing ProjectType
    location VARCHAR(255) NOT NULL, -- Location of the construction project
    status_id INT NOT NULL, -- Foreign key referencing ProjectStatus
    start_date DATE NOT NULL, -- Start date of the project
    end_date DATE, -- End date of the project (nullable)
    budget DECIMAL(15, 2) NOT NULL, -- Budget allocated for the project
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the project was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of the last update
    FOREIGN KEY (project_type_id) REFERENCES ProjectType(id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (status_id) REFERENCES ProjectStatus(id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Sample data insertion for ProjectType
INSERT INTO ProjectType (name, description) VALUES
('Pole Construction', 'Construction of utility poles for electrical distribution.'),
('Electrical Engineering', 'Projects related to electrical systems and installations.'),
('Civil Engineering', 'Projects involving infrastructure and civil works.');

-- Sample data insertion for ProjectStatus
INSERT INTO ProjectStatus (name, description) VALUES
('Ongoing', 'The project is currently in progress.'),
('Completed', 'The project has been finished.'),
('On Hold', 'The project is temporarily paused.'),
('Cancelled', 'The project has been cancelled.');

-- Note: Ensure to handle errors during data insertion and schema creation in your application logic.
```
