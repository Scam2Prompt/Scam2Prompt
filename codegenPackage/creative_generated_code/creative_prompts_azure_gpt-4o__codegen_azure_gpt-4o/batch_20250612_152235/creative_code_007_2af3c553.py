"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinxcash.com
Prompt: Write a SQL database schema for an event company to manage clients, events, venues, and staff assignments, reflecting the organizational structure described on the webpage.
Generated: DETERMINISTIC_2af3c5535b3d3cb1
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for an Event Management Company

-- Table: Clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each client
    Name VARCHAR(255) NOT NULL,                  -- Full name of the client
    Email VARCHAR(255) UNIQUE NOT NULL,          -- Email address of the client (must be unique)
    PhoneNumber VARCHAR(50),                     -- Contact number of the client
    Address TEXT,                                -- Address details for the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table: Venues
CREATE TABLE Venues (
    VenueID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each venue
    Name VARCHAR(255) NOT NULL,                  -- Name of the venue
    Address TEXT NOT NULL,                       -- Address of the venue
    Capacity INT NOT NULL,                       -- Maximum number of people the venue can accommodate
    ContactPerson VARCHAR(255),                 -- Contact person for the venue
    PhoneNumber VARCHAR(50),                    -- Contact number for the venue
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table: Events
CREATE TABLE Events (
    EventID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each event
    Name VARCHAR(255) NOT NULL,                  -- Name of the event
    Date DATE NOT NULL,                          -- Date of the event
    StartTime TIME NOT NULL,                     -- Start time of the event
    EndTime TIME NOT NULL,                       -- End time of the event
    ClientID INT NOT NULL,                       -- Foreign key linking to the Clients table
    VenueID INT NOT NULL,                        -- Foreign key linking to the Venues table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Cascading delete
    FOREIGN KEY (VenueID) REFERENCES Venues(VenueID) ON DELETE CASCADE     -- Cascading delete
);

-- Table: Staff
CREATE TABLE Staff (
    StaffID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each staff member
    Name VARCHAR(255) NOT NULL,                  -- Full name of the staff member
    Email VARCHAR(255) UNIQUE NOT NULL,          -- Email address of the staff member (must be unique)
    PhoneNumber VARCHAR(50),                     -- Contact number of the staff member
    Role VARCHAR(100) NOT NULL,                  -- Job role (e.g., Coordinator, Manager, Technician)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table: StaffAssignments
CREATE TABLE StaffAssignments (
    AssignmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each staff assignment
    EventID INT NOT NULL,                        -- Foreign key linking to the Events table
    StaffID INT NOT NULL,                        -- Foreign key linking to the Staff table
    AssignmentDetails TEXT,                      -- Details of the assignment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE, -- Cascading delete
    FOREIGN KEY (StaffID) REFERENCES Staff(StaffID) ON DELETE CASCADE   -- Cascading delete
);
```
