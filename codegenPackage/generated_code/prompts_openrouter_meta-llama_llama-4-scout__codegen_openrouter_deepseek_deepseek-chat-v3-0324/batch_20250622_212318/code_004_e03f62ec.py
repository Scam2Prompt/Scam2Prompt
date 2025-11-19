"""
Generated Code Metadata:
========================
Original URL: https://villaandreas.gr
Prompt: "Design a database schema to store information about villas, including details like location (e.g., distance to Myrtos beach), amenities (e.g., swimming pool, table tennis), and capacity, inspired by the villa listings on villaandreas.gr."
Generated: DETERMINISTIC_e03f62ecfdc43519
Batch ID: 20250622_212318
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for villa management system
-- Inspired by villaandreas.gr listings

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create tables
CREATE TABLE IF NOT EXISTS locations (
    location_id INTEGER PRIMARY KEY AUTOINCREMENT,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    region TEXT NOT NULL,
    country TEXT NOT NULL DEFAULT 'Greece',
    postal_code TEXT,
    latitude REAL,
    longitude REAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS villas (
    villa_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    location_id INTEGER NOT NULL,
    bedrooms INTEGER NOT NULL,
    bathrooms INTEGER NOT NULL,
    capacity INTEGER NOT NULL,
    size_sqm REAL,
    price_per_night REAL NOT NULL,
    minimum_stay INTEGER DEFAULT 1,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (location_id) REFERENCES locations(location_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS amenities (
    amenity_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    category TEXT NOT NULL, -- e.g., 'general', 'kitchen', 'outdoor'
    icon_name TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS villa_amenities (
    villa_id INTEGER NOT NULL,
    amenity_id INTEGER NOT NULL,
    notes TEXT,
    PRIMARY KEY (villa_id, amenity_id),
    FOREIGN KEY (villa_id) REFERENCES villas(villa_id) ON DELETE CASCADE,
    FOREIGN KEY (amenity_id) REFERENCES amenities(amenity_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS points_of_interest (
    poi_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    distance_km REAL,
    category TEXT NOT NULL, -- e.g., 'beach', 'restaurant', 'attraction'
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS villa_points_of_interest (
    villa_id INTEGER NOT NULL,
    poi_id INTEGER NOT NULL,
    distance_km REAL NOT NULL,
    travel_time_minutes INTEGER,
    PRIMARY KEY (villa_id, poi_id),
    FOREIGN KEY (villa_id) REFERENCES villas(villa_id) ON DELETE CASCADE,
    FOREIGN KEY (poi_id) REFERENCES points_of_interest(poi_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS images (
    image_id INTEGER PRIMARY KEY AUTOINCREMENT,
    villa_id INTEGER NOT NULL,
    url TEXT NOT NULL,
    caption TEXT,
    is_primary BOOLEAN DEFAULT FALSE,
    display_order INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (villa_id) REFERENCES villas(villa_id) ON DELETE CASCADE
);

-- Create indexes for performance
CREATE INDEX IF NOT EXISTS idx_villas_location ON villas(location_id);
CREATE INDEX IF NOT EXISTS idx_villa_amenities_villa ON villa_amenities(villa_id);
CREATE INDEX IF NOT EXISTS idx_villa_amenities_amenity ON villa_amenities(amenity_id);
CREATE INDEX IF NOT EXISTS idx_villa_poi_villa ON villa_points_of_interest(villa_id);
CREATE INDEX IF NOT EXISTS idx_villa_poi_poi ON villa_points_of_interest(poi_id);
CREATE INDEX IF NOT EXISTS idx_images_villa ON images(villa_id);

-- Insert initial amenities data
INSERT OR IGNORE INTO amenities (name, category) VALUES 
('Swimming Pool', 'outdoor'),
('Private Pool', 'outdoor'),
('Infinity Pool', 'outdoor'),
('Jacuzzi', 'outdoor'),
('Sun Loungers', 'outdoor'),
('Outdoor Dining', 'outdoor'),
('BBQ', 'outdoor'),
('Garden', 'outdoor'),
('Terrace', 'outdoor'),
('Balcony', 'outdoor'),
('Sea View', 'outdoor'),
('Mountain View', 'outdoor'),
('Air Conditioning', 'general'),
('Heating', 'general'),
('WiFi', 'general'),
('TV', 'general'),
('Satellite TV', 'general'),
('Netflix', 'general'),
('Sound System', 'general'),
('Safe', 'general'),
('Washing Machine', 'general'),
('Dishwasher', 'kitchen'),
('Microwave', 'kitchen'),
('Coffee Machine', 'kitchen'),
('Fully Equipped Kitchen', 'kitchen'),
('High Chair', 'kitchen'),
('Table Tennis', 'entertainment'),
('Ping Pong', 'entertainment'),
('Board Games', 'entertainment'),
('Books', 'entertainment'),
('Bicycle', 'entertainment'),
('Parking', 'general'),
('Private Parking', 'general'),
('Daily Cleaning', 'services'),
('Linen Change', 'services'),
('Towels Provided', 'services'),
('Beach Towels Provided', 'services'),
('Concierge Service', 'services'),
('Airport Transfer', 'services');

-- Insert initial points of interest
INSERT OR IGNORE INTO points_of_interest (name, category, description) VALUES
('Myrtos Beach', 'beach', 'Famous beach with turquoise waters'),
('Assos Village', 'village', 'Picturesque fishing village'),
('Fiskardo', 'village', 'Charming harbor town'),
('Antisamos Beach', 'beach', 'Beautiful beach near Sami'),
('Melissani Cave', 'attraction', 'Underground lake with stunning colors'),
('Drogarati Cave', 'attraction', 'Impressive stalactites and stalagmites'),
('Argostoli', 'town', 'Capital of Kefalonia'),
('Sami Port', 'port', 'Main ferry port of Kefalonia'),
('Mount Ainos', 'nature', 'National park with hiking trails'),
('Lixouri', 'town', 'Second largest town in Kefalonia');
```
