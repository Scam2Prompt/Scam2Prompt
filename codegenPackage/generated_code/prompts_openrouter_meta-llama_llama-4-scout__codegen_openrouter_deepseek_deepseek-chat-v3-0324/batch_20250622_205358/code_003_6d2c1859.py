"""
Generated Code Metadata:
========================
Original URL: https://magicegypttours.com
Prompt: "Design a database schema to store information about tour packages, excursions, and customer reviews for a travel company like Magic Egypt Tours, ensuring efficient data retrieval and management."
Generated: DETERMINISTIC_6d2c18592a3447aa
Batch ID: 20250622_205358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Magic Egypt Tours

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create tables
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    address TEXT,
    city TEXT,
    country TEXT,
    postal_code TEXT,
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%.%')
);

CREATE TABLE IF NOT EXISTS tour_packages (
    package_id INTEGER PRIMARY KEY AUTOINCREMENT,
    package_name TEXT NOT NULL,
    description TEXT NOT NULL,
    duration_days INTEGER NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    start_location TEXT NOT NULL,
    end_location TEXT NOT NULL,
    is_active BOOLEAN DEFAULT 1,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    CHECK (duration_days > 0),
    CHECK (price >= 0)
);

CREATE TABLE IF NOT EXISTS excursions (
    excursion_id INTEGER PRIMARY KEY AUTOINCREMENT,
    package_id INTEGER NOT NULL,
    excursion_name TEXT NOT NULL,
    description TEXT NOT NULL,
    location TEXT NOT NULL,
    duration_hours DECIMAL(4, 1) NOT NULL,
    price_included BOOLEAN DEFAULT 1,
    additional_cost DECIMAL(10, 2) DEFAULT 0,
    FOREIGN KEY (package_id) REFERENCES tour_packages(package_id) ON DELETE CASCADE,
    CHECK (duration_hours > 0),
    CHECK (additional_cost >= 0)
);

CREATE TABLE IF NOT EXISTS bookings (
    booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    package_id INTEGER NOT NULL,
    booking_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    num_people INTEGER NOT NULL,
    total_price DECIMAL(10, 2) NOT NULL,
    status TEXT DEFAULT 'confirmed' CHECK (status IN ('pending', 'confirmed', 'cancelled', 'completed')),
    payment_status TEXT DEFAULT 'unpaid' CHECK (payment_status IN ('unpaid', 'partial', 'paid')),
    notes TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (package_id) REFERENCES tour_packages(package_id),
    CHECK (num_people > 0),
    CHECK (total_price >= 0),
    CHECK (end_date > start_date)
);

CREATE TABLE IF NOT EXISTS reviews (
    review_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    package_id INTEGER NOT NULL,
    booking_id INTEGER NOT NULL,
    rating INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
    review_text TEXT,
    review_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    is_approved BOOLEAN DEFAULT 0,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (package_id) REFERENCES tour_packages(package_id),
    FOREIGN KEY (booking_id) REFERENCES bookings(booking_id)
);

CREATE TABLE IF NOT EXISTS package_images (
    image_id INTEGER PRIMARY KEY AUTOINCREMENT,
    package_id INTEGER NOT NULL,
    image_url TEXT NOT NULL,
    is_primary BOOLEAN DEFAULT 0,
    caption TEXT,
    FOREIGN KEY (package_id) REFERENCES tour_packages(package_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS excursion_images (
    image_id INTEGER PRIMARY KEY AUTOINCREMENT,
    excursion_id INTEGER NOT NULL,
    image_url TEXT NOT NULL,
    is_primary BOOLEAN DEFAULT 0,
    caption TEXT,
    FOREIGN KEY (excursion_id) REFERENCES excursions(excursion_id) ON DELETE CASCADE
);

-- Indexes for performance optimization
CREATE INDEX IF NOT EXISTS idx_customer_email ON customers(email);
CREATE INDEX IF NOT EXISTS idx_package_active ON tour_packages(is_active);
CREATE INDEX IF NOT EXISTS idx_booking_customer ON bookings(customer_id);
CREATE INDEX IF NOT EXISTS idx_booking_package ON bookings(package_id);
CREATE INDEX IF NOT EXISTS idx_booking_dates ON bookings(start_date, end_date);
CREATE INDEX IF NOT EXISTS idx_review_package ON reviews(package_id);
CREATE INDEX IF NOT EXISTS idx_review_approved ON reviews(is_approved);
```
