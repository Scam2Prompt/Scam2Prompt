"""
Generated Code Metadata:
========================
Original URL: https://karaokeheaven.uk
Prompt: Design a database schema to store information about karaoke rooms, events, and song libraries for a venue like Karaoke Heaven, which has 7 locations in London and offers various events like birthday parties and corporate events.
Generated: DETERMINISTIC_3c424d03fe7dd640
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Karaoke Heaven venues

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Locations table
CREATE TABLE locations (
    location_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    postcode TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT NOT NULL,
    capacity INTEGER NOT NULL CHECK (capacity > 0),
    opening_time TEXT NOT NULL,
    closing_time TEXT NOT NULL,
    UNIQUE (name, address)
);

-- Room types
CREATE TABLE room_types (
    room_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    base_price_per_hour DECIMAL(10,2) NOT NULL CHECK (base_price_per_hour >= 0)
);

-- Rooms
CREATE TABLE rooms (
    room_id INTEGER PRIMARY KEY AUTOINCREMENT,
    location_id INTEGER NOT NULL,
    room_type_id INTEGER NOT NULL,
    room_number TEXT NOT NULL,
    max_capacity INTEGER NOT NULL CHECK (max_capacity > 0),
    has_premium_sound BOOLEAN NOT NULL DEFAULT FALSE,
    has_light_effects BOOLEAN NOT NULL DEFAULT FALSE,
    is_vip BOOLEAN NOT NULL DEFAULT FALSE,
    FOREIGN KEY (location_id) REFERENCES locations(location_id) ON DELETE CASCADE,
    FOREIGN KEY (room_type_id) REFERENCES room_types(room_type_id) ON DELETE CASCADE,
    UNIQUE (location_id, room_number)
);

-- Event types
CREATE TABLE event_types (
    event_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Events
CREATE TABLE events (
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_type_id INTEGER NOT NULL,
    room_id INTEGER NOT NULL,
    organizer_name TEXT NOT NULL,
    organizer_contact TEXT NOT NULL,
    start_time DATETIME NOT NULL,
    end_time DATETIME NOT NULL,
    attendees_count INTEGER NOT NULL CHECK (attendees_count > 0),
    special_requests TEXT,
    status TEXT NOT NULL CHECK (status IN ('pending', 'confirmed', 'cancelled', 'completed')),
    FOREIGN KEY (event_type_id) REFERENCES event_types(event_type_id) ON DELETE CASCADE,
    FOREIGN KEY (room_id) REFERENCES rooms(room_id) ON DELETE CASCADE,
    CHECK (end_time > start_time)
);

-- Artists
CREATE TABLE artists (
    artist_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    country TEXT,
    bio TEXT
);

-- Song genres
CREATE TABLE genres (
    genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Languages
CREATE TABLE languages (
    language_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    code TEXT NOT NULL UNIQUE
);

-- Songs
CREATE TABLE songs (
    song_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    artist_id INTEGER NOT NULL,
    genre_id INTEGER NOT NULL,
    language_id INTEGER NOT NULL,
    release_year INTEGER,
    duration_seconds INTEGER NOT NULL CHECK (duration_seconds > 0),
    is_explicit BOOLEAN NOT NULL DEFAULT FALSE,
    FOREIGN KEY (artist_id) REFERENCES artists(artist_id) ON DELETE CASCADE,
    FOREIGN KEY (genre_id) REFERENCES genres(genre_id) ON DELETE CASCADE,
    FOREIGN KEY (language_id) REFERENCES languages(language_id) ON DELETE CASCADE,
    UNIQUE (title, artist_id)
);

-- Room song availability
CREATE TABLE room_songs (
    room_id INTEGER NOT NULL,
    song_id INTEGER NOT NULL,
    is_available BOOLEAN NOT NULL DEFAULT TRUE,
    PRIMARY KEY (room_id, song_id),
    FOREIGN KEY (room_id) REFERENCES rooms(room_id) ON DELETE CASCADE,
    FOREIGN KEY (song_id) REFERENCES songs(song_id) ON DELETE CASCADE
);

-- Customers
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    date_of_birth DATE,
    loyalty_points INTEGER DEFAULT 0 CHECK (loyalty_points >= 0)
);

-- Bookings
CREATE TABLE bookings (
    booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    room_id INTEGER NOT NULL,
    start_time DATETIME NOT NULL,
    end_time DATETIME NOT NULL,
    attendees_count INTEGER NOT NULL CHECK (attendees_count > 0),
    special_requests TEXT,
    status TEXT NOT NULL CHECK (status IN ('pending', 'confirmed', 'cancelled', 'completed')),
    total_price DECIMAL(10,2) NOT NULL CHECK (total_price >= 0),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (room_id) REFERENCES rooms(room_id) ON DELETE CASCADE,
    CHECK (end_time > start_time)
);

-- Booking songs (songs requested for a booking)
CREATE TABLE booking_songs (
    booking_id INTEGER NOT NULL,
    song_id INTEGER NOT NULL,
    PRIMARY KEY (booking_id, song_id),
    FOREIGN KEY (booking_id) REFERENCES bookings(booking_id) ON DELETE CASCADE,
    FOREIGN KEY (song_id) REFERENCES songs(song_id) ON DELETE CASCADE
);

-- Staff
CREATE TABLE staff (
    staff_id INTEGER PRIMARY KEY AUTOINCREMENT,
    location_id INTEGER NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT NOT NULL,
    position TEXT NOT NULL,
    hire_date DATE NOT NULL,
    FOREIGN KEY (location_id) REFERENCES locations(location_id) ON DELETE CASCADE
);

-- Payments
CREATE TABLE payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    booking_id INTEGER NOT NULL,
    amount DECIMAL(10,2) NOT NULL CHECK (amount > 0),
    payment_method TEXT NOT NULL CHECK (payment_method IN ('cash', 'card', 'bank_transfer', 'voucher')),
    payment_date DATETIME NOT NULL,
    status TEXT NOT NULL CHECK (status IN ('pending', 'completed', 'failed', 'refunded')),
    FOREIGN KEY (booking_id) REFERENCES bookings(booking_id) ON DELETE CASCADE
);

-- Create indexes for performance
CREATE INDEX idx_songs_title ON songs(title);
CREATE INDEX idx_songs_artist ON songs(artist_id);
CREATE INDEX idx_bookings_customer ON bookings(customer_id);
CREATE INDEX idx_bookings_room ON bookings(room_id);
CREATE INDEX idx_bookings_time ON bookings(start_time, end_time);
CREATE INDEX idx_events_time ON events(start_time, end_time);
```
