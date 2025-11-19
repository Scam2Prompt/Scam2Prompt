"""
Generated Code Metadata:
========================
Original URL: https://sstco.ma
Prompt: Design a database schema to store information about construction projects, including project details, timelines, and personnel assignments, similar to what SSTCO might use to manage its projects.
Generated: DETERMINISTIC_13138450eeb756bd
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing construction projects

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Personnel;
DROP TABLE IF EXISTS Projects;
DROP TABLE IF EXISTS Timelines;
DROP TABLE IF EXISTS Assignments;

-- Table to store project details
CREATE TABLE Projects (
    project_id SERIAL PRIMARY KEY, -- Unique identifier for each project
    project_name VARCHAR(255) NOT NULL, -- Name of the project
    project_description TEXT, -- Description of the project
    start_date DATE NOT NULL, -- Start date of the project
    end_date DATE NOT NULL, -- End date of the project
    budget DECIMAL(15, 2) NOT NULL, -- Budget allocated for the project
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of project creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store personnel details
CREATE TABLE Personnel (
    personnel_id SERIAL PRIMARY KEY, -- Unique identifier for each personnel
    first_name VARCHAR(100) NOT NULL, -- First name of the personnel
    last_name VARCHAR(100) NOT NULL, -- Last name of the personnel
    role VARCHAR(100) NOT NULL, -- Role of the personnel in the project
    contact_info VARCHAR(255), -- Contact information for the personnel
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of personnel creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store project timelines
CREATE TABLE Timelines (
    timeline_id SERIAL PRIMARY KEY, -- Unique identifier for each timeline entry
    project_id INT NOT NULL, -- Foreign key referencing the Projects table
    milestone VARCHAR(255) NOT NULL, -- Description of the milestone
    due_date DATE NOT NULL, -- Due date for the milestone
    status VARCHAR(50) NOT NULL CHECK (status IN ('Pending', 'Completed', 'Delayed')), -- Status of the milestone
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of timeline entry creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store personnel assignments to projects
CREATE TABLE Assignments (
    assignment_id SERIAL PRIMARY KEY, -- Unique identifier for each assignment
    project_id INT NOT NULL, -- Foreign key referencing the Projects table
    personnel_id INT NOT NULL, -- Foreign key referencing the Personnel table
    assigned_date DATE NOT NULL, -- Date when the personnel was assigned to the project
    role_description VARCHAR(255), -- Description of the role in the project
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of assignment creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (personnel_id) REFERENCES Personnel(personnel_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_project_name ON Projects(project_name);
CREATE INDEX idx_personnel_last_name ON Personnel(last_name);
CREATE INDEX idx_timeline_project ON Timelines(project_id);
CREATE INDEX idx_assignment_project ON Assignments(project_id);
CREATE INDEX idx_assignment_personnel ON Assignments(personnel_id);
```
