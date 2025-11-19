"""
Generated Code Metadata:
========================
Original URL: https://saltydazeusvi.com
Prompt: "Design a database schema to store information about boat charters, including trip schedules, customer details, and fleet information for a company operating in the U.S. Virgin Islands."
Generated: DETERMINISTIC_a3c460f7b5a72afc
Batch ID: 20250622_212732
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Boat Charter Management System

-- Enable UUID extension for unique identifiers
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Customers table
CREATE TABLE customers (
    customer_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    address TEXT,
    city VARCHAR(100),
    state VARCHAR(50),
    zip_code VARCHAR(20),
    country VARCHAR(100) DEFAULT 'US',
    date_of_birth DATE,
    id_verification_number VARCHAR(50),
    id_verification_type VARCHAR(50),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Boat types table
CREATE TABLE boat_types (
    type_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    type_name VARCHAR(100) NOT NULL,
    description TEXT,
    capacity INTEGER NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Fleet table
CREATE TABLE fleet (
    boat_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    boat_name VARCHAR(100) NOT NULL,
    type_id UUID REFERENCES boat_types(type_id),
    year_built INTEGER,
    length DECIMAL(10,2),
    beam DECIMAL(10,2),
    draft DECIMAL(10,2),
    engine_type VARCHAR(100),
    engine_count INTEGER,
    fuel_capacity DECIMAL(10,2),
    water_capacity DECIMAL(10,2),
    registration_number VARCHAR(100) UNIQUE NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    last_maintenance_date DATE,
    next_maintenance_date DATE,
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Crew members table
CREATE TABLE crew_members (
    crew_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    address TEXT,
    city VARCHAR(100),
    state VARCHAR(50),
    zip_code VARCHAR(20),
    country VARCHAR(100) DEFAULT 'US',
    date_of_birth DATE,
    license_number VARCHAR(50),
    license_type VARCHAR(50),
    is_active BOOLEAN DEFAULT TRUE,
    hire_date DATE,
    termination_date DATE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Destinations table
CREATE TABLE destinations (
    destination_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(100) NOT NULL,
    description TEXT,
    latitude DECIMAL(10,8),
    longitude DECIMAL(11,8),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Charter packages table
CREATE TABLE charter_packages (
    package_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(100) NOT NULL,
    description TEXT,
    duration_hours DECIMAL(10,2) NOT NULL,
    base_price DECIMAL(10,2) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Trips table
CREATE TABLE trips (
    trip_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    customer_id UUID REFERENCES customers(customer_id),
    boat_id UUID REFERENCES fleet(boat_id),
    package_id UUID REFERENCES charter_packages(package_id),
    departure_destination_id UUID REFERENCES destinations(destination_id),
    arrival_destination_id UUID REFERENCES destinations(destination_id),
    scheduled_departure TIMESTAMP WITH TIME ZONE NOT NULL,
    scheduled_arrival TIMESTAMP WITH TIME ZONE NOT NULL,
    actual_departure TIMESTAMP WITH TIME ZONE,
    actual_arrival TIMESTAMP WITH TIME ZONE,
    captain_id UUID REFERENCES crew_members(crew_id),
    first_mate_id UUID REFERENCES crew_members(crew_id),
    passenger_count INTEGER NOT NULL,
    special_requests TEXT,
    status VARCHAR(50) NOT NULL CHECK (status IN ('scheduled', 'in-progress', 'completed', 'cancelled')),
    payment_status VARCHAR(50) NOT NULL CHECK (payment_status IN ('pending', 'partial', 'paid', 'refunded')),
    total_price DECIMAL(10,2) NOT NULL,
    amount_paid DECIMAL(10,2) DEFAULT 0,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Payments table
CREATE TABLE payments (
    payment_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    trip_id UUID REFERENCES trips(trip_id),
    amount DECIMAL(10,2) NOT NULL,
    payment_method VARCHAR(50) NOT NULL,
    transaction_id VARCHAR(100),
    payment_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Maintenance records table
CREATE TABLE maintenance_records (
    record_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    boat_id UUID REFERENCES fleet(boat_id),
    maintenance_type VARCHAR(100) NOT NULL,
    description TEXT,
    maintenance_date DATE NOT NULL,
    cost DECIMAL(10,2),
    performed_by VARCHAR(255),
    next_maintenance_date DATE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Trip destinations junction table (for multi-stop trips)
CREATE TABLE trip_destinations (
    trip_destination_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    trip_id UUID REFERENCES trips(trip_id),
    destination_id UUID REFERENCES destinations(destination_id),
    arrival_time TIMESTAMP WITH TIME ZONE,
    departure_time TIMESTAMP WITH TIME ZONE,
    sequence_number INTEGER NOT NULL,
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance optimization
CREATE INDEX idx_trips_customer_id ON trips(customer_id);
CREATE INDEX idx_trips_boat_id ON trips(boat_id);
CREATE INDEX idx_trips_status ON trips(status);
CREATE INDEX idx_trips_departure ON trips(scheduled_departure);
CREATE INDEX idx_payments_trip_id ON payments(trip_id);
CREATE INDEX idx_fleet_type_id ON fleet(type_id);
CREATE INDEX idx_maintenance_boat_id ON maintenance_records(boat_id);
```
