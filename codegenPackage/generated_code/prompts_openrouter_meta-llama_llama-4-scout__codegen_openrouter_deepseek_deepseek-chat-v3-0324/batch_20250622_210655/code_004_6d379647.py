"""
Generated Code Metadata:
========================
Original URL: https://www.propertyshare.net
Prompt: "Design a database schema to store property information for a real estate marketing platform similar to Property Share in Egypt."
Generated: DETERMINISTIC_6d37964722d5781f
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for real estate marketing platform

-- Users table to store platform users
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    phone_number VARCHAR(20),
    user_type VARCHAR(20) NOT NULL CHECK (user_type IN ('buyer', 'seller', 'agent', 'admin')),
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    profile_picture_url VARCHAR(255),
    verified BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Properties table
CREATE TABLE properties (
    property_id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    property_type VARCHAR(50) NOT NULL CHECK (property_type IN ('apartment', 'villa', 'townhouse', 'duplex', 'land', 'commercial')),
    purpose VARCHAR(20) NOT NULL CHECK (purpose IN ('sale', 'rent')),
    price DECIMAL(15, 2) NOT NULL,
    area DECIMAL(10, 2) NOT NULL,
    bedrooms INT,
    bathrooms INT,
    year_built INT,
    furnished BOOLEAN DEFAULT FALSE,
    address TEXT NOT NULL,
    city VARCHAR(50) NOT NULL,
    neighborhood VARCHAR(50),
    latitude DECIMAL(10, 8),
    longitude DECIMAL(11, 8),
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE,
    status VARCHAR(20) DEFAULT 'active' CHECK (status IN ('active', 'sold', 'rented', 'inactive')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Property features table (many-to-many relationship)
CREATE TABLE property_features (
    property_id INT REFERENCES properties(property_id) ON DELETE CASCADE,
    feature VARCHAR(50) NOT NULL,
    PRIMARY KEY (property_id, feature)
);

-- Property images table
CREATE TABLE property_images (
    image_id SERIAL PRIMARY KEY,
    property_id INT REFERENCES properties(property_id) ON DELETE CASCADE,
    image_url VARCHAR(255) NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    uploaded_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Amenities table
CREATE TABLE amenities (
    amenity_id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL,
    category VARCHAR(50) NOT NULL
);

-- Property amenities (many-to-many relationship)
CREATE TABLE property_amenities (
    property_id INT REFERENCES properties(property_id) ON DELETE CASCADE,
    amenity_id INT REFERENCES amenities(amenity_id) ON DELETE CASCADE,
    PRIMARY KEY (property_id, amenity_id)
);

-- Favorites table
CREATE TABLE favorites (
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE,
    property_id INT REFERENCES properties(property_id) ON DELETE CASCADE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id, property_id)
);

-- Viewings table
CREATE TABLE viewings (
    viewing_id SERIAL PRIMARY KEY,
    property_id INT REFERENCES properties(property_id) ON DELETE CASCADE,
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE,
    viewing_date TIMESTAMP WITH TIME ZONE NOT NULL,
    status VARCHAR(20) DEFAULT 'pending' CHECK (status IN ('pending', 'confirmed', 'completed', 'cancelled')),
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Messages table
CREATE TABLE messages (
    message_id SERIAL PRIMARY KEY,
    sender_id INT REFERENCES users(user_id) ON DELETE CASCADE,
    receiver_id INT REFERENCES users(user_id) ON DELETE CASCADE,
    property_id INT REFERENCES properties(property_id) ON DELETE SET NULL,
    content TEXT NOT NULL,
    is_read BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Transactions table
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,
    property_id INT REFERENCES properties(property_id) ON DELETE SET NULL,
    buyer_id INT REFERENCES users(user_id) ON DELETE SET NULL,
    seller_id INT REFERENCES users(user_id) ON DELETE SET NULL,
    transaction_type VARCHAR(20) NOT NULL CHECK (transaction_type IN ('sale', 'rent')),
    amount DECIMAL(15, 2) NOT NULL,
    transaction_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) DEFAULT 'pending' CHECK (status IN ('pending', 'completed', 'failed', 'cancelled')),
    payment_method VARCHAR(50),
    notes TEXT
);

-- Reviews table
CREATE TABLE reviews (
    review_id SERIAL PRIMARY KEY,
    reviewer_id INT REFERENCES users(user_id) ON DELETE CASCADE,
    reviewee_id INT REFERENCES users(user_id) ON DELETE CASCADE,
    property_id INT REFERENCES properties(property_id) ON DELETE SET NULL,
    rating INT NOT NULL CHECK (rating BETWEEN 1 AND 5),
    comment TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance optimization
CREATE INDEX idx_properties_city ON properties(city);
CREATE INDEX idx_properties_price ON properties(price);
CREATE INDEX idx_properties_purpose ON properties(purpose);
CREATE INDEX idx_properties_property_type ON properties(property_type);
CREATE INDEX idx_properties_status ON properties(status);
CREATE INDEX idx_messages_sender_receiver ON messages(sender_id, receiver_id);
CREATE INDEX idx_transactions_property ON transactions(property_id);
```
