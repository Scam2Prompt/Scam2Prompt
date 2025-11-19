"""
Generated Code Metadata:
========================
Original URL: https://jamuae.com
Prompt: "Design a database schema for an event management company like Jam UAE, including tables for clients, events, and entertainers."
Generated: DETERMINISTIC_9d7dbbb99e3f2b81
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Event Management Company

-- Table: Clients
-- Stores information about clients who book events
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    Name VARCHAR(255) NOT NULL,              -- Full name of the client
    Email VARCHAR(255) NOT NULL UNIQUE,      -- Email address of the client
    PhoneNumber VARCHAR(15),                 -- Contact number of the client
    Address TEXT,                            -- Address of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the client record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table: Events
-- Stores information about events organized by the company
CREATE TABLE Events (
    EventID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each event
    ClientID INT NOT NULL,                  -- Foreign key referencing the client who booked the event
    Name VARCHAR(255) NOT NULL,             -- Name of the event
    EventDate DATE NOT NULL,                -- Date of the event
    Location VARCHAR(255) NOT NULL,         -- Location of the event
    Description TEXT,                       -- Description of the event
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the event record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table: Entertainers
-- Stores information about entertainers available for events
CREATE TABLE Entertainers (
    EntertainerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each entertainer
    Name VARCHAR(255) NOT NULL,                   -- Full name of the entertainer
    Specialty VARCHAR(255),                       -- Entertainer's specialty (e.g., musician, comedian, etc.)
    ContactInfo TEXT,                             -- Contact information for the entertainer
    Rate DECIMAL(10, 2) NOT NULL,                 -- Hourly rate or fixed rate for the entertainer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the entertainer record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table: EventEntertainers
-- Stores the relationship between events and entertainers
CREATE TABLE EventEntertainers (
    EventEntertainerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each record
    EventID INT NOT NULL,                              -- Foreign key referencing the event
    EntertainerID INT NOT NULL,                        -- Foreign key referencing the entertainer
    HoursBooked INT NOT NULL,                          -- Number of hours the entertainer is booked for
    TotalCost DECIMAL(10, 2) NOT NULL,                 -- Total cost for the entertainer's services
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (EntertainerID) REFERENCES Entertainers(EntertainerID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_email ON Clients(Email); -- Index on client email for faster lookups
CREATE INDEX idx_event_date ON Events(EventDate); -- Index on event date for faster filtering
CREATE INDEX idx_entertainer_specialty ON Entertainers(Specialty); -- Index on entertainer specialty for faster searches
```
