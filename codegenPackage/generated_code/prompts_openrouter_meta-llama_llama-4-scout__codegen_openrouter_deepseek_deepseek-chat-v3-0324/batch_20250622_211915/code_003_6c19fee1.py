"""
Generated Code Metadata:
========================
Original URL: https://gamsanlorenzo.gob.bo
Prompt: Develop a basic database schema to store information about the municipality of San Lorenzo, including its history, government regulations, and tourist information.
Generated: DETERMINISTIC_6c19fee19512d2e1
Batch ID: 20250622_211915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for San Lorenzo municipality information
-- This schema supports storing historical, governmental, and tourist information

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create tables

-- Table for storing historical information
CREATE TABLE IF NOT EXISTS history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    period TEXT NOT NULL,  -- e.g., "Pre-colonial", "Spanish Era", etc.
    significance TEXT,
    sources TEXT,          -- References or citations
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for government officials
CREATE TABLE IF NOT EXISTS government_officials (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    position TEXT NOT NULL,
    department TEXT NOT NULL,
    term_start DATE NOT NULL,
    term_end DATE,
    contact_email TEXT,
    contact_phone TEXT,
    biography TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (term_end IS NULL OR term_end > term_start)
);

-- Table for government regulations
CREATE TABLE IF NOT EXISTS regulations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    regulation_code TEXT NOT NULL UNIQUE,  -- Official regulation number/code
    category TEXT NOT NULL,               -- e.g., "Tax", "Zoning", "Health", etc.
    effective_date DATE NOT NULL,
    amendment_date DATE,
    pdf_url TEXT,                         -- Link to official document
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for tourist attractions
CREATE TABLE IF NOT EXISTS tourist_attractions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    category TEXT NOT NULL,               -- e.g., "Historical", "Natural", etc.
    address TEXT,
    latitude REAL,                        -- GPS coordinates
    longitude REAL,
    opening_hours TEXT,
    entrance_fee REAL,
    website_url TEXT,
    contact_phone TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for events
CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    start_datetime DATETIME NOT NULL,
    end_datetime DATETIME NOT NULL,
    location TEXT NOT NULL,
    organizer TEXT,
    category TEXT NOT NULL,               -- e.g., "Cultural", "Festival", etc.
    website_url TEXT,
    ticket_price REAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (end_datetime > start_datetime)
);

-- Table for contact information
CREATE TABLE IF NOT EXISTS contact_information (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    department TEXT NOT NULL,
    phone TEXT,
    email TEXT,
    address TEXT,
    office_hours TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for emergency services
CREATE TABLE IF NOT EXISTS emergency_services (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    service_name TEXT NOT NULL,           -- e.g., "Police", "Hospital", etc.
    phone TEXT NOT NULL,
    address TEXT NOT NULL,
    additional_info TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for news and announcements
CREATE TABLE IF NOT EXISTS news (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    publish_date DATE NOT NULL,
    expiration_date DATE,
    is_important BOOLEAN DEFAULT FALSE,
    author TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (expiration_date IS NULL OR expiration_date > publish_date)
);

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_regulations_category ON regulations(category);
CREATE INDEX IF NOT EXISTS idx_tourist_attractions_category ON tourist_attractions(category);
CREATE INDEX IF NOT EXISTS idx_events_date ON events(start_datetime);
CREATE INDEX IF NOT EXISTS idx_news_date ON news(publish_date);
```
