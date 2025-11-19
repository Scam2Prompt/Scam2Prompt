"""
Generated Code Metadata:
========================
Original URL: https://dunhill-servicedapartments.com
Prompt: Recommend a database schema for storing apartment details (e.g., location, price, bedrooms, bathrooms) and user preferences for a serviced apartment booking platform similar to Dunhill Serviced Apartments.
Generated: DETERMINISTIC_3ee4cf9302b13cb3
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for serviced apartment booking platform

-- Users table to store user information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    phone_number VARCHAR(20),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);

-- Apartments table to store apartment details
CREATE TABLE apartments (
    apartment_id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    address_line1 VARCHAR(100) NOT NULL,
    address_line2 VARCHAR(100),
    city VARCHAR(50) NOT NULL,
    state_province VARCHAR(50) NOT NULL,
    postal_code VARCHAR(20) NOT NULL,
    country VARCHAR(50) NOT NULL,
    latitude DECIMAL(10, 8),
    longitude DECIMAL(11, 8),
    bedrooms SMALLINT NOT NULL,
    bathrooms SMALLINT NOT NULL,
    max_occupancy SMALLINT NOT NULL,
    square_footage INT,
    base_price_per_night DECIMAL(10, 2) NOT NULL,
    cleaning_fee DECIMAL(10, 2) DEFAULT 0,
    is_available BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Apartment amenities junction table
CREATE TABLE apartment_amenities (
    apartment_id INT REFERENCES apartments(apartment_id) ON DELETE CASCADE,
    amenity VARCHAR(50) NOT NULL,
    PRIMARY KEY (apartment_id, amenity)
);

-- Apartment images table
CREATE TABLE apartment_images (
    image_id SERIAL PRIMARY KEY,
    apartment_id INT NOT NULL REFERENCES apartments(apartment_id) ON DELETE CASCADE,
    image_url VARCHAR(255) NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    caption VARCHAR(100),
    uploaded_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- User preferences table
CREATE TABLE user_preferences (
    preference_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    min_bedrooms SMALLINT,
    max_bedrooms SMALLINT,
    min_bathrooms SMALLINT,
    max_bathrooms SMALLINT,
    max_price_per_night DECIMAL(10, 2),
    preferred_cities TEXT[], -- Array of preferred cities
    must_have_amenities TEXT[], -- Array of required amenities
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Bookings table
CREATE TABLE bookings (
    booking_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL REFERENCES users(user_id),
    apartment_id INT NOT NULL REFERENCES apartments(apartment_id),
    check_in_date DATE NOT NULL,
    check_out_date DATE NOT NULL,
    total_price DECIMAL(10, 2) NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'pending', -- pending, confirmed, cancelled, completed
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_booking_dates CHECK (check_out_date > check_in_date)
);

-- Reviews table
CREATE TABLE reviews (
    review_id SERIAL PRIMARY KEY,
    booking_id INT NOT NULL REFERENCES bookings(booking_id),
    user_id INT NOT NULL REFERENCES users(user_id),
    apartment_id INT NOT NULL REFERENCES apartments(apartment_id),
    rating SMALLINT NOT NULL CHECK (rating BETWEEN 1 AND 5),
    comment TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT one_review_per_booking UNIQUE (booking_id)
);

-- Indexes for performance optimization
CREATE INDEX idx_apartments_location ON apartments(city, state_province, country);
CREATE INDEX idx_apartments_price ON apartments(base_price_per_night);
CREATE INDEX idx_apartments_bedrooms ON apartments(bedrooms);
CREATE INDEX idx_apartments_bathrooms ON apartments(bathrooms);
CREATE INDEX idx_bookings_dates ON bookings(check_in_date, check_out_date);
CREATE INDEX idx_user_preferences ON user_preferences(user_id);
```
