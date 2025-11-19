"""
Generated Code Metadata:
========================
Original URL: https://sahlrentacar.com.tr
Prompt: Design a simple database schema to manage car rental bookings and vehicle inventory for a company operating in Turkey.
Generated: DETERMINISTIC_04522bdf97ebe7be
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for car rental management system in Turkey

-- Enable UUID extension for unique identifiers
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Vehicle types table
CREATE TABLE vehicle_types (
    type_id SERIAL PRIMARY KEY,
    type_name VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Vehicle brands table
CREATE TABLE vehicle_brands (
    brand_id SERIAL PRIMARY KEY,
    brand_name VARCHAR(50) NOT NULL,
    country_of_origin VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Vehicle models table
CREATE TABLE vehicle_models (
    model_id SERIAL PRIMARY KEY,
    brand_id INTEGER REFERENCES vehicle_brands(brand_id) ON DELETE CASCADE,
    model_name VARCHAR(50) NOT NULL,
    type_id INTEGER REFERENCES vehicle_types(type_id) ON DELETE SET NULL,
    year INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Vehicles table
CREATE TABLE vehicles (
    vehicle_id SERIAL PRIMARY KEY,
    model_id INTEGER REFERENCES vehicle_models(model_id) ON DELETE SET NULL,
    license_plate VARCHAR(20) NOT NULL UNIQUE,
    color VARCHAR(30),
    mileage INTEGER NOT NULL DEFAULT 0,
    status VARCHAR(20) NOT NULL CHECK (status IN ('available', 'rented', 'maintenance', 'out_of_service')),
    daily_rate DECIMAL(10, 2) NOT NULL,
    insurance_number VARCHAR(50),
    last_maintenance_date DATE,
    next_maintenance_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Locations table for branches
CREATE TABLE locations (
    location_id SERIAL PRIMARY KEY,
    city VARCHAR(50) NOT NULL,
    district VARCHAR(50) NOT NULL,
    address TEXT NOT NULL,
    phone VARCHAR(15) NOT NULL,
    email VARCHAR(100),
    is_headquarter BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Customers table
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    national_id VARCHAR(11) NOT NULL UNIQUE CHECK (LENGTH(national_id) = 11),
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(15) NOT NULL,
    date_of_birth DATE NOT NULL,
    driver_license_number VARCHAR(20) NOT NULL UNIQUE,
    driver_license_expiry DATE NOT NULL,
    address TEXT,
    city VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Employees table
CREATE TABLE employees (
    employee_id SERIAL PRIMARY KEY,
    national_id VARCHAR(11) NOT NULL UNIQUE CHECK (LENGTH(national_id) = 11),
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(15) NOT NULL,
    position VARCHAR(50) NOT NULL,
    salary DECIMAL(10, 2),
    location_id INTEGER REFERENCES locations(location_id) ON DELETE SET NULL,
    hire_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Bookings table
CREATE TABLE bookings (
    booking_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    customer_id INTEGER REFERENCES customers(customer_id) ON DELETE CASCADE,
    vehicle_id INTEGER REFERENCES vehicles(vehicle_id) ON DELETE SET NULL,
    employee_id INTEGER REFERENCES employees(employee_id) ON DELETE SET NULL,
    pickup_location_id INTEGER REFERENCES locations(location_id) ON DELETE SET NULL,
    dropoff_location_id INTEGER REFERENCES locations(location_id) ON DELETE SET NULL,
    pickup_date TIMESTAMP NOT NULL,
    dropoff_date TIMESTAMP NOT NULL,
    actual_dropoff_date TIMESTAMP,
    total_amount DECIMAL(12, 2) NOT NULL,
    status VARCHAR(20) NOT NULL CHECK (status IN ('pending', 'confirmed', 'active', 'completed', 'cancelled')),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (dropoff_date > pickup_date),
    CHECK (actual_dropoff_date IS NULL OR actual_dropoff_date >= pickup_date)
);

-- Payments table
CREATE TABLE payments (
    payment_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    booking_id UUID REFERENCES bookings(booking_id) ON DELETE CASCADE,
    amount DECIMAL(12, 2) NOT NULL,
    payment_method VARCHAR(20) NOT NULL CHECK (payment_method IN ('credit_card', 'debit_card', 'bank_transfer', 'cash')),
    payment_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    transaction_id VARCHAR(100),
    status VARCHAR(20) NOT NULL CHECK (status IN ('pending', 'completed', 'failed', 'refunded')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Maintenance records table
CREATE TABLE maintenance_records (
    maintenance_id SERIAL PRIMARY KEY,
    vehicle_id INTEGER REFERENCES vehicles(vehicle_id) ON DELETE CASCADE,
    employee_id INTEGER REFERENCES employees(employee_id) ON DELETE SET NULL,
    maintenance_type VARCHAR(50) NOT NULL,
    description TEXT,
    cost DECIMAL(10, 2),
    start_date TIMESTAMP NOT NULL,
    end_date TIMESTAMP,
    status VARCHAR(20) NOT NULL CHECK (status IN ('scheduled', 'in_progress', 'completed', 'cancelled')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (end_date IS NULL OR end_date >= start_date)
);

-- Vehicle location history table
CREATE TABLE vehicle_location_history (
    history_id SERIAL PRIMARY KEY,
    vehicle_id INTEGER REFERENCES vehicles(vehicle_id) ON DELETE CASCADE,
    location_id INTEGER REFERENCES locations(location_id) ON DELETE SET NULL,
    start_date TIMESTAMP NOT NULL,
    end_date TIMESTAMP,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (end_date IS NULL OR end_date > start_date)
);

-- Create indexes for performance
CREATE INDEX idx_vehicles_status ON vehicles(status);
CREATE INDEX idx_bookings_customer_id ON bookings(customer_id);
CREATE INDEX idx_bookings_vehicle_id ON bookings(vehicle_id);
CREATE INDEX idx_bookings_status ON bookings(status);
CREATE INDEX idx_bookings_dates ON bookings(pickup_date, dropoff_date);
CREATE INDEX idx_payments_booking_id ON payments(booking_id);
CREATE INDEX idx_maintenance_vehicle_id ON maintenance_records(vehicle_id);

-- Create triggers for updated_at timestamps
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Apply trigger to all tables with updated_at field
DO $$
DECLARE
    t record;
BEGIN
    FOR t IN 
        SELECT table_name 
        FROM information_schema.columns 
        WHERE column_name = 'updated_at' 
        AND table_schema = 'public'
    LOOP
        EXECUTE format('CREATE TRIGGER update_timestamp
                        BEFORE UPDATE ON %I
                        FOR EACH ROW EXECUTE FUNCTION update_timestamp()', 
                        t.table_name);
    END LOOP;
END;
$$ LANGUAGE plpgsql;
```
