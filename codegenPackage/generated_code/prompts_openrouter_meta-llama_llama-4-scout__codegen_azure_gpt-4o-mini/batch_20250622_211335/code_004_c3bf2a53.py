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
-- MySQL Database Schema for ECBC Radio

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS playlists;
DROP TABLE IF EXISTS programs;
DROP TABLE IF EXISTS hosts;

-- Table to store information about hosts
CREATE TABLE hosts (
    host_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each host
    name VARCHAR(100) NOT NULL,               -- Name of the host
    bio TEXT,                                  -- Short biography of the host
    contact_info VARCHAR(255)                  -- Contact information for the host
);

-- Table to store information about programs
CREATE TABLE programs (
    program_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each program
    title VARCHAR(100) NOT NULL,                -- Title of the program
    description TEXT,                            -- Description of the program
    host_id INT,                                 -- Foreign key referencing the host
    day_of_week ENUM('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday') NOT NULL, -- Day of the week
    start_time TIME NOT NULL,                   -- Start time of the program
    end_time TIME NOT NULL,                     -- End time of the program
    FOREIGN KEY (host_id) REFERENCES hosts(host_id) ON DELETE SET NULL -- Relationship with hosts
);

-- Table to store playlists associated with programs
CREATE TABLE playlists (
    playlist_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each playlist
    program_id INT,                              -- Foreign key referencing the program
    song_title VARCHAR(100) NOT NULL,           -- Title of the song
    artist_name VARCHAR(100) NOT NULL,          -- Name of the artist
    duration TIME NOT NULL,                      -- Duration of the song
    FOREIGN KEY (program_id) REFERENCES programs(program_id) ON DELETE CASCADE -- Relationship with programs
);

-- Sample query to retrieve the program schedule for a specific day of the week
-- Replace 'Monday' with the desired day of the week
SELECT 
    p.title AS program_title,
    h.name AS host_name,
    p.start_time,
    p.end_time
FROM 
    programs p
JOIN 
    hosts h ON p.host_id = h.host_id
WHERE 
    p.day_of_week = 'Monday'  -- Specify the day of the week
ORDER BY 
    p.start_time;  -- Order the results by start time
```
