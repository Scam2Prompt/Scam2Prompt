"""
Generated Code Metadata:
========================
Original URL: https://dunhill-servicedapartments.com
Prompt: Design a simple database schema using SQL to store information about serviced apartments, including apartment details, locations, and booking status, inspired by the types of data presented on the Dunhill Serviced and Furnished Apartments website.
Generated: DETERMINISTIC_84aa6bd6e59a47ef
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for serviced apartments
CREATE DATABASE ServicedApartments;

-- Use the created database
USE ServicedApartments;

-- Table to store apartment details
CREATE TABLE Apartments (
    apartment_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each apartment
    name VARCHAR(100) NOT NULL,                    -- Name of the apartment
    description TEXT,                               -- Description of the apartment
    price_per_night DECIMAL(10, 2) NOT NULL,      -- Price per night for the apartment
    number_of_bedrooms INT NOT NULL,               -- Number of bedrooms in the apartment
    number_of_bathrooms INT NOT NULL,              -- Number of bathrooms in the apartment
    amenities JSON,                                 -- JSON field to store amenities
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the apartment was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store location details
CREATE TABLE Locations (
    location_id INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each location
    apartment_id INT NOT NULL,                      -- Foreign key referencing Apartments
    address VARCHAR(255) NOT NULL,                  -- Full address of the apartment
    city VARCHAR(100) NOT NULL,                     -- City where the apartment is located
    state VARCHAR(100) NOT NULL,                    -- State where the apartment is located
    country VARCHAR(100) NOT NULL,                  -- Country where the apartment is located
    postal_code VARCHAR(20) NOT NULL,               -- Postal code for the location
    FOREIGN KEY (apartment_id) REFERENCES Apartments(apartment_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store booking status
CREATE TABLE Bookings (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each booking
    apartment_id INT NOT NULL,                      -- Foreign key referencing Apartments
    guest_name VARCHAR(100) NOT NULL,               -- Name of the guest making the booking
    check_in_date DATE NOT NULL,                    -- Check-in date for the booking
    check_out_date DATE NOT NULL,                   -- Check-out date for the booking
    status ENUM('confirmed', 'pending', 'canceled') NOT NULL DEFAULT 'pending', -- Booking status
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the booking was made
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (apartment_id) REFERENCES Apartments(apartment_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_apartment_name ON Apartments(name);
CREATE INDEX idx_location_city ON Locations(city);
CREATE INDEX idx_booking_status ON Bookings(status);
```
