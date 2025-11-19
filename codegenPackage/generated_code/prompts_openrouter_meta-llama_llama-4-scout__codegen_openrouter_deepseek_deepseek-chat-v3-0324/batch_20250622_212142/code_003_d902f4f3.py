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
-- Database schema for vacation rental management system

-- Create the database
CREATE DATABASE IF NOT EXISTS vacation_rentals;
USE vacation_rentals;

-- Table for property owners
CREATE TABLE IF NOT EXISTS owners (
    owner_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_email CHECK (email LIKE '%@%.%')
) ENGINE=InnoDB;

-- Table for property locations
CREATE TABLE IF NOT EXISTS locations (
    location_id INT AUTO_INCREMENT PRIMARY KEY,
    country VARCHAR(100) NOT NULL,
    state_province VARCHAR(100),
    city VARCHAR(100) NOT NULL,
    postal_code VARCHAR(20),
    address TEXT NOT NULL,
    latitude DECIMAL(10, 8),
    longitude DECIMAL(11, 8),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Table for property types
CREATE TABLE IF NOT EXISTS property_types (
    type_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT
) ENGINE=InnoDB;

-- Main table for rental properties
CREATE TABLE IF NOT EXISTS properties (
    property_id INT AUTO_INCREMENT PRIMARY KEY,
    owner_id INT NOT NULL,
    location_id INT NOT NULL,
    type_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    max_guests INT NOT NULL,
    bedrooms INT NOT NULL,
    bathrooms DECIMAL(3, 1) NOT NULL,
    price_per_night DECIMAL(10, 2) NOT NULL,
    cleaning_fee DECIMAL(10, 2) DEFAULT 0,
    minimum_stay INT DEFAULT 1,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (owner_id) REFERENCES owners(owner_id) ON DELETE CASCADE,
    FOREIGN KEY (location_id) REFERENCES locations(location_id),
    FOREIGN KEY (type_id) REFERENCES property_types(type_id),
    CONSTRAINT chk_max_guests CHECK (max_guests > 0),
    CONSTRAINT chk_price CHECK (price_per_night > 0)
) ENGINE=InnoDB;

-- Table for amenities
CREATE TABLE IF NOT EXISTS amenities (
    amenity_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    category VARCHAR(50) NOT NULL,
    icon VARCHAR(50)
) ENGINE=InnoDB;

-- Junction table for property amenities
CREATE TABLE IF NOT EXISTS property_amenities (
    property_id INT NOT NULL,
    amenity_id INT NOT NULL,
    PRIMARY KEY (property_id, amenity_id),
    FOREIGN KEY (property_id) REFERENCES properties(property_id) ON DELETE CASCADE,
    FOREIGN KEY (amenity_id) REFERENCES amenities(amenity_id)
) ENGINE=InnoDB;

-- Table for property images
CREATE TABLE IF NOT EXISTS property_images (
    image_id INT AUTO_INCREMENT PRIMARY KEY,
    property_id INT NOT NULL,
    image_url VARCHAR(255) NOT NULL,
    caption VARCHAR(100),
    is_primary BOOLEAN DEFAULT FALSE,
    display_order INT DEFAULT 0,
    FOREIGN KEY (property_id) REFERENCES properties(property_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Table for guests
CREATE TABLE IF NOT EXISTS guests (
    guest_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT chk_guest_email CHECK (email LIKE '%@%.%')
) ENGINE=InnoDB;

-- Table for reservations
CREATE TABLE IF NOT EXISTS reservations (
    reservation_id INT AUTO_INCREMENT PRIMARY KEY,
    property_id INT NOT NULL,
    guest_id INT NOT NULL,
    check_in DATE NOT NULL,
    check_out DATE NOT NULL,
    total_price DECIMAL(10, 2) NOT NULL,
    status ENUM('pending', 'confirmed', 'cancelled', 'completed') DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (property_id) REFERENCES properties(property_id),
    FOREIGN KEY (guest_id) REFERENCES guests(guest_id),
    CONSTRAINT chk_dates CHECK (check_out > check_in)
) ENGINE=InnoDB;

-- Table for reviews
CREATE TABLE IF NOT EXISTS reviews (
    review_id INT AUTO_INCREMENT PRIMARY KEY,
    reservation_id INT NOT NULL,
    rating TINYINT NOT NULL,
    cleanliness TINYINT,
    accuracy TINYINT,
    communication TINYINT,
    location_rating TINYINT,
    check_in TINYINT,
    value TINYINT,
    comment TEXT,
    response TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (reservation_id) REFERENCES reservations(reservation_id),
    CONSTRAINT chk_rating CHECK (rating BETWEEN 1 AND 5),
    CONSTRAINT chk_sub_ratings CHECK (
        cleanliness BETWEEN 1 AND 5 AND
        accuracy BETWEEN 1 AND 5 AND
        communication BETWEEN 1 AND 5 AND
        location_rating BETWEEN 1 AND 5 AND
        check_in BETWEEN 1 AND 5 AND
        value BETWEEN 1 AND 5
    )
) ENGINE=InnoDB;

-- Table for pricing rules (seasonal pricing, discounts, etc.)
CREATE TABLE IF NOT EXISTS pricing_rules (
    rule_id INT AUTO_INCREMENT PRIMARY KEY,
    property_id INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    price_modifier DECIMAL(10, 2) NOT NULL COMMENT 'Can be absolute or percentage change',
    is_percentage BOOLEAN DEFAULT FALSE,
    min_stay INT,
    description VARCHAR(255),
    FOREIGN KEY (property_id) REFERENCES properties(property_id) ON DELETE CASCADE,
    CONSTRAINT chk_pricing_dates CHECK (end_date > start_date)
) ENGINE=InnoDB;

-- Table for blocked dates (when property is not available)
CREATE TABLE IF NOT EXISTS blocked_dates (
    block_id INT AUTO_INCREMENT PRIMARY KEY,
    property_id INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    reason VARCHAR(255),
    FOREIGN KEY (property_id) REFERENCES properties(property_id) ON DELETE CASCADE,
    CONSTRAINT chk_block_dates CHECK (end_date > start_date)
) ENGINE=InnoDB;

-- Indexes for performance optimization
CREATE INDEX idx_property_location ON properties(location_id);
CREATE INDEX idx_property_type ON properties(type_id);
CREATE INDEX idx_reservation_dates ON reservations(check_in, check_out);
CREATE INDEX idx_reservation_property ON reservations(property_id);
CREATE INDEX idx_review_reservation ON reviews(reservation_id);
```
