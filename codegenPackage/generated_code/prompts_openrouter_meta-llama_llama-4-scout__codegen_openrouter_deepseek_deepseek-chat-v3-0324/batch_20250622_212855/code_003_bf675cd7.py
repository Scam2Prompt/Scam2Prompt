"""
Generated Code Metadata:
========================
Original URL: https://moonbirds.pro
Prompt: Design a simple database schema to store information about bird migrations, inspired by Moonbird B95's extensive travel history.
Generated: DETERMINISTIC_bf675cd7c0b9457d
Batch ID: 20250622_212855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for tracking bird migrations
-- Inspired by Moonbird B95's extensive travel history

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Table to store bird species information
CREATE TABLE IF NOT EXISTS species (
    species_id INTEGER PRIMARY KEY AUTOINCREMENT,
    scientific_name TEXT NOT NULL UNIQUE,
    common_name TEXT NOT NULL,
    conservation_status TEXT CHECK(conservation_status IN 
        ('Least Concern', 'Near Threatened', 'Vulnerable', 'Endangered', 'Critically Endangered', 'Extinct in the Wild', 'Extinct')),
    average_lifespan_years INTEGER,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store individual birds
CREATE TABLE IF NOT EXISTS birds (
    bird_id INTEGER PRIMARY KEY AUTOINCREMENT,
    species_id INTEGER NOT NULL,
    banding_code TEXT UNIQUE,
    nickname TEXT,
    sex TEXT CHECK(sex IN ('Male', 'Female', 'Unknown')),
    estimated_hatch_year INTEGER,
    banding_location TEXT,
    banding_date DATE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (species_id) REFERENCES species(species_id) ON DELETE CASCADE
);

-- Table to store migration observations
CREATE TABLE IF NOT EXISTS migrations (
    migration_id INTEGER PRIMARY KEY AUTOINCREMENT,
    bird_id INTEGER NOT NULL,
    observation_date TIMESTAMP NOT NULL,
    latitude REAL NOT NULL CHECK(latitude BETWEEN -90 AND 90),
    longitude REAL NOT NULL CHECK(longitude BETWEEN -180 AND 180),
    location_name TEXT,
    country_code TEXT,
    observer_name TEXT,
    notes TEXT,
    distance_km REAL CHECK(distance_km >= 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (bird_id) REFERENCES birds(bird_id) ON DELETE CASCADE
);

-- Table to store migration statistics per bird
CREATE TABLE IF NOT EXISTS migration_stats (
    stat_id INTEGER PRIMARY KEY AUTOINCREMENT,
    bird_id INTEGER NOT NULL UNIQUE,
    total_distance_km REAL DEFAULT 0 CHECK(total_distance_km >= 0),
    first_observation_date TIMESTAMP,
    last_observation_date TIMESTAMP,
    countries_visited_count INTEGER DEFAULT 0 CHECK(countries_visited_count >= 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (bird_id) REFERENCES birds(bird_id) ON DELETE CASCADE
);

-- Trigger to update migration stats when new observations are added
CREATE TRIGGER IF NOT EXISTS update_migration_stats
AFTER INSERT ON migrations
BEGIN
    -- Update total distance
    UPDATE migration_stats
    SET total_distance_km = total_distance_km + COALESCE(NEW.distance_km, 0),
        updated_at = CURRENT_TIMESTAMP
    WHERE bird_id = NEW.bird_id;
    
    -- Update first observation date if this is the earliest
    UPDATE migration_stats
    SET first_observation_date = 
        CASE 
            WHEN first_observation_date IS NULL OR NEW.observation_date < first_observation_date 
            THEN NEW.observation_date 
            ELSE first_observation_date 
        END
    WHERE bird_id = NEW.bird_id;
    
    -- Update last observation date if this is the latest
    UPDATE migration_stats
    SET last_observation_date = 
        CASE 
            WHEN last_observation_date IS NULL OR NEW.observation_date > last_observation_date 
            THEN NEW.observation_date 
            ELSE last_observation_date 
        END
    WHERE bird_id = NEW.bird_id;
    
    -- Increment countries count if this is a new country
    UPDATE migration_stats
    SET countries_visited_count = countries_visited_count + 1
    WHERE bird_id = NEW.bird_id 
    AND NEW.country_code NOT IN (
        SELECT DISTINCT country_code 
        FROM migrations 
        WHERE bird_id = NEW.bird_id 
        AND migration_id != NEW.migration_id
    );
END;

-- Trigger to initialize migration stats when a new bird is added
CREATE TRIGGER IF NOT EXISTS initialize_migration_stats
AFTER INSERT ON birds
BEGIN
    INSERT INTO migration_stats (bird_id) VALUES (NEW.bird_id);
END;

-- Indexes for performance optimization
CREATE INDEX IF NOT EXISTS idx_migrations_bird_id ON migrations(bird_id);
CREATE INDEX IF NOT EXISTS idx_migrations_date ON migrations(observation_date);
CREATE INDEX IF NOT EXISTS idx_migrations_location ON migrations(latitude, longitude);
```
