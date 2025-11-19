"""
Generated Code Metadata:
========================
Original URL: https://windscreensreplacementmelbourne.com.au
Prompt: Develop a simple database schema to store customer information, vehicle details, and service records for a windscreen repair and replacement company in Melbourne.
Generated: DETERMINISTIC_c203f5d5db628d84
Batch ID: 20250622_204944
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a windscreen repair and replacement company

-- Customers table to store customer information
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE CHECK (email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$'),
    phone VARCHAR(20) NOT NULL,
    address VARCHAR(200) NOT NULL,
    suburb VARCHAR(50) NOT NULL,
    postcode VARCHAR(4) NOT NULL CHECK (postcode ~ '^[0-9]{4}$'),
    state VARCHAR(3) DEFAULT 'VIC',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Vehicle makes table (reference data)
CREATE TABLE vehicle_makes (
    make_id SERIAL PRIMARY KEY,
    make_name VARCHAR(50) NOT NULL UNIQUE
);

-- Vehicle models table (reference data)
CREATE TABLE vehicle_models (
    model_id SERIAL PRIMARY KEY,
    make_id INTEGER REFERENCES vehicle_makes(make_id),
    model_name VARCHAR(50) NOT NULL,
    UNIQUE (make_id, model_name)
);

-- Vehicles table to store customer vehicle details
CREATE TABLE vehicles (
    vehicle_id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(customer_id) ON DELETE CASCADE,
    make_id INTEGER REFERENCES vehicle_makes(make_id),
    model_id INTEGER REFERENCES vehicle_models(model_id),
    year INTEGER CHECK (year BETWEEN 1900 AND EXTRACT(YEAR FROM CURRENT_DATE) + 1),
    registration VARCHAR(10) NOT NULL,
    vin VARCHAR(17),
    color VARCHAR(30),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Service types table (reference data)
CREATE TABLE service_types (
    service_type_id SERIAL PRIMARY KEY,
    service_name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    base_price DECIMAL(10, 2) NOT NULL CHECK (base_price >= 0)
);

-- Technicians table
CREATE TABLE technicians (
    technician_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE CHECK (email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$'),
    phone VARCHAR(20) NOT NULL,
    hire_date DATE NOT NULL,
    active BOOLEAN DEFAULT TRUE
);

-- Service records table
CREATE TABLE service_records (
    service_id SERIAL PRIMARY KEY,
    vehicle_id INTEGER REFERENCES vehicles(vehicle_id) ON DELETE CASCADE,
    service_type_id INTEGER REFERENCES service_types(service_type_id),
    technician_id INTEGER REFERENCES technicians(technician_id),
    service_date TIMESTAMP WITH TIME ZONE NOT NULL,
    completion_date TIMESTAMP WITH TIME ZONE,
    notes TEXT,
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0),
    tax_amount DECIMAL(10, 2) NOT NULL CHECK (tax_amount >= 0),
    total_amount DECIMAL(10, 2) GENERATED ALWAYS AS (price + tax_amount) STORED,
    payment_status VARCHAR(20) NOT NULL CHECK (payment_status IN ('Pending', 'Paid', 'Partially Paid', 'Cancelled')),
    warranty_until DATE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Materials used in services
CREATE TABLE materials (
    material_id SERIAL PRIMARY KEY,
    material_name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    unit_price DECIMAL(10, 2) NOT NULL CHECK (unit_price >= 0),
    stock_quantity INTEGER NOT NULL CHECK (stock_quantity >= 0)
);

-- Service materials junction table
CREATE TABLE service_materials (
    service_material_id SERIAL PRIMARY KEY,
    service_id INTEGER REFERENCES service_records(service_id) ON DELETE CASCADE,
    material_id INTEGER REFERENCES materials(material_id),
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    unit_price DECIMAL(10, 2) NOT NULL CHECK (unit_price >= 0),
    total_price DECIMAL(10, 2) GENERATED ALWAYS AS (quantity * unit_price) STORED
);

-- Create indexes for performance
CREATE INDEX idx_customers_email ON customers(email);
CREATE INDEX idx_vehicles_customer ON vehicles(customer_id);
CREATE INDEX idx_vehicles_registration ON vehicles(registration);
CREATE INDEX idx_service_records_vehicle ON service_records(vehicle_id);
CREATE INDEX idx_service_records_date ON service_records(service_date);
CREATE INDEX idx_service_materials_service ON service_materials(service_id);

-- Function to update timestamps
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Triggers for automatic timestamp updates
CREATE TRIGGER update_customer_timestamp
BEFORE UPDATE ON customers
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_vehicle_timestamp
BEFORE UPDATE ON vehicles
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_service_record_timestamp
BEFORE UPDATE ON service_records
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```
