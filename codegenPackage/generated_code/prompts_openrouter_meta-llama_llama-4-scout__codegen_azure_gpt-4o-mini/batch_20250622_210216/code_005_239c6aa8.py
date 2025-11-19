"""
Generated Code Metadata:
========================
Original URL: https://koltinsuchitoto.com
Prompt: Design a database schema to store information about hotel rooms, guests, and reservations for a hostel like Hostal Koltin Suchitoto.
Generated: DETERMINISTIC_239c6aa8d7be01fe
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a hostel management system

-- Create a table to store information about hotel rooms
CREATE TABLE Rooms (
    room_id SERIAL PRIMARY KEY,          -- Unique identifier for each room
    room_number VARCHAR(10) NOT NULL,   -- Room number (e.g., "101", "102")
    room_type VARCHAR(50) NOT NULL,      -- Type of room (e.g., "Single", "Double", "Dormitory")
    capacity INT NOT NULL,                -- Maximum number of guests allowed in the room
    price DECIMAL(10, 2) NOT NULL,       -- Price per night for the room
    is_available BOOLEAN DEFAULT TRUE,    -- Availability status of the room
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of room creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store information about guests
CREATE TABLE Guests (
    guest_id SERIAL PRIMARY KEY,          -- Unique identifier for each guest
    first_name VARCHAR(50) NOT NULL,     -- Guest's first name
    last_name VARCHAR(50) NOT NULL,      -- Guest's last name
    email VARCHAR(100) UNIQUE NOT NULL,   -- Guest's email address (must be unique)
    phone_number VARCHAR(15),             -- Guest's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of guest creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store reservations
CREATE TABLE Reservations (
    reservation_id SERIAL PRIMARY KEY,    -- Unique identifier for each reservation
    guest_id INT NOT NULL,                -- Foreign key referencing the guest
    room_id INT NOT NULL,                 -- Foreign key referencing the room
    check_in_date DATE NOT NULL,          -- Check-in date for the reservation
    check_out_date DATE NOT NULL,         -- Check-out date for the reservation
    total_price DECIMAL(10, 2) NOT NULL,  -- Total price for the reservation
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of reservation creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (guest_id) REFERENCES Guests(guest_id) ON DELETE CASCADE, -- Ensure guest deletion cascades
    FOREIGN KEY (room_id) REFERENCES Rooms(room_id) ON DELETE CASCADE -- Ensure room deletion cascades
);

-- Create an index on the email column in the Guests table for faster lookups
CREATE INDEX idx_guest_email ON Guests(email);

-- Create an index on the room_number column in the Rooms table for faster lookups
CREATE INDEX idx_room_number ON Rooms(room_number);
```
