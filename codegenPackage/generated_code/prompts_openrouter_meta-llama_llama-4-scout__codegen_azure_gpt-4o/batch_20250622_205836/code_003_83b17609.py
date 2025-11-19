"""
Generated Code Metadata:
========================
Original URL: https://kristoslounge.com
Prompt: Design a simple database schema to store information about Kristos Lounge's clients, events, and services offered.
Generated: DETERMINISTIC_83b176090b929a2d
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Kristos Lounge

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Client's email address (must be unique)
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the client record was created
);

-- Table to store event information
CREATE TABLE Events (
    EventID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each event
    EventName VARCHAR(100) NOT NULL,         -- Name of the event
    EventDate DATE NOT NULL,                 -- Date of the event
    StartTime TIME NOT NULL,                 -- Start time of the event
    EndTime TIME NOT NULL,                   -- End time of the event
    Location VARCHAR(100) NOT NULL,          -- Location of the event
    ClientID INT,                            -- Foreign key linking to the client who booked the event
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the event record was created
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE SET NULL -- Handle client deletion gracefully
);

-- Table to store services offered by Kristos Lounge
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,        -- Name of the service
    Description TEXT,                         -- Detailed description of the service
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the service record was created
);

-- Table to store the relationship between events and services
CREATE TABLE EventServices (
    EventServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each record
    EventID INT NOT NULL,                          -- Foreign key linking to the event
    ServiceID INT NOT NULL,                        -- Foreign key linking to the service
    Quantity INT DEFAULT 1,                        -- Quantity of the service requested
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE, -- Cascade delete if event is deleted
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Cascade delete if service is deleted
);

-- Indexes for performance optimization
CREATE INDEX idx_client_email ON Clients(Email); -- Index on email for faster lookups
CREATE INDEX idx_event_date ON Events(EventDate); -- Index on event date for faster filtering
CREATE INDEX idx_service_name ON Services(ServiceName); -- Index on service name for faster lookups
```
