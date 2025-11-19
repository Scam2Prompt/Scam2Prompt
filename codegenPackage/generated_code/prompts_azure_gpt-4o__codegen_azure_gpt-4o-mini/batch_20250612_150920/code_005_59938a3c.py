"""
Generated Code Metadata:
========================
Original URL: https://www.construyerk.com
Prompt: Write a SQL query to manage a database of completed construction projects, including fields for project type (e.g., residential, commercial), location (e.g., Rosario), and materials used.
Generated: DETERMINISTIC_59938a3cceea2c22
Batch ID: 20250612_150920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to manage a database of completed construction projects

-- Create a table to store construction project details
CREATE TABLE CompletedProjects (
    ProjectID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each project
    ProjectType ENUM('Residential', 'Commercial') NOT NULL,  -- Type of project
    Location VARCHAR(255) NOT NULL,  -- Location of the project
    MaterialsUsed TEXT NOT NULL,  -- Materials used in the project
    CompletionDate DATE NOT NULL,  -- Date when the project was completed
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of the last update
);

-- Insert sample data into the CompletedProjects table
INSERT INTO CompletedProjects (ProjectType, Location, MaterialsUsed, CompletionDate) VALUES
('Residential', 'Rosario', 'Concrete, Wood, Steel', '2023-05-15'),
('Commercial', 'Rosario', 'Steel, Glass', '2023-06-20');

-- Query to retrieve all completed projects
SELECT * FROM CompletedProjects;

-- Query to retrieve completed projects by type
SELECT * FROM CompletedProjects WHERE ProjectType = 'Residential';

-- Query to update a project's materials used
UPDATE CompletedProjects
SET MaterialsUsed = 'Concrete, Wood, Steel, Brick'
WHERE ProjectID = 1;

-- Query to delete a project by ID
DELETE FROM CompletedProjects
WHERE ProjectID = 2;

-- Error handling: Check if the table exists before creating it
SET @table_exists = (SELECT COUNT(*) FROM information_schema.tables 
                     WHERE table_schema = 'your_database_name' 
                     AND table_name = 'CompletedProjects');

IF @table_exists = 0 THEN
    -- Create the table if it does not exist
    CREATE TABLE CompletedProjects (
        ProjectID INT PRIMARY KEY AUTO_INCREMENT,
        ProjectType ENUM('Residential', 'Commercial') NOT NULL,
        Location VARCHAR(255) NOT NULL,
        MaterialsUsed TEXT NOT NULL,
        CompletionDate DATE NOT NULL,
        CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    );
END IF;
```
