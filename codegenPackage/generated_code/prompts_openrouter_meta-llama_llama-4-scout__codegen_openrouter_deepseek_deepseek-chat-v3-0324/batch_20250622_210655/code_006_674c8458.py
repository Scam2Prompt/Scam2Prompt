"""
Generated Code Metadata:
========================
Original URL: https://www.al-aanqua.com
Prompt: Design a database schema for storing information about art and cultural events in the Arab world, inspired by the website's content.
Generated: DETERMINISTIC_674c84584a6b2c73
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Arab Art and Cultural Events

-- Enable UUID extension if not already enabled
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Table for countries
CREATE TABLE countries (
    country_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(100) NOT NULL,
    iso_code CHAR(2) UNIQUE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table for cities
CREATE TABLE cities (
    city_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    country_id UUID NOT NULL REFERENCES countries(country_id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table for venues
CREATE TABLE venues (
    venue_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    city_id UUID NOT NULL REFERENCES cities(city_id) ON DELETE CASCADE,
    name VARCHAR(200) NOT NULL,
    address TEXT,
    capacity INTEGER,
    website_url VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table for event categories
CREATE TABLE event_categories (
    category_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table for artists
CREATE TABLE artists (
    artist_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(200) NOT NULL,
    bio TEXT,
    country_id UUID REFERENCES countries(country_id) ON DELETE SET NULL,
    website_url VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table for events
CREATE TABLE events (
    event_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    title VARCHAR(200) NOT NULL,
    description TEXT,
    category_id UUID REFERENCES event_categories(category_id) ON DELETE SET NULL,
    venue_id UUID REFERENCES venues(venue_id) ON DELETE SET NULL,
    start_datetime TIMESTAMP WITH TIME ZONE NOT NULL,
    end_datetime TIMESTAMP WITH TIME ZONE NOT NULL,
    price_range VARCHAR(100),
    is_free BOOLEAN DEFAULT FALSE,
    age_restriction INTEGER,
    featured_image_url VARCHAR(255),
    website_url VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CHECK (end_datetime > start_datetime)
);

-- Junction table for event-artist relationships
CREATE TABLE event_artists (
    event_id UUID NOT NULL REFERENCES events(event_id) ON DELETE CASCADE,
    artist_id UUID NOT NULL REFERENCES artists(artist_id) ON DELETE CASCADE,
    is_headliner BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (event_id, artist_id)
);

-- Table for event media (images, videos)
CREATE TABLE event_media (
    media_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    event_id UUID NOT NULL REFERENCES events(event_id) ON DELETE CASCADE,
    media_url VARCHAR(255) NOT NULL,
    media_type VARCHAR(50) NOT NULL CHECK (media_type IN ('image', 'video')),
    caption TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table for user accounts
CREATE TABLE users (
    user_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    country_id UUID REFERENCES countries(country_id) ON DELETE SET NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table for user saved events
CREATE TABLE user_saved_events (
    user_id UUID NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    event_id UUID NOT NULL REFERENCES events(event_id) ON DELETE CASCADE,
    saved_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id, event_id)
);

-- Table for event reviews
CREATE TABLE event_reviews (
    review_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    event_id UUID NOT NULL REFERENCES events(event_id) ON DELETE CASCADE,
    rating INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
    review_text TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (user_id, event_id)
);

-- Indexes for performance optimization
CREATE INDEX idx_events_date ON events(start_datetime);
CREATE INDEX idx_events_venue ON events(venue_id);
CREATE INDEX idx_events_category ON events(category_id);
CREATE INDEX idx_artists_country ON artists(country_id);
CREATE INDEX idx_cities_country ON cities(country_id);
CREATE INDEX idx_event_artists_artist ON event_artists(artist_id);
CREATE INDEX idx_event_media_event ON event_media(event_id);
CREATE INDEX idx_user_saved_events_event ON user_saved_events(event_id);
CREATE INDEX idx_event_reviews_event ON event_reviews(event_id);

-- Trigger function to update 'updated_at' timestamp
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create triggers for tables with updated_at fields
CREATE TRIGGER update_countries_timestamp
BEFORE UPDATE ON countries
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_cities_timestamp
BEFORE UPDATE ON cities
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_venues_timestamp
BEFORE UPDATE ON venues
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_event_categories_timestamp
BEFORE UPDATE ON event_categories
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_artists_timestamp
BEFORE UPDATE ON artists
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_events_timestamp
BEFORE UPDATE ON events
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_users_timestamp
BEFORE UPDATE ON users
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_event_reviews_timestamp
BEFORE UPDATE ON event_reviews
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```
