"""
Generated Code Metadata:
========================
Original URL: https://kallimos.com
Prompt: Design a database schema for storing information about residents in a Kallimos community, ensuring it supports multi-generational and multi-ability inclusivity.
Generated: DETERMINISTIC_558cfecaa0260f13
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about residents in a Kallimos community
-- Supports multi-generational and multi-ability inclusivity

-- Table to store resident information
CREATE TABLE Residents (
    ResidentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each resident
    FirstName VARCHAR(50) NOT NULL,            -- Resident's first name
    LastName VARCHAR(50) NOT NULL,             -- Resident's last name
    DateOfBirth DATE NOT NULL,                 -- Resident's date of birth
    Gender ENUM('Male', 'Female', 'Non-Binary', 'Other') NOT NULL, -- Gender of the resident
    PhoneNumber VARCHAR(15),                   -- Contact phone number
    Email VARCHAR(100),                        -- Contact email address
    Address VARCHAR(255),                      -- Resident's address
    EmergencyContactName VARCHAR(100),         -- Name of emergency contact
    EmergencyContactPhone VARCHAR(15),         -- Phone number of emergency contact
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about abilities and accessibility needs
CREATE TABLE Abilities (
    AbilityID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each ability
    AbilityName VARCHAR(100) NOT NULL,         -- Name of the ability or need (e.g., "Wheelchair Access", "Sign Language")
    Description TEXT,                          -- Detailed description of the ability or need
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to associate residents with their abilities and accessibility needs
CREATE TABLE ResidentAbilities (
    ResidentAbilityID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the association
    ResidentID INT NOT NULL,                          -- Foreign key to Residents table
    AbilityID INT NOT NULL,                           -- Foreign key to Abilities table
    Notes TEXT,                                       -- Additional notes about the resident's ability or need
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ResidentID) REFERENCES Residents(ResidentID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (AbilityID) REFERENCES Abilities(AbilityID) ON DELETE CASCADE -- Cascade delete
);

-- Table to store family relationships between residents
CREATE TABLE FamilyRelationships (
    RelationshipID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the relationship
    ResidentID1 INT NOT NULL,                      -- Foreign key to Residents table (first resident)
    ResidentID2 INT NOT NULL,                      -- Foreign key to Residents table (second resident)
    RelationshipType ENUM('Parent', 'Child', 'Sibling', 'Spouse', 'Other') NOT NULL, -- Type of relationship
    Notes TEXT,                                    -- Additional notes about the relationship
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ResidentID1) REFERENCES Residents(ResidentID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (ResidentID2) REFERENCES Residents(ResidentID) ON DELETE CASCADE -- Cascade delete
);

-- Indexes for optimizing queries
CREATE INDEX idx_resident_dob ON Residents(DateOfBirth); -- Index for querying residents by date of birth
CREATE INDEX idx_ability_name ON Abilities(AbilityName); -- Index for querying abilities by name
CREATE INDEX idx_relationship_type ON FamilyRelationships(RelationshipType); -- Index for querying relationships by type
```
