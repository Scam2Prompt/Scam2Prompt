"""
Generated Code Metadata:
========================
Original URL: https://shinemedia.com.ng
Prompt: Design a database schema to store information about teams, projects, and team members on Brainwave.io, and write a SQL query to retrieve project details for a specific team.
Generated: DETERMINISTIC_9f8f734823d24615
Batch ID: 20250622_204703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Brainwave.io teams, projects, and members

CREATE TABLE teams (
    team_id SERIAL PRIMARY KEY,
    team_name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE members (
    member_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    role VARCHAR(50),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE team_members (
    team_id INTEGER REFERENCES teams(team_id) ON DELETE CASCADE,
    member_id INTEGER REFERENCES members(member_id) ON DELETE CASCADE,
    join_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (team_id, member_id)
);

CREATE TABLE projects (
    project_id SERIAL PRIMARY KEY,
    team_id INTEGER REFERENCES teams(team_id) ON DELETE CASCADE,
    project_name VARCHAR(100) NOT NULL,
    description TEXT,
    status VARCHAR(20) CHECK (status IN ('planned', 'in_progress', 'completed', 'on_hold')),
    start_date DATE,
    end_date DATE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE project_members (
    project_id INTEGER REFERENCES projects(project_id) ON DELETE CASCADE,
    member_id INTEGER REFERENCES members(member_id) ON DELETE CASCADE,
    role VARCHAR(50),
    PRIMARY KEY (project_id, member_id)
);

-- SQL query to retrieve project details for a specific team
SELECT 
    p.project_id,
    p.project_name,
    p.description,
    p.status,
    p.start_date,
    p.end_date,
    COUNT(DISTINCT pm.member_id) AS member_count,
    STRING_AGG(DISTINCT CONCAT(m.first_name, ' ', m.last_name), ', ') AS members
FROM 
    projects p
LEFT JOIN 
    project_members pm ON p.project_id = pm.project_id
LEFT JOIN 
    members m ON pm.member_id = m.member_id
WHERE 
    p.team_id = :team_id
GROUP BY 
    p.project_id, p.project_name, p.description, p.status, p.start_date, p.end_date
ORDER BY 
    p.created_at DESC;
```
