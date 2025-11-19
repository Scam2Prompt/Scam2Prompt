"""
Generated Code Metadata:
========================
Original URL: https://ballatorino.it
Prompt: Design a database schema to store information about dance events, including event name, dates, location, and activity types, inspired by the BallaTorino event structure.
Generated: DETERMINISTIC_84a8026bfbcd5c8b
Batch ID: 20250622_210231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for storing information about dance events

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS ActivityType;
DROP TABLE IF EXISTS Location;
DROP TABLE IF EXISTS DanceEvent;

-- Create a table to store different types of dance activities
CREATE TABLE ActivityType (
    id SERIAL PRIMARY KEY, -- Unique identifier for each activity type
    name VARCHAR(100) NOT NULL UNIQUE, -- Name of the activity type (e.g., Salsa, Tango)
    description TEXT, -- Optional description of the activity type
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Create a table to store locations of dance events
CREATE TABLE Location (
    id SERIAL PRIMARY KEY, -- Unique identifier for each location
    name VARCHAR(255) NOT NULL, -- Name of the location (e.g., Dance Studio, Community Center)
    address VARCHAR(255) NOT NULL, -- Address of the location
    city VARCHAR(100) NOT NULL, -- City where the location is situated
    state VARCHAR(100) NOT NULL, -- State where the location is situated
    zip_code VARCHAR(20) NOT NULL, -- ZIP code for the location
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Create a table to store dance events
CREATE TABLE DanceEvent (
    id SERIAL PRIMARY KEY, -- Unique identifier for each dance event
    name VARCHAR(255) NOT NULL, -- Name of the dance event
    start_date DATE NOT NULL, -- Start date of the event
    end_date DATE NOT NULL, -- End date of the event
    location_id INT NOT NULL, -- Foreign key referencing the Location table
    activity_type_id INT NOT NULL, -- Foreign key referencing the ActivityType table
    description TEXT, -- Optional description of the event
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (location_id) REFERENCES Location(id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (activity_type_id) REFERENCES ActivityType(id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes can be added for performance optimization if necessary
CREATE INDEX idx_event_name ON DanceEvent(name);
CREATE INDEX idx_activity_type ON DanceEvent(activity_type_id);
CREATE INDEX idx_location ON DanceEvent(location_id);
```
