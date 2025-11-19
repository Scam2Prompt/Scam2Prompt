"""
Generated Code Metadata:
========================
Original URL: https://rimedyahotel.com
Prompt: Create a SQL database schema for a hotel like Grand Rimedya, including tables for rooms (e.g., deluxe oda, twin oda), amenities (e.g., grand salon, restaurant), and customer reservations.
Generated: DETERMINISTIC_03e2816e3170a82d
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for Grand Rimedya Hotel

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS Reservations;
DROP TABLE IF EXISTS Rooms;
DROP TABLE IF EXISTS Amenities;

-- Table for storing room types
CREATE TABLE Rooms (
    room_id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each room
    room_type VARCHAR(50) NOT NULL,          -- Type of room (e.g., deluxe oda, twin oda)
    capacity INT NOT NULL,                    -- Maximum number of guests
    price DECIMAL(10, 2) NOT NULL,           -- Price per night
    description TEXT,                         -- Description of the room
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for record update
);

-- Table for storing amenities
CREATE TABLE Amenities (
    amenity_id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each amenity
    amenity_name VARCHAR(100) NOT NULL,         -- Name of the amenity (e.g., grand salon, restaurant)
    description TEXT,                            -- Description of the amenity
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for record update
);

-- Table for storing customer reservations
CREATE TABLE Reservations (
    reservation_id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each reservation
    customer_name VARCHAR(100) NOT NULL,            -- Name of the customer
    room_id INT NOT NULL,                            -- Foreign key referencing Rooms
    check_in_date DATE NOT NULL,                     -- Check-in date
    check_out_date DATE NOT NULL,                   -- Check-out date
    number_of_guests INT NOT NULL,                  -- Number of guests
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp for record update
    FOREIGN KEY (room_id) REFERENCES Rooms(room_id) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Sample data insertion (optional, for testing purposes)
INSERT INTO Rooms (room_type, capacity, price, description) VALUES
('Deluxe Oda', 2, 150.00, 'Luxurious room with a king-size bed and a beautiful view.'),
('Twin Oda', 2, 100.00, 'Comfortable room with two single beds.');

INSERT INTO Amenities (amenity_name, description) VALUES
('Grand Salon', 'A spacious area for events and gatherings.'),
('Restaurant', 'Fine dining with a variety of cuisines.');

-- Note: Ensure to handle errors and exceptions in your application logic when interacting with this database.
```
