"""
Generated Code Metadata:
========================
Original URL: https://proarteasa.com
Prompt: "Design a database schema for storing information about real estate projects, including details about lots, financing options, and construction progress."
Generated: DETERMINISTIC_7b014056642aaf2e
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about real estate projects

-- Table to store information about real estate projects
CREATE TABLE RealEstateProjects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    ProjectName VARCHAR(255) NOT NULL,        -- Name of the real estate project
    Location VARCHAR(255) NOT NULL,           -- Location of the project
    StartDate DATE NOT NULL,                  -- Start date of the project
    EndDate DATE,                             -- End date of the project (nullable for ongoing projects)
    Status ENUM('Planned', 'In Progress', 'Completed') NOT NULL, -- Current status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store information about lots within a project
CREATE TABLE Lots (
    LotID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each lot
    ProjectID INT NOT NULL,                  -- Foreign key referencing RealEstateProjects
    LotNumber VARCHAR(50) NOT NULL,          -- Lot number or identifier
    Size DECIMAL(10, 2) NOT NULL,            -- Size of the lot (e.g., in square meters)
    Price DECIMAL(15, 2) NOT NULL,           -- Price of the lot
    Status ENUM('Available', 'Sold', 'Reserved') NOT NULL, -- Current status of the lot
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (ProjectID) REFERENCES RealEstateProjects(ProjectID) ON DELETE CASCADE -- Cascade delete if project is deleted
);

-- Table to store financing options for a project
CREATE TABLE FinancingOptions (
    FinancingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each financing option
    ProjectID INT NOT NULL,                     -- Foreign key referencing RealEstateProjects
    OptionName VARCHAR(255) NOT NULL,           -- Name of the financing option
    Description TEXT,                           -- Description of the financing option
    InterestRate DECIMAL(5, 2),                 -- Interest rate for the financing option
    DurationMonths INT,                         -- Duration of the financing option in months
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (ProjectID) REFERENCES RealEstateProjects(ProjectID) ON DELETE CASCADE -- Cascade delete if project is deleted
);

-- Table to store construction progress for a project
CREATE TABLE ConstructionProgress (
    ProgressID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each progress record
    ProjectID INT NOT NULL,                    -- Foreign key referencing RealEstateProjects
    Milestone VARCHAR(255) NOT NULL,           -- Description of the milestone
    CompletionDate DATE,                       -- Date the milestone was completed
    PercentageCompleted DECIMAL(5, 2) NOT NULL, -- Percentage of the project completed
    Notes TEXT,                                -- Additional notes about the milestone
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (ProjectID) REFERENCES RealEstateProjects(ProjectID) ON DELETE CASCADE -- Cascade delete if project is deleted
);

-- Indexes for optimizing queries
CREATE INDEX idx_project_location ON RealEstateProjects(Location); -- Index for querying projects by location
CREATE INDEX idx_lot_status ON Lots(Status); -- Index for querying lots by status
CREATE INDEX idx_financing_option_name ON FinancingOptions(OptionName); -- Index for querying financing options by name
CREATE INDEX idx_progress_completion_date ON ConstructionProgress(CompletionDate); -- Index for querying progress by completion date
```
