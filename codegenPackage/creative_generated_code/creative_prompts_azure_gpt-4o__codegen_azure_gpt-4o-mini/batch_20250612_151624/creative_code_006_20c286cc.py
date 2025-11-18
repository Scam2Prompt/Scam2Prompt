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
-- Create a database schema for cabinetry projects inspired by United Cabinetry's workflow

-- Drop existing tables if they exist to avoid conflicts
DROP TABLE IF EXISTS AfterSalesSupport;
DROP TABLE IF EXISTS TradesCoordination;
DROP TABLE IF EXISTS DesignSpecifications;
DROP TABLE IF EXISTS CabinetryProjects;

-- Create table to store cabinetry projects
CREATE TABLE CabinetryProjects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    ProjectName VARCHAR(255) NOT NULL, -- Name of the cabinetry project
    ClientName VARCHAR(255) NOT NULL, -- Name of the client
    StartDate DATE NOT NULL, -- Start date of the project
    EndDate DATE, -- End date of the project
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') NOT NULL, -- Current status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the project was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of when the project was last updated
);

-- Create table for design specifications
CREATE TABLE DesignSpecifications (
    DesignID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each design specification
    ProjectID INT NOT NULL, -- Foreign key referencing the project
    DesignDetails TEXT NOT NULL, -- Detailed description of the design
    Material VARCHAR(100) NOT NULL, -- Material used for the cabinetry
    Color VARCHAR(100) NOT NULL, -- Color of the cabinetry
    Dimensions VARCHAR(100) NOT NULL, -- Dimensions of the cabinetry
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the design specification was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of when the design specification was last updated
    FOREIGN KEY (ProjectID) REFERENCES CabinetryProjects(ProjectID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create table for trades coordination
CREATE TABLE TradesCoordination (
    TradeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each trade coordination entry
    ProjectID INT NOT NULL, -- Foreign key referencing the project
    TradeType VARCHAR(100) NOT NULL, -- Type of trade (e.g., installation, plumbing, electrical)
    CoordinationDetails TEXT NOT NULL, -- Detailed description of the coordination
    ScheduledDate DATE NOT NULL, -- Date when the trade is scheduled
    Status ENUM('Scheduled', 'Completed', 'Cancelled') NOT NULL, -- Status of the trade coordination
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the coordination entry was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of when the coordination entry was last updated
    FOREIGN KEY (ProjectID) REFERENCES CabinetryProjects(ProjectID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create table for after-sales support
CREATE TABLE AfterSalesSupport (
    SupportID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each after-sales support entry
    ProjectID INT NOT NULL, -- Foreign key referencing the project
    SupportDetails TEXT NOT NULL, -- Detailed description of the support provided
    RequestDate DATE NOT NULL, -- Date when the support request was made
    ResolutionDate DATE, -- Date when the support was resolved
    Status ENUM('Pending', 'Resolved', 'Closed') NOT NULL, -- Status of the after-sales support
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the support entry was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of when the support entry was last updated
    FOREIGN KEY (ProjectID) REFERENCES CabinetryProjects(ProjectID) ON DELETE CASCADE -- Ensures referential integrity
);
```
