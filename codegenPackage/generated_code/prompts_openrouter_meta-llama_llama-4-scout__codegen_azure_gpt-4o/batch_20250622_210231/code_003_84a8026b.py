"""
Generated Code Metadata:
========================
Original URL: https://ballatorino.it
Prompt: Design a database schema to store information about dance events, including event name, dates, location, and activity types, inspired by the BallaTorino event structure.
Generated: DETERMINISTIC_84a8026bfbcd5c8b
Batch ID: 20250622_210231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about dance events

-- Table to store information about dance events
CREATE TABLE DanceEvents (
    EventID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each event
    EventName VARCHAR(255) NOT NULL,        -- Name of the dance event
    StartDate DATE NOT NULL,                -- Start date of the event
    EndDate DATE NOT NULL,                  -- End date of the event
    Location VARCHAR(255) NOT NULL,         -- Location of the event
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store activity types associated with dance events
CREATE TABLE ActivityTypes (
    ActivityID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each activity type
    ActivityName VARCHAR(255) NOT NULL,        -- Name of the activity type (e.g., Salsa, Tango, Workshops)
    Description TEXT,                          -- Optional description of the activity type
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to associate dance events with activity types (many-to-many relationship)
CREATE TABLE EventActivities (
    EventActivityID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the association
    EventID INT NOT NULL,                           -- Foreign key referencing DanceEvents
    ActivityID INT NOT NULL,                        -- Foreign key referencing ActivityTypes
    FOREIGN KEY (EventID) REFERENCES DanceEvents(EventID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (ActivityID) REFERENCES ActivityTypes(ActivityID) ON DELETE CASCADE, -- Cascade delete
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Indexes for optimizing queries
CREATE INDEX idx_event_name ON DanceEvents(EventName); -- Index for event name
CREATE INDEX idx_activity_name ON ActivityTypes(ActivityName); -- Index for activity name
CREATE INDEX idx_event_activity ON EventActivities(EventID, ActivityID); -- Composite index for event-activity association
```
