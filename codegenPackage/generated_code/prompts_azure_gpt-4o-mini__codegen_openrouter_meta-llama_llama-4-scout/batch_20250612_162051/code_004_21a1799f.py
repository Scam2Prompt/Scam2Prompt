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
-- music_events_schema.sql

-- Create schema for music events
CREATE SCHEMA music_events;

-- Set schema for current session
SET search_path TO music_events;

-- Create table for clients
CREATE TABLE clients (
    client_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone_number VARCHAR(20),
    address VARCHAR(255)
);

-- Create table for services
CREATE TABLE services (
    service_id SERIAL PRIMARY KEY,
    service_name VARCHAR(100) NOT NULL,
    service_description TEXT,
    service_price DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create table for music events
CREATE TABLE music_events (
    event_id SERIAL PRIMARY KEY,
    client_id INTEGER NOT NULL,
    event_date DATE NOT NULL,
    event_time TIME NOT NULL,
    event_location VARCHAR(255) NOT NULL,
    event_description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Create table for event services
CREATE TABLE event_services (
    event_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 1,
    PRIMARY KEY (event_id, service_id),
    FOREIGN KEY (event_id) REFERENCES music_events(event_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE
);

-- Create table for payments
CREATE TABLE payments (
    payment_id SERIAL PRIMARY KEY,
    event_id INTEGER NOT NULL,
    payment_date DATE NOT NULL,
    payment_amount DECIMAL(10, 2) NOT NULL,
    payment_method VARCHAR(50) NOT NULL,
    FOREIGN KEY (event_id) REFERENCES music_events(event_id) ON DELETE CASCADE
);

-- Create table for invoices
CREATE TABLE invoices (
    invoice_id SERIAL PRIMARY KEY,
    event_id INTEGER NOT NULL,
    invoice_date DATE NOT NULL,
    invoice_amount DECIMAL(10, 2) NOT NULL,
    invoice_status VARCHAR(50) NOT NULL DEFAULT 'pending',
    FOREIGN KEY (event_id) REFERENCES music_events(event_id) ON DELETE CASCADE
);

-- Create indexes for efficient querying
CREATE INDEX idx_client_id ON music_events(client_id);
CREATE INDEX idx_event_id ON event_services(event_id);
CREATE INDEX idx_service_id ON event_services(service_id);
CREATE INDEX idx_event_id_payments ON payments(event_id);
CREATE INDEX idx_event_id_invoices ON invoices(event_id);
```
