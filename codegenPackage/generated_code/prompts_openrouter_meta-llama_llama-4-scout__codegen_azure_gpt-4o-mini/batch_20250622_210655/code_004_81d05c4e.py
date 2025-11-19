"""
Generated Code Metadata:
========================
Original URL: https://www.aidasdb.org
Prompt: Design a database schema for storing information about AIDA's projects, including project name, description, location, and outcomes, and write a SQL query to retrieve project data.
Generated: DETERMINISTIC_81d05c4e62bb9a1e
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for storing information about AIDA's projects

CREATE TABLE Projects (
    ProjectID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each project
    ProjectName VARCHAR(255) NOT NULL,         -- Name of the project
    Description TEXT,                           -- Detailed description of the project
    Location VARCHAR(255),                      -- Location where the project is based
    Outcomes TEXT,                              -- Outcomes or results of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the project was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for when the project was last updated
);

-- SQL query to retrieve project data
SELECT 
    ProjectID, 
    ProjectName, 
    Description, 
    Location, 
    Outcomes, 
    CreatedAt, 
    UpdatedAt 
FROM 
    Projects
ORDER BY 
    CreatedAt DESC;  -- Order projects by creation date, most recent first
```
