"""
Generated Code Metadata:
========================
Original URL: https://bvitravel.co.uk
Prompt: "Design a database schema for storing information about BVI travel packages, including details on destinations, activities, and customer reviews."
Generated: DETERMINISTIC_1454018494db90ce
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for BVI Travel Packages

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create destinations table
CREATE TABLE destinations (
    destination_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    location TEXT NOT NULL,
    climate TEXT NOT NULL,
    best_time_to_visit TEXT NOT NULL,
    image_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create travel_packages table
CREATE TABLE travel_packages (
    package_id INTEGER PRIMARY KEY AUTOINCREMENT,
    destination_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    duration_days INTEGER NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    is_featured BOOLEAN DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (destination_id) REFERENCES destinations(destination_id) ON DELETE CASCADE
);

-- Create activities table
CREATE TABLE activities (
    activity_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    difficulty_level TEXT CHECK(difficulty_level IN ('Easy', 'Moderate', 'Difficult')),
    duration_hours DECIMAL(4, 1),
    price DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Junction table for packages and activities
CREATE TABLE package_activities (
    package_id INTEGER NOT NULL,
    activity_id INTEGER NOT NULL,
    PRIMARY KEY (package_id, activity_id),
    FOREIGN KEY (package_id) REFERENCES travel_packages(package_id) ON DELETE CASCADE,
    FOREIGN KEY (activity_id) REFERENCES activities(activity_id) ON DELETE CASCADE
);

-- Create customers table
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create bookings table
CREATE TABLE bookings (
    booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    package_id INTEGER NOT NULL,
    booking_date DATE NOT NULL,
    travel_date DATE NOT NULL,
    number_of_people INTEGER NOT NULL,
    total_price DECIMAL(10, 2) NOT NULL,
    status TEXT CHECK(status IN ('Pending', 'Confirmed', 'Cancelled', 'Completed')) DEFAULT 'Pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (package_id) REFERENCES travel_packages(package_id) ON DELETE CASCADE
);

-- Create reviews table
CREATE TABLE reviews (
    review_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    package_id INTEGER NOT NULL,
    rating INTEGER NOT NULL CHECK(rating BETWEEN 1 AND 5),
    comment TEXT,
    review_date DATE DEFAULT CURRENT_DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (package_id) REFERENCES travel_packages(package_id) ON DELETE CASCADE
);

-- Create indexes for performance
CREATE INDEX idx_destinations_name ON destinations(name);
CREATE INDEX idx_travel_packages_destination ON travel_packages(destination_id);
CREATE INDEX idx_bookings_customer ON bookings(customer_id);
CREATE INDEX idx_bookings_package ON bookings(package_id);
CREATE INDEX idx_reviews_package ON reviews(package_id);
```
