"""
Generated Code Metadata:
========================
Original URL: https://co-djs.com
Prompt: Design a database schema to store information about DJ services, including packages (e.g., "Full" DJ Package with a 3.1 channel 3000 watt PA), add-ons (e.g., karaoke, video, and lighting), and client event details.
Generated: DETERMINISTIC_f5f7af00351687c5
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for DJ services

-- Create a table to store information about clients
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each client
    Name VARCHAR(100) NOT NULL,               -- Client's name
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Client's email address
    Phone VARCHAR(15),                        -- Client's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the client was added
);

-- Create a table to store information about DJ packages
CREATE TABLE Packages (
    PackageID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each package
    PackageName VARCHAR(100) NOT NULL,        -- Name of the package
    Description TEXT,                          -- Description of the package
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the package
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the package was added
);

-- Create a table to store information about add-ons
CREATE TABLE AddOns (
    AddOnID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each add-on
    AddOnName VARCHAR(100) NOT NULL,          -- Name of the add-on
    Description TEXT,                          -- Description of the add-on
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the add-on
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the add-on was added
);

-- Create a table to store event details
CREATE TABLE Events (
    EventID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each event
    ClientID INT NOT NULL,                     -- Foreign key referencing Clients
    EventDate DATETIME NOT NULL,               -- Date and time of the event
    Venue VARCHAR(255) NOT NULL,               -- Venue of the event
    PackageID INT NOT NULL,                    -- Foreign key referencing Packages
    TotalPrice DECIMAL(10, 2) NOT NULL,       -- Total price for the event
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the event was added
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (PackageID) REFERENCES Packages(PackageID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Create a junction table to associate events with add-ons
CREATE TABLE EventAddOns (
    EventAddOnID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each event add-on association
    EventID INT NOT NULL,                         -- Foreign key referencing Events
    AddOnID INT NOT NULL,                        -- Foreign key referencing AddOns
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (AddOnID) REFERENCES AddOns(AddOnID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_email ON Clients(Email);
CREATE INDEX idx_package_name ON Packages(PackageName);
CREATE INDEX idx_addon_name ON AddOns(AddOnName);
CREATE INDEX idx_event_date ON Events(EventDate);
```
