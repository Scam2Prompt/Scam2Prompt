"""
Generated Code Metadata:
========================
Original URL: https://thebalconehotel.com
Prompt: Create a SQL database schema for managing room bookings at The Balcone Suites & Resort, including tables for room types (e.g., "Superior Deluxe Room," "Grand Deluxe Mountain View"), customer details, and booking dates.
Generated: DETERMINISTIC_855c46610fe98142
Batch ID: 20250612_145933
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for The Balcone Suites & Resort Booking System

-- Create database
CREATE DATABASE IF NOT EXISTS balcone_resort_booking;
USE balcone_resort_booking;

-- Room types table
CREATE TABLE IF NOT EXISTS room_types (
    room_type_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    max_occupancy INT NOT NULL,
    base_price DECIMAL(10, 2) NOT NULL,
    amenities TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_max_occupancy CHECK (max_occupancy > 0),
    CONSTRAINT chk_base_price CHECK (base_price > 0)
) ENGINE=InnoDB;

-- Rooms inventory table
CREATE TABLE IF NOT EXISTS rooms (
    room_id INT AUTO_INCREMENT PRIMARY KEY,
    room_type_id INT NOT NULL,
    room_number VARCHAR(20) NOT NULL UNIQUE,
    floor_number INT NOT NULL,
    status ENUM('available', 'maintenance', 'out_of_service') DEFAULT 'available',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (room_type_id) REFERENCES room_types(room_type_id) ON DELETE RESTRICT,
    CONSTRAINT chk_floor_number CHECK (floor_number > 0)
) ENGINE=InnoDB;

-- Customers table
CREATE TABLE IF NOT EXISTS customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20) NOT NULL,
    address TEXT,
    city VARCHAR(50),
    country VARCHAR(50),
    id_proof_type VARCHAR(50),
    id_proof_number VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Bookings table
CREATE TABLE IF NOT EXISTS bookings (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    room_id INT NOT NULL,
    check_in_date DATE NOT NULL,
    check_out_date DATE NOT NULL,
    adults INT NOT NULL DEFAULT 1,
    children INT DEFAULT 0,
    total_amount DECIMAL(10, 2) NOT NULL,
    status ENUM('confirmed', 'cancelled', 'checked_in', 'checked_out', 'no_show') DEFAULT 'confirmed',
    special_requests TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE RESTRICT,
    FOREIGN KEY (room_id) REFERENCES rooms(room_id) ON DELETE RESTRICT,
    CONSTRAINT chk_dates CHECK (check_out_date > check_in_date),
    CONSTRAINT chk_adults CHECK (adults > 0),
    CONSTRAINT chk_children CHECK (children >= 0),
    CONSTRAINT chk_total_amount CHECK (total_amount > 0)
) ENGINE=InnoDB;

-- Payments table
CREATE TABLE IF NOT EXISTS payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    booking_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_method ENUM('credit_card', 'debit_card', 'cash', 'bank_transfer', 'online_payment') NOT NULL,
    transaction_id VARCHAR(100),
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status ENUM('pending', 'completed', 'failed', 'refunded') DEFAULT 'pending',
    notes TEXT,
    FOREIGN KEY (booking_id) REFERENCES bookings(booking_id) ON DELETE RESTRICT,
    CONSTRAINT chk_amount CHECK (amount > 0)
) ENGINE=InnoDB;

-- Room rates (for seasonal pricing)
CREATE TABLE IF NOT EXISTS room_rates (
    rate_id INT AUTO_INCREMENT PRIMARY KEY,
    room_type_id INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    rate DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (room_type_id) REFERENCES room_types(room_type_id) ON DELETE CASCADE,
    CONSTRAINT chk_rate_dates CHECK (end_date > start_date),
    CONSTRAINT chk_rate CHECK (rate > 0)
) ENGINE=InnoDB;

-- Create indexes for performance
CREATE INDEX idx_room_type ON rooms(room_type_id);
CREATE INDEX idx_booking_customer ON bookings(customer_id);
CREATE INDEX idx_booking_room ON bookings(room_id);
CREATE INDEX idx_booking_dates ON bookings(check_in_date, check_out_date);
CREATE INDEX idx_payment_booking ON payments(booking_id);
CREATE INDEX idx_room_rate_type ON room_rates(room_type_id);
CREATE INDEX idx_room_rate_dates ON room_rates(start_date, end_date);
```
