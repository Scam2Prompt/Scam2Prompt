"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bandadorada.com
Prompt: Outline a database schema for storing information about music events, clients, and services, similar to the structure used by Orquesta Dorada for managing their bookings.
Generated: DETERMINISTIC_21a1799f44631b28
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for managing music events, clients, and services

-- Table: Clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- First name of the client
    LastName VARCHAR(50) NOT NULL,           -- Last name of the client
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Contact email of the client
    PhoneNumber VARCHAR(15),                 -- Contact phone number of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the client was added
);

-- Table: Services
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for a service
    ServiceName VARCHAR(100) NOT NULL,        -- Name of the service (e.g., "Live Band", "DJ")
    Description TEXT,                         -- Detailed description of the service
    Price DECIMAL(10, 2) NOT NULL,            -- Cost of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the service was added
);

-- Table: Events
CREATE TABLE Events (
    EventID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for an event
    ClientID INT NOT NULL,                   -- Reference to the client who booked the event
    EventDate DATETIME NOT NULL,             -- Date and time of the event
    Location VARCHAR(255) NOT NULL,          -- Location of the event
    Notes TEXT,                              -- Additional notes about the event
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the event was added
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) -- Relationship to Clients table
);

-- Table: EventServices
CREATE TABLE EventServices (
    EventServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the event-service association
    EventID INT NOT NULL,                          -- Reference to the event
    ServiceID INT NOT NULL,                        -- Reference to the service
    Quantity INT DEFAULT 1,                        -- Number of units for the service (e.g., 2 DJs)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the association was added
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE, -- Relationship to Events table
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Relationship to Services table
);

-- Indexes for improved query performance
CREATE INDEX idx_clients_email ON Clients(Email);            -- Index for email in Clients table
CREATE INDEX idx_events_date ON Events(EventDate);           -- Index for event date in Events table
CREATE INDEX idx_eventservices_eventid ON EventServices(EventID); -- Index for EventID in EventServices table
```
