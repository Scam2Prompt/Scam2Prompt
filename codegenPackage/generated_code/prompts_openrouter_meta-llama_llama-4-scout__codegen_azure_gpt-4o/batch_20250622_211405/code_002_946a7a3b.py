"""
Generated Code Metadata:
========================
Original URL: https://daddys-universitys.com
Prompt: "Generate a sample database schema for storing information about traditional buildings and their restoration projects, similar to those handled by Inaka Revive Solutions."
Generated: DETERMINISTIC_946a7a3bf886736e
Batch ID: 20250622_211405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about traditional buildings and their restoration projects

-- Create a table to store information about traditional buildings
CREATE TABLE TraditionalBuildings (
    BuildingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each building
    Name VARCHAR(255) NOT NULL,                -- Name of the building
    Location VARCHAR(255) NOT NULL,            -- Location of the building
    YearBuilt INT,                             -- Year the building was constructed
    ArchitecturalStyle VARCHAR(255),           -- Style of architecture
    HistoricalSignificance TEXT,               -- Description of historical significance
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table to store information about restoration projects
CREATE TABLE RestorationProjects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each project
    BuildingID INT NOT NULL,                   -- Foreign key referencing the building being restored
    ProjectName VARCHAR(255) NOT NULL,         -- Name of the restoration project
    StartDate DATE NOT NULL,                   -- Start date of the project
    EndDate DATE,                              -- End date of the project (nullable for ongoing projects)
    Budget DECIMAL(15, 2),                     -- Budget allocated for the project
    Description TEXT,                          -- Detailed description of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    CONSTRAINT FK_Building FOREIGN KEY (BuildingID) REFERENCES TraditionalBuildings(BuildingID) ON DELETE CASCADE
);

-- Create a table to store information about contractors involved in restoration projects
CREATE TABLE Contractors (
    ContractorID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each contractor
    Name VARCHAR(255) NOT NULL,                  -- Name of the contractor
    ContactInfo VARCHAR(255),                    -- Contact information (e.g., phone, email)
    Specialization VARCHAR(255),                 -- Area of expertise or specialization
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table to store the relationship between contractors and restoration projects
CREATE TABLE ProjectContractors (
    ProjectID INT NOT NULL,                      -- Foreign key referencing the restoration project
    ContractorID INT NOT NULL,                   -- Foreign key referencing the contractor
    Role VARCHAR(255),                           -- Role of the contractor in the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    PRIMARY KEY (ProjectID, ContractorID),       -- Composite primary key
    CONSTRAINT FK_Project FOREIGN KEY (ProjectID) REFERENCES RestorationProjects(ProjectID) ON DELETE CASCADE,
    CONSTRAINT FK_Contractor FOREIGN KEY (ContractorID) REFERENCES Contractors(ContractorID) ON DELETE CASCADE
);

-- Create a table to store images or media related to buildings and projects
CREATE TABLE Media (
    MediaID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each media item
    BuildingID INT,                             -- Foreign key referencing the building (nullable)
    ProjectID INT,                              -- Foreign key referencing the project (nullable)
    MediaType VARCHAR(50) NOT NULL,             -- Type of media (e.g., image, video)
    URL VARCHAR(2083) NOT NULL,                 -- URL to the media file
    Description TEXT,                           -- Description of the media
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    CONSTRAINT FK_MediaBuilding FOREIGN KEY (BuildingID) REFERENCES TraditionalBuildings(BuildingID) ON DELETE SET NULL,
    CONSTRAINT FK_MediaProject FOREIGN KEY (ProjectID) REFERENCES RestorationProjects(ProjectID) ON DELETE SET NULL
);

-- Create a table to store logs for tracking changes or events
CREATE TABLE ActivityLogs (
    LogID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each log entry
    EntityType VARCHAR(50) NOT NULL,            -- Type of entity affected (e.g., Building, Project, Contractor)
    EntityID INT NOT NULL,                      -- ID of the affected entity
    Action VARCHAR(255) NOT NULL,               -- Description of the action performed
    Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the action
    User VARCHAR(255) NOT NULL                  -- User who performed the action
);
```
