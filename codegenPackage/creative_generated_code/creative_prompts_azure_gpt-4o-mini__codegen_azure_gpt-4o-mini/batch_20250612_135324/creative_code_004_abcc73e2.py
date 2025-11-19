"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://strk.site
Prompt: Design a database schema for storing information about completed renovation projects, including client details, project scope, and costs, inspired by the project management approach mentioned on the STRK site.
Generated: DETERMINISTIC_abcc73e29fa08c44
Batch ID: 20250612_135324
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing information about completed renovation projects

-- Drop existing tables if they exist for a clean slate
DROP TABLE IF EXISTS Clients;
DROP TABLE IF EXISTS Projects;
DROP TABLE IF EXISTS ProjectCosts;

-- Table to store client details
CREATE TABLE Clients (
    client_id SERIAL PRIMARY KEY,          -- Unique identifier for each client
    name VARCHAR(100) NOT NULL,            -- Client's full name
    email VARCHAR(100) UNIQUE NOT NULL,    -- Client's email address (must be unique)
    phone VARCHAR(15),                      -- Client's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the client was added
);

-- Table to store project details
CREATE TABLE Projects (
    project_id SERIAL PRIMARY KEY,          -- Unique identifier for each project
    client_id INT NOT NULL,                 -- Foreign key referencing Clients table
    project_name VARCHAR(100) NOT NULL,     -- Name of the renovation project
    project_scope TEXT NOT NULL,             -- Description of the project scope
    start_date DATE NOT NULL,                -- Date project started
    end_date DATE NOT NULL,                  -- Date project completed
    status VARCHAR(50) DEFAULT 'Completed',  -- Current status of the project
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the project was added
    FOREIGN KEY (client_id) REFERENCES Clients(client_id) ON DELETE CASCADE -- Maintain referential integrity
);

-- Table to store project cost details
CREATE TABLE ProjectCosts (
    cost_id SERIAL PRIMARY KEY,              -- Unique identifier for each cost entry
    project_id INT NOT NULL,                  -- Foreign key referencing Projects table
    cost_description VARCHAR(100) NOT NULL,  -- Description of the cost (e.g., materials, labor)
    amount DECIMAL(10, 2) NOT NULL,          -- Amount of the cost
    incurred_date DATE NOT NULL,              -- Date the cost was incurred
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the cost entry was added
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE -- Maintain referential integrity
);

-- Sample query to retrieve completed projects with client details and costs
-- This can be utilized to fetch relevant project data
SELECT 
    p.project_name, 
    c.name AS client_name, 
    c.email AS client_email, 
    SUM(pc.amount) AS total_cost,
    p.start_date,
    p.end_date
FROM 
    Projects p
JOIN 
    Clients c ON p.client_id = c.client_id
JOIN 
    ProjectCosts pc ON p.project_id = pc.project_id
WHERE 
    p.status = 'Completed'
GROUP BY 
    p.project_id, c.client_id;
```
