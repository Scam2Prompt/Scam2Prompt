"""
Generated Code Metadata:
========================
Original URL: https://pozymedia.com
Prompt: Design a database schema for storing event-related data, including information about venues, event staff, and audio-visual equipment.
Generated: DETERMINISTIC_2d675c95768b5c8b
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing event-related data

-- Table to store information about venues
CREATE TABLE Venues (
    VenueID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the venue
    Name VARCHAR(255) NOT NULL,             -- Name of the venue
    Address VARCHAR(255) NOT NULL,          -- Address of the venue
    Capacity INT NOT NULL,                  -- Maximum capacity of the venue
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store information about events
CREATE TABLE Events (
    EventID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the event
    Name VARCHAR(255) NOT NULL,             -- Name of the event
    Description TEXT,                       -- Description of the event
    StartDate DATETIME NOT NULL,            -- Start date and time of the event
    EndDate DATETIME NOT NULL,              -- End date and time of the event
    VenueID INT NOT NULL,                   -- Foreign key referencing the venue
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (VenueID) REFERENCES Venues(VenueID) ON DELETE CASCADE -- Cascade delete if venue is removed
);

-- Table to store information about event staff
CREATE TABLE EventStaff (
    StaffID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the staff member
    FirstName VARCHAR(255) NOT NULL,        -- First name of the staff member
    LastName VARCHAR(255) NOT NULL,         -- Last name of the staff member
    Role VARCHAR(255) NOT NULL,             -- Role of the staff member (e.g., coordinator, technician)
    ContactInfo VARCHAR(255),               -- Contact information (e.g., phone or email)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to associate staff members with events
CREATE TABLE EventStaffAssignments (
    AssignmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the assignment
    EventID INT NOT NULL,                        -- Foreign key referencing the event
    StaffID INT NOT NULL,                        -- Foreign key referencing the staff member
    AssignedRole VARCHAR(255) NOT NULL,          -- Role assigned for the event
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE, -- Cascade delete if event is removed
    FOREIGN KEY (StaffID) REFERENCES EventStaff(StaffID) ON DELETE CASCADE -- Cascade delete if staff is removed
);

-- Table to store information about audio-visual equipment
CREATE TABLE Equipment (
    EquipmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the equipment
    Name VARCHAR(255) NOT NULL,                 -- Name of the equipment
    Type VARCHAR(255) NOT NULL,                 -- Type of equipment (e.g., projector, microphone)
    Quantity INT NOT NULL,                      -- Quantity available
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to associate equipment with events
CREATE TABLE EventEquipment (
    EventEquipmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the association
    EventID INT NOT NULL,                            -- Foreign key referencing the event
    EquipmentID INT NOT NULL,                        -- Foreign key referencing the equipment
    QuantityUsed INT NOT NULL,                       -- Quantity of equipment used for the event
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp for record creation
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE, -- Cascade delete if event is removed
    FOREIGN KEY (EquipmentID) REFERENCES Equipment(EquipmentID) ON DELETE CASCADE -- Cascade delete if equipment is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_event_venue ON Events(VenueID); -- Index for venue lookup in events
CREATE INDEX idx_event_staff ON EventStaffAssignments(EventID, StaffID); -- Index for event-staff assignments
CREATE INDEX idx_event_equipment ON EventEquipment(EventID, EquipmentID); -- Index for event-equipment associations
```
