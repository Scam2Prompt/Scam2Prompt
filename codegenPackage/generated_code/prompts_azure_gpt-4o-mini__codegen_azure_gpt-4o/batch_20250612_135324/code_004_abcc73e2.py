"""
Generated Code Metadata:
========================
Original URL: https://strk.site
Prompt: Design a database schema for storing information about completed renovation projects, including client details, project scope, and costs, inspired by the project management approach mentioned on the STRK site.
Generated: DETERMINISTIC_abcc73e29fa08c44
Batch ID: 20250612_135324
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about completed renovation projects

-- Table to store client details
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Client's email address (must be unique)
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    Address TEXT                             -- Client's address
);

-- Table to store project details
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    ClientID INT NOT NULL,                    -- Foreign key referencing the Clients table
    ProjectName VARCHAR(100) NOT NULL,        -- Name of the renovation project
    ProjectScope TEXT NOT NULL,               -- Detailed description of the project scope
    StartDate DATE NOT NULL,                  -- Project start date
    EndDate DATE,                             -- Project end date (nullable for ongoing projects)
    TotalCost DECIMAL(10, 2) NOT NULL,        -- Total cost of the project
    Status ENUM('Completed', 'In Progress', 'Cancelled') NOT NULL, -- Current status of the project
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Cascade delete if client is removed
);

-- Table to store cost breakdown for each project
CREATE TABLE CostBreakdown (
    CostID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each cost entry
    ProjectID INT NOT NULL,                -- Foreign key referencing the Projects table
    Description VARCHAR(255) NOT NULL,     -- Description of the cost item (e.g., materials, labor)
    Amount DECIMAL(10, 2) NOT NULL,        -- Amount for the cost item
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Cascade delete if project is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_client_email ON Clients(Email); -- Index for quick lookup by email
CREATE INDEX idx_project_status ON Projects(Status); -- Index for filtering projects by status

-- Error handling considerations:
-- - Ensure proper validation in application code before inserting data into these tables.
-- - Use transactions in the application layer to maintain data integrity during complex operations.
```
