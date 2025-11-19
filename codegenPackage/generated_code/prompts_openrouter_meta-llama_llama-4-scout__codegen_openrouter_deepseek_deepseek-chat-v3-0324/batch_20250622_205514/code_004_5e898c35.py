"""
Generated Code Metadata:
========================
Original URL: https://roc-remi.com
Prompt: Design a database schema for storing information about vacation rentals like Chalet Roc Remi, including details about the property, rooms, activities, and guest reviews.
Generated: DETERMINISTIC_5e898c3579abe4ea
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Vacation Rental Database Schema

```sql
-- Database schema for vacation rental management system
-- Supports properties, rooms, amenities, activities, bookings, and reviews

CREATE TABLE property_types (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT
);

CREATE TABLE properties (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    address TEXT NOT NULL,
    city VARCHAR(100) NOT NULL,
    region VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL,
    postal_code VARCHAR(20) NOT NULL,
    latitude DECIMAL(10, 8),
    longitude DECIMAL(11, 8),
    property_type_id INTEGER REFERENCES property_types(id),
    max_guests INTEGER NOT NULL,
    bedrooms INTEGER NOT NULL,
    bathrooms INTEGER NOT NULL,
    square_meters INTEGER,
    base_price DECIMAL(10, 2) NOT NULL,
    minimum_stay INTEGER DEFAULT 1,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE property_images (
    id SERIAL PRIMARY KEY,
    property_id INTEGER REFERENCES properties(id) ON DELETE CASCADE,
    image_url TEXT NOT NULL,
    caption VARCHAR(255),
    is_primary BOOLEAN DEFAULT FALSE,
    display_order INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE amenities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    icon VARCHAR(50),
    category VARCHAR(50) NOT NULL
);

CREATE TABLE property_amenities (
    property_id INTEGER REFERENCES properties(id) ON DELETE CASCADE,
    amenity_id INTEGER REFERENCES amenities(id) ON DELETE CASCADE,
    notes TEXT,
    PRIMARY KEY (property_id, amenity_id)
);

CREATE TABLE rooms (
    id SERIAL PRIMARY KEY,
    property_id INTEGER REFERENCES properties(id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    room_type VARCHAR(50) NOT NULL,
    beds INTEGER NOT NULL,
    bed_type VARCHAR(50) NOT NULL,
    max_occupancy INTEGER NOT NULL,
    size_sqm INTEGER
);

CREATE TABLE room_images (
    id SERIAL PRIMARY KEY,
    room_id INTEGER REFERENCES rooms(id) ON DELETE CASCADE,
    image_url TEXT NOT NULL,
    caption VARCHAR(255),
    is_primary BOOLEAN DEFAULT FALSE,
    display_order INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE activities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    category VARCHAR(50) NOT NULL,
    difficulty_level VARCHAR(20),
    seasonality VARCHAR(50),
    duration_minutes INTEGER
);

CREATE TABLE property_activities (
    property_id INTEGER REFERENCES properties(id) ON DELETE CASCADE,
    activity_id INTEGER REFERENCES activities(id) ON DELETE CASCADE,
    distance_km DECIMAL(5, 2),
    notes TEXT,
    PRIMARY KEY (property_id, activity_id)
);

CREATE TABLE guests (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(20),
    address TEXT,
    city VARCHAR(100),
    country VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    property_id INTEGER REFERENCES properties(id),
    guest_id INTEGER REFERENCES guests(id),
    check_in_date DATE NOT NULL,
    check_out_date DATE NOT NULL,
    adults INTEGER NOT NULL,
    children INTEGER DEFAULT 0,
    infants INTEGER DEFAULT 0,
    total_price DECIMAL(10, 2) NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'confirmed',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_dates CHECK (check_out_date > check_in_date)
);

CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    property_id INTEGER REFERENCES properties(id),
    booking_id INTEGER REFERENCES bookings(id) UNIQUE,
    guest_id INTEGER REFERENCES guests(id),
    cleanliness_rating INTEGER CHECK (cleanliness_rating BETWEEN 1 AND 5),
    comfort_rating INTEGER CHECK (comfort_rating BETWEEN 1 AND 5),
    location_rating INTEGER CHECK (location_rating BETWEEN 1 AND 5),
    value_rating INTEGER CHECK (value_rating BETWEEN 1 AND 5),
    overall_rating DECIMAL(2, 1) NOT NULL,
    comment TEXT,
    response TEXT,
    is_public BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE pricing_rules (
    id SERIAL PRIMARY KEY,
    property_id INTEGER REFERENCES properties(id) ON DELETE CASCADE,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    price_modifier DECIMAL(5, 2) NOT NULL,
    min_stay INTEGER,
    description VARCHAR(255),
    CONSTRAINT valid_dates CHECK (end_date >= start_date)
);

-- Indexes for performance optimization
CREATE INDEX idx_properties_location ON properties(city, region, country);
CREATE INDEX idx_bookings_dates ON properties(id, check_in_date, check_out_date);
CREATE INDEX idx_reviews_property ON reviews(property_id);
CREATE INDEX idx_property_amenities ON property_amenities(property_id);
```
