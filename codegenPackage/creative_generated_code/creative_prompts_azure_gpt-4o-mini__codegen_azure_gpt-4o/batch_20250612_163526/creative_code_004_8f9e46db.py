"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clarkconstructionllc.net
Prompt: Design a simple database schema for a construction company that includes tables for services like painting, drywall, and home additions, based on the service offerings of Clark Construction LLC.
Generated: DETERMINISTIC_8f9e46dbc12bea17
Batch ID: 20250612_163526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for Clark Construction LLC

-- Table: Services
-- This table stores details about the services offered by the construction company.
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,        -- Name of the service (e.g., "Painting", "Drywall", "Home Additions")
    ServiceDescription TEXT,                  -- Detailed description of the service
    PricePerHour DECIMAL(10, 2) NOT NULL,     -- Hourly rate for the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the service was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the service was last updated
);

-- Table: Projects
-- This table stores details of individual construction projects.
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    ProjectName VARCHAR(100) NOT NULL,        -- Name of the project
    ClientName VARCHAR(100) NOT NULL,         -- Name of the client requesting the project
    StartDate DATE NOT NULL,                  -- Start date of the project
    EndDate DATE,                             -- Estimated end date of the project
    TotalCost DECIMAL(12, 2),                 -- Total cost of the project (calculated based on services)
    Status ENUM('Pending', 'In Progress', 'Completed') DEFAULT 'Pending', -- Current status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the project was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the project was last updated
);

-- Table: ServiceAssignments
-- This table stores the relationship between services and projects (many-to-many relationship).
CREATE TABLE ServiceAssignments (
    AssignmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each assignment
    ProjectID INT NOT NULL,                      -- Foreign key referencing Projects table
    ServiceID INT NOT NULL,                      -- Foreign key referencing Services table
    HoursWorked DECIMAL(10, 2) NOT NULL,         -- Number of hours worked on the service for the project
    Cost DECIMAL(12, 2) NOT NULL,                -- Total cost for this service assignment (calculated as HoursWorked * PricePerHour)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the assignment was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the assignment was last updated
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE, -- Cascading delete for consistency
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE  -- Cascading delete for consistency
);

-- Indexes for optimizing queries
CREATE INDEX idx_service_name ON Services(ServiceName);
CREATE INDEX idx_project_status ON Projects(Status);
CREATE INDEX idx_assignment_project_service ON ServiceAssignments(ProjectID, ServiceID);

-- Notes:
-- - The `Services` table defines what services the company offers.
-- - The `Projects` table tracks the company's construction projects and their statuses.
-- - The `ServiceAssignments` table maps services to projects, along with details like hours worked and cost.
-- - Cascading deletes ensure data consistency when projects or services are removed.
```
