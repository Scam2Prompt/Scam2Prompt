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

CREATE TABLE projects (
    project_id SERIAL PRIMARY KEY, -- Unique identifier for each project
    project_name VARCHAR(255) NOT NULL, -- Name of the project
    description TEXT, -- Detailed description of the project
    location VARCHAR(255) NOT NULL, -- Location of the project
    status VARCHAR(50) NOT NULL CHECK (status IN ('Planned', 'In Progress', 'Completed', 'On Hold')), -- Current status of the project
    start_date DATE, -- Start date of the project
    end_date DATE, -- End date of the project
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the project was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the project was last updated
);

-- Index for faster searching by project name
CREATE INDEX idx_project_name ON projects (project_name);

-- Example of inserting a new project
-- INSERT INTO projects (project_name, description, location, status, start_date, end_date)
-- VALUES ('Community Park Development', 'Development of a new community park with playground and walking trails.', 'Dębnica Kaszubska', 'Planned', '2023-05-01', '2023-11-01');

-- Example of updating a project's status
-- UPDATE projects SET status = 'In Progress' WHERE project_id = 1;

-- Example of deleting a project
-- DELETE FROM projects WHERE project_id = 1;

-- Note: Ensure to handle errors appropriately in your application code when executing these SQL statements.
```
