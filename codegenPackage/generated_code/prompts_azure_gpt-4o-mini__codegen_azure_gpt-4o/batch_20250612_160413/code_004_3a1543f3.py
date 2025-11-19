"""
Generated Code Metadata:
========================
Original URL: https://myflowfoundationke.org
Prompt: Design a data model in SQL to manage the records of girls impacted by menstrual health initiatives, similar to the tracking done by My Flow Foundation.
Generated: DETERMINISTIC_3a1543f3ceb01dfb
Batch ID: 20250612_160413
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for managing records of girls impacted by menstrual health initiatives
-- This schema includes tables for storing personal information, program participation, and health data.

-- Create a table to store personal information of the girls
CREATE TABLE Girls (
    GirlID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each girl
    FirstName VARCHAR(50) NOT NULL,        -- First name of the girl
    LastName VARCHAR(50) NOT NULL,         -- Last name of the girl
    DateOfBirth DATE NOT NULL,             -- Date of birth
    Address VARCHAR(255),                  -- Address (optional)
    ContactNumber VARCHAR(15),             -- Contact number (optional)
    Email VARCHAR(100),                    -- Email address (optional)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table to store information about the programs the girls participate in
CREATE TABLE Programs (
    ProgramID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each program
    ProgramName VARCHAR(100) NOT NULL,        -- Name of the program
    Description TEXT,                         -- Description of the program
    StartDate DATE NOT NULL,                  -- Start date of the program
    EndDate DATE,                             -- End date of the program (optional)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table to track participation of girls in programs
CREATE TABLE ProgramParticipation (
    ParticipationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each participation record
    GirlID INT NOT NULL,                            -- Foreign key referencing Girls table
    ProgramID INT NOT NULL,                         -- Foreign key referencing Programs table
    ParticipationDate DATE NOT NULL,                -- Date of participation
    Feedback TEXT,                                  -- Feedback provided by the girl (optional)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (GirlID) REFERENCES Girls(GirlID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (ProgramID) REFERENCES Programs(ProgramID) ON DELETE CASCADE -- Cascade delete
);

-- Create a table to store health-related data for the girls
CREATE TABLE HealthRecords (
    HealthRecordID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each health record
    GirlID INT NOT NULL,                           -- Foreign key referencing Girls table
    RecordDate DATE NOT NULL,                      -- Date of the health record
    MenstrualCycleLength INT,                      -- Length of menstrual cycle in days (optional)
    MenstrualFlow VARCHAR(50),                     -- Description of menstrual flow (e.g., light, moderate, heavy)
    Notes TEXT,                                    -- Additional notes (optional)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (GirlID) REFERENCES Girls(GirlID) ON DELETE CASCADE -- Cascade delete
);

-- Create a table to store educational resources provided to the girls
CREATE TABLE EducationalResources (
    ResourceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each resource
    ResourceName VARCHAR(100) NOT NULL,        -- Name of the resource
    Description TEXT,                          -- Description of the resource
    URL VARCHAR(255),                          -- URL to access the resource (optional)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table to track distribution of educational resources to the girls
CREATE TABLE ResourceDistribution (
    DistributionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each distribution record
    GirlID INT NOT NULL,                           -- Foreign key referencing Girls table
    ResourceID INT NOT NULL,                       -- Foreign key referencing EducationalResources table
    DistributionDate DATE NOT NULL,                -- Date of distribution
    Notes TEXT,                                    -- Additional notes (optional)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (GirlID) REFERENCES Girls(GirlID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (ResourceID) REFERENCES EducationalResources(ResourceID) ON DELETE CASCADE -- Cascade delete
);

-- Ensure proper indexing for efficient querying
CREATE INDEX idx_girl_program ON ProgramParticipation (GirlID, ProgramID);
CREATE INDEX idx_girl_health ON HealthRecords (GirlID, RecordDate);
CREATE INDEX idx_girl_resource ON ResourceDistribution (GirlID, ResourceID);
```
