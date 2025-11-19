"""
Generated Code Metadata:
========================
Original URL: https://karaokeheaven.uk
Prompt: Design a database schema to store information about karaoke rooms, events, and song libraries for a venue like Karaoke Heaven, which has 7 locations in London and offers various events like birthday parties and corporate events.
Generated: DETERMINISTIC_3c424d03fe7dd640
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Karaoke Heaven

-- Table to store information about locations
CREATE TABLE Locations (
    LocationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each location
    Name VARCHAR(100) NOT NULL,                -- Name of the location
    Address VARCHAR(255) NOT NULL,             -- Address of the location
    City VARCHAR(100) NOT NULL,                -- City where the location is situated
    PostalCode VARCHAR(20) NOT NULL,           -- Postal code of the location
    PhoneNumber VARCHAR(20),                   -- Contact number for the location
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store information about karaoke rooms
CREATE TABLE KaraokeRooms (
    RoomID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each room
    LocationID INT NOT NULL,                   -- Foreign key referencing Locations table
    Name VARCHAR(100) NOT NULL,                -- Name of the room
    Capacity INT NOT NULL,                     -- Maximum capacity of the room
    IsAvailable BOOLEAN DEFAULT TRUE,          -- Availability status of the room
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (LocationID) REFERENCES Locations(LocationID) ON DELETE CASCADE
);

-- Table to store information about events
CREATE TABLE Events (
    EventID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each event
    LocationID INT NOT NULL,                   -- Foreign key referencing Locations table
    RoomID INT NOT NULL,                       -- Foreign key referencing KaraokeRooms table
    EventType VARCHAR(100) NOT NULL,           -- Type of event (e.g., birthday party, corporate event)
    EventDate DATE NOT NULL,                   -- Date of the event
    StartTime TIME NOT NULL,                   -- Start time of the event
    EndTime TIME NOT NULL,                     -- End time of the event
    OrganizerName VARCHAR(100) NOT NULL,       -- Name of the event organizer
    OrganizerContact VARCHAR(20),              -- Contact information of the organizer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (LocationID) REFERENCES Locations(LocationID) ON DELETE CASCADE,
    FOREIGN KEY (RoomID) REFERENCES KaraokeRooms(RoomID) ON DELETE CASCADE
);

-- Table to store information about songs in the library
CREATE TABLE SongLibrary (
    SongID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each song
    Title VARCHAR(255) NOT NULL,               -- Title of the song
    Artist VARCHAR(255) NOT NULL,              -- Artist of the song
    Genre VARCHAR(100),                        -- Genre of the song
    Language VARCHAR(100),                     -- Language of the song
    Duration TIME,                             -- Duration of the song
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store the association between karaoke rooms and songs
CREATE TABLE RoomSongMapping (
    MappingID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each mapping
    RoomID INT NOT NULL,                       -- Foreign key referencing KaraokeRooms table
    SongID INT NOT NULL,                       -- Foreign key referencing SongLibrary table
    FOREIGN KEY (RoomID) REFERENCES KaraokeRooms(RoomID) ON DELETE CASCADE,
    FOREIGN KEY (SongID) REFERENCES SongLibrary(SongID) ON DELETE CASCADE
);

-- Table to store the association between events and songs
CREATE TABLE EventSongMapping (
    MappingID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each mapping
    EventID INT NOT NULL,                      -- Foreign key referencing Events table
    SongID INT NOT NULL,                       -- Foreign key referencing SongLibrary table
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE,
    FOREIGN KEY (SongID) REFERENCES SongLibrary(SongID) ON DELETE CASCADE
);
```
