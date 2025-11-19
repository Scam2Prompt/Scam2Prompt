"""
Generated Code Metadata:
========================
Original URL: https://tda.org.sa
Prompt: Design a database schema to store information about non-profit organizations, including their mission, vision, values, and programs, and write a SQL query to retrieve the data.
Generated: DETERMINISTIC_ed611e1bfd0f56f4
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema
CREATE DATABASE non_profits;

-- Use the database
USE non_profits;

-- Create table for non-profit organizations
CREATE TABLE organizations (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  mission TEXT,
  vision TEXT,
  values TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for programs
CREATE TABLE programs (
  id INT AUTO_INCREMENT,
  organization_id INT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (organization_id) REFERENCES organizations(id) ON DELETE CASCADE
);

-- Insert sample data
INSERT INTO organizations (name, mission, vision, values)
VALUES 
  ('Charity A', 'Mission of Charity A', 'Vision of Charity A', 'Values of Charity A'),
  ('Charity B', 'Mission of Charity B', 'Vision of Charity B', 'Values of Charity B');

INSERT INTO programs (organization_id, name, description)
VALUES 
  (1, 'Program 1', 'Description of Program 1'),
  (1, 'Program 2', 'Description of Program 2'),
  (2, 'Program 3', 'Description of Program 3');

-- Retrieve data SQL query
SELECT 
  o.id,
  o.name,
  o.mission,
  o.vision,
  o.values,
  p.id AS program_id,
  p.name AS program_name,
  p.description AS program_description
FROM 
  organizations o
  LEFT JOIN programs p ON o.id = p.organization_id
ORDER BY 
  o.id, p.id;

-- Stored procedure to retrieve organization data with programs
DELIMITER //
CREATE PROCEDURE GetOrganizationData()
BEGIN
  SELECT 
    o.id,
    o.name,
    o.mission,
    o.vision,
    o.values,
    p.id AS program_id,
    p.name AS program_name,
    p.description AS program_description
  FROM 
    organizations o
    LEFT JOIN programs p ON o.id = p.organization_id
  ORDER BY 
    o.id, p.id;
END//
DELIMITER ;

-- Call the stored procedure
CALL GetOrganizationData();
```
