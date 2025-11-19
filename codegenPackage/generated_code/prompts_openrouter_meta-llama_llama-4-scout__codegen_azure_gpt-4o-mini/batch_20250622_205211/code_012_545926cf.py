"""
Generated Code Metadata:
========================
Original URL: https://www.predaiaarteenatura.eu
Prompt: Create a database schema to store information about the artists, exhibitions, and events organized by the Predaia Arte e Natura project.
Generated: DETERMINISTIC_545926cfb72c263c
Batch ID: 20250622_205211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Predaia Arte e Natura project

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Events;
DROP TABLE IF EXISTS Exhibitions;
DROP TABLE IF EXISTS Artists;

-- Table to store information about artists
CREATE TABLE Artists (
    artist_id SERIAL PRIMARY KEY, -- Unique identifier for each artist
    name VARCHAR(100) NOT NULL, -- Name of the artist
    bio TEXT, -- Biography of the artist
    website VARCHAR(255), -- Artist's website URL
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about exhibitions
CREATE TABLE Exhibitions (
    exhibition_id SERIAL PRIMARY KEY, -- Unique identifier for each exhibition
    title VARCHAR(100) NOT NULL, -- Title of the exhibition
    description TEXT, -- Description of the exhibition
    start_date DATE NOT NULL, -- Start date of the exhibition
    end_date DATE NOT NULL, -- End date of the exhibition
    location VARCHAR(255), -- Location of the exhibition
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about events
CREATE TABLE Events (
    event_id SERIAL PRIMARY KEY, -- Unique identifier for each event
    title VARCHAR(100) NOT NULL, -- Title of the event
    description TEXT, -- Description of the event
    event_date DATE NOT NULL, -- Date of the event
    location VARCHAR(255), -- Location of the event
    artist_id INT, -- Foreign key referencing the artist
    exhibition_id INT, -- Foreign key referencing the exhibition
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (artist_id) REFERENCES Artists(artist_id) ON DELETE SET NULL, -- Handle artist deletion
    FOREIGN KEY (exhibition_id) REFERENCES Exhibitions(exhibition_id) ON DELETE SET NULL -- Handle exhibition deletion
);

-- Indexes for faster querying
CREATE INDEX idx_artist_name ON Artists(name);
CREATE INDEX idx_exhibition_title ON Exhibitions(title);
CREATE INDEX idx_event_title ON Events(title);
```
