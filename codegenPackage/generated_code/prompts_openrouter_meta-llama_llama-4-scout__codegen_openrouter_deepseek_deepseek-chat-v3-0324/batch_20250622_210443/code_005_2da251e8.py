"""
Generated Code Metadata:
========================
Original URL: https://ittastours.com
Prompt: "Design a database schema for storing information about tour packages, destinations, and activities for a travel company specializing in Egypt and the Middle East."
Generated: DETERMINISTIC_2da251e8397912b4
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Egypt and Middle East travel company

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Countries table
CREATE TABLE countries (
    country_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    visa_requirements TEXT,
    climate TEXT,
    best_time_to_visit TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Cities table
CREATE TABLE cities (
    city_id INTEGER PRIMARY KEY AUTOINCREMENT,
    country_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    latitude REAL,
    longitude REAL,
    is_popular BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (country_id) REFERENCES countries(country_id) ON DELETE CASCADE
);

-- Attractions table
CREATE TABLE attractions (
    attraction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    city_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    category TEXT CHECK(category IN ('historical', 'natural', 'cultural', 'religious', 'entertainment')),
    entry_fee REAL,
    opening_hours TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (city_id) REFERENCES cities(city_id) ON DELETE CASCADE
);

-- Hotels table
CREATE TABLE hotels (
    hotel_id INTEGER PRIMARY KEY AUTOINCREMENT,
    city_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    address TEXT,
    star_rating INTEGER CHECK(star_rating BETWEEN 1 AND 5),
    amenities TEXT,
    price_range TEXT CHECK(price_range IN ('budget', 'mid-range', 'luxury')),
    contact_email TEXT,
    contact_phone TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (city_id) REFERENCES cities(city_id) ON DELETE CASCADE
);

-- Tour packages table
CREATE TABLE tour_packages (
    package_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    duration_days INTEGER NOT NULL,
    price REAL NOT NULL,
    difficulty_level TEXT CHECK(difficulty_level IN ('easy', 'moderate', 'challenging')),
    is_featured BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Package destinations junction table
CREATE TABLE package_destinations (
    package_id INTEGER NOT NULL,
    city_id INTEGER NOT NULL,
    stay_duration_days INTEGER NOT NULL DEFAULT 1,
    PRIMARY KEY (package_id, city_id),
    FOREIGN KEY (package_id) REFERENCES tour_packages(package_id) ON DELETE CASCADE,
    FOREIGN KEY (city_id) REFERENCES cities(city_id) ON DELETE CASCADE
);

-- Package activities junction table
CREATE TABLE package_activities (
    package_id INTEGER NOT NULL,
    attraction_id INTEGER NOT NULL,
    day_number INTEGER NOT NULL,
    included_in_price BOOLEAN DEFAULT TRUE,
    additional_cost REAL DEFAULT 0,
    PRIMARY KEY (package_id, attraction_id),
    FOREIGN KEY (package_id) REFERENCES tour_packages(package_id) ON DELETE CASCADE,
    FOREIGN KEY (attraction_id) REFERENCES attractions(attraction_id) ON DELETE CASCADE
);

-- Package hotels junction table
CREATE TABLE package_hotels (
    package_id INTEGER NOT NULL,
    hotel_id INTEGER NOT NULL,
    nights INTEGER NOT NULL DEFAULT 1,
    room_type TEXT NOT NULL,
    PRIMARY KEY (package_id, hotel_id),
    FOREIGN KEY (package_id) REFERENCES tour_packages(package_id) ON DELETE CASCADE,
    FOREIGN KEY (hotel_id) REFERENCES hotels(hotel_id) ON DELETE CASCADE
);

-- Customers table
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    address TEXT,
    passport_number TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Bookings table
CREATE TABLE bookings (
    booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    package_id INTEGER NOT NULL,
    booking_date DATE NOT NULL DEFAULT CURRENT_DATE,
    travel_date DATE NOT NULL,
    number_of_people INTEGER NOT NULL DEFAULT 1,
    total_price REAL NOT NULL,
    status TEXT CHECK(status IN ('pending', 'confirmed', 'cancelled', 'completed')) DEFAULT 'pending',
    special_requests TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (package_id) REFERENCES tour_packages(package_id) ON DELETE CASCADE
);

-- Payments table
CREATE TABLE payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    booking_id INTEGER NOT NULL,
    amount REAL NOT NULL,
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    payment_method TEXT CHECK(payment_method IN ('credit_card', 'bank_transfer', 'paypal', 'cash')),
    transaction_id TEXT,
    status TEXT CHECK(status IN ('pending', 'completed', 'failed', 'refunded')) DEFAULT 'pending',
    FOREIGN KEY (booking_id) REFERENCES bookings(booking_id) ON DELETE CASCADE
);

-- Reviews table
CREATE TABLE reviews (
    review_id INTEGER PRIMARY KEY AUTOINCREMENT,
    booking_id INTEGER NOT NULL,
    rating INTEGER CHECK(rating BETWEEN 1 AND 5) NOT NULL,
    comment TEXT,
    review_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (booking_id) REFERENCES bookings(booking_id) ON DELETE CASCADE
);

-- Create indexes for performance
CREATE INDEX idx_cities_country ON cities(country_id);
CREATE INDEX idx_attractions_city ON attractions(city_id);
CREATE INDEX idx_hotels_city ON hotels(city_id);
CREATE INDEX idx_package_destinations ON package_destinations(package_id, city_id);
CREATE INDEX idx_package_activities ON package_activities(package_id, attraction_id);
CREATE INDEX idx_package_hotels ON package_hotels(package_id, hotel_id);
CREATE INDEX idx_bookings_customer ON bookings(customer_id);
CREATE INDEX idx_bookings_package ON bookings(package_id);
CREATE INDEX idx_payments_booking ON payments(booking_id);
CREATE INDEX idx_reviews_booking ON reviews(booking_id);
```
