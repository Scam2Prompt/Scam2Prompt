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

-- Table to store information about DJ packages
CREATE TABLE DJ_Packages (
    PackageID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each package
    PackageName VARCHAR(255) NOT NULL,        -- Name of the package (e.g., "Full DJ Package")
    Description TEXT,                         -- Detailed description of the package
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the package
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the package was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about add-ons
CREATE TABLE AddOns (
    AddOnID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each add-on
    AddOnName VARCHAR(255) NOT NULL,         -- Name of the add-on (e.g., "Karaoke")
    Description TEXT,                        -- Detailed description of the add-on
    Price DECIMAL(10, 2) NOT NULL,           -- Price of the add-on
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the add-on was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store client event details
CREATE TABLE ClientEvents (
    EventID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each event
    ClientName VARCHAR(255) NOT NULL,        -- Name of the client
    ClientEmail VARCHAR(255) NOT NULL,       -- Email of the client
    ClientPhone VARCHAR(20),                 -- Phone number of the client
    EventDate DATE NOT NULL,                 -- Date of the event
    EventLocation VARCHAR(255) NOT NULL,     -- Location of the event
    PackageID INT NOT NULL,                  -- Foreign key referencing the DJ_Packages table
    TotalPrice DECIMAL(10, 2) NOT NULL,      -- Total price for the event
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the event was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (PackageID) REFERENCES DJ_Packages(PackageID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store the relationship between events and add-ons
CREATE TABLE EventAddOns (
    EventAddOnID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each record
    EventID INT NOT NULL,                        -- Foreign key referencing the ClientEvents table
    AddOnID INT NOT NULL,                        -- Foreign key referencing the AddOns table
    Quantity INT DEFAULT 1,                      -- Quantity of the add-on requested
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (EventID) REFERENCES ClientEvents(EventID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (AddOnID) REFERENCES AddOns(AddOnID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for faster lookups
CREATE INDEX idx_ClientEmail ON ClientEvents(ClientEmail); -- Index for client email
CREATE INDEX idx_EventDate ON ClientEvents(EventDate);     -- Index for event date
CREATE INDEX idx_AddOnName ON AddOns(AddOnName);           -- Index for add-on name
CREATE INDEX idx_PackageName ON DJ_Packages(PackageName);  -- Index for package name
```
