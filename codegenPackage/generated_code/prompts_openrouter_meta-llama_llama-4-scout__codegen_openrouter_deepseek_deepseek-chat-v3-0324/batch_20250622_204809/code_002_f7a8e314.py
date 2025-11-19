"""
Generated Code Metadata:
========================
Original URL: https://springsinternational.org
Prompt: Generate a sample database schema for storing information about upcoming events, previous events, and event galleries for a ministry organization like SIM.
Generated: DETERMINISTIC_f7a8e3148253167a
Batch ID: 20250622_204809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for ministry event management system

-- Users table for authentication and authorization
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(20) NOT NULL CHECK (role IN ('admin', 'editor', 'viewer')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);

-- Event categories table
CREATE TABLE event_categories (
    category_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Events table
CREATE TABLE events (
    event_id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    description TEXT NOT NULL,
    start_datetime TIMESTAMP WITH TIME ZONE NOT NULL,
    end_datetime TIMESTAMP WITH TIME ZONE NOT NULL,
    location VARCHAR(200) NOT NULL,
    category_id INTEGER REFERENCES event_categories(category_id),
    is_featured BOOLEAN DEFAULT FALSE,
    registration_url VARCHAR(255),
    max_attendees INTEGER,
    created_by INTEGER REFERENCES users(user_id),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) NOT NULL CHECK (status IN ('upcoming', 'ongoing', 'completed', 'cancelled')),
    CHECK (end_datetime > start_datetime)
);

-- Event registration table
CREATE TABLE event_registrations (
    registration_id SERIAL PRIMARY KEY,
    event_id INTEGER REFERENCES events(event_id) ON DELETE CASCADE,
    attendee_name VARCHAR(100) NOT NULL,
    attendee_email VARCHAR(100) NOT NULL,
    attendee_phone VARCHAR(20),
    registration_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) DEFAULT 'confirmed' CHECK (status IN ('confirmed', 'waiting', 'cancelled')),
    notes TEXT
);

-- Event galleries table
CREATE TABLE event_galleries (
    gallery_id SERIAL PRIMARY KEY,
    event_id INTEGER REFERENCES events(event_id) ON DELETE CASCADE,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Gallery media table
CREATE TABLE gallery_media (
    media_id SERIAL PRIMARY KEY,
    gallery_id INTEGER REFERENCES event_galleries(gallery_id) ON DELETE CASCADE,
    file_path VARCHAR(255) NOT NULL,
    file_type VARCHAR(50) NOT NULL CHECK (file_type IN ('image', 'video', 'document')),
    caption TEXT,
    upload_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    uploaded_by INTEGER REFERENCES users(user_id),
    display_order INTEGER DEFAULT 0
);

-- Event speakers table
CREATE TABLE event_speakers (
    speaker_id SERIAL PRIMARY KEY,
    event_id INTEGER REFERENCES events(event_id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    title VARCHAR(100),
    organization VARCHAR(100),
    bio TEXT,
    photo_path VARCHAR(255),
    display_order INTEGER DEFAULT 0
);

-- Event testimonials table
CREATE TABLE event_testimonials (
    testimonial_id SERIAL PRIMARY KEY,
    event_id INTEGER REFERENCES events(event_id) ON DELETE CASCADE,
    attendee_name VARCHAR(100) NOT NULL,
    attendee_title VARCHAR(100),
    content TEXT NOT NULL,
    is_featured BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    approved_by INTEGER REFERENCES users(user_id),
    approval_status VARCHAR(20) DEFAULT 'pending' CHECK (approval_status IN ('pending', 'approved', 'rejected'))
);

-- Create indexes for performance
CREATE INDEX idx_events_status ON events(status);
CREATE INDEX idx_events_datetime ON events(start_datetime, end_datetime);
CREATE INDEX idx_event_registrations_event ON event_registrations(event_id);
CREATE INDEX idx_gallery_media_gallery ON gallery_media(gallery_id);
```
