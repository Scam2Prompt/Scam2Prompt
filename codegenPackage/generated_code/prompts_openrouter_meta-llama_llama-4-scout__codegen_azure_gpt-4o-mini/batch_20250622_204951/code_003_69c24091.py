"""
Generated Code Metadata:
========================
Original URL: https://thebalconehotel.com
Prompt: Design a database schema to store information about hotel rooms, guests, and reservations for a system like The Balcone Suites & Resort.
Generated: DETERMINISTIC_69c240913da56bfe
Batch ID: 20250622_204951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for The Balcone Suites & Resort

-- Create a table to store information about hotel rooms
CREATE TABLE Rooms (
    room_id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each room
    room_number VARCHAR(10) NOT NULL,        -- Room number (e.g., "101", "202")
    room_type VARCHAR(50) NOT NULL,          -- Type of room (e.g., "Single", "Double", "Suite")
    capacity INT NOT NULL,                    -- Maximum number of guests allowed in the room
    price DECIMAL(10, 2) NOT NULL,           -- Price per night for the room
    status ENUM('available', 'occupied', 'maintenance') NOT NULL DEFAULT 'available', -- Current status of the room
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the room was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Create a table to store information about guests
CREATE TABLE Guests (
    guest_id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each guest
    first_name VARCHAR(50) NOT NULL,         -- Guest's first name
    last_name VARCHAR(50) NOT NULL,          -- Guest's last name
    email VARCHAR(100) UNIQUE NOT NULL,      -- Guest's email address (must be unique)
    phone_number VARCHAR(15),                 -- Guest's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the guest was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Create a table to store information about reservations
CREATE TABLE Reservations (
    reservation_id INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each reservation
    guest_id INT NOT NULL,                         -- Foreign key referencing the guest
    room_id INT NOT NULL,                          -- Foreign key referencing the room
    check_in_date DATE NOT NULL,                   -- Check-in date for the reservation
    check_out_date DATE NOT NULL,                 -- Check-out date for the reservation
    status ENUM('confirmed', 'checked_in', 'checked_out', 'canceled') NOT NULL DEFAULT 'confirmed', -- Current status of the reservation
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the reservation was made
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of the last update
    FOREIGN KEY (guest_id) REFERENCES Guests(guest_id) ON DELETE CASCADE, -- Ensure guest deletion cascades
    FOREIGN KEY (room_id) REFERENCES Rooms(room_id) ON DELETE CASCADE -- Ensure room deletion cascades
);

-- Create an index on the check-in and check-out dates for faster queries
CREATE INDEX idx_checkin_checkout ON Reservations (check_in_date, check_out_date);
```
