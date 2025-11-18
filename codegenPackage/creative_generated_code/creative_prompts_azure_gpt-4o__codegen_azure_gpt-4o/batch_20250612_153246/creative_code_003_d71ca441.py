"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://youngistaan.org
Prompt: Develop a database schema for managing projects such as "Siksha," "Medical Programs," and "Road Safety Program" described by Youngistaan Foundation.
Generated: DETERMINISTIC_d71ca44167fad400
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Managing Projects

-- Create 'projects' table to store information about various projects.
CREATE TABLE projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    project_name VARCHAR(100) NOT NULL,        -- Name of the project (e.g., "Siksha", "Medical Programs")
    project_description TEXT,                  -- Detailed description of the project
    start_date DATE NOT NULL,                  -- Project start date
    end_date DATE,                             -- Project end date (nullable, for ongoing projects)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last updated timestamp
);

-- Create 'members' table to store information about individuals associated with projects.
CREATE TABLE members (
    member_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each member
    member_name VARCHAR(100) NOT NULL,        -- Name of the member
    email VARCHAR(100) UNIQUE NOT NULL,       -- Email address for contacting the member
    phone_number VARCHAR(15),                 -- Phone number of the member (nullable)
    role VARCHAR(50) NOT NULL,                -- Role played in the project (e.g., Volunteer, Manager)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last updated timestamp
);

-- Create 'project_members' table to associate members with specific projects (many-to-many relationship).
CREATE TABLE project_members (
    project_id INT NOT NULL,                      -- Foreign key referencing 'projects' table
    member_id INT NOT NULL,                       -- Foreign key referencing 'members' table
    joined_date DATE NOT NULL,                    -- Date the member joined the project
    PRIMARY KEY (project_id, member_id),          -- Composite primary key for project-member relationship
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE, -- Cascade delete for projects
    FOREIGN KEY (member_id) REFERENCES members(member_id) ON DELETE CASCADE  -- Cascade delete for members
);

-- Create 'tasks' table to store tasks associated with projects.
CREATE TABLE tasks (
    task_id INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each task
    project_id INT NOT NULL,                      -- Foreign key referencing 'projects' table
    task_name VARCHAR(100) NOT NULL,              -- Name of the task
    task_description TEXT,                        -- Detailed description of the task
    assigned_to INT,                              -- Foreign key referencing 'members' table (nullable)
    due_date DATE,                                -- Task due date
    status ENUM('Pending', 'In Progress', 'Completed') DEFAULT 'Pending', -- Task status
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last updated timestamp
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE, -- Cascade delete for projects
    FOREIGN KEY (assigned_to) REFERENCES members(member_id) ON DELETE SET NULL  -- Set NULL on member deletion
);

-- Indexes for performance optimization
CREATE INDEX idx_project_name ON projects(project_name); -- Index on project_name for faster search
CREATE INDEX idx_member_email ON members(email);         -- Index on email for faster lookup
CREATE INDEX idx_task_status ON tasks(status);           -- Index on task status for filtering
```
