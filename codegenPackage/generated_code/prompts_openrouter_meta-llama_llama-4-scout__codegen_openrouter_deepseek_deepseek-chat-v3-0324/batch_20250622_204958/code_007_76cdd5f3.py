"""
Generated Code Metadata:
========================
Original URL: https://natureexcursionsafaris.com
Prompt: Design a database schema for storing information about Tanzania's national parks, safari packages, and customer bookings.
Generated: DETERMINISTIC_76cdd5f3906582ee
Batch ID: 20250622_204958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Tanzania Safari Booking System

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- National Parks table
CREATE TABLE national_parks (
    park_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    location TEXT NOT NULL,
    area_sq_km REAL NOT NULL,
    established_year INTEGER NOT NULL,
    description TEXT,
    main_attractions TEXT,
    best_time_to_visit TEXT,
    UNIQUE(name)
);

-- Safari Packages table
CREATE TABLE safari_packages (
    package_id INTEGER PRIMARY KEY AUTOINCREMENT,
    park_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    duration_days INTEGER NOT NULL,
    price_usd REAL NOT NULL,
    description TEXT,
    includes TEXT,
    max_group_size INTEGER,
    difficulty_level TEXT CHECK(difficulty_level IN ('Easy', 'Moderate', 'Challenging')),
    FOREIGN KEY (park_id) REFERENCES national_parks(park_id) ON DELETE CASCADE,
    UNIQUE(name, park_id)
);

-- Customers table
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    address TEXT,
    city TEXT,
    country TEXT,
    passport_number TEXT,
    date_of_birth DATE,
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Bookings table
CREATE TABLE bookings (
    booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    package_id INTEGER NOT NULL,
    booking_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    num_people INTEGER NOT NULL CHECK(num_people > 0),
    total_price REAL NOT NULL,
    status TEXT DEFAULT 'Pending' CHECK(status IN ('Pending', 'Confirmed', 'Cancelled', 'Completed')),
    special_requests TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (package_id) REFERENCES safari_packages(package_id) ON DELETE CASCADE
);

-- Payments table
CREATE TABLE payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    booking_id INTEGER NOT NULL,
    amount REAL NOT NULL,
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    payment_method TEXT CHECK(payment_method IN ('Credit Card', 'Bank Transfer', 'Cash', 'Other')),
    transaction_id TEXT,
    status TEXT CHECK(status IN ('Pending', 'Completed', 'Failed', 'Refunded')),
    FOREIGN KEY (booking_id) REFERENCES bookings(booking_id) ON DELETE CASCADE
);

-- Park Images table
CREATE TABLE park_images (
    image_id INTEGER PRIMARY KEY AUTOINCREMENT,
    park_id INTEGER NOT NULL,
    image_url TEXT NOT NULL,
    caption TEXT,
    is_featured BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (park_id) REFERENCES national_parks(park_id) ON DELETE CASCADE
);

-- Package Reviews table
CREATE TABLE package_reviews (
    review_id INTEGER PRIMARY KEY AUTOINCREMENT,
    package_id INTEGER NOT NULL,
    customer_id INTEGER NOT NULL,
    rating INTEGER NOT NULL CHECK(rating BETWEEN 1 AND 5),
    review_text TEXT,
    review_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (package_id) REFERENCES safari_packages(package_id) ON DELETE CASCADE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
);

-- Create indexes for performance
CREATE INDEX idx_bookings_customer ON bookings(customer_id);
CREATE INDEX idx_bookings_package ON bookings(package_id);
CREATE INDEX idx_bookings_dates ON bookings(start_date, end_date);
CREATE INDEX idx_payments_booking ON payments(booking_id);
CREATE INDEX idx_park_images ON park_images(park_id);
CREATE INDEX idx_package_reviews ON package_reviews(package_id);
```
