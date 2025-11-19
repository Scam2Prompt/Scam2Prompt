"""
Generated Code Metadata:
========================
Original URL: https://syncconnects.com
Prompt: Design a database schema for storing user information, membership details, and event data for a networking platform like Sync Connects.
Generated: DETERMINISTIC_8e6fca14fe1cb106
Batch ID: 20250622_211551
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a networking platform like Sync Connects

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    FirstName VARCHAR(50) NOT NULL,        -- User's first name
    LastName VARCHAR(50) NOT NULL,         -- User's last name
    Email VARCHAR(100) UNIQUE NOT NULL,    -- User's email address (must be unique)
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    ProfilePictureURL VARCHAR(255),        -- URL to the user's profile picture
    Bio TEXT,                              -- Short biography of the user
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the user was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store membership details
CREATE TABLE Memberships (
    MembershipID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each membership
    UserID INT NOT NULL,                         -- Foreign key referencing Users table
    MembershipType ENUM('Free', 'Premium', 'VIP') NOT NULL, -- Type of membership
    StartDate DATE NOT NULL,                     -- Start date of the membership
    EndDate DATE,                                -- End date of the membership (NULL for ongoing memberships)
    Status ENUM('Active', 'Inactive') NOT NULL DEFAULT 'Active', -- Status of the membership
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the membership was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is deleted
);

-- Table to store event data
CREATE TABLE Events (
    EventID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each event
    EventName VARCHAR(100) NOT NULL,        -- Name of the event
    Description TEXT,                       -- Description of the event
    Location VARCHAR(255),                  -- Location of the event
    StartDateTime DATETIME NOT NULL,        -- Start date and time of the event
    EndDateTime DATETIME NOT NULL,          -- End date and time of the event
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the event was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store user-event relationships (e.g., RSVPs)
CREATE TABLE UserEvents (
    UserEventID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user-event relationship
    UserID INT NOT NULL,                        -- Foreign key referencing Users table
    EventID INT NOT NULL,                       -- Foreign key referencing Events table
    RSVPStatus ENUM('Attending', 'Not Attending', 'Maybe') NOT NULL, -- RSVP status of the user
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the RSVP was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if user is deleted
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE -- Cascade delete if event is deleted
);

-- Indexes for optimizing queries
CREATE INDEX idx_user_email ON Users(Email); -- Index for quick lookup by email
CREATE INDEX idx_event_start_datetime ON Events(StartDateTime); -- Index for quick lookup by event start time
CREATE INDEX idx_user_event ON UserEvents(UserID, EventID); -- Composite index for user-event relationships
```
