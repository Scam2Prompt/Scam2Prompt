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
-- schema.sql

-- Create database schema for Brainwave.io
CREATE DATABASE brainwave;

-- Use brainwave database
USE brainwave;

-- Create teams table
CREATE TABLE teams (
  team_id INT AUTO_INCREMENT,
  team_name VARCHAR(255) NOT NULL,
  team_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (team_id)
);

-- Create projects table
CREATE TABLE projects (
  project_id INT AUTO_INCREMENT,
  team_id INT NOT NULL,
  project_name VARCHAR(255) NOT NULL,
  project_description TEXT,
  start_date DATE,
  end_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (project_id),
  FOREIGN KEY (team_id) REFERENCES teams(team_id) ON DELETE CASCADE
);

-- Create team_members table
CREATE TABLE team_members (
  member_id INT AUTO_INCREMENT,
  team_id INT NOT NULL,
  member_name VARCHAR(255) NOT NULL,
  member_email VARCHAR(255) UNIQUE NOT NULL,
  role VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (member_id),
  FOREIGN KEY (team_id) REFERENCES teams(team_id) ON DELETE CASCADE
);

-- Create project_members table (many-to-many relationship)
CREATE TABLE project_members (
  project_id INT NOT NULL,
  member_id INT NOT NULL,
  PRIMARY KEY (project_id, member_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
  FOREIGN KEY (member_id) REFERENCES team_members(member_id) ON DELETE CASCADE
);

-- query.sql

-- Retrieve project details for a specific team
DELIMITER //

CREATE PROCEDURE GetProjectDetailsByTeam(IN teamId INT)
BEGIN
  SELECT 
    p.project_id,
    p.project_name,
    p.project_description,
    p.start_date,
    p.end_date,
    tm.member_name AS project_manager,
    tm.member_email AS project_manager_email
  FROM 
    projects p
  LEFT JOIN 
    team_members tm ON p.team_id = tm.team_id AND tm.role = 'Project Manager'
  WHERE 
    p.team_id = teamId;
END //

DELIMITER ;

-- Call the stored procedure
CALL GetProjectDetailsByTeam(1);
```

```sql
-- Alternatively, you can use a SELECT statement
-- Retrieve project details for a specific team
SELECT 
  p.project_id,
  p.project_name,
  p.project_description,
  p.start_date,
  p.end_date,
  tm.member_name AS project_manager,
  tm.member_email AS project_manager_email
FROM 
  projects p
LEFT JOIN 
  team_members tm ON p.team_id = tm.team_id AND tm.role = 'Project Manager'
WHERE 
  p.team_id = 1;
```
