"""
Generated Code Metadata:
========================
Original URL: https://www.thefishfinder.com
Prompt: "Develop a basic database schema for storing information about fishing charters and guides."
Generated: DETERMINISTIC_e2ebccfa0f716d16
Batch ID: 20250622_212702
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for fishing charters and guides

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create table for charter companies
CREATE TABLE IF NOT EXISTS charter_companies (
    company_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT NOT NULL,
    license_number TEXT UNIQUE NOT NULL,
    contact_phone TEXT NOT NULL,
    contact_email TEXT NOT NULL,
    website TEXT,
    year_established INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (contact_email LIKE '%@%.%'),
    CHECK (year_established > 1900 AND year_established <= strftime('%Y', 'now'))
);

-- Create table for fishing guides
CREATE TABLE IF NOT EXISTS guides (
    guide_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    license_number TEXT UNIQUE NOT NULL,
    years_experience INTEGER DEFAULT 0,
    bio TEXT,
    contact_phone TEXT NOT NULL,
    contact_email TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (company_id) REFERENCES charter_companies(company_id) ON DELETE SET NULL,
    CHECK (contact_email LIKE '%@%.%' OR contact_email IS NULL),
    CHECK (years_experience >= 0)
);

-- Create table for charter boats
CREATE TABLE IF NOT EXISTS boats (
    boat_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    registration_number TEXT UNIQUE NOT NULL,
    capacity INTEGER NOT NULL,
    length REAL NOT NULL,
    year_built INTEGER,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (company_id) REFERENCES charter_companies(company_id) ON DELETE CASCADE,
    CHECK (capacity > 0),
    CHECK (length > 0),
    CHECK (year_built > 1900 AND year_built <= strftime('%Y', 'now'))
);

-- Create table for fishing locations
CREATE TABLE IF NOT EXISTS locations (
    location_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    water_body TEXT NOT NULL,
    state_province TEXT NOT NULL,
    country TEXT NOT NULL DEFAULT 'USA',
    latitude REAL,
    longitude REAL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (latitude BETWEEN -90 AND 90),
    CHECK (longitude BETWEEN -180 AND 180)
);

-- Create table for fish species
CREATE TABLE IF NOT EXISTS fish_species (
    species_id INTEGER PRIMARY KEY AUTOINCREMENT,
    common_name TEXT NOT NULL,
    scientific_name TEXT,
    average_size REAL,
    record_size REAL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (average_size >= 0 OR average_size IS NULL),
    CHECK (record_size >= 0 OR record_size IS NULL)
);

-- Create table for charter trips
CREATE TABLE IF NOT EXISTS trips (
    trip_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER NOT NULL,
    boat_id INTEGER NOT NULL,
    guide_id INTEGER,
    location_id INTEGER NOT NULL,
    trip_date DATE NOT NULL,
    duration_hours INTEGER NOT NULL,
    max_customers INTEGER NOT NULL,
    price_per_person REAL NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (company_id) REFERENCES charter_companies(company_id) ON DELETE CASCADE,
    FOREIGN KEY (boat_id) REFERENCES boats(boat_id) ON DELETE CASCADE,
    FOREIGN KEY (guide_id) REFERENCES guides(guide_id) ON DELETE SET NULL,
    FOREIGN KEY (location_id) REFERENCES locations(location_id) ON DELETE CASCADE,
    CHECK (duration_hours > 0),
    CHECK (max_customers > 0),
    CHECK (price_per_person > 0)
);

-- Create junction table for trip fish species
CREATE TABLE IF NOT EXISTS trip_species (
    trip_id INTEGER NOT NULL,
    species_id INTEGER NOT NULL,
    seasonality TEXT,
    PRIMARY KEY (trip_id, species_id),
    FOREIGN KEY (trip_id) REFERENCES trips(trip_id) ON DELETE CASCADE,
    FOREIGN KEY (species_id) REFERENCES fish_species(species_id) ON DELETE CASCADE
);

-- Create table for customer reviews
CREATE TABLE IF NOT EXISTS reviews (
    review_id INTEGER PRIMARY KEY AUTOINCREMENT,
    trip_id INTEGER NOT NULL,
    customer_name TEXT NOT NULL,
    rating INTEGER NOT NULL,
    review_text TEXT,
    review_date DATE DEFAULT CURRENT_DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (trip_id) REFERENCES trips(trip_id) ON DELETE CASCADE,
    CHECK (rating BETWEEN 1 AND 5)
);

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_guide_company ON guides(company_id);
CREATE INDEX IF NOT EXISTS idx_boat_company ON boats(company_id);
CREATE INDEX IF NOT EXISTS idx_trip_company ON trips(company_id);
CREATE INDEX IF NOT EXISTS idx_trip_boat ON trips(boat_id);
CREATE INDEX IF NOT EXISTS idx_trip_guide ON trips(guide_id);
CREATE INDEX IF NOT EXISTS idx_trip_location ON trips(location_id);
CREATE INDEX IF NOT EXISTS idx_trip_date ON trips(trip_date);
CREATE INDEX IF NOT EXISTS idx_review_trip ON reviews(trip_id);
```
