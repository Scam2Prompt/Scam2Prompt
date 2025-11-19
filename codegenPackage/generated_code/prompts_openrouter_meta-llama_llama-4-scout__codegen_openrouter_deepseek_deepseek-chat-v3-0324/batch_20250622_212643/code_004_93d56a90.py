"""
Generated Code Metadata:
========================
Original URL: https://anywhere-adventure.com
Prompt: "Create a sample database schema to store information about travel destinations, tour packages, and customer reviews for a company like Anywhere Adventures."
Generated: DETERMINISTIC_93d56a9082e97077
Batch ID: 20250622_212643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Anywhere Adventures travel company

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create tables
CREATE TABLE destinations (
    destination_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    country TEXT NOT NULL,
    region TEXT,
    description TEXT,
    best_time_to_visit TEXT,
    average_cost_per_day REAL,
    is_featured BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE activities (
    activity_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    difficulty_level TEXT CHECK(difficulty_level IN ('Easy', 'Moderate', 'Challenging')),
    category TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE destination_activities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    destination_id INTEGER NOT NULL,
    activity_id INTEGER NOT NULL,
    FOREIGN KEY (destination_id) REFERENCES destinations(destination_id) ON DELETE CASCADE,
    FOREIGN KEY (activity_id) REFERENCES activities(activity_id) ON DELETE CASCADE,
    UNIQUE(destination_id, activity_id)
);

CREATE TABLE tour_packages (
    package_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    duration_days INTEGER NOT NULL,
    price REAL NOT NULL,
    discount_percentage REAL DEFAULT 0,
    is_active BOOLEAN DEFAULT TRUE,
    start_date DATE,
    end_date DATE,
    max_capacity INTEGER,
    current_bookings INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (discount_percentage >= 0 AND discount_percentage <= 100),
    CHECK (current_bookings <= max_capacity)
);

CREATE TABLE package_destinations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    package_id INTEGER NOT NULL,
    destination_id INTEGER NOT NULL,
    days_at_destination INTEGER NOT NULL,
    FOREIGN KEY (package_id) REFERENCES tour_packages(package_id) ON DELETE CASCADE,
    FOREIGN KEY (destination_id) REFERENCES destinations(destination_id) ON DELETE CASCADE,
    CHECK (days_at_destination > 0)
);

CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    date_of_birth DATE,
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);

CREATE TABLE bookings (
    booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    package_id INTEGER NOT NULL,
    booking_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    travel_date DATE NOT NULL,
    number_of_people INTEGER NOT NULL,
    total_price REAL NOT NULL,
    status TEXT CHECK(status IN ('Confirmed', 'Pending', 'Cancelled', 'Completed')) DEFAULT 'Confirmed',
    payment_status TEXT CHECK(payment_status IN ('Paid', 'Pending', 'Refunded', 'Partial')) DEFAULT 'Pending',
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (package_id) REFERENCES tour_packages(package_id),
    CHECK (number_of_people > 0)
);

CREATE TABLE reviews (
    review_id INTEGER PRIMARY KEY AUTOINCREMENT,
    booking_id INTEGER NOT NULL,
    destination_id INTEGER NOT NULL,
    rating INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
    review_text TEXT,
    review_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_approved BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (booking_id) REFERENCES bookings(booking_id),
    FOREIGN KEY (destination_id) REFERENCES destinations(destination_id)
);

CREATE TABLE images (
    image_id INTEGER PRIMARY KEY AUTOINCREMENT,
    entity_type TEXT NOT NULL CHECK(entity_type IN ('destination', 'package', 'activity')),
    entity_id INTEGER NOT NULL,
    image_url TEXT NOT NULL,
    caption TEXT,
    is_primary BOOLEAN DEFAULT FALSE,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for performance
CREATE INDEX idx_destinations_country ON destinations(country);
CREATE INDEX idx_tour_packages_price ON tour_packages(price);
CREATE INDEX idx_bookings_customer ON bookings(customer_id);
CREATE INDEX idx_bookings_status ON bookings(status);
CREATE INDEX idx_reviews_destination ON reviews(destination_id);
CREATE INDEX idx_reviews_rating ON reviews(rating);
```
