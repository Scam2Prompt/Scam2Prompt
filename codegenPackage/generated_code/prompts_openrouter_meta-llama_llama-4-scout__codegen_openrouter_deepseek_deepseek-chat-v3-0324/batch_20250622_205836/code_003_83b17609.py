"""
Generated Code Metadata:
========================
Original URL: https://kristoslounge.com
Prompt: Design a simple database schema to store information about Kristos Lounge's clients, events, and services offered.
Generated: DETERMINISTIC_83b176090b929a2d
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Kristos Lounge

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Clients table
CREATE TABLE clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL CHECK(email LIKE '%@%.%'),
    phone TEXT NOT NULL CHECK(length(phone) >= 10),
    join_date DATE NOT NULL DEFAULT CURRENT_DATE,
    vip_status BOOLEAN NOT NULL DEFAULT FALSE,
    notes TEXT
);

-- Services table
CREATE TABLE services (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    price DECIMAL(10,2) NOT NULL CHECK(price >= 0),
    duration_minutes INTEGER NOT NULL CHECK(duration_minutes > 0),
    is_active BOOLEAN NOT NULL DEFAULT TRUE
);

-- Events table
CREATE TABLE events (
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    event_date DATETIME NOT NULL,
    capacity INTEGER NOT NULL CHECK(capacity > 0),
    ticket_price DECIMAL(10,2) CHECK(ticket_price >= 0),
    is_cancelled BOOLEAN NOT NULL DEFAULT FALSE
);

-- Client-Service bookings
CREATE TABLE client_services (
    booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    booking_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    scheduled_time DATETIME NOT NULL,
    status TEXT NOT NULL CHECK(status IN ('pending', 'confirmed', 'completed', 'cancelled')),
    notes TEXT,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE
);

-- Client-Event registrations
CREATE TABLE client_events (
    registration_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    event_id INTEGER NOT NULL,
    registration_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    guests INTEGER NOT NULL DEFAULT 0 CHECK(guests >= 0),
    payment_status TEXT NOT NULL CHECK(payment_status IN ('pending', 'paid', 'refunded')),
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE
);

-- Create indexes for better performance
CREATE INDEX idx_client_email ON clients(email);
CREATE INDEX idx_event_date ON events(event_date);
CREATE INDEX idx_client_service_date ON client_services(scheduled_time);
CREATE INDEX idx_client_event_registration ON client_events(event_id, client_id);
```
