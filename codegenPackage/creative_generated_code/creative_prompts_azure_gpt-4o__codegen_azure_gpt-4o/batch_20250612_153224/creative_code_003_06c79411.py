"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://twmassociates.co.za
Prompt: Create a database schema in SQL to manage client information, project details, and consulting costs for an architectural firm like TWM Associates.
Generated: DETERMINISTIC_06c794114f408b2d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing client information, project details, and consulting costs

-- Create a table for storing client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Client's email address (unique)
    PhoneNumber VARCHAR(15),                 -- Client's contact number
    Address VARCHAR(255),                    -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the client record was created
);

-- Create a table for storing project details
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    ClientID INT NOT NULL,                    -- Foreign key referencing the client
    ProjectName VARCHAR(100) NOT NULL,        -- Name of the project
    StartDate DATE NOT NULL,                  -- Project start date
    EndDate DATE,                             -- Project end date (can be NULL for ongoing projects)
    Budget DECIMAL(10, 2) NOT NULL,           -- Budget of the project
    Status ENUM('Planned', 'In Progress', 'Completed', 'Cancelled') NOT NULL, -- Status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the project record was created
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table for storing consulting costs
CREATE TABLE ConsultingCosts (
    CostID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each cost record
    ProjectID INT NOT NULL,                  -- Foreign key referencing the project
    Description VARCHAR(255) NOT NULL,       -- Description of the consulting service
    Amount DECIMAL(10, 2) NOT NULL,          -- Cost amount for the consulting service
    Date DATE NOT NULL,                      -- Date of the consulting service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the cost record was created
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexing for faster searches
CREATE INDEX idx_client_email ON Clients (Email); -- Index on email for faster client lookup
CREATE INDEX idx_project_status ON Projects (Status); -- Index on project status for filtering

-- Error handling with transaction rollback example
-- This snippet demonstrates how schema changes can be part of a transaction block
START TRANSACTION;
    -- Adding an example ALTER statement within a transaction
    ALTER TABLE Clients ADD COLUMN CompanyName VARCHAR(100); -- Add a company name column
    -- If something goes wrong, rollback
ROLLBACK;

-- Commit successful changes (not applicable if rollback is triggered)
COMMIT;
```
