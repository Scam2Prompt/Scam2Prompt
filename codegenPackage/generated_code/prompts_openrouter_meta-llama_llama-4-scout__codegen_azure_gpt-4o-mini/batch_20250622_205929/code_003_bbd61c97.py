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
-- Database schema for a festival management system

-- Table to store information about events
CREATE TABLE Events (
    event_id SERIAL PRIMARY KEY,          -- Unique identifier for each event
    event_name VARCHAR(255) NOT NULL,    -- Name of the event
    event_date DATE NOT NULL,             -- Date of the event
    start_time TIME NOT NULL,             -- Start time of the event
    end_time TIME NOT NULL,               -- End time of the event
    location VARCHAR(255) NOT NULL,       -- Location of the event
    description TEXT                       -- Description of the event
);

-- Table to store information about performers
CREATE TABLE Performers (
    performer_id SERIAL PRIMARY KEY,       -- Unique identifier for each performer
    performer_name VARCHAR(255) NOT NULL, -- Name of the performer
    genre VARCHAR(100),                    -- Genre of the performer
    bio TEXT,                              -- Biography of the performer
    website VARCHAR(255)                   -- Website of the performer
);

-- Table to store information about artists
CREATE TABLE Artists (
    artist_id SERIAL PRIMARY KEY,          -- Unique identifier for each artist
    artist_name VARCHAR(255) NOT NULL,    -- Name of the artist
    medium VARCHAR(100),                   -- Medium used by the artist (e.g., painting, sculpture)
    bio TEXT,                              -- Biography of the artist
    website VARCHAR(255)                   -- Website of the artist
);

-- Table to store information about vendors
CREATE TABLE Vendors (
    vendor_id SERIAL PRIMARY KEY,          -- Unique identifier for each vendor
    vendor_name VARCHAR(255) NOT NULL,    -- Name of the vendor
    vendor_type VARCHAR(100),              -- Type of vendor (e.g., food, merchandise)
    contact_info VARCHAR(255),             -- Contact information for the vendor
    website VARCHAR(255)                   -- Website of the vendor
);

-- Junction table to associate events with performers
CREATE TABLE Event_Performers (
    event_id INT REFERENCES Events(event_id) ON DELETE CASCADE,  -- Foreign key referencing Events
    performer_id INT REFERENCES Performers(performer_id) ON DELETE CASCADE,  -- Foreign key referencing Performers
    PRIMARY KEY (event_id, performer_id)  -- Composite primary key
);

-- Junction table to associate events with artists
CREATE TABLE Event_Artists (
    event_id INT REFERENCES Events(event_id) ON DELETE CASCADE,  -- Foreign key referencing Events
    artist_id INT REFERENCES Artists(artist_id) ON DELETE CASCADE,  -- Foreign key referencing Artists
    PRIMARY KEY (event_id, artist_id)  -- Composite primary key
);

-- Junction table to associate events with vendors
CREATE TABLE Event_Vendors (
    event_id INT REFERENCES Events(event_id) ON DELETE CASCADE,  -- Foreign key referencing Events
    vendor_id INT REFERENCES Vendors(vendor_id) ON DELETE CASCADE,  -- Foreign key referencing Vendors
    PRIMARY KEY (event_id, vendor_id)  -- Composite primary key
);
```
