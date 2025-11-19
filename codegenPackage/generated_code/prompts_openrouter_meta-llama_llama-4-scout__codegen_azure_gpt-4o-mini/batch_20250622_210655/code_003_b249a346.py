"""
Generated Code Metadata:
========================
Original URL: https://afranaden.org
Prompt: Develop a simple database schema to store information about humanitarian projects, including project names, locations, and types of aid provided, inspired by the projects listed on the organization's website.
Generated: DETERMINISTIC_b249a34637b3590f
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for storing information about humanitarian projects

-- Create a new database for humanitarian projects
CREATE DATABASE HumanitarianProjects;

-- Use the newly created database
USE HumanitarianProjects;

-- Table to store information about different types of aid
CREATE TABLE AidTypes (
    AidTypeID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each aid type
    AidTypeName VARCHAR(100) NOT NULL UNIQUE,  -- Name of the aid type (e.g., Food, Medical, Shelter)
    Description TEXT,                           -- Description of the aid type
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store information about project locations
CREATE TABLE Locations (
    LocationID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each location
    Country VARCHAR(100) NOT NULL,              -- Country where the project is located
    City VARCHAR(100),                           -- City where the project is located
    Latitude DECIMAL(9, 6),                     -- Latitude for geographical reference
    Longitude DECIMAL(9, 6),                    -- Longitude for geographical reference
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store information about humanitarian projects
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each project
    ProjectName VARCHAR(255) NOT NULL,           -- Name of the project
    LocationID INT NOT NULL,                      -- Foreign key referencing Locations table
    AidTypeID INT NOT NULL,                       -- Foreign key referencing AidTypes table
    StartDate DATE NOT NULL,                      -- Start date of the project
    EndDate DATE,                                 -- End date of the project (nullable)
    Budget DECIMAL(15, 2),                       -- Budget allocated for the project
    Description TEXT,                             -- Description of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of last update
    FOREIGN KEY (LocationID) REFERENCES Locations(LocationID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (AidTypeID) REFERENCES AidTypes(AidTypeID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_project_name ON Projects(ProjectName);
CREATE INDEX idx_location_country ON Locations(Country);
CREATE INDEX idx_aid_type_name ON AidTypes(AidTypeName);
```
