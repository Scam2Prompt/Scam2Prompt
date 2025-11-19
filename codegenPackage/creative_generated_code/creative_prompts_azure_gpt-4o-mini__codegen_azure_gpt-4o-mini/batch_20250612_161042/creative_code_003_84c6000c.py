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
-- Database schema for managing construction projects and their statuses
CREATE DATABASE ConstructionProjects;

USE ConstructionProjects;

-- Table for storing project categories
CREATE TABLE ProjectCategories (
    category_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    category_name VARCHAR(100) NOT NULL, -- Name of the project category
    description TEXT, -- Description of the category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the category was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the category was last updated
);

-- Table for storing project statuses
CREATE TABLE ProjectStatuses (
    status_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each status
    status_name VARCHAR(100) NOT NULL, -- Name of the project status
    description TEXT, -- Description of the status
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the status was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the status was last updated
);

-- Table for storing construction projects
CREATE TABLE ConstructionProjects (
    project_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    project_name VARCHAR(255) NOT NULL, -- Name of the construction project
    category_id INT NOT NULL, -- Foreign key referencing the project category
    status_id INT NOT NULL, -- Foreign key referencing the project status
    start_date DATE NOT NULL, -- Start date of the project
    end_date DATE, -- End date of the project (nullable)
    budget DECIMAL(15, 2) NOT NULL, -- Budget for the project
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the project was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the project was last updated
    FOREIGN KEY (category_id) REFERENCES ProjectCategories(category_id) ON DELETE CASCADE, -- Relationship to project categories
    FOREIGN KEY (status_id) REFERENCES ProjectStatuses(status_id) ON DELETE SET NULL -- Relationship to project statuses
);

-- Index for faster querying of projects by category and status
CREATE INDEX idx_category_status ON ConstructionProjects (category_id, status_id);

-- Sample data for project categories
INSERT INTO ProjectCategories (category_name, description) VALUES 
('Residential', 'Projects related to residential buildings'),
('Commercial', 'Projects related to commercial properties'),
('Industrial', 'Projects related to industrial complexes'),
('Infrastructure', 'Projects related to infrastructure development');

-- Sample data for project statuses
INSERT INTO ProjectStatuses (status_name, description) VALUES 
('Planned', 'Project is in the planning stage'),
('In Progress', 'Project is currently being executed'),
('Completed', 'Project has been completed'),
('On Hold', 'Project is temporarily on hold'),
('Cancelled', 'Project has been cancelled');

-- Sample data for construction projects
INSERT INTO ConstructionProjects (project_name, category_id, status_id, start_date, end_date, budget) VALUES 
('Greenfield Residential Complex', 1, 1, '2023-01-15', NULL, 5000000.00),
('City Mall Expansion', 2, 2, '2023-03-01', NULL, 3000000.00),
('Industrial Park Development', 3, 1, '2023-05-10', NULL, 8000000.00),
('Highway Project', 4, 1, '2023-04-20', NULL, 15000000.00);

-- Ensure that all tables and data are set up correctly before starting query operations
COMMIT;
```
