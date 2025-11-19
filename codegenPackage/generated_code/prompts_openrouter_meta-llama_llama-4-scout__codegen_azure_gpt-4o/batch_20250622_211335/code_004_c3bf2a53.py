"""
Generated Code Metadata:
========================
Original URL: https://ecbc.online
Prompt: Design a MySQL database schema to store information about ECBC Radio's programs, hosts, and playlists, and provide a sample query to retrieve the program schedule for a specific day of the week.
Generated: DETERMINISTIC_c3bf2a5330a77c5f
Batch ID: 20250622_211335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for ECBC Radio
CREATE DATABASE IF NOT EXISTS ECBC_Radio;
USE ECBC_Radio;

-- Table to store information about programs
CREATE TABLE Programs (
    ProgramID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each program
    ProgramName VARCHAR(255) NOT NULL,        -- Name of the program
    Description TEXT,                         -- Description of the program
    DayOfWeek ENUM('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday') NOT NULL, -- Day of the week the program airs
    StartTime TIME NOT NULL,                  -- Start time of the program
    EndTime TIME NOT NULL                     -- End time of the program
);

-- Table to store information about hosts
CREATE TABLE Hosts (
    HostID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each host
    HostName VARCHAR(255) NOT NULL,          -- Name of the host
    Bio TEXT                                 -- Short biography of the host
);

-- Table to store the relationship between programs and hosts
CREATE TABLE ProgramHosts (
    ProgramID INT NOT NULL,                  -- Foreign key referencing Programs table
    HostID INT NOT NULL,                     -- Foreign key referencing Hosts table
    PRIMARY KEY (ProgramID, HostID),         -- Composite primary key
    FOREIGN KEY (ProgramID) REFERENCES Programs(ProgramID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (HostID) REFERENCES Hosts(HostID) ON DELETE CASCADE           -- Cascade delete
);

-- Table to store playlists for each program
CREATE TABLE Playlists (
    PlaylistID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each playlist
    ProgramID INT NOT NULL,                    -- Foreign key referencing Programs table
    SongTitle VARCHAR(255) NOT NULL,           -- Title of the song
    ArtistName VARCHAR(255) NOT NULL,          -- Name of the artist
    FOREIGN KEY (ProgramID) REFERENCES Programs(ProgramID) ON DELETE CASCADE -- Cascade delete
);

-- Sample query to retrieve the program schedule for a specific day of the week
-- Replace 'Monday' with the desired day of the week
SELECT 
    ProgramName,
    Description,
    StartTime,
    EndTime,
    GROUP_CONCAT(HostName SEPARATOR ', ') AS Hosts
FROM 
    Programs
LEFT JOIN 
    ProgramHosts ON Programs.ProgramID = ProgramHosts.ProgramID
LEFT JOIN 
    Hosts ON ProgramHosts.HostID = Hosts.HostID
WHERE 
    DayOfWeek = 'Monday'
GROUP BY 
    Programs.ProgramID
ORDER BY 
    StartTime;
```
