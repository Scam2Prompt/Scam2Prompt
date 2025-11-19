"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-200--nervous-kare-6f3c45.netlify.app
Prompt: Suggest a database schema for storing refuse and recycling collection data, including fields for collection dates, types of waste, and pickup locations specific to the City of York.
Generated: DETERMINISTIC_7cfd3561da29f436
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for refuse and recycling collection data in the City of York

-- Table for storing collection schedules
CREATE TABLE collection_schedules (
    schedule_id SERIAL PRIMARY KEY,
    location_id INTEGER NOT NULL,
    collection_type_id INTEGER NOT NULL,
    collection_day VARCHAR(10) NOT NULL, -- e.g., "Monday", "Tuesday"
    frequency VARCHAR(20) NOT NULL, -- e.g., "Weekly", "Fortnightly"
    start_date DATE NOT NULL,
    end_date DATE,
    is_active BOOLEAN DEFAULT TRUE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (location_id) REFERENCES collection_locations(location_id),
    FOREIGN KEY (collection_type_id) REFERENCES collection_types(collection_type_id)
);

-- Table for storing collection locations
CREATE TABLE collection_locations (
    location_id SERIAL PRIMARY KEY,
    address_line1 VARCHAR(100) NOT NULL,
    address_line2 VARCHAR(100),
    postcode VARCHAR(10) NOT NULL,
    ward VARCHAR(50),
    latitude DECIMAL(10, 8),
    longitude DECIMAL(11, 8),
    property_type VARCHAR(50), -- e.g., "Residential", "Commercial"
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing collection types
CREATE TABLE collection_types (
    collection_type_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL, -- e.g., "General Waste", "Recycling", "Garden Waste"
    description TEXT,
    color_code VARCHAR(7), -- Hex color for UI representation
    is_recyclable BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing actual collection records
CREATE TABLE collection_records (
    record_id SERIAL PRIMARY KEY,
    schedule_id INTEGER NOT NULL,
    collection_date DATE NOT NULL,
    status VARCHAR(20) NOT NULL, -- e.g., "Completed", "Missed", "Rescheduled"
    crew_id INTEGER,
    vehicle_id INTEGER,
    weight_kg DECIMAL(10, 2),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (schedule_id) REFERENCES collection_schedules(schedule_id),
    FOREIGN KEY (crew_id) REFERENCES collection_crews(crew_id),
    FOREIGN KEY (vehicle_id) REFERENCES collection_vehicles(vehicle_id)
);

-- Table for storing collection crews
CREATE TABLE collection_crews (
    crew_id SERIAL PRIMARY KEY,
    crew_name VARCHAR(100) NOT NULL,
    supervisor_id INTEGER,
    contact_number VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing collection vehicles
CREATE TABLE collection_vehicles (
    vehicle_id SERIAL PRIMARY KEY,
    registration_number VARCHAR(20) NOT NULL,
    vehicle_type VARCHAR(50) NOT NULL, -- e.g., "Refuse Truck", "Recycling Lorry"
    capacity_kg DECIMAL(10, 2),
    last_maintenance_date DATE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing holidays and exceptions
CREATE TABLE collection_exceptions (
    exception_id SERIAL PRIMARY KEY,
    exception_date DATE NOT NULL,
    description VARCHAR(100) NOT NULL, -- e.g., "Christmas Day", "Bank Holiday"
    rescheduled_date DATE,
    affects_all BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for linking exceptions to specific schedules
CREATE TABLE schedule_exceptions (
    schedule_id INTEGER NOT NULL,
    exception_id INTEGER NOT NULL,
    PRIMARY KEY (schedule_id, exception_id),
    FOREIGN KEY (schedule_id) REFERENCES collection_schedules(schedule_id),
    FOREIGN KEY (exception_id) REFERENCES collection_exceptions(exception_id)
);

-- Table for storing resident notifications
CREATE TABLE resident_notifications (
    notification_id SERIAL PRIMARY KEY,
    location_id INTEGER NOT NULL,
    notification_type VARCHAR(50) NOT NULL, -- e.g., "Schedule Change", "Missed Collection"
    message TEXT NOT NULL,
    sent_date TIMESTAMP NOT NULL,
    delivery_method VARCHAR(20) NOT NULL, -- e.g., "Email", "SMS", "Letter"
    status VARCHAR(20) NOT NULL, -- e.g., "Sent", "Delivered", "Failed"
    FOREIGN KEY (location_id) REFERENCES collection_locations(location_id)
);

-- Indexes for performance optimization
CREATE INDEX idx_collection_schedules_location ON collection_schedules(location_id);
CREATE INDEX idx_collection_schedules_type ON collection_schedules(collection_type_id);
CREATE INDEX idx_collection_records_date ON collection_records(collection_date);
CREATE INDEX idx_collection_records_status ON collection_records(status);
CREATE INDEX idx_collection_locations_postcode ON collection_locations(postcode);
```
