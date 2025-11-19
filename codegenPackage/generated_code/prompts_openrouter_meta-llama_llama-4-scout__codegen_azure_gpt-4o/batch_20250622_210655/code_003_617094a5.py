"""
Generated Code Metadata:
========================
Original URL: https://chatnchill.com
Prompt: Design a database schema for storing information about beach bar events, including Sunday Pig Roast, weddings, and other activities offered by Chat 'N' Chill.
Generated: DETERMINISTIC_617094a5b20d23c5
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about beach bar events

-- Table to store information about events
CREATE TABLE Events (
    EventID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each event
    EventName VARCHAR(255) NOT NULL,        -- Name of the event (e.g., Sunday Pig Roast, Wedding)
    EventDescription TEXT,                  -- Detailed description of the event
    EventDate DATE NOT NULL,                -- Date of the event
    StartTime TIME NOT NULL,                -- Start time of the event
    EndTime TIME,                           -- End time of the event (optional)
    Location VARCHAR(255) NOT NULL,         -- Location of the event (e.g., Chat 'N' Chill Beach)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the event was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about event types
CREATE TABLE EventTypes (
    EventTypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each event type
    TypeName VARCHAR(255) NOT NULL UNIQUE,      -- Name of the event type (e.g., Wedding, Roast, Activity)
    TypeDescription TEXT                        -- Description of the event type
);

-- Table to associate events with their types (many-to-many relationship)
CREATE TABLE EventTypeMapping (
    MappingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the mapping
    EventID INT NOT NULL,                     -- Foreign key referencing Events table
    EventTypeID INT NOT NULL,                 -- Foreign key referencing EventTypes table
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE,
    FOREIGN KEY (EventTypeID) REFERENCES EventTypes(EventTypeID) ON DELETE CASCADE
);

-- Table to store attendees for events
CREATE TABLE Attendees (
    AttendeeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each attendee
    EventID INT NOT NULL,                      -- Foreign key referencing Events table
    AttendeeName VARCHAR(255) NOT NULL,        -- Name of the attendee
    AttendeeEmail VARCHAR(255) NOT NULL,       -- Email of the attendee
    RSVPStatus ENUM('Pending', 'Confirmed', 'Cancelled') DEFAULT 'Pending', -- RSVP status
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE
);

-- Table to store additional resources or services for events
CREATE TABLE EventResources (
    ResourceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each resource
    EventID INT NOT NULL,                      -- Foreign key referencing Events table
    ResourceName VARCHAR(255) NOT NULL,        -- Name of the resource (e.g., Catering, Decorations)
    ResourceDescription TEXT,                  -- Description of the resource
    ResourceCost DECIMAL(10, 2),               -- Cost of the resource
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_event_date ON Events(EventDate); -- Index for querying events by date
CREATE INDEX idx_event_type ON EventTypeMapping(EventTypeID); -- Index for querying events by type
CREATE INDEX idx_attendee_email ON Attendees(AttendeeEmail); -- Index for querying attendees by email
```
