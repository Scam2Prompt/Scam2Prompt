"""
Generated Code Metadata:
========================
Original URL: https://chatnchill.com
Prompt: Design a database schema for storing information about beach bar events, including Sunday Pig Roast, weddings, and other activities offered by Chat 'N' Chill.
Generated: DETERMINISTIC_617094a5b20d23c5
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Chat 'N' Chill beach bar events

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Event types table
CREATE TABLE event_types (
    event_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    is_active BOOLEAN NOT NULL DEFAULT 1,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Events table
CREATE TABLE events (
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_type_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    start_datetime TIMESTAMP NOT NULL,
    end_datetime TIMESTAMP NOT NULL,
    location TEXT NOT NULL,
    price DECIMAL(10,2),
    capacity INTEGER,
    is_recurring BOOLEAN NOT NULL DEFAULT 0,
    recurrence_pattern TEXT,
    is_active BOOLEAN NOT NULL DEFAULT 1,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (event_type_id) REFERENCES event_types(event_type_id),
    CHECK (end_datetime > start_datetime)
);

-- Event images table
CREATE TABLE event_images (
    image_id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id INTEGER NOT NULL,
    image_url TEXT NOT NULL,
    is_primary BOOLEAN NOT NULL DEFAULT 0,
    caption TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE
);

-- Special event features table (e.g., pig roast, wedding packages)
CREATE TABLE event_features (
    feature_id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    additional_price DECIMAL(10,2) DEFAULT 0.00,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE
);

-- Event bookings table
CREATE TABLE event_bookings (
    booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id INTEGER NOT NULL,
    customer_name TEXT NOT NULL,
    customer_email TEXT NOT NULL,
    customer_phone TEXT,
    num_attendees INTEGER NOT NULL,
    special_requests TEXT,
    booking_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    status TEXT NOT NULL DEFAULT 'pending' CHECK (status IN ('pending', 'confirmed', 'cancelled', 'completed')),
    payment_status TEXT NOT NULL DEFAULT 'unpaid' CHECK (payment_status IN ('unpaid', 'partial', 'paid', 'refunded')),
    total_amount DECIMAL(10,2) NOT NULL,
    amount_paid DECIMAL(10,2) NOT NULL DEFAULT 0.00,
    FOREIGN KEY (event_id) REFERENCES events(event_id)
);

-- Event reviews table
CREATE TABLE event_reviews (
    review_id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id INTEGER NOT NULL,
    booking_id INTEGER,
    reviewer_name TEXT NOT NULL,
    rating INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
    review_text TEXT,
    review_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    is_approved BOOLEAN NOT NULL DEFAULT 0,
    FOREIGN KEY (event_id) REFERENCES events(event_id),
    FOREIGN KEY (booking_id) REFERENCES event_bookings(booking_id)
);

-- Triggers for updated_at timestamps
CREATE TRIGGER update_event_types_timestamp
AFTER UPDATE ON event_types
FOR EACH ROW
BEGIN
    UPDATE event_types SET updated_at = CURRENT_TIMESTAMP WHERE event_type_id = OLD.event_type_id;
END;

CREATE TRIGGER update_events_timestamp
AFTER UPDATE ON events
FOR EACH ROW
BEGIN
    UPDATE events SET updated_at = CURRENT_TIMESTAMP WHERE event_id = OLD.event_id;
END;

-- Initial data for event types
INSERT INTO event_types (name, description) VALUES 
('Sunday Pig Roast', 'Weekly Sunday pig roast event with live music'),
('Wedding', 'Beach wedding packages and services'),
('Live Music', 'Regular live music performances'),
('Special Event', 'Other special events and activities');

-- Indexes for better performance
CREATE INDEX idx_events_type ON events(event_type_id);
CREATE INDEX idx_events_datetime ON events(start_datetime);
CREATE INDEX idx_bookings_event ON event_bookings(event_id);
CREATE INDEX idx_bookings_status ON event_bookings(status);
CREATE INDEX idx_reviews_event ON event_reviews(event_id);
```
