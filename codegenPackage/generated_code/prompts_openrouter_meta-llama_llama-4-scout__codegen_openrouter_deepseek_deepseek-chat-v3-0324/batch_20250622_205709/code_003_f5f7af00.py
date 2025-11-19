"""
Generated Code Metadata:
========================
Original URL: https://co-djs.com
Prompt: Design a database schema to store information about DJ services, including packages (e.g., "Full" DJ Package with a 3.1 channel 3000 watt PA), add-ons (e.g., karaoke, video, and lighting), and client event details.
Generated: DETERMINISTIC_f5f7af00351687c5
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Database Schema for DJ Services

```sql
-- Database schema for DJ Services Management System

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Clients table
CREATE TABLE clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT NOT NULL,
    address TEXT,
    city TEXT,
    state TEXT,
    zip_code TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%.%')
);

-- Events table
CREATE TABLE events (
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    event_name TEXT NOT NULL,
    event_type TEXT NOT NULL,
    event_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    venue_name TEXT NOT NULL,
    venue_address TEXT NOT NULL,
    venue_contact TEXT,
    notes TEXT,
    status TEXT DEFAULT 'Pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    CHECK (event_date >= DATE('now')),
    CHECK (end_time > start_time)
);

-- DJ Packages table
CREATE TABLE packages (
    package_id INTEGER PRIMARY KEY AUTOINCREMENT,
    package_name TEXT NOT NULL UNIQUE,
    description TEXT NOT NULL,
    base_price DECIMAL(10, 2) NOT NULL,
    duration_hours INTEGER NOT NULL,
    pa_system TEXT NOT NULL,
    max_attendees INTEGER,
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (base_price >= 0),
    CHECK (duration_hours > 0)
);

-- Add-ons table
CREATE TABLE add_ons (
    add_on_id INTEGER PRIMARY KEY AUTOINCREMENT,
    add_on_name TEXT NOT NULL UNIQUE,
    description TEXT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    category TEXT NOT NULL, -- e.g., 'Lighting', 'Video', 'Karaoke'
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (price >= 0)
);

-- Event Packages (junction table for events and packages)
CREATE TABLE event_packages (
    event_package_id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id INTEGER NOT NULL,
    package_id INTEGER NOT NULL,
    custom_price DECIMAL(10, 2),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE,
    FOREIGN KEY (package_id) REFERENCES packages(package_id),
    CHECK (custom_price >= 0 OR custom_price IS NULL),
    UNIQUE (event_id, package_id)
);

-- Event Add-ons (junction table for events and add-ons)
CREATE TABLE event_add_ons (
    event_add_on_id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id INTEGER NOT NULL,
    add_on_id INTEGER NOT NULL,
    quantity INTEGER DEFAULT 1,
    custom_price DECIMAL(10, 2),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE,
    FOREIGN KEY (add_on_id) REFERENCES add_ons(add_on_id),
    CHECK (quantity > 0),
    CHECK (custom_price >= 0 OR custom_price IS NULL),
    UNIQUE (event_id, add_on_id)
);

-- Payments table
CREATE TABLE payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id INTEGER NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_date DATE NOT NULL,
    payment_method TEXT NOT NULL,
    transaction_id TEXT,
    status TEXT NOT NULL, -- 'Pending', 'Completed', 'Failed', 'Refunded'
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE,
    CHECK (amount > 0)
);

-- Triggers for updated_at timestamps
CREATE TRIGGER update_client_timestamp
AFTER UPDATE ON clients
FOR EACH ROW
BEGIN
    UPDATE clients SET updated_at = CURRENT_TIMESTAMP WHERE client_id = OLD.client_id;
END;

CREATE TRIGGER update_event_timestamp
AFTER UPDATE ON events
FOR EACH ROW
BEGIN
    UPDATE events SET updated_at = CURRENT_TIMESTAMP WHERE event_id = OLD.event_id;
END;

CREATE TRIGGER update_package_timestamp
AFTER UPDATE ON packages
FOR EACH ROW
BEGIN
    UPDATE packages SET updated_at = CURRENT_TIMESTAMP WHERE package_id = OLD.package_id;
END;

CREATE TRIGGER update_add_on_timestamp
AFTER UPDATE ON add_ons
FOR EACH ROW
BEGIN
    UPDATE add_ons SET updated_at = CURRENT_TIMESTAMP WHERE add_on_id = OLD.add_on_id;
END;
```
