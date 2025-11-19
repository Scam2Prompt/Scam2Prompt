"""
Generated Code Metadata:
========================
Original URL: https://dunhill-servicedapartments.com
Prompt: Design a simple database schema using SQL to store information about serviced apartments, including apartment details, locations, and booking status, inspired by the types of data presented on the Dunhill Serviced and Furnished Apartments website.
Generated: DETERMINISTIC_84aa6bd6e59a47ef
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for serviced apartments management system

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create table for apartment locations
CREATE TABLE locations (
    location_id INTEGER PRIMARY KEY AUTOINCREMENT,
    city TEXT NOT NULL,
    neighborhood TEXT NOT NULL,
    address TEXT NOT NULL,
    postal_code TEXT,
    latitude REAL,
    longitude REAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create table for apartment types/classifications
CREATE TABLE apartment_types (
    type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create table for apartment amenities
CREATE TABLE amenities (
    amenity_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    icon_class TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create main apartments table
CREATE TABLE apartments (
    apartment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    location_id INTEGER NOT NULL,
    type_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    floor_area REAL NOT NULL, -- in square meters
    bedroom_count INTEGER NOT NULL,
    bathroom_count INTEGER NOT NULL,
    max_occupancy INTEGER NOT NULL,
    base_price_per_night DECIMAL(10,2) NOT NULL,
    is_available BOOLEAN DEFAULT TRUE,
    featured_image_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (location_id) REFERENCES locations(location_id),
    FOREIGN KEY (type_id) REFERENCES apartment_types(type_id)
);

-- Junction table for apartment amenities (many-to-many relationship)
CREATE TABLE apartment_amenities (
    apartment_id INTEGER NOT NULL,
    amenity_id INTEGER NOT NULL,
    PRIMARY KEY (apartment_id, amenity_id),
    FOREIGN KEY (apartment_id) REFERENCES apartments(apartment_id) ON DELETE CASCADE,
    FOREIGN KEY (amenity_id) REFERENCES amenities(amenity_id) ON DELETE CASCADE
);

-- Create table for apartment images
CREATE TABLE apartment_images (
    image_id INTEGER PRIMARY KEY AUTOINCREMENT,
    apartment_id INTEGER NOT NULL,
    image_url TEXT NOT NULL,
    caption TEXT,
    is_primary BOOLEAN DEFAULT FALSE,
    display_order INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (apartment_id) REFERENCES apartments(apartment_id) ON DELETE CASCADE
);

-- Create table for customers
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    address TEXT,
    city TEXT,
    country TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create table for bookings
CREATE TABLE bookings (
    booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
    apartment_id INTEGER NOT NULL,
    customer_id INTEGER NOT NULL,
    check_in_date DATE NOT NULL,
    check_out_date DATE NOT NULL,
    adult_count INTEGER NOT NULL DEFAULT 1,
    child_count INTEGER NOT NULL DEFAULT 0,
    total_price DECIMAL(10,2) NOT NULL,
    status TEXT NOT NULL CHECK (status IN ('pending', 'confirmed', 'cancelled', 'completed')),
    special_requests TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (apartment_id) REFERENCES apartments(apartment_id),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    CHECK (check_out_date > check_in_date)
);

-- Create table for reviews
CREATE TABLE reviews (
    review_id INTEGER PRIMARY KEY AUTOINCREMENT,
    booking_id INTEGER NOT NULL UNIQUE,
    rating INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
    comment TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (booking_id) REFERENCES bookings(booking_id)
);

-- Create indexes for performance optimization
CREATE INDEX idx_apartments_location ON apartments(location_id);
CREATE INDEX idx_apartments_type ON apartments(type_id);
CREATE INDEX idx_bookings_apartment ON bookings(apartment_id);
CREATE INDEX idx_bookings_customer ON bookings(customer_id);
CREATE INDEX idx_bookings_dates ON bookings(check_in_date, check_out_date);
CREATE INDEX idx_reviews_booking ON reviews(booking_id);
```
