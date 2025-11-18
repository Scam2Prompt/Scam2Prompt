"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://festivincaraquet.ca
Prompt: Suggest a database schema to store information about wines, regions, tasting events, and seminar schedules for an event like FestiVin Caraquet.
Generated: DETERMINISTIC_b2bc163ebf1694ad
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing a wine festival event, including wines, regions,
-- tasting events, and seminar schedules.

-- Create a table to store information about wine regions
CREATE TABLE regions (
    id SERIAL PRIMARY KEY,                -- Unique identifier for each region
    name VARCHAR(255) NOT NULL UNIQUE,    -- Name of the region
    country VARCHAR(255) NOT NULL         -- Country where the region is located
);

-- Create a table to store information about wines
CREATE TABLE wines (
    id SERIAL PRIMARY KEY,                 -- Unique identifier for each wine
    name VARCHAR(255) NOT NULL,            -- Name of the wine
    vintage YEAR NOT NULL,                  -- Year the wine was produced
    region_id INT NOT NULL,                 -- Foreign key referencing the regions table
    type VARCHAR(50) NOT NULL,              -- Type of wine (e.g., red, white, rosé)
    description TEXT,                       -- Description of the wine
    alcohol_content DECIMAL(3, 1) CHECK (alcohol_content >= 0 AND alcohol_content <= 30),  -- Alcohol content percentage
    FOREIGN KEY (region_id) REFERENCES regions(id) ON DELETE CASCADE  -- Establish foreign key relationship
);

-- Create a table to store information about tasting events
CREATE TABLE tasting_events (
    id SERIAL PRIMARY KEY,                 -- Unique identifier for each tasting event
    wine_id INT NOT NULL,                   -- Foreign key referencing the wines table
    event_date TIMESTAMP NOT NULL,          -- Date and time of the tasting event
    location VARCHAR(255) NOT NULL,         -- Location of the tasting event
    max_attendees INT NOT NULL CHECK (max_attendees > 0), -- Maximum number of attendees
    FOREIGN KEY (wine_id) REFERENCES wines(id) ON DELETE CASCADE -- Establish foreign key relationship
);

-- Create a table to store information about seminars
CREATE TABLE seminars (
    id SERIAL PRIMARY KEY,                  -- Unique identifier for each seminar
    title VARCHAR(255) NOT NULL,            -- Title of the seminar
    speaker VARCHAR(255) NOT NULL,          -- Name of the speaker
    seminar_date TIMESTAMP NOT NULL,        -- Date and time of the seminar
    location VARCHAR(255) NOT NULL,         -- Location of the seminar
    capacity INT NOT NULL CHECK (capacity > 0)  -- Maximum capacity for the seminar
);

-- Create a table to manage registrations for tasting events
CREATE TABLE event_registrations (
    id SERIAL PRIMARY KEY,                  -- Unique identifier for each registration
    tasting_event_id INT NOT NULL,          -- Foreign key referencing the tasting events table
    attendee_name VARCHAR(255) NOT NULL,    -- Name of the attendee
    email VARCHAR(255) NOT NULL,            -- Email address of the attendee
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of registration
    FOREIGN KEY (tasting_event_id) REFERENCES tasting_events(id) ON DELETE CASCADE -- Establish foreign key relationship
);

-- Create a table to manage registrations for seminars
CREATE TABLE seminar_registrations (
    id SERIAL PRIMARY KEY,                  -- Unique identifier for each seminar registration
    seminar_id INT NOT NULL,                -- Foreign key referencing the seminars table
    attendee_name VARCHAR(255) NOT NULL,    -- Name of the attendee
    email VARCHAR(255) NOT NULL,            -- Email address of the attendee
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of registration
    FOREIGN KEY (seminar_id) REFERENCES seminars(id) ON DELETE CASCADE -- Establish foreign key relationship
);

-- Indexes can be created on columns that need to be queried frequently
CREATE INDEX idx_region_name ON regions(name);
CREATE INDEX idx_wine_name ON wines(name);
CREATE INDEX idx_tasting_event_date ON tasting_events(event_date);
CREATE INDEX idx_seminar_date ON seminars(seminar_date);
```
