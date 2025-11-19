"""
Generated Code Metadata:
========================
Original URL: https://potencia.in
Prompt: Create a database schema for managing hostel facilities, including features like internet access, laundry services, and reading rooms, as described on the Potencia Academy website.
Generated: DETERMINISTIC_f856d4a11f917c64
Batch ID: 20250612_142620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing hostel facilities

-- Create the database
CREATE DATABASE IF NOT EXISTS hostel_management;
USE hostel_management;

-- Hostel table
CREATE TABLE IF NOT EXISTS hostels (
    hostel_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    location VARCHAR(255) NOT NULL,
    total_rooms INT NOT NULL,
    contact_number VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_rooms CHECK (total_rooms > 0)
) ENGINE=InnoDB;

-- Room types table
CREATE TABLE IF NOT EXISTS room_types (
    type_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    capacity INT NOT NULL,
    price_per_month DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_capacity CHECK (capacity > 0),
    CONSTRAINT chk_price CHECK (price_per_month > 0)
) ENGINE=InnoDB;

-- Rooms table
CREATE TABLE IF NOT EXISTS rooms (
    room_id INT AUTO_INCREMENT PRIMARY KEY,
    hostel_id INT NOT NULL,
    type_id INT NOT NULL,
    room_number VARCHAR(20) NOT NULL,
    floor_number INT NOT NULL,
    status ENUM('available', 'occupied', 'maintenance') DEFAULT 'available',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (hostel_id) REFERENCES hostels(hostel_id) ON DELETE CASCADE,
    FOREIGN KEY (type_id) REFERENCES room_types(type_id) ON DELETE CASCADE,
    CONSTRAINT chk_floor CHECK (floor_number >= 0),
    UNIQUE KEY unique_room (hostel_id, room_number)
) ENGINE=InnoDB;

-- Facilities table
CREATE TABLE IF NOT EXISTS facilities (
    facility_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    operational_hours VARCHAR(100),
    status ENUM('available', 'unavailable', 'maintenance') DEFAULT 'available',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Hostel facilities mapping table
CREATE TABLE IF NOT EXISTS hostel_facilities (
    hostel_id INT NOT NULL,
    facility_id INT NOT NULL,
    additional_info TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (hostel_id, facility_id),
    FOREIGN KEY (hostel_id) REFERENCES hostels(hostel_id) ON DELETE CASCADE,
    FOREIGN KEY (facility_id) REFERENCES facilities(facility_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Internet access table (specialized facility)
CREATE TABLE IF NOT EXISTS internet_access (
    facility_id INT PRIMARY KEY,
    speed VARCHAR(50),
    connection_type ENUM('wired', 'wireless') NOT NULL,
    price_per_month DECIMAL(10, 2),
    is_unlimited BOOLEAN DEFAULT TRUE,
    data_cap VARCHAR(50),
    FOREIGN KEY (facility_id) REFERENCES facilities(facility_id) ON DELETE CASCADE,
    CONSTRAINT chk_internet_price CHECK (price_per_month >= 0)
) ENGINE=InnoDB;

-- Laundry services table (specialized facility)
CREATE TABLE IF NOT EXISTS laundry_services (
    facility_id INT PRIMARY KEY,
    price_per_kg DECIMAL(10, 2) NOT NULL,
    pickup_days VARCHAR(100),
    delivery_days VARCHAR(100),
    ironing_included BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (facility_id) REFERENCES facilities(facility_id) ON DELETE CASCADE,
    CONSTRAINT chk_laundry_price CHECK (price_per_kg > 0)
) ENGINE=InnoDB;

-- Reading rooms table (specialized facility)
CREATE TABLE IF NOT EXISTS reading_rooms (
    facility_id INT PRIMARY KEY,
    seating_capacity INT NOT NULL,
    opening_hours VARCHAR(100) NOT NULL,
    has_silent_zone BOOLEAN DEFAULT FALSE,
    has_computers BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (facility_id) REFERENCES facilities(facility_id) ON DELETE CASCADE,
    CONSTRAINT chk_capacity_reading CHECK (seating_capacity > 0)
) ENGINE=InnoDB;

-- Residents table
CREATE TABLE IF NOT EXISTS residents (
    resident_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone_number VARCHAR(20) NOT NULL,
    date_of_birth DATE,
    emergency_contact VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Bookings table
CREATE TABLE IF NOT EXISTS bookings (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    resident_id INT NOT NULL,
    room_id INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    status ENUM('confirmed', 'pending', 'cancelled', 'completed') DEFAULT 'pending',
    total_amount DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (resident_id) REFERENCES residents(resident_id) ON DELETE CASCADE,
    FOREIGN KEY (room_id) REFERENCES rooms(room_id) ON DELETE CASCADE,
    CONSTRAINT chk_dates CHECK (start_date < end_date),
    CONSTRAINT chk_amount CHECK (total_amount > 0)
) ENGINE=InnoDB;

-- Facility bookings table
CREATE TABLE IF NOT EXISTS facility_bookings (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    resident_id INT NOT NULL,
    facility_id INT NOT NULL,
    booking_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    status ENUM('confirmed', 'pending', 'cancelled', 'completed') DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (resident_id) REFERENCES residents(resident_id) ON DELETE CASCADE,
    FOREIGN KEY (facility_id) REFERENCES facilities(facility_id) ON DELETE CASCADE,
    CONSTRAINT chk_times CHECK (start_time < end_time)
) ENGINE=InnoDB;

-- Payments table
CREATE TABLE IF NOT EXISTS payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    booking_id INT,
    facility_booking_id INT,
    resident_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    payment_method ENUM('credit_card', 'debit_card', 'bank_transfer', 'cash', 'other') NOT NULL,
    status ENUM('pending', 'completed', 'failed', 'refunded') DEFAULT 'pending',
    transaction_reference VARCHAR(100),
    notes TEXT,
    FOREIGN KEY (booking_id) REFERENCES bookings(booking_id) ON DELETE SET NULL,
    FOREIGN KEY (facility_booking_id) REFERENCES facility_bookings(booking_id) ON DELETE SET NULL,
    FOREIGN KEY (resident_id) REFERENCES residents(resident_id) ON DELETE CASCADE,
    CONSTRAINT chk_payment_amount CHECK (amount > 0),
    CONSTRAINT chk_payment_reference CHECK (
        (booking_id IS NOT NULL AND facility_booking_id IS NULL) OR 
        (booking_id IS NULL AND facility_booking_id IS NOT NULL)
    )
) ENGINE=InnoDB;

-- Maintenance requests table
CREATE TABLE IF NOT EXISTS maintenance_requests (
    request_id INT AUTO_INCREMENT PRIMARY KEY,
    resident_id INT,
    room_id INT,
    facility_id INT,
    title VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    status ENUM('pending', 'in_progress', 'completed', 'cancelled') DEFAULT 'pending',
    priority ENUM('low', 'medium', 'high', 'emergency') DEFAULT 'medium',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    completed_at TIMESTAMP NULL,
    FOREIGN KEY (resident_id) REFERENCES residents(resident_id) ON DELETE SET NULL,
    FOREIGN KEY (room_id) REFERENCES rooms(room_id) ON DELETE SET NULL,
    FOREIGN KEY (facility_id) REFERENCES facilities(facility_id) ON DELETE SET NULL,
    CONSTRAINT chk_maintenance_reference CHECK (
        (room_id IS NOT NULL AND facility_id IS NULL) OR 
        (room_id IS NULL AND facility_id IS NOT NULL)
    )
) ENGINE=InnoDB;

-- Create indexes for better performance
CREATE INDEX idx_rooms_hostel ON rooms(hostel_id);
CREATE INDEX idx_rooms_type ON rooms(type_id);
CREATE INDEX idx_bookings_resident ON bookings(resident_id);
CREATE INDEX idx_bookings_room ON bookings(room_id);
CREATE INDEX idx_facility_bookings_resident ON facility_book
