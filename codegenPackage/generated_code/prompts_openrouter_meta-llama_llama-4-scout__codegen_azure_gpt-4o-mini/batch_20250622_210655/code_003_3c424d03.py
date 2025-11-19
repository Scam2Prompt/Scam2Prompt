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
-- Database schema for Karaoke Heaven

-- Create a table to store information about karaoke rooms
CREATE TABLE karaoke_rooms (
    room_id SERIAL PRIMARY KEY,          -- Unique identifier for each karaoke room
    location_id INT NOT NULL,            -- Foreign key referencing the location
    room_name VARCHAR(100) NOT NULL,     -- Name of the karaoke room
    capacity INT NOT NULL,                -- Maximum capacity of the room
    amenities TEXT,                       -- Description of amenities available in the room
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (location_id) REFERENCES locations(location_id) -- Foreign key constraint
);

-- Create a table to store information about locations
CREATE TABLE locations (
    location_id SERIAL PRIMARY KEY,       -- Unique identifier for each location
    location_name VARCHAR(100) NOT NULL,  -- Name of the location
    address VARCHAR(255) NOT NULL,        -- Address of the location
    phone_number VARCHAR(15),              -- Contact number for the location
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Create a table to store information about events
CREATE TABLE events (
    event_id SERIAL PRIMARY KEY,           -- Unique identifier for each event
    location_id INT NOT NULL,              -- Foreign key referencing the location
    event_name VARCHAR(100) NOT NULL,      -- Name of the event
    event_date TIMESTAMP NOT NULL,         -- Date and time of the event
    event_type VARCHAR(50) NOT NULL,       -- Type of event (e.g., birthday, corporate)
    description TEXT,                      -- Description of the event
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (location_id) REFERENCES locations(location_id) -- Foreign key constraint
);

-- Create a table to store information about songs
CREATE TABLE songs (
    song_id SERIAL PRIMARY KEY,            -- Unique identifier for each song
    title VARCHAR(255) NOT NULL,           -- Title of the song
    artist VARCHAR(255) NOT NULL,          -- Artist of the song
    genre VARCHAR(100),                     -- Genre of the song
    duration INT,                          -- Duration of the song in seconds
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Create a table to link songs to karaoke rooms
CREATE TABLE room_songs (
    room_song_id SERIAL PRIMARY KEY,       -- Unique identifier for each room-song link
    room_id INT NOT NULL,                  -- Foreign key referencing the karaoke room
    song_id INT NOT NULL,                  -- Foreign key referencing the song
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (room_id) REFERENCES karaoke_rooms(room_id), -- Foreign key constraint
    FOREIGN KEY (song_id) REFERENCES songs(song_id) -- Foreign key constraint
);

-- Create a table to store bookings for events
CREATE TABLE bookings (
    booking_id SERIAL PRIMARY KEY,         -- Unique identifier for each booking
    event_id INT NOT NULL,                 -- Foreign key referencing the event
    customer_name VARCHAR(100) NOT NULL,   -- Name of the customer making the booking
    contact_number VARCHAR(15),             -- Contact number of the customer
    number_of_guests INT NOT NULL,         -- Number of guests for the booking
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (event_id) REFERENCES events(event_id) -- Foreign key constraint
);
```
