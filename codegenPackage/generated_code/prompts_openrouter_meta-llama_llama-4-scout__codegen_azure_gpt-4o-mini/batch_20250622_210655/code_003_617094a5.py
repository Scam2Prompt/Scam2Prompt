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
-- Database schema for storing information about beach bar events at Chat 'N' Chill

-- Create a table to store event types
CREATE TABLE EventTypes (
    EventTypeID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each event type
    EventTypeName VARCHAR(100) NOT NULL UNIQUE,  -- Name of the event type (e.g., 'Sunday Pig Roast', 'Wedding')
    Description TEXT,                             -- Description of the event type
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the event type was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the event type was last updated
);

-- Create a table to store events
CREATE TABLE Events (
    EventID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each event
    EventTypeID INT NOT NULL,                     -- Foreign key referencing EventTypes
    EventName VARCHAR(100) NOT NULL,              -- Name of the event
    EventDate DATE NOT NULL,                       -- Date of the event
    StartTime TIME NOT NULL,                      -- Start time of the event
    EndTime TIME NOT NULL,                        -- End time of the event
    Location VARCHAR(255) NOT NULL,               -- Location of the event
    Description TEXT,                             -- Description of the event
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the event was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the event was last updated
    FOREIGN KEY (EventTypeID) REFERENCES EventTypes(EventTypeID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store attendees
CREATE TABLE Attendees (
    AttendeeID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each attendee
    EventID INT NOT NULL,                          -- Foreign key referencing Events
    Name VARCHAR(100) NOT NULL,                    -- Name of the attendee
    Email VARCHAR(100) NOT NULL UNIQUE,            -- Email of the attendee
    Phone VARCHAR(15),                             -- Phone number of the attendee
    RSVPStatus ENUM('Pending', 'Confirmed', 'Cancelled') DEFAULT 'Pending', -- RSVP status of the attendee
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the attendee was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the attendee was last updated
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store feedback for events
CREATE TABLE Feedback (
    FeedbackID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each feedback entry
    EventID INT NOT NULL,                          -- Foreign key referencing Events
    AttendeeID INT NOT NULL,                       -- Foreign key referencing Attendees
    Rating INT CHECK (Rating BETWEEN 1 AND 5),     -- Rating given by the attendee (1 to 5)
    Comments TEXT,                                 -- Comments provided by the attendee
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the feedback was created
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (AttendeeID) REFERENCES Attendees(AttendeeID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_event_date ON Events(EventDate);
CREATE INDEX idx_attendee_email ON Attendees(Email);
```
