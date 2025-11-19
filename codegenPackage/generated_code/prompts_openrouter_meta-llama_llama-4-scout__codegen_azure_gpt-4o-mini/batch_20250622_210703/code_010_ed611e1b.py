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
-- Database schema for storing information about non-profit organizations

-- Create a table to store non-profit organizations
CREATE TABLE NonProfitOrganizations (
    id SERIAL PRIMARY KEY, -- Unique identifier for each organization
    name VARCHAR(255) NOT NULL, -- Name of the organization
    mission TEXT NOT NULL, -- Mission statement of the organization
    vision TEXT NOT NULL, -- Vision statement of the organization
    values TEXT NOT NULL, -- Core values of the organization
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Create a table to store programs associated with non-profit organizations
CREATE TABLE Programs (
    id SERIAL PRIMARY KEY, -- Unique identifier for each program
    organization_id INT NOT NULL, -- Foreign key referencing the NonProfitOrganizations table
    name VARCHAR(255) NOT NULL, -- Name of the program
    description TEXT, -- Description of the program
    start_date DATE, -- Start date of the program
    end_date DATE, -- End date of the program
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of the last update
    FOREIGN KEY (organization_id) REFERENCES NonProfitOrganizations(id) ON DELETE CASCADE -- Ensures referential integrity
);

-- SQL query to retrieve all non-profit organizations along with their programs
SELECT 
    n.id AS organization_id,
    n.name AS organization_name,
    n.mission,
    n.vision,
    n.values,
    p.id AS program_id,
    p.name AS program_name,
    p.description AS program_description,
    p.start_date,
    p.end_date
FROM 
    NonProfitOrganizations n
LEFT JOIN 
    Programs p ON n.id = p.organization_id
ORDER BY 
    n.name, p.name; -- Order by organization name and program name
```
