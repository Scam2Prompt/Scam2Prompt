"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unitedcabinetry.com.au
Prompt: Create a database schema in SQL to store cabinetry project details, including design specifications, trades coordination, and after-sales support, inspired by United Cabinetry's workflow.
Generated: DETERMINISTIC_20c286cc776ecfa9
Batch ID: 20250612_151624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for cabinetry project details inspired by United Cabinetry's workflow.

-- Table to store details of cabinetry projects
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each project
    ProjectName VARCHAR(255) NOT NULL,             -- Name of the project
    CustomerName VARCHAR(255) NOT NULL,            -- Name of the customer
    StartDate DATE NOT NULL,                       -- Start date of the project
    EndDate DATE,                                  -- End date of the project (nullable)
    Status ENUM('Planning', 'In Progress', 'Completed', 'On Hold') DEFAULT 'Planning', -- Current status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the project was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the project was last updated
);

-- Table to store design specifications for each project
CREATE TABLE DesignSpecifications (
    SpecificationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each specification
    ProjectID INT NOT NULL,                         -- Foreign key referencing Projects table
    CabinetType VARCHAR(255) NOT NULL,              -- Type of cabinetry (e.g., kitchen, bathroom, custom)
    Material VARCHAR(255) NOT NULL,                 -- Material used (e.g., oak, maple, plywood)
    Dimensions VARCHAR(255) NOT NULL,               -- Dimensions of the cabinetry
    Color VARCHAR(255),                             -- Color of the cabinetry (nullable)
    DesignNotes TEXT,                               -- Additional notes for the design (nullable)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp when the specification was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the specification was last updated
    CONSTRAINT FK_DesignSpecifications_Project FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE
);

-- Table to store trades coordination details
CREATE TABLE TradesCoordination (
    CoordinationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each coordination entry
    ProjectID INT NOT NULL,                        -- Foreign key referencing Projects table
    TradeType ENUM('Electrician', 'Plumber', 'Painter', 'Carpenter') NOT NULL, -- Type of trade
    ContactName VARCHAR(255) NOT NULL,             -- Name of the trade contact
    ContactPhone VARCHAR(20),                      -- Phone number of the trade contact (nullable)
    ScheduledDate DATE NOT NULL,                   -- Date when the trade is scheduled
    Notes TEXT,                                    -- Additional notes (nullable)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the coordination entry was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the coordination entry was last updated
    CONSTRAINT FK_TradesCoordination_Project FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE
);

-- Table to store details of after-sales support
CREATE TABLE AfterSalesSupport (
    SupportID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each support entry
    ProjectID INT NOT NULL,                        -- Foreign key referencing Projects table
    IssueDescription TEXT NOT NULL,                -- Description of the issue reported
    ResolutionStatus ENUM('Pending', 'Resolved', 'Closed') DEFAULT 'Pending', -- Status of the resolution process
    ResolutionNotes TEXT,                          -- Notes about the resolution process (nullable)
    ReportedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the issue was reported
    ResolvedDate TIMESTAMP,                        -- Timestamp when the issue was resolved (nullable)
    CONSTRAINT FK_AfterSalesSupport_Project FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE
);

-- Ensure proper indexing and query optimization
CREATE INDEX IDX_Projects_Status ON Projects(Status); -- Index for querying projects by status
CREATE INDEX IDX_DesignSpecifications_ProjectID ON DesignSpecifications(ProjectID); -- Index for design specs lookup
CREATE INDEX IDX_TradesCoordination_ProjectID ON TradesCoordination(ProjectID); -- Index for trades coordination lookup
CREATE INDEX IDX_AfterSalesSupport_ProjectID ON AfterSalesSupport(ProjectID); -- Index for after-sales support lookup
```
