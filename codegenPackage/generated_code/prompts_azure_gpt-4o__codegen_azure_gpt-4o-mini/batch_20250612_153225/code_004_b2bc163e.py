"""
Generated Code Metadata:
========================
Original URL: https://festivincaraquet.ca
Prompt: Suggest a database schema to store information about wines, regions, tasting events, and seminar schedules for an event like FestiVin Caraquet.
Generated: DETERMINISTIC_b2bc163ebf1694ad
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about wines, regions, tasting events, and seminar schedules for FestiVin Caraquet

-- Table to store information about wine regions
CREATE TABLE Regions (
    region_id SERIAL PRIMARY KEY, -- Unique identifier for each region
    name VARCHAR(100) NOT NULL, -- Name of the region
    country VARCHAR(100) NOT NULL, -- Country where the region is located
    description TEXT, -- Description of the region
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store information about wines
CREATE TABLE Wines (
    wine_id SERIAL PRIMARY KEY, -- Unique identifier for each wine
    name VARCHAR(100) NOT NULL, -- Name of the wine
    region_id INT NOT NULL, -- Foreign key referencing the Regions table
    varietal VARCHAR(100), -- Type of grape used
    vintage YEAR, -- Year the wine was produced
    description TEXT, -- Description of the wine
    price DECIMAL(10, 2), -- Price of the wine
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (region_id) REFERENCES Regions(region_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store information about tasting events
CREATE TABLE TastingEvents (
    event_id SERIAL PRIMARY KEY, -- Unique identifier for each tasting event
    name VARCHAR(100) NOT NULL, -- Name of the tasting event
    event_date DATE NOT NULL, -- Date of the event
    location VARCHAR(100), -- Location of the event
    description TEXT, -- Description of the event
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store information about seminars
CREATE TABLE Seminars (
    seminar_id SERIAL PRIMARY KEY, -- Unique identifier for each seminar
    title VARCHAR(100) NOT NULL, -- Title of the seminar
    speaker VARCHAR(100), -- Name of the speaker
    seminar_date DATE NOT NULL, -- Date of the seminar
    time TIME NOT NULL, -- Time of the seminar
    description TEXT, -- Description of the seminar
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to link wines to tasting events (many-to-many relationship)
CREATE TABLE EventWines (
    event_id INT NOT NULL, -- Foreign key referencing the TastingEvents table
    wine_id INT NOT NULL, -- Foreign key referencing the Wines table
    PRIMARY KEY (event_id, wine_id), -- Composite primary key
    FOREIGN KEY (event_id) REFERENCES TastingEvents(event_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (wine_id) REFERENCES Wines(wine_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to link seminars to tasting events (many-to-many relationship)
CREATE TABLE EventSeminars (
    event_id INT NOT NULL, -- Foreign key referencing the TastingEvents table
    seminar_id INT NOT NULL, -- Foreign key referencing the Seminars table
    PRIMARY KEY (event_id, seminar_id), -- Composite primary key
    FOREIGN KEY (event_id) REFERENCES TastingEvents(event_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (seminar_id) REFERENCES Seminars(seminar_id) ON DELETE CASCADE -- Ensures referential integrity
);
```
