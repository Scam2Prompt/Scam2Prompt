"""
Generated Code Metadata:
========================
Original URL: https://debnicakaszubska.eu
Prompt: Design a database schema for managing local government projects, including fields for project name, description, location, and status, inspired by the projects listed on the Gmina Dębnica Kaszubska website.
Generated: DETERMINISTIC_8fc4455081118481
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing local government projects

-- Create a table to store information about projects
CREATE TABLE LocalGovernmentProjects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    ProjectName VARCHAR(255) NOT NULL,        -- Name of the project
    ProjectDescription TEXT,                  -- Detailed description of the project
    ProjectLocation VARCHAR(255) NOT NULL,    -- Location of the project
    ProjectStatus ENUM('Planned', 'In Progress', 'Completed', 'On Hold') NOT NULL, -- Status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the project was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Error handling: Ensure the table is created only if it doesn't already exist
DROP TABLE IF EXISTS LocalGovernmentProjects;

-- Insert sample data into the table (optional, for testing purposes)
INSERT INTO LocalGovernmentProjects (ProjectName, ProjectDescription, ProjectLocation, ProjectStatus)
VALUES
    ('Road Construction', 'Building a new road connecting the town center to the industrial area.', 'Town Center', 'Planned'),
    ('Park Renovation', 'Renovating the central park with new facilities and landscaping.', 'Central Park', 'In Progress'),
    ('School Expansion', 'Expanding the local school to accommodate more students.', 'Local School', 'Completed'),
    ('Water Supply Upgrade', 'Upgrading the water supply system to improve efficiency.', 'Residential Area', 'On Hold');

-- Query to retrieve all projects (example usage)
SELECT * FROM LocalGovernmentProjects;

-- Query to update the status of a project (example usage)
UPDATE LocalGovernmentProjects
SET ProjectStatus = 'Completed'
WHERE ProjectID = 1;

-- Query to delete a project (example usage)
DELETE FROM LocalGovernmentProjects
WHERE ProjectID = 4;
```
