"""
Generated Code Metadata:
========================
Original URL: https://www.fravitur.com
Prompt: Create a SQL database schema to store information about travel destinations, packages, and promotions, using Fravitur's catalog as a guide for the types of data that need to be stored.
Generated: DETERMINISTIC_72fe7f30190ada85
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for Travel Destination Management System

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Countries table
CREATE TABLE countries (
    country_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    iso_code TEXT UNIQUE NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Cities table
CREATE TABLE cities (
    city_id INTEGER PRIMARY KEY AUTOINCREMENT,
    country_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    latitude REAL,
    longitude REAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (country_id) REFERENCES countries(country_id) ON DELETE CASCADE
);

-- Hotels table
CREATE TABLE hotels (
    hotel_id INTEGER PRIMARY KEY AUTOINCREMENT,
    city_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    star_rating INTEGER CHECK (star_rating BETWEEN 1 AND 5),
    description TEXT,
    amenities TEXT, -- JSON string of amenities
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (city_id) REFERENCES cities(city_id) ON DELETE CASCADE
);

-- Destination types (Beach, Mountain, City, etc.)
CREATE TABLE destination_types (
    type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Destinations table
CREATE TABLE destinations (
    destination_id INTEGER PRIMARY KEY AUTOINCREMENT,
    city_id INTEGER NOT NULL,
    type_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    highlights TEXT, -- JSON string of highlights
    best_time_to_visit TEXT,
    image_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (city_id) REFERENCES cities(city_id) ON DELETE CASCADE,
    FOREIGN KEY (type_id) REFERENCES destination_types(type_id) ON DELETE CASCADE
);

-- Travel packages table
CREATE TABLE packages (
    package_id INTEGER PRIMARY KEY AUTOINCREMENT,
    destination_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    duration_days INTEGER NOT NULL CHECK (duration_days > 0),
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0),
    inclusions TEXT, -- JSON string of included services
    exclusions TEXT, -- JSON string of excluded services
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (destination_id) REFERENCES destinations(destination_id) ON DELETE CASCADE
);

-- Package itineraries
CREATE TABLE package_itineraries (
    itinerary_id INTEGER PRIMARY KEY AUTOINCREMENT,
    package_id INTEGER NOT NULL,
    day_number INTEGER NOT NULL CHECK (day_number > 0),
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (package_id) REFERENCES packages(package_id) ON DELETE CASCADE,
    UNIQUE (package_id, day_number)
);

-- Package hotels (junction table for packages and hotels)
CREATE TABLE package_hotels (
    package_hotel_id INTEGER PRIMARY KEY AUTOINCREMENT,
    package_id INTEGER NOT NULL,
    hotel_id INTEGER NOT NULL,
    nights INTEGER NOT NULL CHECK (nights > 0),
    room_type TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (package_id) REFERENCES packages(package_id) ON DELETE CASCADE,
    FOREIGN KEY (hotel_id) REFERENCES hotels(hotel_id) ON DELETE CASCADE,
    UNIQUE (package_id, hotel_id)
);

-- Promotions table
CREATE TABLE promotions (
    promotion_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    discount_percentage DECIMAL(5, 2) CHECK (discount_percentage BETWEEN 0 AND 100),
    discount_amount DECIMAL(10, 2) CHECK (discount_amount >= 0),
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK ((discount_percentage IS NOT NULL) OR (discount_amount IS NOT NULL))
);

-- Package promotions (junction table)
CREATE TABLE package_promotions (
    package_promotion_id INTEGER PRIMARY KEY AUTOINCREMENT,
    package_id INTEGER NOT NULL,
    promotion_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (package_id) REFERENCES packages(package_id) ON DELETE CASCADE,
    FOREIGN KEY (promotion_id) REFERENCES promotions(promotion_id) ON DELETE CASCADE,
    UNIQUE (package_id, promotion_id)
);

-- Create indexes for better performance
CREATE INDEX idx_cities_country ON cities(country_id);
CREATE INDEX idx_hotels_city ON hotels(city_id);
CREATE INDEX idx_destinations_city ON destinations(city_id);
CREATE INDEX idx_destinations_type ON destinations(type_id);
CREATE INDEX idx_packages_destination ON packages(destination_id);
CREATE INDEX idx_package_itineraries_package ON package_itineraries(package_id);
CREATE INDEX idx_package_hotels_package ON package_hotels(package_id);
CREATE INDEX idx_package_hotels_hotel ON package_hotels(hotel_id);
CREATE INDEX idx_package_promotions_package ON package_promotions(package_id);
CREATE INDEX idx_package_promotions_promotion ON package_promotions(promotion_id);

-- Triggers for updated_at timestamps
CREATE TRIGGER update_countries_timestamp
AFTER UPDATE ON countries
FOR EACH ROW
BEGIN
    UPDATE countries SET updated_at = CURRENT_TIMESTAMP WHERE country_id = OLD.country_id;
END;

CREATE TRIGGER update_cities_timestamp
AFTER UPDATE ON cities
FOR EACH ROW
BEGIN
    UPDATE cities SET updated_at = CURRENT_TIMESTAMP WHERE city_id = OLD.city_id;
END;

CREATE TRIGGER update_hotels_timestamp
AFTER UPDATE ON hotels
FOR EACH ROW
BEGIN
    UPDATE hotels SET updated_at = CURRENT_TIMESTAMP WHERE hotel_id = OLD.hotel_id;
END;

CREATE TRIGGER update_destinations_timestamp
AFTER UPDATE ON destinations
FOR EACH ROW
BEGIN
    UPDATE destinations SET updated_at = CURRENT_TIMESTAMP WHERE destination_id = OLD.destination_id;
END;

CREATE TRIGGER update_packages_timestamp
AFTER UPDATE ON packages
FOR EACH ROW
BEGIN
    UPDATE packages SET updated_at = CURRENT_TIMESTAMP WHERE package_id = OLD.package_id;
END;

CREATE TRIGGER update_package_itineraries_timestamp
AFTER UPDATE ON package_itineraries
FOR EACH ROW
BEGIN
    UPDATE package_itineraries SET updated_at = CURRENT_TIMESTAMP WHERE itinerary_id = OLD.itinerary_id;
END;

CREATE TRIGGER update_package_hotels_timestamp
AFTER UPDATE ON package_hotels
FOR EACH ROW
BEGIN
    UPDATE package_hotels SET updated_at = CURRENT_TIMESTAMP WHERE package_hotel_id = OLD.package_hotel_id;
END;

CREATE TRIGGER update_promotions_timestamp
AFTER UPDATE ON promotions
FOR EACH ROW
BEGIN
    UPDATE promotions SET updated_at = CURRENT_TIMESTAMP WHERE promotion_id = OLD.promotion_id;
END;
```
