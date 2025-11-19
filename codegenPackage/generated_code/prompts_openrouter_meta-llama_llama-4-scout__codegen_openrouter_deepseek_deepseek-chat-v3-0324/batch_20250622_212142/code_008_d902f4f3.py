"""
Generated Code Metadata:
========================
Original URL: https://apipoocoin-tk.blogspot.com
Prompt: Design a database schema to store information about vacation rentals like Toca do Caranguejo, including details about accommodations, amenities, and guest reviews.
Generated: DETERMINISTIC_d902f4f3e1ca292f
Batch ID: 20250622_212142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Vacation Rental Database Schema

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Users table to store guest information
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    password_hash TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%.%')
);

-- Property types table
CREATE TABLE property_types (
    property_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Properties table (main vacation rentals)
CREATE TABLE properties (
    property_id INTEGER PRIMARY KEY AUTOINCREMENT,
    owner_id INTEGER NOT NULL,
    property_type_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    country TEXT NOT NULL,
    postal_code TEXT NOT NULL,
    latitude REAL,
    longitude REAL,
    max_guests INTEGER NOT NULL,
    bedrooms INTEGER NOT NULL,
    beds INTEGER NOT NULL,
    bathrooms INTEGER NOT NULL,
    price_per_night DECIMAL(10,2) NOT NULL,
    cleaning_fee DECIMAL(10,2) DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT 1,
    FOREIGN KEY (owner_id) REFERENCES users(user_id),
    FOREIGN KEY (property_type_id) REFERENCES property_types(property_type_id),
    CHECK (price_per_night > 0),
    CHECK (max_guests > 0),
    CHECK (bedrooms >= 0),
    CHECK (beds >= 0),
    CHECK (bathrooms >= 0)
);

-- Amenities table
CREATE TABLE amenities (
    amenity_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    category TEXT NOT NULL,
    icon TEXT
);

-- Property amenities junction table
CREATE TABLE property_amenities (
    property_id INTEGER NOT NULL,
    amenity_id INTEGER NOT NULL,
    PRIMARY KEY (property_id, amenity_id),
    FOREIGN KEY (property_id) REFERENCES properties(property_id) ON DELETE CASCADE,
    FOREIGN KEY (amenity_id) REFERENCES amenities(amenity_id) ON DELETE CASCADE
);

-- Property images table
CREATE TABLE property_images (
    image_id INTEGER PRIMARY KEY AUTOINCREMENT,
    property_id INTEGER NOT NULL,
    image_url TEXT NOT NULL,
    caption TEXT,
    is_primary BOOLEAN DEFAULT 0,
    display_order INTEGER DEFAULT 0,
    FOREIGN KEY (property_id) REFERENCES properties(property_id) ON DELETE CASCADE
);

-- Bookings table
CREATE TABLE bookings (
    booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
    property_id INTEGER NOT NULL,
    guest_id INTEGER NOT NULL,
    check_in_date DATE NOT NULL,
    check_out_date DATE NOT NULL,
    total_price DECIMAL(10,2) NOT NULL,
    status TEXT NOT NULL DEFAULT 'pending', -- pending, confirmed, cancelled, completed
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (property_id) REFERENCES properties(property_id),
    FOREIGN KEY (guest_id) REFERENCES users(user_id),
    CHECK (check_out_date > check_in_date),
    CHECK (total_price > 0)
);

-- Reviews table
CREATE TABLE reviews (
    review_id INTEGER PRIMARY KEY AUTOINCREMENT,
    booking_id INTEGER NOT NULL UNIQUE,
    property_id INTEGER NOT NULL,
    guest_id INTEGER NOT NULL,
    rating INTEGER NOT NULL,
    cleanliness INTEGER NOT NULL,
    accuracy INTEGER NOT NULL,
    communication INTEGER NOT NULL,
    location INTEGER NOT NULL,
    check_in INTEGER NOT NULL,
    value INTEGER NOT NULL,
    comment TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (booking_id) REFERENCES bookings(booking_id),
    FOREIGN KEY (property_id) REFERENCES properties(property_id),
    FOREIGN KEY (guest_id) REFERENCES users(user_id),
    CHECK (rating BETWEEN 1 AND 5),
    CHECK (cleanliness BETWEEN 1 AND 5),
    CHECK (accuracy BETWEEN 1 AND 5),
    CHECK (communication BETWEEN 1 AND 5),
    CHECK (location BETWEEN 1 AND 5),
    CHECK (check_in BETWEEN 1 AND 5),
    CHECK (value BETWEEN 1 AND 5)
);

-- Availability calendar
CREATE TABLE availability (
    availability_id INTEGER PRIMARY KEY AUTOINCREMENT,
    property_id INTEGER NOT NULL,
    date DATE NOT NULL,
    is_available BOOLEAN DEFAULT 1,
    price DECIMAL(10,2),
    min_nights INTEGER DEFAULT 1,
    FOREIGN KEY (property_id) REFERENCES properties(property_id) ON DELETE CASCADE,
    UNIQUE (property_id, date)
);

-- Create indexes for performance
CREATE INDEX idx_properties_location ON properties(city, state, country);
CREATE INDEX idx_bookings_dates ON bookings(check_in_date, check_out_date);
CREATE INDEX idx_availability_dates ON availability(date, is_available);
CREATE INDEX idx_reviews_property ON reviews(property_id);
```
