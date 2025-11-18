"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inaro.com.co
Prompt: Provide an example of a database schema for storing information about construction projects, including fields for project name, location, client, number of apartments, and hours worked, as detailed in INARO S.A.S.'s project descriptions.
Generated: DETERMINISTIC_38be978432942b16
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL Database Schema for Construction Projects

CREATE TABLE Clients (
    client_id SERIAL PRIMARY KEY,          -- Unique identifier for each client
    name VARCHAR(255) NOT NULL,           -- Name of the client
    contact_info VARCHAR(255),             -- Contact information for the client
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the client is added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

CREATE TABLE Projects (
    project_id SERIAL PRIMARY KEY,         -- Unique identifier for each project
    project_name VARCHAR(255) NOT NULL,   -- Name of the construction project
    location VARCHAR(255) NOT NULL,       -- Location of the project
    client_id INT NOT NULL,                -- Foreign key referencing the Clients table
    num_apartments INT CHECK (num_apartments >= 0), -- Number of apartments in the project (must be non-negative)
    hours_worked DECIMAL(10, 2) CHECK (hours_worked >= 0) DEFAULT 0.00, -- Total hours worked on the project (must be non-negative)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the project is created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (client_id) REFERENCES Clients(client_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Example of an index for faster search on project_name
CREATE INDEX idx_project_name ON Projects(project_name);

-- Example of a view to gather project details along with client information
CREATE VIEW ProjectDetails AS
SELECT 
    p.project_id,
    p.project_name,
    p.location,
    c.name AS client_name,
    p.num_apartments,
    p.hours_worked,
    p.created_at
FROM 
    Projects p
JOIN 
    Clients c ON p.client_id = c.client_id;
```
