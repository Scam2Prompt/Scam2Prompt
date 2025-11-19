"""
Generated Code Metadata:
========================
Original URL: https://protezioneciviletorredisola.it
Prompt: Create a sample database schema to store information about volunteers, equipment, and activities for a civil protection group like the one in Torre d'Isola.
Generated: DETERMINISTIC_d598f0a283d5b077
Batch ID: 20250622_210803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a civil protection group

-- Table to store information about volunteers
CREATE TABLE Volunteers (
    VolunteerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each volunteer
    FirstName VARCHAR(50) NOT NULL,            -- First name of the volunteer
    LastName VARCHAR(50) NOT NULL,             -- Last name of the volunteer
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Email address of the volunteer
    PhoneNumber VARCHAR(15),                   -- Contact phone number
    DateOfBirth DATE,                          -- Date of birth of the volunteer
    JoinDate DATE NOT NULL,                    -- Date the volunteer joined the group
    IsActive BOOLEAN DEFAULT TRUE              -- Whether the volunteer is currently active
);

-- Table to store information about equipment
CREATE TABLE Equipment (
    EquipmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each equipment item
    Name VARCHAR(100) NOT NULL,                 -- Name of the equipment
    Description TEXT,                           -- Description of the equipment
    Quantity INT NOT NULL CHECK (Quantity >= 0),-- Quantity available
    PurchaseDate DATE,                          -- Date the equipment was purchased
    LastMaintenanceDate DATE,                   -- Date of the last maintenance
    IsOperational BOOLEAN DEFAULT TRUE          -- Whether the equipment is operational
);

-- Table to store information about activities
CREATE TABLE Activities (
    ActivityID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each activity
    Name VARCHAR(100) NOT NULL,                 -- Name of the activity
    Description TEXT,                           -- Description of the activity
    StartDateTime DATETIME NOT NULL,            -- Start date and time of the activity
    EndDateTime DATETIME NOT NULL,              -- End date and time of the activity
    Location VARCHAR(255) NOT NULL              -- Location of the activity
);

-- Table to track volunteer participation in activities
CREATE TABLE VolunteerActivities (
    VolunteerActivityID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each record
    VolunteerID INT NOT NULL,                           -- ID of the volunteer
    ActivityID INT NOT NULL,                            -- ID of the activity
    Role VARCHAR(50),                                   -- Role of the volunteer in the activity
    FOREIGN KEY (VolunteerID) REFERENCES Volunteers(VolunteerID) ON DELETE CASCADE,
    FOREIGN KEY (ActivityID) REFERENCES Activities(ActivityID) ON DELETE CASCADE
);

-- Table to track equipment usage in activities
CREATE TABLE EquipmentActivities (
    EquipmentActivityID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each record
    EquipmentID INT NOT NULL,                           -- ID of the equipment
    ActivityID INT NOT NULL,                            -- ID of the activity
    QuantityUsed INT NOT NULL CHECK (QuantityUsed > 0), -- Quantity of equipment used
    FOREIGN KEY (EquipmentID) REFERENCES Equipment(EquipmentID) ON DELETE CASCADE,
    FOREIGN KEY (ActivityID) REFERENCES Activities(ActivityID) ON DELETE CASCADE
);

-- Indexes for performance optimization
CREATE INDEX idx_volunteer_email ON Volunteers (Email);
CREATE INDEX idx_activity_start_end ON Activities (StartDateTime, EndDateTime);
CREATE INDEX idx_equipment_name ON Equipment (Name);
```
