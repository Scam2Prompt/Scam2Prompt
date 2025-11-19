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
-- Database schema for FestiVin Caraquet wine festival

-- Table to store wine regions
CREATE TABLE regions (
    region_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL,
    description TEXT,
    climate VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store wineries
CREATE TABLE wineries (
    winery_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    region_id INTEGER REFERENCES regions(region_id) ON DELETE SET NULL,
    founded_year INTEGER,
    website VARCHAR(255),
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store wine types
CREATE TABLE wine_types (
    type_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store wines
CREATE TABLE wines (
    wine_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    winery_id INTEGER REFERENCES wineries(winery_id) ON DELETE CASCADE,
    type_id INTEGER REFERENCES wine_types(type_id) ON DELETE SET NULL,
    vintage INTEGER,
    alcohol_content DECIMAL(4,2),
    price DECIMAL(10,2),
    description TEXT,
    image_url VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store tasting notes
CREATE TABLE tasting_notes (
    note_id SERIAL PRIMARY KEY,
    wine_id INTEGER REFERENCES wines(wine_id) ON DELETE CASCADE,
    appearance TEXT,
    aroma TEXT,
    palate TEXT,
    finish TEXT,
    overall_rating INTEGER CHECK (overall_rating BETWEEN 1 AND 5),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store event venues
CREATE TABLE venues (
    venue_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address TEXT NOT NULL,
    capacity INTEGER,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store event types
CREATE TABLE event_types (
    type_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store events
CREATE TABLE events (
    event_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    type_id INTEGER REFERENCES event_types(type_id) ON DELETE SET NULL,
    venue_id INTEGER REFERENCES venues(venue_id) ON DELETE SET NULL,
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP NOT NULL,
    description TEXT,
    max_attendees INTEGER,
    price DECIMAL(10,2),
    image_url VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (end_time > start_time)
);

-- Junction table for wines featured at events
CREATE TABLE event_wines (
    event_id INTEGER REFERENCES events(event_id) ON DELETE CASCADE,
    wine_id INTEGER REFERENCES wines(wine_id) ON DELETE CASCADE,
    PRIMARY KEY (event_id, wine_id)
);

-- Table to store speakers/presenters
CREATE TABLE presenters (
    presenter_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    title VARCHAR(100),
    bio TEXT,
    company VARCHAR(100),
    image_url VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store seminars
CREATE TABLE seminars (
    seminar_id SERIAL PRIMARY KEY,
    event_id INTEGER REFERENCES events(event_id) ON DELETE CASCADE,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Junction table for seminar presenters
CREATE TABLE seminar_presenters (
    seminar_id INTEGER REFERENCES seminars(seminar_id) ON DELETE CASCADE,
    presenter_id INTEGER REFERENCES presenters(presenter_id) ON DELETE CASCADE,
    PRIMARY KEY (seminar_id, presenter_id)
);

-- Table to store attendees
CREATE TABLE attendees (
    attendee_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store event registrations
CREATE TABLE registrations (
    registration_id SERIAL PRIMARY KEY,
    attendee_id INTEGER REFERENCES attendees(attendee_id) ON DELETE CASCADE,
    event_id INTEGER REFERENCES events(event_id) ON DELETE CASCADE,
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    payment_status VARCHAR(20) DEFAULT 'pending',
    payment_amount DECIMAL(10,2),
    notes TEXT,
    UNIQUE (attendee_id, event_id)
);

-- Table to store user reviews/ratings
CREATE TABLE reviews (
    review_id SERIAL PRIMARY KEY,
    attendee_id INTEGER REFERENCES attendees(attendee_id) ON DELETE SET NULL,
    event_id INTEGER REFERENCES events(event_id) ON DELETE CASCADE,
    rating INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
    comment TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for performance
CREATE INDEX idx_wines_winery ON wines(winery_id);
CREATE INDEX idx_wines_type ON wines(type_id);
CREATE INDEX idx_events_venue ON events(venue_id);
CREATE INDEX idx_events_time ON events(start_time, end_time);
CREATE INDEX idx_registrations_attendee ON registrations(attendee_id);
CREATE INDEX idx_registrations_event ON registrations(event_id);
```
