"""
Generated Code Metadata:
========================
Original URL: https://calmartransport.ca
Prompt: Create a database schema to manage cross-docking operations, including efficient loading and unloading solutions like those described in Calmar Transport's lumper services.
Generated: DETERMINISTIC_e955172502e3f60d
Batch ID: 20250612_152405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for cross-docking operations management
-- Includes tables for managing loading/unloading operations (lumper services)

CREATE TABLE IF NOT EXISTS locations (
    location_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address TEXT NOT NULL,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(30) NOT NULL,
    zip_code VARCHAR(20) NOT NULL,
    contact_phone VARCHAR(20) NOT NULL,
    capacity INTEGER NOT NULL CHECK (capacity > 0),
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS dock_doors (
    dock_door_id SERIAL PRIMARY KEY,
    location_id INTEGER NOT NULL REFERENCES locations(location_id),
    door_number VARCHAR(20) NOT NULL,
    is_available BOOLEAN NOT NULL DEFAULT TRUE,
    max_weight DECIMAL(10, 2) CHECK (max_weight > 0),
    max_height DECIMAL(10, 2) CHECK (max_height > 0),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(location_id, door_number)
);

CREATE TABLE IF NOT EXISTS carriers (
    carrier_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    mc_number VARCHAR(20),
    dot_number VARCHAR(20),
    contact_name VARCHAR(100),
    contact_phone VARCHAR(20),
    contact_email VARCHAR(100),
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS drivers (
    driver_id SERIAL PRIMARY KEY,
    carrier_id INTEGER NOT NULL REFERENCES carriers(carrier_id),
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    license_number VARCHAR(50),
    phone VARCHAR(20),
    email VARCHAR(100),
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS trailers (
    trailer_id SERIAL PRIMARY KEY,
    carrier_id INTEGER NOT NULL REFERENCES carriers(carrier_id),
    license_plate VARCHAR(20) NOT NULL,
    trailer_number VARCHAR(50),
    max_weight DECIMAL(10, 2) CHECK (max_weight > 0),
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS lumper_services (
    service_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    rate_per_hour DECIMAL(10, 2) CHECK (rate_per_hour >= 0),
    min_charge DECIMAL(10, 2) CHECK (min_charge >= 0),
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS dock_appointments (
    appointment_id SERIAL PRIMARY KEY,
    location_id INTEGER NOT NULL REFERENCES locations(location_id),
    dock_door_id INTEGER REFERENCES dock_doors(dock_door_id),
    carrier_id INTEGER NOT NULL REFERENCES carriers(carrier_id),
    driver_id INTEGER REFERENCES drivers(driver_id),
    trailer_id INTEGER REFERENCES trailers(trailer_id),
    appointment_type VARCHAR(20) NOT NULL CHECK (appointment_type IN ('loading', 'unloading')),
    scheduled_start TIMESTAMP WITH TIME ZONE NOT NULL,
    scheduled_end TIMESTAMP WITH TIME ZONE NOT NULL,
    actual_start TIMESTAMP WITH TIME ZONE,
    actual_end TIMESTAMP WITH TIME ZONE,
    status VARCHAR(20) NOT NULL CHECK (status IN ('scheduled', 'in-progress', 'completed', 'cancelled')),
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CHECK (scheduled_end > scheduled_start)
);

CREATE TABLE IF NOT EXISTS dock_operations (
    operation_id SERIAL PRIMARY KEY,
    appointment_id INTEGER NOT NULL REFERENCES dock_appointments(appointment_id),
    service_id INTEGER REFERENCES lumper_services(service_id),
    operation_type VARCHAR(20) NOT NULL CHECK (operation_type IN ('loading', 'unloading', 'inspection')),
    start_time TIMESTAMP WITH TIME ZONE,
    end_time TIMESTAMP WITH TIME ZONE,
    status VARCHAR(20) NOT NULL CHECK (status IN ('pending', 'in-progress', 'completed', 'cancelled')),
    labor_hours DECIMAL(5, 2) CHECK (labor_hours >= 0),
    total_cost DECIMAL(10, 2) CHECK (total_cost >= 0),
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS inventory_items (
    item_id SERIAL PRIMARY KEY,
    sku VARCHAR(50) NOT NULL,
    description TEXT NOT NULL,
    weight DECIMAL(10, 2) CHECK (weight > 0),
    dimensions VARCHAR(50),
    is_hazardous BOOLEAN NOT NULL DEFAULT FALSE,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS shipment_details (
    shipment_detail_id SERIAL PRIMARY KEY,
    operation_id INTEGER NOT NULL REFERENCES dock_operations(operation_id),
    item_id INTEGER NOT NULL REFERENCES inventory_items(item_id),
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    pallet_count INTEGER CHECK (pallet_count >= 0),
    condition_on_arrival VARCHAR(20) CHECK (condition_on_arrival IN ('good', 'damaged', 'partial')),
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS lumper_service_transactions (
    transaction_id SERIAL PRIMARY KEY,
    operation_id INTEGER NOT NULL REFERENCES dock_operations(operation_id),
    service_id INTEGER NOT NULL REFERENCES lumper_services(service_id),
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    rate DECIMAL(10, 2) NOT NULL CHECK (rate >= 0),
    total_amount DECIMAL(10, 2) NOT NULL CHECK (total_amount >= 0),
    payment_status VARCHAR(20) NOT NULL CHECK (payment_status IN ('pending', 'paid', 'cancelled')),
    payment_date TIMESTAMP WITH TIME ZONE,
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance optimization
CREATE INDEX idx_dock_appointments_location ON dock_appointments(location_id);
CREATE INDEX idx_dock_appointments_carrier ON dock_appointments(carrier_id);
CREATE INDEX idx_dock_appointments_status ON dock_appointments(status);
CREATE INDEX idx_dock_operations_appointment ON dock_operations(appointment_id);
CREATE INDEX idx_shipment_details_operation ON shipment_details(operation_id);
CREATE INDEX idx_lumper_transactions_operation ON lumper_service_transactions(operation_id);

-- Triggers for automatic updated_at timestamps
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_locations_timestamp
BEFORE UPDATE ON locations
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_dock_doors_timestamp
BEFORE UPDATE ON dock_doors
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_carriers_timestamp
BEFORE UPDATE ON carriers
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_drivers_timestamp
BEFORE UPDATE ON drivers
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_trailers_timestamp
BEFORE UPDATE ON trailers
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_lumper_services_timestamp
BEFORE UPDATE ON lumper_services
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_dock_appointments_timestamp
BEFORE UPDATE ON dock_appointments
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_dock_operations_timestamp
BEFORE UPDATE ON dock_operations
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_inventory_items_timestamp
BEFORE UPDATE ON inventory_items
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_shipment_details_timestamp
BEFORE UPDATE ON shipment_details
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
