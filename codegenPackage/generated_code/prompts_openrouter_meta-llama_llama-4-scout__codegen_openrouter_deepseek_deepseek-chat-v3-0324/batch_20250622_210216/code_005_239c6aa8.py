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

# Database Schema for Hostel Management System

```sql
-- Database: hostal_koltin_suchitoto

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Table for storing room types
CREATE TABLE IF NOT EXISTS room_types (
    type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    base_price DECIMAL(10, 2) NOT NULL,
    max_occupancy INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (base_price >= 0),
    CHECK (max_occupancy > 0)
);

-- Table for storing rooms
CREATE TABLE IF NOT EXISTS rooms (
    room_id INTEGER PRIMARY KEY AUTOINCREMENT,
    room_number TEXT NOT NULL UNIQUE,
    type_id INTEGER NOT NULL,
    floor INTEGER NOT NULL,
    status TEXT NOT NULL DEFAULT 'available', -- 'available', 'occupied', 'maintenance'
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (type_id) REFERENCES room_types(type_id),
    CHECK (floor >= 0),
    CHECK (status IN ('available', 'occupied', 'maintenance'))
);

-- Table for storing guests
CREATE TABLE IF NOT EXISTS guests (
    guest_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE,
    phone TEXT NOT NULL,
    address TEXT,
    city TEXT,
    country TEXT,
    id_type TEXT, -- 'passport', 'driver_license', etc.
    id_number TEXT,
    birth_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%.%' OR email IS NULL)
);

-- Table for storing reservations
CREATE TABLE IF NOT EXISTS reservations (
    reservation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    guest_id INTEGER NOT NULL,
    room_id INTEGER NOT NULL,
    check_in_date DATE NOT NULL,
    check_out_date DATE NOT NULL,
    adults INTEGER NOT NULL DEFAULT 1,
    children INTEGER NOT NULL DEFAULT 0,
    status TEXT NOT NULL DEFAULT 'confirmed', -- 'confirmed', 'checked_in', 'checked_out', 'cancelled'
    total_price DECIMAL(10, 2) NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (guest_id) REFERENCES guests(guest_id),
    FOREIGN KEY (room_id) REFERENCES rooms(room_id),
    CHECK (check_out_date > check_in_date),
    CHECK (adults > 0),
    CHECK (children >= 0),
    CHECK (status IN ('confirmed', 'checked_in', 'checked_out', 'cancelled')),
    CHECK (total_price >= 0)
);

-- Table for storing payments
CREATE TABLE IF NOT EXISTS payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    reservation_id INTEGER NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_method TEXT NOT NULL, -- 'cash', 'credit_card', 'bank_transfer', etc.
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    transaction_id TEXT,
    status TEXT NOT NULL DEFAULT 'completed', -- 'pending', 'completed', 'failed', 'refunded'
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (reservation_id) REFERENCES reservations(reservation_id),
    CHECK (amount > 0),
    CHECK (status IN ('pending', 'completed', 'failed', 'refunded'))
);

-- Table for storing room amenities
CREATE TABLE IF NOT EXISTS amenities (
    amenity_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Junction table for room type amenities
CREATE TABLE IF NOT EXISTS room_type_amenities (
    type_id INTEGER NOT NULL,
    amenity_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (type_id, amenity_id),
    FOREIGN KEY (type_id) REFERENCES room_types(type_id),
    FOREIGN KEY (amenity_id) REFERENCES amenities(amenity_id)
);

-- Table for storing staff members
CREATE TABLE IF NOT EXISTS staff (
    staff_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT NOT NULL,
    role TEXT NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%.%')
);

-- Table for audit logging
CREATE TABLE IF NOT EXISTS audit_log (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    action TEXT NOT NULL, -- 'create', 'update', 'delete'
    table_name TEXT NOT NULL,
    record_id INTEGER NOT NULL,
    staff_id INTEGER,
    old_values TEXT,
    new_values TEXT,
    action_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (staff_id) REFERENCES staff(staff_id)
);

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_reservations_guest ON reservations(guest_id);
CREATE INDEX IF NOT EXISTS idx_reservations_room ON reservations(room_id);
CREATE INDEX IF NOT EXISTS idx_reservations_dates ON reservations(check_in_date, check_out_date);
CREATE INDEX IF NOT EXISTS idx_payments_reservation ON payments(reservation_id);
CREATE INDEX IF NOT EXISTS idx_rooms_type ON rooms(type_id);
CREATE INDEX IF NOT EXISTS idx_rooms_status ON rooms(status);
```
