"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wcdevent.com
Prompt: Generate code for a database schema to manage event details, including social and corporate event types, client preferences, and design specifications.
Generated: DETERMINISTIC_b742922b09a8bbf2
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema to Manage Event Details

-- Table: EventTypes
-- This table stores the types of events, such as social and corporate.
CREATE TABLE EventTypes (
    EventTypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for an event type
    Name VARCHAR(50) NOT NULL,                 -- Name of the event type (e.g., Social, Corporate)
    Description TEXT                           -- Optional description of the event type
);

-- Table: Clients
-- This table stores information about clients who request events.
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for a client
    FullName VARCHAR(100) NOT NULL,          -- Full name of the client
    Email VARCHAR(100) NOT NULL UNIQUE,      -- Email address of the client
    PhoneNumber VARCHAR(20),                 -- Optional phone number of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the client record was created
);

-- Table: Events
-- This table stores details of individual events.
CREATE TABLE Events (
    EventID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for an event
    EventTypeID INT NOT NULL,               -- Foreign key referencing EventTypes table
    ClientID INT NOT NULL,                  -- Foreign key referencing Clients table
    Title VARCHAR(100) NOT NULL,            -- Title or name of the event
    EventDate DATE NOT NULL,                -- Date of the event
    Location VARCHAR(255),                  -- Optional location of the event
    Budget DECIMAL(10,2),                   -- Optional budget for the event
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the event record was created
    FOREIGN KEY (EventTypeID) REFERENCES EventTypes(EventTypeID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Table: ClientPreferences
-- This table stores specific preferences provided by clients for their events.
CREATE TABLE ClientPreferences (
    PreferenceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for a preference
    ClientID INT NOT NULL,                       -- Foreign key referencing Clients table
    EventID INT NOT NULL,                        -- Foreign key referencing Events table
    PreferenceDetails TEXT NOT NULL,            -- Detailed description of the preference
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Table: DesignSpecifications
-- This table stores design-related specifications for events, such as themes, color schemes, etc.
CREATE TABLE DesignSpecifications (
    SpecificationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for a design specification
    EventID INT NOT NULL,                           -- Foreign key referencing Events table
    Theme VARCHAR(50),                              -- Optional theme for the event
    ColorScheme VARCHAR(50),                        -- Optional color scheme for the event
    AdditionalDetails TEXT,                         -- Additional design-related details
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Indexes for Performance
CREATE INDEX idx_event_type ON Events(EventTypeID);
CREATE INDEX idx_client_event ON ClientPreferences(ClientID, EventID);
CREATE INDEX idx_event_spec ON DesignSpecifications(EventID);

-- Error Handling Note:
-- Ensure application-level error handling for unique constraints, foreign key violations, 
-- and input validations before inserting data into these tables.
```
