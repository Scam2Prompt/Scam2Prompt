"""
Generated Code Metadata:
========================
Original URL: https://boomgardi-sunland.com
Prompt: Design a simple database schema to store information about guests, rooms, and reservations for the San Land Eco-Lodge.
Generated: DETERMINISTIC_e7461a5e8c5a687f
Batch ID: 20250622_211850
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for San Land Eco-Lodge management system

-- Create database
CREATE DATABASE IF NOT EXISTS san_land_eco_lodge;
USE san_land_eco_lodge;

-- Guests table
CREATE TABLE IF NOT EXISTS guests (
    guest_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    address VARCHAR(255),
    city VARCHAR(50),
    country VARCHAR(50),
    passport_number VARCHAR(50),
    date_of_birth DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_email (email),
    INDEX idx_name (last_name, first_name)
) ENGINE=InnoDB;

-- Room types table
CREATE TABLE IF NOT EXISTS room_types (
    room_type_id INT AUTO_INCREMENT PRIMARY KEY,
    type_name VARCHAR(50) NOT NULL,
    description TEXT,
    base_price DECIMAL(10, 2) NOT NULL,
    max_occupancy INT NOT NULL,
    amenities TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Rooms table
CREATE TABLE IF NOT EXISTS rooms (
    room_id INT AUTO_INCREMENT PRIMARY KEY,
    room_number VARCHAR(10) UNIQUE NOT NULL,
    room_type_id INT NOT NULL,
    floor_number INT NOT NULL,
    view_type ENUM('garden', 'mountain', 'ocean', 'forest') NOT NULL,
    status ENUM('available', 'occupied', 'maintenance', 'cleaning') DEFAULT 'available',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (room_type_id) REFERENCES room_types(room_type_id) ON DELETE RESTRICT,
    INDEX idx_status (status)
) ENGINE=InnoDB;

-- Reservations table
CREATE TABLE IF NOT EXISTS reservations (
    reservation_id INT AUTO_INCREMENT PRIMARY KEY,
    guest_id INT NOT NULL,
    room_id INT NOT NULL,
    check_in_date DATE NOT NULL,
    check_out_date DATE NOT NULL,
    adults INT NOT NULL DEFAULT 1,
    children INT NOT NULL DEFAULT 0,
    special_requests TEXT,
    status ENUM('confirmed', 'cancelled', 'checked_in', 'checked_out', 'no_show') DEFAULT 'confirmed',
    total_price DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (guest_id) REFERENCES guests(guest_id) ON DELETE CASCADE,
    FOREIGN KEY (room_id) REFERENCES rooms(room_id) ON DELETE RESTRICT,
    INDEX idx_dates (check_in_date, check_out_date),
    INDEX idx_status (status),
    CONSTRAINT chk_dates CHECK (check_out_date > check_in_date)
) ENGINE=InnoDB;

-- Payments table
CREATE TABLE IF NOT EXISTS payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    reservation_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_method ENUM('credit_card', 'debit_card', 'cash', 'bank_transfer', 'other') NOT NULL,
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    transaction_id VARCHAR(100),
    status ENUM('pending', 'completed', 'failed', 'refunded') DEFAULT 'completed',
    notes TEXT,
    FOREIGN KEY (reservation_id) REFERENCES reservations(reservation_id) ON DELETE CASCADE,
    INDEX idx_payment_date (payment_date)
) ENGINE=InnoDB;

-- Create a view for available rooms
CREATE VIEW available_rooms AS
SELECT r.room_id, r.room_number, rt.type_name, rt.base_price, r.floor_number, r.view_type
FROM rooms r
JOIN room_types rt ON r.room_type_id = rt.room_type_id
WHERE r.status = 'available' AND r.room_id NOT IN (
    SELECT room_id FROM reservations 
    WHERE status IN ('confirmed', 'checked_in')
    AND CURRENT_DATE BETWEEN check_in_date AND check_out_date
);

-- Create a view for current guests
CREATE VIEW current_guests AS
SELECT g.guest_id, g.first_name, g.last_name, g.email, g.phone,
       r.room_number, res.check_in_date, res.check_out_date
FROM guests g
JOIN reservations res ON g.guest_id = res.guest_id
JOIN rooms r ON res.room_id = r.room_id
WHERE res.status = 'checked_in' AND CURRENT_DATE BETWEEN res.check_in_date AND res.check_out_date;
```
