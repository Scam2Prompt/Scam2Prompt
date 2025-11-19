"""
Generated Code Metadata:
========================
Original URL: https://hotelbangaloregate.com
Prompt: Design a database schema for managing hotel room inventory, bookings, and customer information, inspired by the features and services offered by Bangalore Gate Hotel & Conferences.
Generated: DETERMINISTIC_abc89521961e208c
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Bangalore Gate Hotel & Conferences management system

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create tables

-- Customer information
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT NOT NULL,
    address TEXT,
    city TEXT,
    state TEXT,
    country TEXT NOT NULL,
    postal_code TEXT,
    id_proof_type TEXT,
    id_proof_number TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%.%')
);

-- Room types
CREATE TABLE room_types (
    room_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    type_name TEXT NOT NULL UNIQUE,
    description TEXT,
    base_price DECIMAL(10, 2) NOT NULL,
    max_occupancy INTEGER NOT NULL,
    amenities TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (base_price > 0),
    CHECK (max_occupancy > 0)
);

-- Rooms inventory
CREATE TABLE rooms (
    room_id INTEGER PRIMARY KEY AUTOINCREMENT,
    room_number TEXT NOT NULL UNIQUE,
    room_type_id INTEGER NOT NULL,
    floor_number INTEGER NOT NULL,
    status TEXT NOT NULL DEFAULT 'available', -- available, occupied, maintenance
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (room_type_id) REFERENCES room_types(room_type_id),
    CHECK (status IN ('available', 'occupied', 'maintenance')),
    CHECK (floor_number > 0)
);

-- Booking statuses
CREATE TABLE booking_statuses (
    status_id INTEGER PRIMARY KEY AUTOINCREMENT,
    status_name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Bookings
CREATE TABLE bookings (
    booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    room_id INTEGER NOT NULL,
    status_id INTEGER NOT NULL DEFAULT 1, -- default to 'confirmed'
    check_in_date DATE NOT NULL,
    check_out_date DATE NOT NULL,
    adults INTEGER NOT NULL DEFAULT 1,
    children INTEGER NOT NULL DEFAULT 0,
    total_amount DECIMAL(10, 2) NOT NULL,
    special_requests TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (room_id) REFERENCES rooms(room_id),
    FOREIGN KEY (status_id) REFERENCES booking_statuses(status_id),
    CHECK (check_out_date > check_in_date),
    CHECK (adults > 0),
    CHECK (children >= 0),
    CHECK (total_amount > 0)
);

-- Payments
CREATE TABLE payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    booking_id INTEGER NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_method TEXT NOT NULL,
    transaction_id TEXT,
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status TEXT NOT NULL DEFAULT 'pending', -- pending, completed, failed, refunded
    FOREIGN KEY (booking_id) REFERENCES bookings(booking_id),
    CHECK (amount > 0),
    CHECK (status IN ('pending', 'completed', 'failed', 'refunded'))
);

-- Services (restaurant, spa, conference rooms, etc.)
CREATE TABLE services (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    service_name TEXT NOT NULL UNIQUE,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (price >= 0)
);

-- Booked services (additional services booked with rooms)
CREATE TABLE booked_services (
    booking_service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    booking_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 1,
    scheduled_time TIMESTAMP,
    notes TEXT,
    FOREIGN KEY (booking_id) REFERENCES bookings(booking_id),
    FOREIGN KEY (service_id) REFERENCES services(service_id),
    CHECK (quantity > 0)
);

-- Staff information
CREATE TABLE staff (
    staff_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT NOT NULL,
    position TEXT NOT NULL,
    department TEXT NOT NULL,
    hire_date DATE NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%.%')
);

-- Room maintenance log
CREATE TABLE maintenance_log (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    room_id INTEGER NOT NULL,
    staff_id INTEGER NOT NULL,
    issue_description TEXT NOT NULL,
    reported_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    resolved_date TIMESTAMP,
    status TEXT NOT NULL DEFAULT 'reported', -- reported, in_progress, resolved
    FOREIGN KEY (room_id) REFERENCES rooms(room_id),
    FOREIGN KEY (staff_id) REFERENCES staff(staff_id),
    CHECK (status IN ('reported', 'in_progress', 'resolved'))
);

-- Insert initial data for booking statuses
INSERT INTO booking_statuses (status_name, description) VALUES 
('confirmed', 'Booking is confirmed'),
('cancelled', 'Booking was cancelled'),
('checked_in', 'Guest has checked in'),
('checked_out', 'Guest has checked out'),
('no_show', 'Guest did not arrive');

-- Create indexes for performance
CREATE INDEX idx_rooms_room_type ON rooms(room_type_id);
CREATE INDEX idx_bookings_customer ON bookings(customer_id);
CREATE INDEX idx_bookings_room ON bookings(room_id);
CREATE INDEX idx_bookings_dates ON bookings(check_in_date, check_out_date);
CREATE INDEX idx_payments_booking ON payments(booking_id);
CREATE INDEX idx_booked_services_booking ON booked_services(booking_id);
```
