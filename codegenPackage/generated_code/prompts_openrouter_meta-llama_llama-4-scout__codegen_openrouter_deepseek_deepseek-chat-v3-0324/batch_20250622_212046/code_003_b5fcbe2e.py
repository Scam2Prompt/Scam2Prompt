"""
Generated Code Metadata:
========================
Original URL: https://viamare.com.gr
Prompt: "Design a database schema to store information about yacht charter services, VIP concierge services, and travel arrangements for a company like Viamare Yachting."
Generated: DETERMINISTIC_b5fcbe2ef7ec3bd7
Batch ID: 20250622_212046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Viamare Yachting services

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Users table (clients and staff)
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    password_hash TEXT NOT NULL, -- Hashed password for authentication
    user_type TEXT NOT NULL CHECK(user_type IN ('client', 'staff', 'admin')),
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Yacht information
CREATE TABLE yachts (
    yacht_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    model TEXT NOT NULL,
    year INTEGER NOT NULL,
    length FLOAT NOT NULL, -- in meters
    capacity INTEGER NOT NULL,
    cabins INTEGER NOT NULL,
    crew_count INTEGER NOT NULL,
    description TEXT,
    base_price_per_day DECIMAL(10, 2) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    image_url TEXT,
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Yacht features
CREATE TABLE yacht_features (
    feature_id INTEGER PRIMARY KEY AUTOINCREMENT,
    yacht_id INTEGER NOT NULL,
    feature_name TEXT NOT NULL,
    feature_description TEXT,
    FOREIGN KEY (yacht_id) REFERENCES yachts(yacht_id) ON DELETE CASCADE
);

-- Yacht availability
CREATE TABLE yacht_availability (
    availability_id INTEGER PRIMARY KEY AUTOINCREMENT,
    yacht_id INTEGER NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    is_available BOOLEAN DEFAULT TRUE,
    notes TEXT,
    FOREIGN KEY (yacht_id) REFERENCES yachts(yacht_id) ON DELETE CASCADE,
    CHECK (start_date <= end_date)
);

-- Charter bookings
CREATE TABLE charter_bookings (
    booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
    yacht_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    total_price DECIMAL(12, 2) NOT NULL,
    status TEXT NOT NULL CHECK(status IN ('pending', 'confirmed', 'cancelled', 'completed')),
    special_requests TEXT,
    payment_status TEXT NOT NULL CHECK(payment_status IN ('unpaid', 'partial', 'paid')),
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (yacht_id) REFERENCES yachts(yacht_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    CHECK (start_date <= end_date)
);

-- VIP concierge services
CREATE TABLE concierge_services (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    base_price DECIMAL(10, 2) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE
);

-- Concierge service requests
CREATE TABLE concierge_requests (
    request_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    booking_id INTEGER, -- Optional link to a charter booking
    request_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    event_date DATE NOT NULL,
    special_requests TEXT,
    status TEXT NOT NULL CHECK(status IN ('pending', 'confirmed', 'cancelled', 'completed')),
    total_price DECIMAL(12, 2) NOT NULL,
    notes TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (service_id) REFERENCES concierge_services(service_id),
    FOREIGN KEY (booking_id) REFERENCES charter_bookings(booking_id)
);

-- Travel arrangements (flights, transfers, etc.)
CREATE TABLE travel_arrangements (
    arrangement_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    booking_id INTEGER, -- Optional link to a charter booking
    arrangement_type TEXT NOT NULL CHECK(arrangement_type IN ('flight', 'transfer', 'hotel', 'other')),
    description TEXT NOT NULL,
    start_date DATE,
    end_date DATE,
    departure_location TEXT,
    arrival_location TEXT,
    status TEXT NOT NULL CHECK(status IN ('pending', 'confirmed', 'cancelled', 'completed')),
    cost DECIMAL(12, 2) NOT NULL,
    notes TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (booking_id) REFERENCES charter_bookings(booking_id),
    CHECK (start_date <= end_date)
);

-- Payments
CREATE TABLE payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    booking_id INTEGER, -- Optional for charter bookings
    concierge_request_id INTEGER, -- Optional for concierge services
    travel_arrangement_id INTEGER, -- Optional for travel arrangements
    amount DECIMAL(12, 2) NOT NULL,
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    payment_method TEXT NOT NULL CHECK(payment_method IN ('credit_card', 'bank_transfer', 'cash', 'other')),
    transaction_reference TEXT,
    status TEXT NOT NULL CHECK(status IN ('pending', 'completed', 'failed', 'refunded')),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (booking_id) REFERENCES charter_bookings(booking_id),
    FOREIGN KEY (concierge_request_id) REFERENCES concierge_requests(request_id),
    FOREIGN KEY (travel_arrangement_id) REFERENCES travel_arrangements(arrangement_id)
);

-- Crew information
CREATE TABLE crew (
    crew_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    yacht_id INTEGER NOT NULL,
    position TEXT NOT NULL,
    bio TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (yacht_id) REFERENCES yachts(yacht_id)
);

-- Yacht reviews
CREATE TABLE reviews (
    review_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    yacht_id INTEGER NOT NULL,
    booking_id INTEGER NOT NULL,
    rating INTEGER NOT NULL CHECK(rating BETWEEN 1 AND 5),
    review_text TEXT,
    review_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (yacht_id) REFERENCES yachts(yacht_id),
    FOREIGN KEY (booking_id) REFERENCES charter_bookings(booking_id)
);

-- Create indexes for better performance
CREATE INDEX idx_yacht_availability ON yacht_availability(yacht_id, start_date, end_date);
CREATE INDEX idx_charter_bookings ON charter_bookings(yacht_id, user_id, start_date, end_date);
CREATE INDEX idx_concierge_requests ON concierge_requests(user_id, service_id);
CREATE INDEX idx_travel_arrangements ON travel_arrangements(user_id, booking_id);
```
