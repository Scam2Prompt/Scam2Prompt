"""
Generated Code Metadata:
========================
Original URL: https://myrmp.org
Prompt: Design a database schema to store information about members, events, and resources for a professional organization like RMP.
Generated: DETERMINISTIC_af8b6f3b093964aa
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a professional organization

-- Table to store information about members
CREATE TABLE Members (
    MemberID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each member
    FirstName VARCHAR(50) NOT NULL,          -- Member's first name
    LastName VARCHAR(50) NOT NULL,           -- Member's last name
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Member's email address (must be unique)
    PhoneNumber VARCHAR(15),                 -- Member's phone number
    JoinDate DATE NOT NULL,                  -- Date the member joined the organization
    MembershipStatus ENUM('Active', 'Inactive', 'Suspended') DEFAULT 'Active', -- Membership status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about events
CREATE TABLE Events (
    EventID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each event
    EventName VARCHAR(100) NOT NULL,         -- Name of the event
    EventDate DATE NOT NULL,                 -- Date of the event
    StartTime TIME NOT NULL,                 -- Start time of the event
    EndTime TIME NOT NULL,                   -- End time of the event
    Location VARCHAR(255) NOT NULL,          -- Location of the event
    Description TEXT,                        -- Detailed description of the event
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about resources
CREATE TABLE Resources (
    ResourceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each resource
    ResourceName VARCHAR(100) NOT NULL,        -- Name of the resource
    ResourceType ENUM('Document', 'Video', 'Image', 'Other') NOT NULL, -- Type of resource
    URL VARCHAR(255) NOT NULL,                 -- URL or location of the resource
    Description TEXT,                          -- Detailed description of the resource
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to track member attendance at events
CREATE TABLE EventAttendance (
    AttendanceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for attendance record
    MemberID INT NOT NULL,                       -- Foreign key referencing Members table
    EventID INT NOT NULL,                        -- Foreign key referencing Events table
    AttendanceStatus ENUM('Attended', 'Absent', 'Cancelled') DEFAULT 'Attended', -- Attendance status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID) ON DELETE CASCADE, -- Cascade delete for member
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE -- Cascade delete for event
);

-- Table to track resource access by members
CREATE TABLE ResourceAccess (
    AccessID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for resource access record
    MemberID INT NOT NULL,                   -- Foreign key referencing Members table
    ResourceID INT NOT NULL,                 -- Foreign key referencing Resources table
    AccessDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of access
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID) ON DELETE CASCADE, -- Cascade delete for member
    FOREIGN KEY (ResourceID) REFERENCES Resources(ResourceID) ON DELETE CASCADE -- Cascade delete for resource
);

-- Indexes for optimizing queries
CREATE INDEX idx_member_email ON Members(Email); -- Index for quick lookup by email
CREATE INDEX idx_event_date ON Events(EventDate); -- Index for quick lookup by event date
CREATE INDEX idx_resource_type ON Resources(ResourceType); -- Index for quick lookup by resource type
```
