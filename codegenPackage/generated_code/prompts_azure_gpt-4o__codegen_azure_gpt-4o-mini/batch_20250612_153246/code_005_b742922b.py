"""
Generated Code Metadata:
========================
Original URL: https://wcdevent.com
Prompt: Generate code for a database schema to manage event details, including social and corporate event types, client preferences, and design specifications.
Generated: DETERMINISTIC_b742922b09a8bbf2
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing event details, including social and corporate event types, client preferences, and design specifications.

-- Create a database for event management
CREATE DATABASE EventManagement;

-- Use the created database
USE EventManagement;

-- Table to store event types (e.g., social, corporate)
CREATE TABLE EventTypes (
    EventTypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each event type
    EventTypeName VARCHAR(100) NOT NULL UNIQUE, -- Name of the event type
    Description TEXT -- Description of the event type
);

-- Table to store clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    ClientName VARCHAR(255) NOT NULL, -- Name of the client
    ContactEmail VARCHAR(255) NOT NULL UNIQUE, -- Email address of the client
    PhoneNumber VARCHAR(15), -- Phone number of the client
    Preferences TEXT -- Client preferences for events
);

-- Table to store event details
CREATE TABLE Events (
    EventID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each event
    EventTypeID INT NOT NULL, -- Foreign key referencing EventTypes
    ClientID INT NOT NULL, -- Foreign key referencing Clients
    EventDate DATETIME NOT NULL, -- Date and time of the event
    Location VARCHAR(255) NOT NULL, -- Location of the event
    DesignSpecifications TEXT, -- Design specifications for the event
    FOREIGN KEY (EventTypeID) REFERENCES EventTypes(EventTypeID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store event attendees
CREATE TABLE Attendees (
    AttendeeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each attendee
    EventID INT NOT NULL, -- Foreign key referencing Events
    AttendeeName VARCHAR(255) NOT NULL, -- Name of the attendee
    RSVPStatus ENUM('Pending', 'Confirmed', 'Declined') DEFAULT 'Pending', -- RSVP status of the attendee
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store feedback for events
CREATE TABLE Feedback (
    FeedbackID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each feedback entry
    EventID INT NOT NULL, -- Foreign key referencing Events
    ClientID INT NOT NULL, -- Foreign key referencing Clients
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating given by the client (1 to 5)
    Comments TEXT, -- Additional comments from the client
    FeedbackDate DATETIME DEFAULT CURRENT_TIMESTAMP, -- Date and time of feedback submission
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_event_type ON Events(EventTypeID);
CREATE INDEX idx_client ON Events(ClientID);
CREATE INDEX idx_event_attendee ON Attendees(EventID);
CREATE INDEX idx_event_feedback ON Feedback(EventID);
CREATE INDEX idx_client_feedback ON Feedback(ClientID);
```
