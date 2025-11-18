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
-- Database schema for managing projects related to Youngistaan Foundation

-- Create a new database for the projects
CREATE DATABASE YoungistaanFoundation;

-- Switch to the newly created database
USE YoungistaanFoundation;

-- Table to store project information
CREATE TABLE Projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each project
    project_name VARCHAR(255) NOT NULL,         -- Name of the project
    description TEXT,                             -- Brief description of the project
    start_date DATE,                             -- Start date of the project
    end_date DATE,                               -- End date of the project
    status ENUM('Planned', 'Ongoing', 'Completed') DEFAULT 'Planned',  -- Current status of the project
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the project was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for when the project was last updated
);

-- Table to store project team members
CREATE TABLE TeamMembers (
    member_id INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each team member
    project_id INT NOT NULL,                      -- ID of the project the member is associated with
    member_name VARCHAR(255) NOT NULL,           -- Name of the team member
    role VARCHAR(100),                            -- Role of the team member in the project
    contact_email VARCHAR(255),                   -- Email address of the team member
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the member was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp for when the member was last updated
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE  -- Foreign key constraint
);

-- Table to store project updates
CREATE TABLE ProjectUpdates (
    update_id INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each update
    project_id INT NOT NULL,                      -- ID of the project the update belongs to
    update_description TEXT NOT NULL,             -- Description of the update
    update_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Date when the update was made
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE  -- Foreign key constraint
);

-- Table to store project budgets
CREATE TABLE ProjectBudgets (
    budget_id INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each budget entry
    project_id INT NOT NULL,                      -- ID of the project the budget is associated with
    allocated_amount DECIMAL(10, 2) NOT NULL,    -- Allocated budget amount
    spent_amount DECIMAL(10, 2) DEFAULT 0.00,    -- Amount spent so far
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the budget entry was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp for when the budget entry was last updated
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE  -- Foreign key constraint
);

-- Table to store stakeholders involved in projects
CREATE TABLE Stakeholders (
    stakeholder_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each stakeholder
    project_id INT NOT NULL,                       -- ID of the project the stakeholder is involved in
    stakeholder_name VARCHAR(255) NOT NULL,       -- Name of the stakeholder
    contact_info VARCHAR(255),                     -- Contact information for the stakeholder
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the stakeholder was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp for when the stakeholder was last updated
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE  -- Foreign key constraint
);

-- Indexing for performance improvement
CREATE INDEX idx_project_name ON Projects (project_name);
CREATE INDEX idx_member_name ON TeamMembers (member_name);
CREATE INDEX idx_project_id ON ProjectUpdates (project_id);
CREATE INDEX idx_budget_project ON ProjectBudgets (project_id);
CREATE INDEX idx_stakeholder_project ON Stakeholders (project_id);
```
