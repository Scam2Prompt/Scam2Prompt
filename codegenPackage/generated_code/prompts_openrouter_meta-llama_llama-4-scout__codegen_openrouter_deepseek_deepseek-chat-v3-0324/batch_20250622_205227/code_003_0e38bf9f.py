"""
Generated Code Metadata:
========================
Original URL: https://www.sharethomecare.com.au
Prompt: "Design a database schema to store information about NDIS services, including supported independent living, assistance with travel and transport, and community participation activities."
Generated: DETERMINISTIC_0e38bf9fc20e36d9
Batch ID: 20250622_205227
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for NDIS services

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create tables

-- Service Provider table
CREATE TABLE IF NOT EXISTS service_provider (
    provider_id INTEGER PRIMARY KEY AUTOINCREMENT,
    provider_name TEXT NOT NULL,
    abn TEXT UNIQUE NOT NULL,
    contact_number TEXT NOT NULL,
    email TEXT NOT NULL,
    address TEXT NOT NULL,
    registration_date DATE NOT NULL,
    active_status BOOLEAN DEFAULT TRUE,
    CHECK (email LIKE '%@%.%')
);

-- Service Category table
CREATE TABLE IF NOT EXISTS service_category (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Service table
CREATE TABLE IF NOT EXISTS service (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    provider_id INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    service_name TEXT NOT NULL,
    description TEXT,
    hourly_rate DECIMAL(10, 2) NOT NULL,
    active_status BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (provider_id) REFERENCES service_provider(provider_id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES service_category(category_id) ON DELETE RESTRICT
);

-- Supported Independent Living table
CREATE TABLE IF NOT EXISTS supported_independent_living (
    service_id INTEGER PRIMARY KEY,
    assistance_level TEXT NOT NULL,
    support_type TEXT NOT NULL,
    available_days TEXT NOT NULL, -- Comma-separated days (e.g., "Mon,Tue,Wed")
    max_hours_per_week INTEGER NOT NULL,
    FOREIGN KEY (service_id) REFERENCES service(service_id) ON DELETE CASCADE
);

-- Travel and Transport Assistance table
CREATE TABLE IF NOT EXISTS travel_transport_assistance (
    service_id INTEGER PRIMARY KEY,
    vehicle_type TEXT NOT NULL,
    max_distance_km INTEGER NOT NULL,
    wheelchair_accessible BOOLEAN DEFAULT FALSE,
    available_hours TEXT NOT NULL, -- e.g., "9:00-17:00"
    FOREIGN KEY (service_id) REFERENCES service(service_id) ON DELETE CASCADE
);

-- Community Participation table
CREATE TABLE IF NOT EXISTS community_participation (
    service_id INTEGER PRIMARY KEY,
    activity_type TEXT NOT NULL,
    group_size INTEGER NOT NULL,
    staff_to_participant_ratio TEXT NOT NULL,
    location TEXT NOT NULL,
    FOREIGN KEY (service_id) REFERENCES service(service_id) ON DELETE CASCADE
);

-- Participant table
CREATE TABLE IF NOT EXISTS participant (
    participant_id INTEGER PRIMARY KEY AUTOINCREMENT,
    ndis_number TEXT UNIQUE NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    date_of_birth DATE NOT NULL,
    contact_number TEXT NOT NULL,
    email TEXT,
    address TEXT NOT NULL,
    plan_start_date DATE NOT NULL,
    plan_end_date DATE NOT NULL,
    CHECK (email LIKE '%@%.%' OR email IS NULL),
    CHECK (plan_end_date > plan_start_date)
);

-- Booking table
CREATE TABLE IF NOT EXISTS booking (
    booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
    participant_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    booking_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    status TEXT NOT NULL DEFAULT 'Scheduled', -- Scheduled, Completed, Cancelled
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (participant_id) REFERENCES participant(participant_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES service(service_id) ON DELETE RESTRICT,
    CHECK (end_time > start_time)
);

-- Create triggers for updated_at timestamp
CREATE TRIGGER IF NOT EXISTS update_service_timestamp
AFTER UPDATE ON service
FOR EACH ROW
BEGIN
    UPDATE service SET updated_at = CURRENT_TIMESTAMP WHERE service_id = OLD.service_id;
END;

-- Create indexes for performance
CREATE INDEX IF NOT EXISTS idx_service_provider ON service(provider_id);
CREATE INDEX IF NOT EXISTS idx_service_category ON service(category_id);
CREATE INDEX IF NOT EXISTS idx_booking_participant ON booking(participant_id);
CREATE INDEX IF NOT EXISTS idx_booking_service ON booking(service_id);
CREATE INDEX IF NOT EXISTS idx_booking_date ON booking(booking_date);
```
