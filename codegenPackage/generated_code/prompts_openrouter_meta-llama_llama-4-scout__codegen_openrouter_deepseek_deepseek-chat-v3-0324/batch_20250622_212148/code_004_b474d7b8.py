"""
Generated Code Metadata:
========================
Original URL: https://cem-ac.org
Prompt: Design a basic database schema (using SQL) for an organization like Cinematográfica y Escénica de México AC to manage its film or theater production catalog, including details about the works, artists, and cultural events.
Generated: DETERMINISTIC_b474d7b8ad8bb444
Batch ID: 20250622_212148
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Cinematográfica y Escénica de México AC
-- Manages film/theater productions, artists, and cultural events

CREATE TABLE Organizations (
    organization_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    founded_date DATE,
    website_url VARCHAR(255),
    contact_email VARCHAR(100),
    phone_number VARCHAR(20),
    address TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Productions (
    production_id SERIAL PRIMARY KEY,
    organization_id INTEGER REFERENCES Organizations(organization_id),
    title VARCHAR(100) NOT NULL,
    description TEXT,
    production_type VARCHAR(50) CHECK (production_type IN ('Film', 'Theater', 'Documentary', 'Short Film', 'Other')),
    genre VARCHAR(50),
    release_year INTEGER,
    duration_minutes INTEGER,
    language VARCHAR(50),
    country_of_origin VARCHAR(50),
    rating VARCHAR(20),
    budget DECIMAL(12, 2),
    revenue DECIMAL(12, 2),
    poster_url VARCHAR(255),
    trailer_url VARCHAR(255),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Artists (
    artist_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    birth_date DATE,
    birth_place VARCHAR(100),
    biography TEXT,
    gender VARCHAR(20),
    nationality VARCHAR(50),
    profile_picture_url VARCHAR(255),
    website_url VARCHAR(255),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE ProductionRoles (
    role_id SERIAL PRIMARY KEY,
    role_name VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE ProductionArtists (
    production_artist_id SERIAL PRIMARY KEY,
    production_id INTEGER REFERENCES Productions(production_id) ON DELETE CASCADE,
    artist_id INTEGER REFERENCES Artists(artist_id) ON DELETE CASCADE,
    role_id INTEGER REFERENCES ProductionRoles(role_id) ON DELETE CASCADE,
    character_name VARCHAR(100),
    is_featured BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Events (
    event_id SERIAL PRIMARY KEY,
    production_id INTEGER REFERENCES Productions(production_id) ON DELETE SET NULL,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    event_type VARCHAR(50) CHECK (event_type IN ('Screening', 'Performance', 'Festival', 'Exhibition', 'Workshop', 'Other')),
    start_datetime TIMESTAMP NOT NULL,
    end_datetime TIMESTAMP NOT NULL,
    venue_name VARCHAR(100),
    address TEXT,
    city VARCHAR(50),
    country VARCHAR(50),
    ticket_price DECIMAL(10, 2),
    ticket_url VARCHAR(255),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (end_datetime > start_datetime)
);

CREATE TABLE EventArtists (
    event_artist_id SERIAL PRIMARY KEY,
    event_id INTEGER REFERENCES Events(event_id) ON DELETE CASCADE,
    artist_id INTEGER REFERENCES Artists(artist_id) ON DELETE CASCADE,
    role_description VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Media (
    media_id SERIAL PRIMARY KEY,
    production_id INTEGER REFERENCES Productions(production_id) ON DELETE CASCADE,
    media_type VARCHAR(50) CHECK (media_type IN ('Image', 'Video', 'Audio', 'Document')),
    url VARCHAR(255) NOT NULL,
    title VARCHAR(100),
    description TEXT,
    is_public BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Reviews (
    review_id SERIAL PRIMARY KEY,
    production_id INTEGER REFERENCES Productions(production_id) ON DELETE CASCADE,
    reviewer_name VARCHAR(100),
    publication_name VARCHAR(100),
    review_date DATE,
    rating DECIMAL(3, 1) CHECK (rating >= 0 AND rating <= 10),
    content TEXT,
    review_url VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance optimization
CREATE INDEX idx_productions_organization ON Productions(organization_id);
CREATE INDEX idx_productions_type ON Productions(production_type);
CREATE INDEX idx_productions_year ON Productions(release_year);
CREATE INDEX idx_production_artists_production ON ProductionArtists(production_id);
CREATE INDEX idx_production_artists_artist ON ProductionArtists(artist_id);
CREATE INDEX idx_events_production ON Events(production_id);
CREATE INDEX idx_events_datetime ON Events(start_datetime, end_datetime);
CREATE INDEX idx_event_artists_event ON EventArtists(event_id);
CREATE INDEX idx_media_production ON Media(production_id);
CREATE INDEX idx_reviews_production ON Reviews(production_id);
```
