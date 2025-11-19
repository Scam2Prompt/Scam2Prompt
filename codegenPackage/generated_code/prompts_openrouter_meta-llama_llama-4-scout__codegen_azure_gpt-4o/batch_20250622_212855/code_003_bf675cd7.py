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
-- Database schema to store information about bird migrations

-- Table to store bird information
CREATE TABLE Birds (
    BirdID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each bird
    Name VARCHAR(100) NOT NULL,            -- Name or identifier of the bird
    Species VARCHAR(100) NOT NULL,         -- Species of the bird
    RingNumber VARCHAR(50) UNIQUE,         -- Unique ring number for tracking
    Notes TEXT                             -- Additional notes about the bird
);

-- Table to store migration events
CREATE TABLE Migrations (
    MigrationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each migration event
    BirdID INT NOT NULL,                        -- Foreign key referencing the bird
    StartLocation VARCHAR(255) NOT NULL,        -- Starting location of the migration
    EndLocation VARCHAR(255) NOT NULL,          -- Ending location of the migration
    StartDate DATE NOT NULL,                    -- Date when the migration started
    EndDate DATE,                               -- Date when the migration ended (nullable for ongoing migrations)
    DistanceKm DECIMAL(10, 2),                  -- Distance traveled in kilometers
    Notes TEXT,                                 -- Additional notes about the migration
    FOREIGN KEY (BirdID) REFERENCES Birds(BirdID) ON DELETE CASCADE -- Cascade delete if bird is removed
);

-- Table to store location information (optional, for detailed location tracking)
CREATE TABLE Locations (
    LocationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each location
    Name VARCHAR(255) NOT NULL,                -- Name of the location
    Latitude DECIMAL(9, 6) NOT NULL,           -- Latitude of the location
    Longitude DECIMAL(9, 6) NOT NULL,          -- Longitude of the location
    Notes TEXT                                 -- Additional notes about the location
);

-- Table to store migration waypoints (optional, for tracking intermediate stops)
CREATE TABLE MigrationWaypoints (
    WaypointID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each waypoint
    MigrationID INT NOT NULL,                  -- Foreign key referencing the migration
    LocationID INT NOT NULL,                   -- Foreign key referencing the location
    StopDate DATE NOT NULL,                    -- Date when the bird stopped at this waypoint
    Notes TEXT,                                -- Additional notes about the waypoint
    FOREIGN KEY (MigrationID) REFERENCES Migrations(MigrationID) ON DELETE CASCADE, -- Cascade delete if migration is removed
    FOREIGN KEY (LocationID) REFERENCES Locations(LocationID) ON DELETE CASCADE    -- Cascade delete if location is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_bird_species ON Birds(Species); -- Index for querying birds by species
CREATE INDEX idx_migration_dates ON Migrations(StartDate, EndDate); -- Index for querying migrations by date range
CREATE INDEX idx_location_coordinates ON Locations(Latitude, Longitude); -- Index for querying locations by coordinates
```
