"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kallimos.com
Prompt: Create a database schema for managing housing options in a Kallimos-style community, including compact houses, tiny homes, studio apartments, and shared spaces like Kallimos Commons.
Generated: DETERMINISTIC_59a8a64fc983dfef
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create database schema for Kallimos-style community housing management

-- Create a table to store information about housing types
CREATE TABLE HousingTypes (
    HousingTypeID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for the housing type
    Name VARCHAR(50) NOT NULL,                    -- Name of the housing type (e.g., "Compact House", "Tiny Home", etc.)
    Description TEXT                              -- Description of the housing type
);

-- Create a table to store individual housing unit details
CREATE TABLE HousingUnits (
    HousingUnitID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for the housing unit
    HousingTypeID INT NOT NULL,                   -- Foreign key referencing the HousingTypes table
    Name VARCHAR(100) NOT NULL,                   -- Name or designation of the housing unit (e.g., "Unit A")
    SquareFeet INT NOT NULL,                      -- Size of the housing unit in square feet
    MaxOccupancy INT NOT NULL,                    -- Maximum number of occupants allowed
    MonthlyRent DECIMAL(10, 2) NOT NULL,          -- Monthly rent for the housing unit
    IsAvailable BOOLEAN DEFAULT TRUE,             -- Availability status of the housing unit
    CONSTRAINT FK_HousingType FOREIGN KEY (HousingTypeID) REFERENCES HousingTypes(HousingTypeID)
);

-- Create a table to store shared space details
CREATE TABLE SharedSpaces (
    SharedSpaceID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for the shared space
    Name VARCHAR(100) NOT NULL,                   -- Name of the shared space (e.g., "Kallimos Commons")
    Description TEXT,                             -- Description of the shared space
    SquareFeet INT NOT NULL,                      -- Size of the shared space in square feet
    MaxOccupancy INT,                             -- Maximum number of occupants allowed
    IsAccessible BOOLEAN DEFAULT TRUE             -- Accessibility status of the shared space
);

-- Create a table to store residents' information
CREATE TABLE Residents (
    ResidentID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for the resident
    FirstName VARCHAR(50) NOT NULL,               -- First name of the resident
    LastName VARCHAR(50) NOT NULL,                -- Last name of the resident
    Email VARCHAR(100) UNIQUE NOT NULL,           -- Email address of the resident
    PhoneNumber VARCHAR(15),                      -- Phone number of the resident
    MoveInDate DATE NOT NULL,                     -- Date when the resident moved in
    HousingUnitID INT,                            -- Foreign key referencing the HousingUnits table
    CONSTRAINT FK_HousingUnit FOREIGN KEY (HousingUnitID) REFERENCES HousingUnits(HousingUnitID)
);

-- Create a table to log interactions with shared spaces
CREATE TABLE SharedSpaceUsage (
    UsageID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each usage record
    SharedSpaceID INT NOT NULL,                   -- Foreign key referencing the SharedSpaces table
    ResidentID INT,                               -- Foreign key referencing the Residents table
    UsageDate DATE NOT NULL,                      -- Date of shared space usage
    DurationHours DECIMAL(5, 2) NOT NULL,         -- Duration of shared space usage (in hours)
    CONSTRAINT FK_SharedSpace FOREIGN KEY (SharedSpaceID) REFERENCES SharedSpaces(SharedSpaceID),
    CONSTRAINT FK_Resident FOREIGN KEY (ResidentID) REFERENCES Residents(ResidentID)
);

-- Create a table to store maintenance requests for housing units and shared spaces
CREATE TABLE MaintenanceRequests (
    RequestID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for the maintenance request
    HousingUnitID INT,                            -- Optional foreign key referencing the HousingUnits table
    SharedSpaceID INT,                            -- Optional foreign key referencing the SharedSpaces table
    ResidentID INT NOT NULL,                      -- Foreign key referencing the Residents table (who reported the issue)
    RequestDate DATE NOT NULL,                    -- Date the maintenance request was made
    Description TEXT NOT NULL,                    -- Description of the maintenance issue
    Status ENUM('Pending', 'In Progress', 'Completed') DEFAULT 'Pending', -- Current status of the maintenance request
    CONSTRAINT FK_Maintenance_HousingUnit FOREIGN KEY (HousingUnitID) REFERENCES HousingUnits(HousingUnitID),
    CONSTRAINT FK_Maintenance_SharedSpace FOREIGN KEY (SharedSpaceID) REFERENCES SharedSpaces(SharedSpaceID),
    CONSTRAINT FK_Maintenance_Resident FOREIGN KEY (ResidentID) REFERENCES Residents(ResidentID)
);

-- Ensure all tables are created successfully
-- Schema complete for managing Kallimos-style community housing
```
