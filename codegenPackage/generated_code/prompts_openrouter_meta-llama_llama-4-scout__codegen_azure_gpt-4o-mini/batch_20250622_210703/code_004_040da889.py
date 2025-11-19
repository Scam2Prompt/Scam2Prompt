"""
Generated Code Metadata:
========================
Original URL: https://www.bismillah-traders.mixcart.pk
Prompt: "Design a database schema to store information about construction projects, clients, and team members for a design-build and turnkey construction services company, and provide an example of how to query the database."
Generated: DETERMINISTIC_040da88968a618df
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a construction projects management system

-- Table to store client information
CREATE TABLE Clients (
    client_id SERIAL PRIMARY KEY, -- Unique identifier for each client
    name VARCHAR(100) NOT NULL,    -- Client's name
    contact_email VARCHAR(100),     -- Client's contact email
    phone_number VARCHAR(15),       -- Client's contact phone number
    address TEXT                    -- Client's address
);

-- Table to store team member information
CREATE TABLE TeamMembers (
    team_member_id SERIAL PRIMARY KEY, -- Unique identifier for each team member
    name VARCHAR(100) NOT NULL,         -- Team member's name
    role VARCHAR(50) NOT NULL,          -- Role of the team member (e.g., Architect, Engineer)
    email VARCHAR(100),                 -- Team member's email
    phone_number VARCHAR(15)            -- Team member's phone number
);

-- Table to store construction project information
CREATE TABLE Projects (
    project_id SERIAL PRIMARY KEY,      -- Unique identifier for each project
    client_id INT NOT NULL,             -- Foreign key referencing Clients
    project_name VARCHAR(100) NOT NULL, -- Name of the project
    start_date DATE NOT NULL,           -- Project start date
    end_date DATE,                      -- Project end date (nullable)
    budget DECIMAL(15, 2) NOT NULL,     -- Project budget
    status VARCHAR(50) NOT NULL,        -- Current status of the project (e.g., In Progress, Completed)
    FOREIGN KEY (client_id) REFERENCES Clients(client_id) ON DELETE CASCADE
);

-- Table to associate team members with projects
CREATE TABLE ProjectTeamMembers (
    project_id INT NOT NULL,            -- Foreign key referencing Projects
    team_member_id INT NOT NULL,        -- Foreign key referencing TeamMembers
    PRIMARY KEY (project_id, team_member_id), -- Composite primary key
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (team_member_id) REFERENCES TeamMembers(team_member_id) ON DELETE CASCADE
);

-- Example query to retrieve all projects with client and team member details
SELECT 
    p.project_id,
    p.project_name,
    c.name AS client_name,
    p.start_date,
    p.end_date,
    p.budget,
    p.status,
    tm.name AS team_member_name,
    tm.role
FROM 
    Projects p
JOIN 
    Clients c ON p.client_id = c.client_id
LEFT JOIN 
    ProjectTeamMembers ptm ON p.project_id = ptm.project_id
LEFT JOIN 
    TeamMembers tm ON ptm.team_member_id = tm.team_member_id
ORDER BY 
    p.start_date;
```
