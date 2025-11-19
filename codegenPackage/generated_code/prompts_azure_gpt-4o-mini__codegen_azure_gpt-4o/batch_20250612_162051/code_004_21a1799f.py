"""
Generated Code Metadata:
========================
Original URL: https://bandadorada.com
Prompt: Outline a database schema for storing information about music events, clients, and services, similar to the structure used by Orquesta Dorada for managing their bookings.
Generated: DETERMINISTIC_21a1799f44631b28
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing music events, clients, and services

-- Table to store information about clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Client's email address
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the client was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about music events
CREATE TABLE MusicEvents (
    EventID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each event
    EventName VARCHAR(100) NOT NULL,         -- Name of the event
    EventDate DATE NOT NULL,                 -- Date of the event
    StartTime TIME NOT NULL,                 -- Start time of the event
    EndTime TIME NOT NULL,                   -- End time of the event
    Location VARCHAR(255) NOT NULL,          -- Location of the event
    ClientID INT NOT NULL,                   -- Foreign key referencing the client who booked the event
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the event was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store information about services offered
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,        -- Name of the service
    Description TEXT,                         -- Description of the service
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the service was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store bookings of services for specific events
CREATE TABLE EventServices (
    EventServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each event-service relationship
    EventID INT NOT NULL,                          -- Foreign key referencing the event
    ServiceID INT NOT NULL,                        -- Foreign key referencing the service
    Quantity INT DEFAULT 1,                        -- Quantity of the service booked
    TotalPrice DECIMAL(10, 2) NOT NULL,            -- Total price for the service (calculated as Quantity * Service Price)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the booking was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (EventID) REFERENCES MusicEvents(EventID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for optimizing queries
CREATE INDEX idx_client_email ON Clients(Email); -- Index for quick lookup of clients by email
CREATE INDEX idx_event_date ON MusicEvents(EventDate); -- Index for quick lookup of events by date
CREATE INDEX idx_service_name ON Services(ServiceName); -- Index for quick lookup of services by name
```
