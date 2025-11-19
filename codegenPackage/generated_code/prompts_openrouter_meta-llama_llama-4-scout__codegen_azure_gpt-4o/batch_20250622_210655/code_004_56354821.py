"""
Generated Code Metadata:
========================
Original URL: https://bismillah-traders.com
Prompt: "Design a database schema to store information about construction projects, including details like project type (residential, commercial, etc.), location, and services offered (design-build, turnkey, etc.), similar to Bismillah Traders' project portfolio."
Generated: DETERMINISTIC_563548211b7ca919
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about construction projects

-- Table to store project types (e.g., residential, commercial, etc.)
CREATE TABLE ProjectTypes (
    ProjectTypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for project type
    TypeName VARCHAR(100) NOT NULL,              -- Name of the project type
    Description TEXT                             -- Optional description of the project type
);

-- Table to store services offered (e.g., design-build, turnkey, etc.)
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for service
    ServiceName VARCHAR(100) NOT NULL,           -- Name of the service
    Description TEXT                             -- Optional description of the service
);

-- Table to store construction projects
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for the project
    ProjectName VARCHAR(255) NOT NULL,           -- Name of the project
    ProjectTypeID INT NOT NULL,                  -- Foreign key referencing ProjectTypes
    Location VARCHAR(255) NOT NULL,              -- Location of the project
    StartDate DATE,                              -- Optional start date of the project
    EndDate DATE,                                -- Optional end date of the project
    Budget DECIMAL(15, 2),                       -- Optional budget for the project
    FOREIGN KEY (ProjectTypeID) REFERENCES ProjectTypes(ProjectTypeID) ON DELETE CASCADE
);

-- Junction table to associate projects with services offered
CREATE TABLE ProjectServices (
    ProjectServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the association
    ProjectID INT NOT NULL,                          -- Foreign key referencing Projects
    ServiceID INT NOT NULL,                          -- Foreign key referencing Services
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE,
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE
);

-- Indexes for faster querying
CREATE INDEX idx_project_type ON Projects(ProjectTypeID);
CREATE INDEX idx_project_service ON ProjectServices(ProjectID, ServiceID);

-- Example of error handling: Ensure all required fields are provided
-- This is handled by NOT NULL constraints in the schema above.
```
