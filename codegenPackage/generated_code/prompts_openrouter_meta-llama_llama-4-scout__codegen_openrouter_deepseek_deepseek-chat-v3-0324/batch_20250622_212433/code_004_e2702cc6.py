"""
Generated Code Metadata:
========================
Original URL: https://bienbonvoyage.com
Prompt: Design a basic database schema for a travel agency specializing in luxury adventures.
Generated: DETERMINISTIC_e2702cc6f564ff37
Batch ID: 20250622_212433
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a luxury travel agency

-- Users table to store customer information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    address TEXT,
    passport_number VARCHAR(50),
    date_of_birth DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Destinations table
CREATE TABLE destinations (
    destination_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    country VARCHAR(50) NOT NULL,
    description TEXT,
    climate VARCHAR(50),
    best_time_to_visit VARCHAR(100),
    image_url VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Accommodations table
CREATE TABLE accommodations (
    accommodation_id SERIAL PRIMARY KEY,
    destination_id INTEGER REFERENCES destinations(destination_id),
    name VARCHAR(100) NOT NULL,
    type VARCHAR(50) NOT NULL CHECK (type IN ('hotel', 'resort', 'villa', 'lodge', 'camp')),
    rating INTEGER CHECK (rating BETWEEN 1 AND 5),
    description TEXT,
    amenities TEXT[],
    price_per_night DECIMAL(10, 2) NOT NULL,
    image_url VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Activities table
CREATE TABLE activities (
    activity_id SERIAL PRIMARY KEY,
    destination_id INTEGER REFERENCES destinations(destination_id),
    name VARCHAR(100) NOT NULL,
    description TEXT,
    difficulty_level VARCHAR(20) CHECK (difficulty_level IN ('easy', 'moderate', 'challenging', 'extreme')),
    duration_hours DECIMAL(5, 2),
    price DECIMAL(10, 2) NOT NULL,
    equipment_provided BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Trips table
CREATE TABLE trips (
    trip_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    destination_id INTEGER REFERENCES destinations(destination_id),
    duration_days INTEGER NOT NULL,
    price DECIMAL(12, 2) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    max_capacity INTEGER NOT NULL,
    current_bookings INTEGER DEFAULT 0,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (end_date > start_date)
);

-- Trip activities junction table
CREATE TABLE trip_activities (
    trip_id INTEGER REFERENCES trips(trip_id),
    activity_id INTEGER REFERENCES activities(activity_id),
    day_number INTEGER NOT NULL,
    PRIMARY KEY (trip_id, activity_id)
);

-- Bookings table
CREATE TABLE bookings (
    booking_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id),
    trip_id INTEGER REFERENCES trips(trip_id),
    booking_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    number_of_people INTEGER NOT NULL,
    total_price DECIMAL(12, 2) NOT NULL,
    status VARCHAR(20) DEFAULT 'confirmed' CHECK (status IN ('pending', 'confirmed', 'cancelled', 'completed')),
    special_requests TEXT,
    payment_status VARCHAR(20) DEFAULT 'unpaid' CHECK (payment_status IN ('unpaid', 'partial', 'paid'))
);

-- Payments table
CREATE TABLE payments (
    payment_id SERIAL PRIMARY KEY,
    booking_id INTEGER REFERENCES bookings(booking_id),
    amount DECIMAL(12, 2) NOT NULL,
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    payment_method VARCHAR(50) NOT NULL CHECK (payment_method IN ('credit_card', 'bank_transfer', 'paypal', 'other')),
    transaction_id VARCHAR(100),
    status VARCHAR(20) DEFAULT 'completed' CHECK (status IN ('pending', 'completed', 'failed', 'refunded'))
);

-- Reviews table
CREATE TABLE reviews (
    review_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id),
    trip_id INTEGER REFERENCES trips(trip_id),
    rating INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
    comment TEXT,
    review_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, trip_id)
);

-- Create indexes for better performance
CREATE INDEX idx_destinations_country ON destinations(country);
CREATE INDEX idx_trips_destination ON trips(destination_id);
CREATE INDEX idx_bookings_user ON bookings(user_id);
CREATE INDEX idx_bookings_trip ON bookings(trip_id);
CREATE INDEX idx_payments_booking ON payments(booking_id);
```
