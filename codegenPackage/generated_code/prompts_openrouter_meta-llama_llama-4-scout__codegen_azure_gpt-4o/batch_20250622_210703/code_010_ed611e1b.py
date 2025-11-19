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
-- Database Schema for Non-Profit Organizations

-- Table to store information about non-profit organizations
CREATE TABLE NonProfitOrganizations (
    OrganizationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each organization
    Name VARCHAR(255) NOT NULL,                   -- Name of the organization
    Mission TEXT NOT NULL,                        -- Mission statement of the organization
    Vision TEXT NOT NULL,                         -- Vision statement of the organization
    Values TEXT NOT NULL,                         -- Core values of the organization
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Table to store information about programs run by non-profit organizations
CREATE TABLE Programs (
    ProgramID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each program
    OrganizationID INT NOT NULL,                  -- Foreign key referencing NonProfitOrganizations
    Name VARCHAR(255) NOT NULL,                   -- Name of the program
    Description TEXT NOT NULL,                    -- Description of the program
    StartDate DATE NOT NULL,                      -- Start date of the program
    EndDate DATE NULL,                            -- End date of the program (nullable for ongoing programs)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the record was last updated
    FOREIGN KEY (OrganizationID) REFERENCES NonProfitOrganizations(OrganizationID) ON DELETE CASCADE -- Cascade delete
);

-- SQL Query to retrieve all information about non-profit organizations and their programs
SELECT 
    o.OrganizationID,
    o.Name AS OrganizationName,
    o.Mission,
    o.Vision,
    o.Values,
    p.ProgramID,
    p.Name AS ProgramName,
    p.Description AS ProgramDescription,
    p.StartDate,
    p.EndDate
FROM 
    NonProfitOrganizations o
LEFT JOIN 
    Programs p
ON 
    o.OrganizationID = p.OrganizationID
ORDER BY 
    o.Name, p.StartDate; -- Order by organization name and program start date
```
