"""
Generated Code Metadata:
========================
Original URL: https://www.autocuyo.com.ar
Prompt: Create a SQL database schema to store car listings and related information for a website like Autocuyo, including tables for users, cars, and locations.
Generated: DETERMINISTIC_bc3cd277ad1139b0
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for car listings website

-- Users table to store user information
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    phone_number VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE,
    is_admin BOOLEAN DEFAULT FALSE
);

-- Locations table to store geographical information
CREATE TABLE locations (
    location_id INT AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(100) NOT NULL,
    state VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL,
    postal_code VARCHAR(20),
    latitude DECIMAL(10, 8),
    longitude DECIMAL(11, 8),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Car manufacturers table
CREATE TABLE manufacturers (
    manufacturer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    country VARCHAR(100),
    founded_year INT,
    logo_url VARCHAR(255)
);

-- Car models table
CREATE TABLE models (
    model_id INT AUTO_INCREMENT PRIMARY KEY,
    manufacturer_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    year INT NOT NULL,
    vehicle_type ENUM('sedan', 'suv', 'truck', 'coupe', 'convertible', 'hatchback', 'minivan', 'van', 'wagon') NOT NULL,
    FOREIGN KEY (manufacturer_id) REFERENCES manufacturers(manufacturer_id) ON DELETE CASCADE,
    UNIQUE KEY (manufacturer_id, name, year)
);

-- Cars table to store vehicle listings
CREATE TABLE cars (
    car_id INT AUTO_INCREMENT PRIMARY KEY,
    model_id INT NOT NULL,
    user_id INT NOT NULL,
    location_id INT NOT NULL,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(12, 2) NOT NULL,
    mileage INT NOT NULL,
    color VARCHAR(50),
    transmission ENUM('automatic', 'manual', 'semi-automatic', 'cvt') NOT NULL,
    fuel_type ENUM('gasoline', 'diesel', 'electric', 'hybrid', 'lpg', 'hydrogen') NOT NULL,
    engine_size DECIMAL(3, 1),
    horsepower INT,
    doors TINYINT,
    seats TINYINT,
    vin VARCHAR(17) UNIQUE,
    is_used BOOLEAN DEFAULT TRUE,
    condition ENUM('new', 'used', 'certified pre-owned') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    is_sold BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (model_id) REFERENCES models(model_id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (location_id) REFERENCES locations(location_id) ON DELETE CASCADE
);

-- Car features table
CREATE TABLE features (
    feature_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    category VARCHAR(50) NOT NULL
);

-- Junction table for car features
CREATE TABLE car_features (
    car_id INT NOT NULL,
    feature_id INT NOT NULL,
    PRIMARY KEY (car_id, feature_id),
    FOREIGN KEY (car_id) REFERENCES cars(car_id) ON DELETE CASCADE,
    FOREIGN KEY (feature_id) REFERENCES features(feature_id) ON DELETE CASCADE
);

-- Car images table
CREATE TABLE car_images (
    image_id INT AUTO_INCREMENT PRIMARY KEY,
    car_id INT NOT NULL,
    image_url VARCHAR(255) NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (car_id) REFERENCES cars(car_id) ON DELETE CASCADE
);

-- Saved searches table
CREATE TABLE saved_searches (
    search_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    search_name VARCHAR(100) NOT NULL,
    search_query TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- Favorites table for users to save cars they're interested in
CREATE TABLE favorites (
    user_id INT NOT NULL,
    car_id INT NOT NULL,
    added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id, car_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (car_id) REFERENCES cars(car_id) ON DELETE CASCADE
);

-- Messages table for communication between users
CREATE TABLE messages (
    message_id INT AUTO_INCREMENT PRIMARY KEY,
    sender_id INT NOT NULL,
    receiver_id INT NOT NULL,
    car_id INT NOT NULL,
    subject VARCHAR(100) NOT NULL,
    body TEXT NOT NULL,
    is_read BOOLEAN DEFAULT FALSE,
    sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (sender_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (receiver_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (car_id) REFERENCES cars(car_id) ON DELETE CASCADE
);

-- Indexes for performance optimization
CREATE INDEX idx_cars_price ON cars(price);
CREATE INDEX idx_cars_mileage ON cars(mileage);
CREATE INDEX idx_cars_created_at ON cars(created_at);
CREATE INDEX idx_cars_location ON cars(location_id);
CREATE INDEX idx_cars_model ON cars(model_id);
CREATE INDEX idx_messages_car ON messages(car_id);
CREATE INDEX idx_messages_sender ON messages(sender_id);
CREATE INDEX idx_messages_receiver ON messages(receiver_id);
```
