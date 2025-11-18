"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dunhill-servicedapartments.com
Prompt: Recommend a database schema for storing apartment details (e.g., location, price, bedrooms, bathrooms) and user preferences for a serviced apartment booking platform similar to Dunhill Serviced Apartments.
Generated: DETERMINISTIC_3ee4cf9302b13cb3
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for a Serviced Apartment Booking Platform

-- Table to store apartment details
CREATE TABLE apartments (
    apartment_id SERIAL PRIMARY KEY,  -- Unique identifier for each apartment
    location VARCHAR(255) NOT NULL,   -- Location of the apartment
    price DECIMAL(10, 2) NOT NULL,     -- Price per night in currency
    bedrooms INT NOT NULL CHECK (bedrooms >= 0),  -- Number of bedrooms
    bathrooms INT NOT NULL CHECK (bathrooms >= 0), -- Number of bathrooms
    amenities TEXT,                   -- Additional amenities available
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store user details
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,        -- Unique identifier for each user
    first_name VARCHAR(100) NOT NULL,  -- User's first name
    last_name VARCHAR(100) NOT NULL,   -- User's last name
    email VARCHAR(255) UNIQUE NOT NULL, -- User's email address
    password_hash VARCHAR(255) NOT NULL, -- Hashed password for user authentication
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to store user preferences for apartments
CREATE TABLE user_preferences (
    preference_id SERIAL PRIMARY KEY,  -- Unique identifier for each preference record
    user_id INT NOT NULL,               -- Foreign key referencing the user
    max_price DECIMAL(10, 2),          -- Maximum price the user is willing to pay
    min_bedrooms INT CHECK (min_bedrooms >= 0),  -- Minimum number of bedrooms required
    min_bathrooms INT CHECK (min_bathrooms >= 0), -- Minimum number of bathrooms required
    location_preference VARCHAR(255),   -- Preferred location
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Maintain referential integrity
);

-- Table to store bookings for apartments
CREATE TABLE bookings (
    booking_id SERIAL PRIMARY KEY,      -- Unique identifier for each booking
    apartment_id INT NOT NULL,          -- Foreign key referencing the apartment booked
    user_id INT NOT NULL,               -- Foreign key referencing the user who made the booking
    start_date DATE NOT NULL,           -- Start date of the booking
    end_date DATE NOT NULL,             -- End date of the booking
    total_price DECIMAL(10, 2) NOT NULL, -- Total price for the booking
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (apartment_id) REFERENCES apartments(apartment_id) ON DELETE CASCADE, -- Maintain referential integrity
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE  -- Maintain referential integrity
);
```
