"""
Generated Code Metadata:
========================
Original URL: https://hamptons-uk.com
Prompt: Provide an example of a database schema for a Property Management System (PMS) in hotel operations, based on the concepts taught in Hampton's Hotel Institute's Hotel Operations Management course.
Generated: DETERMINISTIC_a92a38b986cfc740
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a Property Management System (PMS) in hotel operations

-- Create a table for storing hotel information
CREATE TABLE Hotels (
    hotel_id SERIAL PRIMARY KEY, -- Unique identifier for each hotel
    name VARCHAR(255) NOT NULL, -- Name of the hotel
    address VARCHAR(255) NOT NULL, -- Address of the hotel
    city VARCHAR(100) NOT NULL, -- City where the hotel is located
    state VARCHAR(100) NOT NULL, -- State where the hotel is located
    zip_code VARCHAR(20) NOT NULL, -- ZIP code for the hotel
    phone VARCHAR(20), -- Contact phone number for the hotel
    email VARCHAR(100), -- Contact email for the hotel
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table for storing room information
CREATE TABLE Rooms (
    room_id SERIAL PRIMARY KEY, -- Unique identifier for each room
    hotel_id INT NOT NULL, -- Foreign key referencing the hotel
    room_number VARCHAR(10) NOT NULL, -- Room number
    room_type VARCHAR(50) NOT NULL, -- Type of room (e.g., Single, Double, Suite)
    price DECIMAL(10, 2) NOT NULL, -- Price per night for the room
    status VARCHAR(20) NOT NULL DEFAULT 'Available', -- Current status of the room
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (hotel_id) REFERENCES Hotels(hotel_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table for storing guest information
CREATE TABLE Guests (
    guest_id SERIAL PRIMARY KEY, -- Unique identifier for each guest
    first_name VARCHAR(100) NOT NULL, -- Guest's first name
    last_name VARCHAR(100) NOT NULL, -- Guest's last name
    email VARCHAR(100) UNIQUE NOT NULL, -- Guest's email (must be unique)
    phone VARCHAR(20), -- Guest's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table for storing reservations
CREATE TABLE Reservations (
    reservation_id SERIAL PRIMARY KEY, -- Unique identifier for each reservation
    guest_id INT NOT NULL, -- Foreign key referencing the guest
    room_id INT NOT NULL, -- Foreign key referencing the room
    check_in_date DATE NOT NULL, -- Check-in date
    check_out_date DATE NOT NULL, -- Check-out date
    total_price DECIMAL(10, 2) NOT NULL, -- Total price for the reservation
    status VARCHAR(20) NOT NULL DEFAULT 'Confirmed', -- Current status of the reservation
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (guest_id) REFERENCES Guests(guest_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (room_id) REFERENCES Rooms(room_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table for storing payments
CREATE TABLE Payments (
    payment_id SERIAL PRIMARY KEY, -- Unique identifier for each payment
    reservation_id INT NOT NULL, -- Foreign key referencing the reservation
    amount DECIMAL(10, 2) NOT NULL, -- Amount paid
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of payment
    payment_method VARCHAR(50) NOT NULL, -- Method of payment (e.g., Credit Card, Cash)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (reservation_id) REFERENCES Reservations(reservation_id) ON DELETE CASCADE -- Ensure referential integrity
);
```
