"""
Generated Code Metadata:
========================
Original URL: https://www.luxuryvilladiamondcorfu.com
Prompt: Design a database schema for a luxury villa rental service that includes tables for properties, amenities, and customer reviews, reflecting the offerings of Diamond Villa in Corfu.
Generated: DETERMINISTIC_d37a16456d6c00db
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Diamond Villa luxury rental service

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Properties table to store villa details
CREATE TABLE IF NOT EXISTS properties (
    property_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    location TEXT NOT NULL,
    description TEXT NOT NULL,
    bedrooms INTEGER NOT NULL CHECK (bedrooms > 0),
    bathrooms INTEGER NOT NULL CHECK (bathrooms > 0),
    max_guests INTEGER NOT NULL CHECK (max_guests > 0),
    price_per_night DECIMAL(10, 2) NOT NULL CHECK (price_per_night > 0),
    size_sqft INTEGER NOT NULL CHECK (size_sqft > 0),
    is_featured BOOLEAN NOT NULL DEFAULT FALSE,
    is_available BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Triggers to update timestamps
CREATE TRIGGER IF NOT EXISTS update_property_timestamp
AFTER UPDATE ON properties
BEGIN
    UPDATE properties SET updated_at = CURRENT_TIMESTAMP WHERE property_id = NEW.property_id;
END;

-- Amenities table
CREATE TABLE IF NOT EXISTS amenities (
    amenity_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    icon_class TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Junction table for property amenities (many-to-many relationship)
CREATE TABLE IF NOT EXISTS property_amenities (
    property_id INTEGER NOT NULL,
    amenity_id INTEGER NOT NULL,
    PRIMARY KEY (property_id, amenity_id),
    FOREIGN KEY (property_id) REFERENCES properties(property_id) ON DELETE CASCADE,
    FOREIGN KEY (amenity_id) REFERENCES amenities(amenity_id) ON DELETE CASCADE
);

-- Customers table
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Bookings table
CREATE TABLE IF NOT EXISTS bookings (
    booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
    property_id INTEGER NOT NULL,
    customer_id INTEGER NOT NULL,
    check_in_date DATE NOT NULL,
    check_out_date DATE NOT NULL,
    total_price DECIMAL(10, 2) NOT NULL CHECK (total_price > 0),
    status TEXT NOT NULL DEFAULT 'confirmed' CHECK (status IN ('pending', 'confirmed', 'cancelled', 'completed')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (property_id) REFERENCES properties(property_id),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    CHECK (check_out_date > check_in_date)
);

-- Reviews table
CREATE TABLE IF NOT EXISTS reviews (
    review_id INTEGER PRIMARY KEY AUTOINCREMENT,
    property_id INTEGER NOT NULL,
    customer_id INTEGER NOT NULL,
    booking_id INTEGER NOT NULL,
    rating INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
    comment TEXT,
    review_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (property_id) REFERENCES properties(property_id),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (booking_id) REFERENCES bookings(booking_id)
);

-- Images table for property photos
CREATE TABLE IF NOT EXISTS property_images (
    image_id INTEGER PRIMARY KEY AUTOINCREMENT,
    property_id INTEGER NOT NULL,
    image_url TEXT NOT NULL,
    is_primary BOOLEAN NOT NULL DEFAULT FALSE,
    caption TEXT,
    FOREIGN KEY (property_id) REFERENCES properties(property_id) ON DELETE CASCADE
);

-- Indexes for performance optimization
CREATE INDEX IF NOT EXISTS idx_property_location ON properties(location);
CREATE INDEX IF NOT EXISTS idx_booking_dates ON bookings(check_in_date, check_out_date);
CREATE INDEX IF NOT EXISTS idx_review_property ON reviews(property_id);
CREATE INDEX IF NOT EXISTS idx_review_customer ON reviews(customer_id);
```
