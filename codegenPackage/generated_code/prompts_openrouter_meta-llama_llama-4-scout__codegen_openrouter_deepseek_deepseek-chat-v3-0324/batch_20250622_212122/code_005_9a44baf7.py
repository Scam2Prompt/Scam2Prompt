"""
Generated Code Metadata:
========================
Original URL: https://merdeka-tower.com
Prompt: Create a SQL database schema to store information about the different components of Merdeka 118 Tower, such as the hotel, offices, mall, and observation decks.
Generated: DETERMINISTIC_9a44baf722441925
Batch ID: 20250622_212122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# SQL Database Schema for Merdeka 118 Tower Components

```sql
-- Database schema for Merdeka 118 Tower components
-- This schema stores information about different components of the tower including:
-- - Hotel
-- - Offices
-- - Mall
-- - Observation decks
-- - Building facilities

CREATE TABLE building_components (
    component_id SERIAL PRIMARY KEY,
    component_name VARCHAR(100) NOT NULL,
    component_type VARCHAR(50) NOT NULL CHECK (
        component_type IN ('hotel', 'office', 'mall', 'observation_deck', 'facility')
    ),
    floor_range VARCHAR(50) NOT NULL,
    area_sqm DECIMAL(10, 2) NOT NULL,
    opening_date DATE,
    description TEXT,
    capacity INT,
    is_public BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE hotel_rooms (
    room_id SERIAL PRIMARY KEY,
    component_id INT REFERENCES building_components(component_id),
    room_number VARCHAR(20) NOT NULL,
    room_type VARCHAR(50) NOT NULL CHECK (
        room_type IN ('standard', 'deluxe', 'suite', 'presidential')
    ),
    floor_number INT NOT NULL,
    max_occupancy INT NOT NULL,
    nightly_rate DECIMAL(10, 2) NOT NULL,
    is_available BOOLEAN DEFAULT TRUE,
    amenities TEXT[],
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE office_spaces (
    office_id SERIAL PRIMARY KEY,
    component_id INT REFERENCES building_components(component_id),
    tenant_name VARCHAR(100) NOT NULL,
    floor_number INT NOT NULL,
    unit_number VARCHAR(20) NOT NULL,
    area_sqm DECIMAL(10, 2) NOT NULL,
    lease_start_date DATE,
    lease_end_date DATE,
    monthly_rent DECIMAL(15, 2) NOT NULL,
    is_occupied BOOLEAN DEFAULT TRUE,
    contact_email VARCHAR(255),
    contact_phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE mall_stores (
    store_id SERIAL PRIMARY KEY,
    component_id INT REFERENCES building_components(component_id),
    store_name VARCHAR(100) NOT NULL,
    floor_number INT NOT NULL,
    unit_number VARCHAR(20) NOT NULL,
    category VARCHAR(100) NOT NULL,
    area_sqm DECIMAL(10, 2) NOT NULL,
    opening_hours VARCHAR(100),
    is_anchor_tenant BOOLEAN DEFAULT FALSE,
    contact_email VARCHAR(255),
    contact_phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE observation_decks (
    deck_id SERIAL PRIMARY KEY,
    component_id INT REFERENCES building_components(component_id),
    deck_name VARCHAR(100) NOT NULL,
    floor_number INT NOT NULL,
    ticket_price_adult DECIMAL(10, 2) NOT NULL,
    ticket_price_child DECIMAL(10, 2) NOT NULL,
    ticket_price_senior DECIMAL(10, 2) NOT NULL,
    max_capacity INT NOT NULL,
    has_restaurant BOOLEAN DEFAULT FALSE,
    has_gift_shop BOOLEAN DEFAULT FALSE,
    opening_hours VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE facilities (
    facility_id SERIAL PRIMARY KEY,
    component_id INT REFERENCES building_components(component_id),
    facility_name VARCHAR(100) NOT NULL,
    floor_number INT NOT NULL,
    facility_type VARCHAR(50) NOT NULL CHECK (
        facility_type IN ('restaurant', 'gym', 'pool', 'conference_room', 'parking', 'other')
    ),
    opening_hours VARCHAR(100),
    is_public BOOLEAN DEFAULT FALSE,
    capacity INT,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE maintenance_logs (
    log_id SERIAL PRIMARY KEY,
    component_id INT REFERENCES building_components(component_id),
    maintenance_type VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    maintenance_date DATE NOT NULL,
    completion_date DATE,
    status VARCHAR(20) NOT NULL CHECK (
        status IN ('scheduled', 'in_progress', 'completed', 'cancelled')
    ),
    cost DECIMAL(15, 2),
    contractor_name VARCHAR(100),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for better performance
CREATE INDEX idx_component_type ON building_components(component_type);
CREATE INDEX idx_hotel_floor ON hotel_rooms(floor_number);
CREATE INDEX idx_office_floor ON office_spaces(floor_number);
CREATE INDEX idx_store_category ON mall_stores(category);
CREATE INDEX idx_maintenance_status ON maintenance_logs(status);
```
