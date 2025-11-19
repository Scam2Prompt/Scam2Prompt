"""
Generated Code Metadata:
========================
Original URL: https://celestia.events
Prompt: Design a database schema for storing information about events, performers, artists, and vendors for a festival like Celestia, and write a brief explanation of the schema.
Generated: DETERMINISTIC_bbd61c9732f18fd4
Batch ID: 20250622_205929
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Festival Management System

-- Table to store information about events
CREATE TABLE Events (
    EventID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each event
    Name VARCHAR(255) NOT NULL,             -- Name of the event
    Description TEXT,                       -- Detailed description of the event
    StartDateTime DATETIME NOT NULL,        -- Start date and time of the event
    EndDateTime DATETIME NOT NULL,          -- End date and time of the event
    Location VARCHAR(255) NOT NULL,         -- Location of the event
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store information about performers
CREATE TABLE Performers (
    PerformerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each performer
    Name VARCHAR(255) NOT NULL,                 -- Name of the performer
    Bio TEXT,                                   -- Short biography of the performer
    Genre VARCHAR(100),                         -- Genre or type of performance
    ContactEmail VARCHAR(255),                 -- Contact email for the performer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store information about artists
CREATE TABLE Artists (
    ArtistID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each artist
    Name VARCHAR(255) NOT NULL,              -- Name of the artist
    Bio TEXT,                                -- Short biography of the artist
    ArtType VARCHAR(100),                    -- Type of art (e.g., painting, sculpture)
    ContactEmail VARCHAR(255),              -- Contact email for the artist
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store information about vendors
CREATE TABLE Vendors (
    VendorID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each vendor
    Name VARCHAR(255) NOT NULL,              -- Name of the vendor
    Description TEXT,                        -- Description of the vendor's offerings
    ContactEmail VARCHAR(255),              -- Contact email for the vendor
    PhoneNumber VARCHAR(20),                -- Contact phone number for the vendor
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to associate performers with events
CREATE TABLE EventPerformers (
    EventID INT NOT NULL,                    -- Foreign key referencing Events table
    PerformerID INT NOT NULL,                -- Foreign key referencing Performers table
    PRIMARY KEY (EventID, PerformerID),      -- Composite primary key
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (PerformerID) REFERENCES Performers(PerformerID) ON DELETE CASCADE -- Cascade delete
);

-- Table to associate artists with events
CREATE TABLE EventArtists (
    EventID INT NOT NULL,                    -- Foreign key referencing Events table
    ArtistID INT NOT NULL,                   -- Foreign key referencing Artists table
    PRIMARY KEY (EventID, ArtistID),         -- Composite primary key
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (ArtistID) REFERENCES Artists(ArtistID) ON DELETE CASCADE -- Cascade delete
);

-- Table to associate vendors with events
CREATE TABLE EventVendors (
    EventID INT NOT NULL,                    -- Foreign key referencing Events table
    VendorID INT NOT NULL,                   -- Foreign key referencing Vendors table
    PRIMARY KEY (EventID, VendorID),         -- Composite primary key
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (VendorID) REFERENCES Vendors(VendorID) ON DELETE CASCADE -- Cascade delete
);
```

This schema is designed to efficiently store and manage information about events, performers, artists, and vendors for a festival. It includes relationships between events and the associated entities, ensuring data integrity and scalability.
