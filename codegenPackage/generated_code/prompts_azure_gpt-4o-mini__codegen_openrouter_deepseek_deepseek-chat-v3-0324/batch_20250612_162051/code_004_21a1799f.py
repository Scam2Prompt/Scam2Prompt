"""
Generated Code Metadata:
========================
Original URL: https://bandadorada.com
Prompt: Outline a database schema for storing information about music events, clients, and services, similar to the structure used by Orquesta Dorada for managing their bookings.
Generated: DETERMINISTIC_21a1799f44631b28
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for music event management system

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Clients table to store client information
CREATE TABLE IF NOT EXISTS clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    phone TEXT NOT NULL,
    address TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Event types table (e.g., wedding, corporate, private party)
CREATE TABLE IF NOT EXISTS event_types (
    type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Events table to store event information
CREATE TABLE IF NOT EXISTS events (
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    type_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    venue_name TEXT NOT NULL,
    venue_address TEXT NOT NULL,
    status TEXT NOT NULL CHECK(status IN ('pending', 'confirmed', 'completed', 'cancelled')),
    price DECIMAL(10, 2) NOT NULL,
    deposit DECIMAL(10, 2) DEFAULT 0,
    deposit_paid BOOLEAN DEFAULT FALSE,
    balance_paid BOOLEAN DEFAULT FALSE,
    special_requirements TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (type_id) REFERENCES event_types(type_id)
);

-- Services table (e.g., full band, quartet, DJ)
CREATE TABLE IF NOT EXISTS services (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT NOT NULL,
    base_price DECIMAL(10, 2) NOT NULL,
    min_duration INTEGER NOT NULL -- in minutes
);

-- Event services junction table (many-to-many relationship)
CREATE TABLE IF NOT EXISTS event_services (
    event_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    duration INTEGER NOT NULL, -- in minutes
    price DECIMAL(10, 2) NOT NULL,
    notes TEXT,
    PRIMARY KEY (event_id, service_id),
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(service_id)
);

-- Musicians table
CREATE TABLE IF NOT EXISTS musicians (
    musician_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    phone TEXT NOT NULL,
