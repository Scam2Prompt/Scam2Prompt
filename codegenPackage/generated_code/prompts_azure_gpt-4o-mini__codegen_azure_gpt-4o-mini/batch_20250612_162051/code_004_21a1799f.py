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

-- Create a table to store information about clients
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each client
    Name VARCHAR(100) NOT NULL,               -- Client's name
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Client's email address
    Phone VARCHAR(15),                        -- Client's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Create a table to store information about music events
CREATE TABLE Events (
    EventID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each event
    ClientID INT NOT NULL,                     -- Foreign key referencing Clients
    EventName VARCHAR(100) NOT NULL,          -- Name of the event
    EventDate DATETIME NOT NULL,               -- Date and time of the event
    Venue VARCHAR(100) NOT NULL,               -- Venue of the event
    Description TEXT,                          -- Description of the event
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Create a table to store information about services offered
CREATE TABLE Services (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,         -- Name of the service
    Description TEXT,                           -- Description of the service
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Create a table to link events with services
CREATE TABLE EventServices (
    EventServiceID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each event-service link
    EventID INT NOT NULL,                           -- Foreign key referencing Events
    ServiceID INT NOT NULL,                         -- Foreign key referencing Services
    Quantity INT DEFAULT 1,                        -- Quantity of the service requested
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Create an index on the EventDate for faster queries
CREATE INDEX idx_event_date ON Events(EventDate);

-- Create an index on the ClientID for faster queries
CREATE INDEX idx_client_id ON Events(ClientID);
```
