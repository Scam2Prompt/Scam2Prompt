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

-- Create a table to store information about volunteers
CREATE TABLE Volunteers (
    VolunteerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each volunteer
    FirstName VARCHAR(50) NOT NULL,              -- First name of the volunteer
    LastName VARCHAR(50) NOT NULL,                -- Last name of the volunteer
    Email VARCHAR(100) UNIQUE NOT NULL,           -- Email address of the volunteer
    Phone VARCHAR(15),                            -- Phone number of the volunteer
    JoinDate DATE NOT NULL DEFAULT CURRENT_DATE,  -- Date when the volunteer joined
    Status ENUM('Active', 'Inactive') NOT NULL DEFAULT 'Active'  -- Status of the volunteer
);

-- Create a table to store information about equipment
CREATE TABLE Equipment (
    EquipmentID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each equipment
    Name VARCHAR(100) NOT NULL,                   -- Name of the equipment
    Type VARCHAR(50) NOT NULL,                    -- Type of the equipment (e.g., tool, vehicle)
    Quantity INT NOT NULL DEFAULT 1,              -- Quantity of the equipment available
    Condition ENUM('New', 'Good', 'Needs Repair', 'Damaged') NOT NULL DEFAULT 'New',  -- Condition of the equipment
    LastMaintenance DATE                          -- Date of the last maintenance
);

-- Create a table to store information about activities
CREATE TABLE Activities (
    ActivityID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each activity
    ActivityName VARCHAR(100) NOT NULL,           -- Name of the activity
    Description TEXT,                              -- Description of the activity
    ActivityDate DATE NOT NULL,                    -- Date of the activity
    Location VARCHAR(100) NOT NULL,               -- Location where the activity takes place
    Status ENUM('Scheduled', 'Completed', 'Cancelled') NOT NULL DEFAULT 'Scheduled'  -- Status of the activity
);

-- Create a junction table to associate volunteers with activities
CREATE TABLE VolunteerActivities (
    VolunteerID INT,                               -- Foreign key referencing Volunteers
    ActivityID INT,                                -- Foreign key referencing Activities
    PRIMARY KEY (VolunteerID, ActivityID),        -- Composite primary key
    FOREIGN KEY (VolunteerID) REFERENCES Volunteers(VolunteerID) ON DELETE CASCADE,  -- Ensures referential integrity
    FOREIGN KEY (ActivityID) REFERENCES Activities(ActivityID) ON DELETE CASCADE   -- Ensures referential integrity
);

-- Create a table to track equipment used in activities
CREATE TABLE ActivityEquipment (
    ActivityID INT,                               -- Foreign key referencing Activities
    EquipmentID INT,                              -- Foreign key referencing Equipment
    QuantityUsed INT NOT NULL DEFAULT 1,         -- Quantity of equipment used in the activity
    PRIMARY KEY (ActivityID, EquipmentID),       -- Composite primary key
    FOREIGN KEY (ActivityID) REFERENCES Activities(ActivityID) ON DELETE CASCADE,  -- Ensures referential integrity
    FOREIGN KEY (EquipmentID) REFERENCES Equipment(EquipmentID) ON DELETE CASCADE  -- Ensures referential integrity
);
```
