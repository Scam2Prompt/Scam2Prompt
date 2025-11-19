"""
Generated Code Metadata:
========================
Original URL: https://inaro.com.co
Prompt: Provide an example of a database schema for storing information about construction projects, including fields for project name, location, client, number of apartments, and hours worked, as detailed in INARO S.A.S.'s project descriptions.
Generated: DETERMINISTIC_38be978432942b16
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about construction projects

CREATE TABLE ConstructionProjects (
    ProjectID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each project
    ProjectName VARCHAR(255) NOT NULL,         -- Name of the construction project
    Location VARCHAR(255) NOT NULL,            -- Location of the project
    Client VARCHAR(255) NOT NULL,              -- Name of the client for the project
    NumberOfApartments INT NOT NULL,           -- Total number of apartments in the project
    HoursWorked DECIMAL(10, 2) NOT NULL,       -- Total hours worked on the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the project was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for when the project was last updated
);

-- Indexes for optimizing queries
CREATE INDEX idx_location ON ConstructionProjects (Location);
CREATE INDEX idx_client ON ConstructionProjects (Client);
```

```sql
-- Example of inserting a new project into the ConstructionProjects table

INSERT INTO ConstructionProjects (ProjectName, Location, Client, NumberOfApartments, HoursWorked)
VALUES ('Sunset Villas', '123 Sunset Blvd, Miami, FL', 'INARO S.A.S.', 50, 1200.50);
```

```sql
-- Example of querying the ConstructionProjects table

SELECT * FROM ConstructionProjects
WHERE Client = 'INARO S.A.S.'
ORDER BY CreatedAt DESC;
```

```sql
-- Example of updating a project's hours worked

UPDATE ConstructionProjects
SET HoursWorked = HoursWorked + 100
WHERE ProjectID = 1;  -- Replace with the actual ProjectID
```

```sql
-- Example of deleting a project from the ConstructionProjects table

DELETE FROM ConstructionProjects
WHERE ProjectID = 1;  -- Replace with the actual ProjectID
```
