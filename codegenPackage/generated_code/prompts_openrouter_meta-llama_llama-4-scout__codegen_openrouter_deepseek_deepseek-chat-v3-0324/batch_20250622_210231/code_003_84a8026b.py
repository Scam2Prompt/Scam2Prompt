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
-- Database schema for dance events (inspired by BallaTorino)

-- Enable UUID extension if not already enabled
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Table for event locations
CREATE TABLE locations (
    location_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(100) NOT NULL,
    address TEXT NOT NULL,
    city VARCHAR(50) NOT NULL,
    country VARCHAR(50) NOT NULL,
    latitude DECIMAL(10, 8),
    longitude DECIMAL(11, 8),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table for dance activity types
CREATE TABLE activity_types (
    activity_type_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Main events table
CREATE TABLE events (
    event_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(100) NOT NULL,
    description TEXT,
    start_date TIMESTAMP WITH TIME ZONE NOT NULL,
    end_date TIMESTAMP WITH TIME ZONE NOT NULL,
    location_id UUID REFERENCES locations(location_id) ON DELETE SET NULL,
    organizer VARCHAR(100),
    website_url VARCHAR(255),
    is_recurring BOOLEAN DEFAULT FALSE,
    recurrence_pattern VARCHAR(50),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CHECK (end_date >= start_date)
);

-- Junction table for events and activity types (many-to-many relationship)
CREATE TABLE event_activities (
    event_id UUID REFERENCES events(event_id) ON DELETE CASCADE,
    activity_type_id UUID REFERENCES activity_types(activity_type_id) ON DELETE CASCADE,
    PRIMARY KEY (event_id, activity_type_id)
);

-- Table for event schedules (sub-events within a main event)
CREATE TABLE event_schedules (
    schedule_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    event_id UUID REFERENCES events(event_id) ON DELETE CASCADE,
    activity_type_id UUID REFERENCES activity_types(activity_type_id) ON DELETE SET NULL,
    start_time TIMESTAMP WITH TIME ZONE NOT NULL,
    end_time TIMESTAMP WITH TIME ZONE NOT NULL,
    title VARCHAR(100),
    description TEXT,
    instructor VARCHAR(100),
    price DECIMAL(10, 2),
    currency VARCHAR(3) DEFAULT 'EUR',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CHECK (end_time >= start_time)
);

-- Trigger function to update the updated_at timestamp
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create triggers for all tables with updated_at field
CREATE TRIGGER update_locations_timestamp
BEFORE UPDATE ON locations
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_activity_types_timestamp
BEFORE UPDATE ON activity_types
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_events_timestamp
BEFORE UPDATE ON events
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_event_schedules_timestamp
BEFORE UPDATE ON event_schedules
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```
