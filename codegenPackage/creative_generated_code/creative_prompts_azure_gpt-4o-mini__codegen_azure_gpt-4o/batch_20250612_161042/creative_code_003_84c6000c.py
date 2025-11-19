"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.sadadeng.com
Prompt: Develop a database schema for managing construction projects and their statuses, inspired by the project categories mentioned on the Sadad Engineering site.
Generated: DETERMINISTIC_84c6000cc50a5178
Batch ID: 20250612_161042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Managing Construction Projects and Their Statuses

-- Create table for managing project categories
CREATE TABLE project_categories (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for each category
    name VARCHAR(255) NOT NULL,        -- Name of the category (e.g., "Residential", "Commercial")
    description TEXT,                  -- Detailed description of the category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the category is created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create table for managing construction projects
CREATE TABLE construction_projects (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for each project
    name VARCHAR(255) NOT NULL,        -- Name of the project
    description TEXT,                  -- Detailed description of the project
    category_id INT NOT NULL,          -- Foreign key referencing project_categories
    status ENUM('Pending', 'In Progress', 'Completed', 'On Hold') NOT NULL, -- Status of the project
    start_date DATE,                   -- Start date of the project
    end_date DATE,                     -- End date of the project (nullable in case of ongoing projects)
    budget DECIMAL(15,2),              -- Budget allocated for the project
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the project is created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (category_id) REFERENCES project_categories(id) -- Establish relationship with project categories
);

-- Create table for project status history
CREATE TABLE project_status_history (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for each status history entry
    project_id INT NOT NULL,           -- Foreign key referencing construction_projects
    old_status ENUM('Pending', 'In Progress', 'Completed', 'On Hold') NOT NULL, -- Previous status
    new_status ENUM('Pending', 'In Progress', 'Completed', 'On Hold') NOT NULL, -- Updated status
    changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the status was changed
    FOREIGN KEY (project_id) REFERENCES construction_projects(id) -- Establish relationship with construction projects
);

-- Ensure proper error handling in case of failed transactions
-- Wrap any INSERT or UPDATE operations in transactions in application code for consistency

-- Example Indexing
CREATE INDEX idx_project_status ON construction_projects(status); -- Index on status for faster filtering
CREATE INDEX idx_project_category ON construction_projects(category_id); -- Index on category_id for faster lookups
```
