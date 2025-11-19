"""
Generated Code Metadata:
========================
Original URL: https://samaneventos.com
Prompt: Design a database schema to store information about hotel rooms, restaurant menus, and event planning services, similar to those offered by Saman Eventos.
Generated: DETERMINISTIC_b0596554b9c56c61
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Database Schema for Hotel, Restaurant, and Event Planning Services

```sql
-- Database schema for Saman Eventos-like service
-- Includes tables for hotels, rooms, menus, events, and related entities

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Hotels table
CREATE TABLE hotels (
    hotel_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT NOT NULL,
    rating REAL CHECK (rating BETWEEN 0 AND 5),
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_hotel_email UNIQUE (email)
);

-- Room types table
CREATE TABLE room_types (
    type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    base_price REAL NOT NULL CHECK (base_price >= 0),
    max_occupancy INTEGER NOT NULL CHECK (max_occupancy > 0),
    amenities TEXT
);

-- Hotel rooms table
CREATE TABLE rooms (
    room_id INTEGER PRIMARY KEY AUTOINCREMENT,
    hotel_id INTEGER NOT NULL,
    type_id INTEGER NOT NULL,
    room_number TEXT NOT NULL,
    floor INTEGER NOT NULL,
    is_available BOOLEAN DEFAULT TRUE,
    special_notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (hotel_id) REFERENCES hotels(hotel_id) ON DELETE CASCADE,
    FOREIGN KEY (type_id) REFERENCES room_types(type_id),
    CONSTRAINT unique_room_number UNIQUE (hotel_id, room_number)
);

-- Restaurant categories table
CREATE TABLE restaurant_categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT
);

-- Restaurants table
CREATE TABLE restaurants (
    restaurant_id INTEGER PRIMARY KEY AUTOINCREMENT,
    hotel_id INTEGER,
    name TEXT NOT NULL,
    address TEXT,
    city TEXT,
    country TEXT,
    phone TEXT NOT NULL,
    email TEXT NOT NULL,
    opening_hours TEXT,
    capacity INTEGER CHECK (capacity >= 0),
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (hotel_id) REFERENCES hotels(hotel_id) ON DELETE SET NULL,
    CONSTRAINT unique_restaurant_email UNIQUE (email)
);

-- Menu items table
CREATE TABLE menu_items (
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    restaurant_id INTEGER NOT NULL,
    category_id INTEGER,
    name TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL CHECK (price >= 0),
    is_vegetarian BOOLEAN DEFAULT FALSE,
    is_vegan BOOLEAN DEFAULT FALSE,
    is_gluten_free BOOLEAN DEFAULT FALSE,
    preparation_time INTEGER CHECK (preparation_time >= 0),
    FOREIGN KEY (restaurant_id) REFERENCES restaurants(restaurant_id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES restaurant_categories(category_id) ON DELETE SET NULL
);

-- Event types table
CREATE TABLE event_types (
    type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT
);

-- Events table
CREATE TABLE events (
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    type_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    start_datetime TIMESTAMP NOT NULL,
    end_datetime TIMESTAMP NOT NULL,
    location TEXT,
    expected_attendees INTEGER CHECK (expected_attendees >= 0),
    budget REAL CHECK (budget >= 0),
    status TEXT DEFAULT 'planned' CHECK (status IN ('planned', 'confirmed', 'in-progress', 'completed', 'cancelled')),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (type_id) REFERENCES event_types(type_id),
    CHECK (end_datetime > start_datetime)
);

-- Event services table (many-to-many relationship)
CREATE TABLE event_services (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id INTEGER NOT NULL,
    service_type TEXT NOT NULL CHECK (service_type IN ('catering', 'decoration', 'entertainment', 'other')),
    provider_id INTEGER,
    description TEXT NOT NULL,
    cost REAL NOT NULL CHECK (cost >= 0),
    status TEXT DEFAULT 'pending' CHECK (status IN ('pending', 'confirmed', 'completed', 'cancelled')),
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE
);

-- Bookings table (for rooms and events)
CREATE TABLE bookings (
    booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT NOT NULL,
    customer_email TEXT NOT NULL,
    customer_phone TEXT NOT NULL,
    booking_type TEXT NOT NULL CHECK (booking_type IN ('room', 'event')),
    room_id INTEGER,
    event_id INTEGER,
    check_in_date DATE,
    check_out_date DATE,
    num_guests INTEGER CHECK (num_guests > 0),
    special_requests TEXT,
    status TEXT DEFAULT 'pending' CHECK (status IN ('pending', 'confirmed', 'checked-in', 'checked-out', 'cancelled')),
    total_amount REAL CHECK (total_amount >= 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (room_id) REFERENCES rooms(room_id) ON DELETE SET NULL,
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE SET NULL,
    CHECK (
        (booking_type = 'room' AND room_id IS NOT NULL AND check_in_date IS NOT NULL AND check_out_date IS NOT NULL) OR
        (booking_type = 'event' AND event_id IS NOT NULL)
    ),
    CHECK (check_out_date > check_in_date OR booking_type = 'event')
);

-- Payments table
CREATE TABLE payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    booking_id INTEGER NOT NULL,
    amount REAL NOT NULL CHECK (amount > 0),
    payment_method TEXT NOT NULL CHECK (payment_method IN ('credit_card', 'debit_card', 'cash', 'bank_transfer', 'other')),
    transaction_id TEXT,
    status TEXT NOT NULL CHECK (status IN ('pending', 'completed', 'failed', 'refunded')),
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    FOREIGN KEY (booking_id) REFERENCES bookings(booking_id) ON DELETE CASCADE
);

-- Create indexes for better performance
CREATE INDEX idx_rooms_hotel_id ON rooms(hotel_id);
CREATE INDEX idx_menu_items_restaurant_id ON menu_items(restaurant_id);
CREATE INDEX idx_events_type_id ON events(type_id);
CREATE INDEX idx_event_services_event_id ON event_services(event_id);
CREATE INDEX idx_bookings_room_id ON bookings(room_id);
CREATE INDEX idx_bookings_event_id ON bookings(event_id);
CREATE INDEX idx_payments_booking_id ON payments(booking_id);
```
