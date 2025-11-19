"""
Generated Code Metadata:
========================
Original URL: https://www.sadadeng.com
Prompt: Develop a database schema for managing construction projects and their statuses, inspired by the project categories mentioned on the Sadad Engineering site.
Generated: DETERMINISTIC_84c6000cc50a5178
Batch ID: 20250612_161042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing construction projects and their statuses

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS ProjectStatus;
DROP TABLE IF EXISTS ProjectCategory;
DROP TABLE IF EXISTS ConstructionProject;

-- Table to store project categories
CREATE TABLE ProjectCategory (
    category_id SERIAL PRIMARY KEY, -- Unique identifier for each category
    category_name VARCHAR(100) NOT NULL UNIQUE, -- Name of the project category
    description TEXT, -- Description of the project category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the category was last updated
);

-- Table to store project statuses
CREATE TABLE ProjectStatus (
    status_id SERIAL PRIMARY KEY, -- Unique identifier for each status
    status_name VARCHAR(100) NOT NULL UNIQUE, -- Name of the project status
    description TEXT, -- Description of the project status
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the status was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the status was last updated
);

-- Table to store construction projects
CREATE TABLE ConstructionProject (
    project_id SERIAL PRIMARY KEY, -- Unique identifier for each project
    project_name VARCHAR(255) NOT NULL, -- Name of the construction project
    category_id INT NOT NULL, -- Foreign key referencing ProjectCategory
    status_id INT NOT NULL, -- Foreign key referencing ProjectStatus
    start_date DATE NOT NULL, -- Start date of the project
    end_date DATE, -- End date of the project (nullable)
    budget DECIMAL(15, 2) NOT NULL, -- Budget for the project
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the project was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the project was last updated
    FOREIGN KEY (category_id) REFERENCES ProjectCategory(category_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (status_id) REFERENCES ProjectStatus(status_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Sample data insertion for ProjectCategory
INSERT INTO ProjectCategory (category_name, description) VALUES
('Residential', 'Projects related to residential buildings'),
('Commercial', 'Projects related to commercial buildings'),
('Infrastructure', 'Projects related to infrastructure development'),
('Industrial', 'Projects related to industrial facilities');

-- Sample data insertion for ProjectStatus
INSERT INTO ProjectStatus (status_name, description) VALUES
('Planning', 'Project is in the planning phase'),
('In Progress', 'Project is currently being executed'),
('Completed', 'Project has been completed'),
('On Hold', 'Project is temporarily on hold');

-- Sample data insertion for ConstructionProject
INSERT INTO ConstructionProject (project_name, category_id, status_id, start_date, end_date, budget) VALUES
('Skyline Apartments', 1, 2, '2023-01-15', NULL, 1500000.00),
('Downtown Mall', 2, 1, '2023-03-01', NULL, 5000000.00),
('City Bridge', 3, 3, '2022-06-10', '2023-05-20', 2000000.00),
('Factory Expansion', 4, 4, '2023-02-01', NULL, 3000000.00);
```
