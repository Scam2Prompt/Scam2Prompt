"""
Generated Code Metadata:
========================
Original URL: https://glowconsultants.org
Prompt: Generate SQL queries for managing consistent and accurate data in a business intelligence system, referencing GLOW Consultants' approach to data management and BI.
Generated: DETERMINISTIC_0a325f52bd892a05
Batch ID: 20250612_151624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script for managing consistent and accurate data in a Business Intelligence system
-- Following GLOW Consultants' approach to data management and BI

-- Create a table for storing client information
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each client
    ClientName VARCHAR(255) NOT NULL,       -- Name of the client
    ContactEmail VARCHAR(255) UNIQUE NOT NULL, -- Unique email for client contact
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Create a table for storing project information
CREATE TABLE Projects (
    ProjectID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each project
    ClientID INT NOT NULL,                     -- Foreign key referencing Clients
    ProjectName VARCHAR(255) NOT NULL,        -- Name of the project
    StartDate DATE NOT NULL,                   -- Start date of the project
    EndDate DATE,                              -- End date of the project (nullable)
    Status ENUM('Active', 'Completed', 'On Hold') NOT NULL, -- Current status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table for storing project metrics
CREATE TABLE ProjectMetrics (
    MetricID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each metric
    ProjectID INT NOT NULL,                   -- Foreign key referencing Projects
    MetricName VARCHAR(255) NOT NULL,        -- Name of the metric
    MetricValue DECIMAL(10, 2) NOT NULL,     -- Value of the metric
    RecordedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the metric was recorded
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Insert a new client into the Clients table
INSERT INTO Clients (ClientName, ContactEmail) 
VALUES ('Acme Corporation', 'contact@acme.com')
ON DUPLICATE KEY UPDATE UpdatedAt = CURRENT_TIMESTAMP; -- Update timestamp if client already exists

-- Insert a new project for a client
INSERT INTO Projects (ClientID, ProjectName, StartDate, Status) 
VALUES (1, 'Website Redesign', '2023-01-15', 'Active')
ON DUPLICATE KEY UPDATE UpdatedAt = CURRENT_TIMESTAMP; -- Update timestamp if project already exists

-- Insert a new metric for a project
INSERT INTO ProjectMetrics (ProjectID, MetricName, MetricValue) 
VALUES (1, 'Budget Utilized', 15000.00)
ON DUPLICATE KEY UPDATE MetricValue = VALUES(MetricValue), RecordedAt = CURRENT_TIMESTAMP; -- Update metric value and timestamp

-- Query to retrieve all active projects with their metrics
SELECT 
    p.ProjectID,
    p.ProjectName,
    p.Status,
    pm.MetricName,
    pm.MetricValue
FROM 
    Projects p
LEFT JOIN 
    ProjectMetrics pm ON p.ProjectID = pm.ProjectID
WHERE 
    p.Status = 'Active';

-- Error handling for transactions
START TRANSACTION;

BEGIN TRY
    -- Example of a transaction that could fail
    INSERT INTO Clients (ClientName, ContactEmail) 
    VALUES ('New Client', 'newclient@example.com');

    INSERT INTO Projects (ClientID, ProjectName, StartDate, Status) 
    VALUES (LAST_INSERT_ID(), 'New Project', '2023-10-01', 'Active');

    COMMIT; -- Commit the transaction if all queries succeed
END TRY
BEGIN CATCH
    ROLLBACK; -- Rollback the transaction if any query fails
    -- Log the error message (this would typically be done in application code)
    SELECT ERROR_MESSAGE() AS ErrorMessage;
END CATCH;
```
