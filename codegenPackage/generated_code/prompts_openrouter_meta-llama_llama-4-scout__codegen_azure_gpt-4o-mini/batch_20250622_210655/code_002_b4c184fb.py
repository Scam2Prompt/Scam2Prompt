"""
Generated Code Metadata:
========================
Original URL: https://uranpres.sk
Prompt: "Generate a sample database schema for storing information about construction projects, including underground construction, geological surveys, and client details, similar to what URANPRES, s.r.o. might use."
Generated: DETERMINISTIC_b4c184fb22988bf2
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
-- This schema includes tables for projects, clients, geological surveys, and underground constructions.

CREATE DATABASE ConstructionProjects;

USE ConstructionProjects;

-- Table to store client details
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each client
    ClientName VARCHAR(255) NOT NULL,         -- Name of the client
    ContactPerson VARCHAR(255),                -- Name of the contact person
    PhoneNumber VARCHAR(20),                   -- Contact phone number
    Email VARCHAR(255),                        -- Contact email address
    Address VARCHAR(255),                      -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store construction projects
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each project
    ProjectName VARCHAR(255) NOT NULL,         -- Name of the project
    ClientID INT NOT NULL,                      -- Foreign key referencing Clients
    StartDate DATE NOT NULL,                   -- Project start date
    EndDate DATE,                              -- Project end date (nullable)
    Status ENUM('Planned', 'In Progress', 'Completed', 'On Hold') NOT NULL,  -- Current status of the project
    Budget DECIMAL(15, 2),                     -- Budget allocated for the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Table to store geological survey details
CREATE TABLE GeologicalSurveys (
    SurveyID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each survey
    ProjectID INT NOT NULL,                     -- Foreign key referencing Projects
    SurveyDate DATE NOT NULL,                   -- Date of the survey
    SurveyDetails TEXT,                         -- Detailed description of the survey
    Findings TEXT,                             -- Findings from the survey
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Table to store underground construction details
CREATE TABLE UndergroundConstructions (
    ConstructionID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each underground construction
    ProjectID INT NOT NULL,                         -- Foreign key referencing Projects
    ConstructionType VARCHAR(255) NOT NULL,        -- Type of underground construction
    Depth DECIMAL(10, 2),                          -- Depth of the construction
    Length DECIMAL(10, 2),                         -- Length of the construction
    Width DECIMAL(10, 2),                          -- Width of the construction
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_name ON Clients(ClientName);
CREATE INDEX idx_project_name ON Projects(ProjectName);
CREATE INDEX idx_survey_date ON GeologicalSurveys(SurveyDate);
CREATE INDEX idx_construction_type ON UndergroundConstructions(ConstructionType);
```
