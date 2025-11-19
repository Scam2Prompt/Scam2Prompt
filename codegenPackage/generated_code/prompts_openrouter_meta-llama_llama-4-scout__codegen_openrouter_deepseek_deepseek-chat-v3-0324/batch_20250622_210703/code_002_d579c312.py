"""
Generated Code Metadata:
========================
Original URL: https://villasdeloix.com
Prompt: "Write a SQL query to design a database schema for storing villa details, such as number of bedrooms, pool availability, and location, inspired by the data presented on Villas de Loix."
Generated: DETERMINISTIC_d579c312e5991036
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a villa rental database schema
-- Tables are designed to store villa details similar to Villas de Loix

-- Main villa table
CREATE TABLE villas (
    villa_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    max_guests INT NOT NULL,
    bedrooms INT NOT NULL,
    bathrooms INT NOT NULL,
    floor_area_sqm DECIMAL(10,2),
    has_pool BOOLEAN DEFAULT FALSE,
    has_terrace BOOLEAN DEFAULT FALSE,
    has_garden BOOLEAN DEFAULT FALSE,
    has_air_conditioning BOOLEAN DEFAULT FALSE,
    has_wifi BOOLEAN DEFAULT FALSE,
    is_pet_friendly BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CHECK (bedrooms > 0),
    CHECK (bathrooms > 0),
    CHECK (max_guests > 0)
);

-- Location information table
CREATE TABLE locations (
    location_id INT PRIMARY KEY AUTO_INCREMENT,
    villa_id INT NOT NULL,
    address_line1 VARCHAR(100) NOT NULL,
    address_line2 VARCHAR(100),
    city VARCHAR(50) NOT NULL,
    region VARCHAR(50),
    postal_code VARCHAR(20) NOT NULL,
    country VARCHAR(50) NOT NULL DEFAULT 'Spain',
    latitude DECIMAL(10,8),
    longitude DECIMAL(11,8),
    FOREIGN KEY (villa_id) REFERENCES villas(villa_id) ON DELETE CASCADE
);

-- Villa amenities junction table
CREATE TABLE villa_amenities (
    villa_id INT NOT NULL,
    amenity VARCHAR(50) NOT NULL,
    PRIMARY KEY (villa_id, amenity),
    FOREIGN KEY (villa_id) REFERENCES villas(villa_id) ON DELETE CASCADE
);

-- Villa images table
CREATE TABLE villa_images (
    image_id INT PRIMARY KEY AUTO_INCREMENT,
    villa_id INT NOT NULL,
    image_url VARCHAR(255) NOT NULL,
    caption VARCHAR(100),
    is_primary BOOLEAN DEFAULT FALSE,
    display_order INT DEFAULT 0,
    FOREIGN KEY (villa_id) REFERENCES villas(villa_id) ON DELETE CASCADE
);

-- Pricing and availability table
CREATE TABLE villa_pricing (
    pricing_id INT PRIMARY KEY AUTO_INCREMENT,
    villa_id INT NOT NULL,
    base_price_per_night DECIMAL(10,2) NOT NULL,
    min_nights INT DEFAULT 1,
    cleaning_fee DECIMAL(10,2) DEFAULT 0,
    security_deposit DECIMAL(10,2) DEFAULT 0,
    seasonal_multiplier DECIMAL(3,2) DEFAULT 1.00,
    currency VARCHAR(3) DEFAULT 'EUR',
    FOREIGN KEY (villa_id) REFERENCES villas(villa_id) ON DELETE CASCADE,
    CHECK (base_price_per_night > 0),
    CHECK (min_nights > 0)
);

-- Create indexes for performance
CREATE INDEX idx_villas_bedrooms ON villas(bedrooms);
CREATE INDEX idx_villas_has_pool ON villas(has_pool);
CREATE INDEX idx_locations_city ON locations(city);
CREATE INDEX idx_locations_country ON locations(country);
```
