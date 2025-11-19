"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-209--nervous-kare-6f3c45.netlify.app
Prompt: Design a simple database schema to store information about recycling centers and collection routes for a city like York.
Generated: DETERMINISTIC_81be54931d9bf94e
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for recycling centers and collection routes
-- Designed for PostgreSQL but can be adapted for other RDBMS

-- Enable UUID extension if not already enabled
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Create enum type for recycling center types
CREATE TYPE center_type AS ENUM (
    'household_waste', 
    'recycling_only', 
    'hazardous_waste', 
    'reuse_center'
);

-- Create enum type for days of the week
CREATE TYPE day_of_week AS ENUM (
    'monday',
    'tuesday',
    'wednesday',
    'thursday',
    'friday',
    'saturday',
    'sunday'
);

-- Create enum type for waste categories
CREATE TYPE waste_category AS ENUM (
    'paper',
    'glass',
    'plastic',
    'metal',
    'organic',
    'electronics',
    'hazardous',
    'textiles',
    'other'
);

-- Table for recycling centers
CREATE TABLE recycling_centers (
    center_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(100) NOT NULL,
    type center_type NOT NULL,
    address TEXT NOT NULL,
    postcode VARCHAR(10) NOT NULL,
    latitude DECIMAL(10, 8) NOT NULL,
    longitude DECIMAL(11, 8) NOT NULL,
    contact_phone VARCHAR(20),
    contact_email VARCHAR(100),
    website_url VARCHAR(255),
    opening_hours TEXT,
    capacity_kg_per_day INTEGER,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_email CHECK (contact_email IS NULL OR contact_email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$')
);

-- Table for materials accepted at each center
CREATE TABLE center_materials (
    center_material_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    center_id UUID NOT NULL,
    category waste_category NOT NULL,
    description TEXT,
    fee_per_kg DECIMAL(10, 2) DEFAULT 0.00,
    max_quantity_per_visit_kg INTEGER,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (center_id) REFERENCES recycling_centers(center_id) ON DELETE CASCADE,
    CONSTRAINT positive_fee CHECK (fee_per_kg >= 0),
    CONSTRAINT positive_quantity CHECK (max_quantity_per_visit_kg IS NULL OR max_quantity_per_visit_kg > 0)
);

-- Table for collection vehicles
CREATE TABLE collection_vehicles (
    vehicle_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    registration_number VARCHAR(20) NOT NULL UNIQUE,
    vehicle_type VARCHAR(50) NOT NULL,
    capacity_kg INTEGER NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    last_maintenance_date DATE,
    next_maintenance_date DATE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_capacity CHECK (capacity_kg > 0),
    CONSTRAINT valid_maintenance_dates CHECK (
        last_maintenance_date IS NULL OR 
        next_maintenance_date IS NULL OR 
        next_maintenance_date > last_maintenance_date
    )
);

-- Table for collection routes
CREATE TABLE collection_routes (
    route_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    route_name VARCHAR(100) NOT NULL,
    vehicle_id UUID,
    start_time TIME NOT NULL,
    estimated_duration_minutes INTEGER NOT NULL,
    is_recurring BOOLEAN DEFAULT FALSE,
    is_active BOOLEAN DEFAULT TRUE,
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (vehicle_id) REFERENCES collection_vehicles(vehicle_id) ON DELETE SET NULL,
    CONSTRAINT positive_duration CHECK (estimated_duration_minutes > 0)
);

-- Table for route schedules
CREATE TABLE route_schedules (
    schedule_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    route_id UUID NOT NULL,
    day day_of_week NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (route_id) REFERENCES collection_routes(route_id) ON DELETE CASCADE,
    UNIQUE (route_id, day)
);

-- Table for route waypoints (collection points)
CREATE TABLE route_waypoints (
    waypoint_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    route_id UUID NOT NULL,
    sequence_number INTEGER NOT NULL,
    center_id UUID,
    address TEXT,
    latitude DECIMAL(10, 8),
    longitude DECIMAL(11, 8),
    estimated_stop_duration_minutes INTEGER DEFAULT 5,
    notes TEXT,
    FOREIGN KEY (route_id) REFERENCES collection_routes(route_id) ON DELETE CASCADE,
    FOREIGN KEY (center_id) REFERENCES recycling_centers(center_id) ON DELETE SET NULL,
    CONSTRAINT positive_sequence CHECK (sequence_number > 0),
    CONSTRAINT positive_stop_duration CHECK (estimated_stop_duration_minutes > 0),
    CONSTRAINT valid_location CHECK (
        (center_id IS NOT NULL) OR 
        (latitude IS NOT NULL AND longitude IS NOT NULL)
    )
);

-- Create indexes for performance
CREATE INDEX idx_centers_location ON recycling_centers(latitude, longitude);
CREATE INDEX idx_centers_postcode ON recycling_centers(postcode);
CREATE INDEX idx_center_materials_center ON center_materials(center_id);
CREATE INDEX idx_route_waypoints_route ON route_waypoints(route_id);
CREATE INDEX idx_route_schedules_route ON route_schedules(route_id);

-- Trigger function to update timestamps
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create triggers for tables with updated_at fields
CREATE TRIGGER update_center_timestamp
BEFORE UPDATE ON recycling_centers
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_route_timestamp
BEFORE UPDATE ON collection_routes
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```
