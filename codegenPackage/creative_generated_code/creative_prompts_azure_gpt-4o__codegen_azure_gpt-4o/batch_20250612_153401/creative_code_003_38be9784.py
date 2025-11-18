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
-- Database schema for storing information about construction projects

-- Create a table to store project details
CREATE TABLE ConstructionProjects (
    ProjectID SERIAL PRIMARY KEY, -- Unique identifier for each project
    ProjectName VARCHAR(255) NOT NULL, -- Name of the construction project
    Location VARCHAR(255) NOT NULL, -- Location of the project
    ClientName VARCHAR(255) NOT NULL, -- Name of the client
    NumberOfApartments INT CHECK(NumberOfApartments >= 0), -- Number of apartments in the project, must be non-negative
    HoursWorked INT CHECK(HoursWorked >= 0), -- Total hours worked on the project, must be non-negative
    CreatedAt TIMESTAMP DEFAULT NOW(), -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT NOW() -- Timestamp for when the record was last updated
);

-- Add a trigger to automatically update the UpdatedAt field on update
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.UpdatedAt = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER set_updated_at
BEFORE UPDATE ON ConstructionProjects
FOR EACH ROW
EXECUTE FUNCTION update_timestamp();

-- Example query to insert data into the ConstructionProjects table
-- INSERT INTO ConstructionProjects (ProjectName, Location, ClientName, NumberOfApartments, HoursWorked)
-- VALUES ('Skyview Towers', 'New York, NY', 'INARO S.A.S.', 120, 5000);
```
