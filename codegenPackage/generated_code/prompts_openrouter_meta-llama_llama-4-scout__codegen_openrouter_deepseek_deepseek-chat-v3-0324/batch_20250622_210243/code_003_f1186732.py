"""
Generated Code Metadata:
========================
Original URL: https://plm.cr
Prompt: "Design a database schema to store information about logistics and distribution centers, inspired by PLM's business model, including entities such as clients, warehouses, and transportation units."
Generated: DETERMINISTIC_f1186732c9c26b8d
Batch ID: 20250622_210243
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for logistics and distribution centers management

-- Clients table to store client information
CREATE TABLE clients (
    client_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    contact_person VARCHAR(100),
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    address TEXT,
    tax_id VARCHAR(50),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);

-- Warehouse types classification
CREATE TABLE warehouse_types (
    type_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT
);

-- Warehouses table
CREATE TABLE warehouses (
    warehouse_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    type_id INTEGER REFERENCES warehouse_types(type_id),
    address TEXT NOT NULL,
    city VARCHAR(100) NOT NULL,
    state VARCHAR(100),
    country VARCHAR(100) NOT NULL,
    postal_code VARCHAR(20),
    latitude DECIMAL(10, 8),
    longitude DECIMAL(11, 8),
    capacity DECIMAL(12, 2) NOT NULL, -- in cubic meters
    operational_hours TEXT,
    manager_name VARCHAR(100),
    manager_contact VARCHAR(20),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);

-- Transportation unit types
CREATE TABLE transport_unit_types (
    type_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    capacity DECIMAL(12, 2) NOT NULL, -- in cubic meters
    max_weight DECIMAL(12, 2) NOT NULL -- in kg
);

-- Transportation units table
CREATE TABLE transport_units (
    unit_id SERIAL PRIMARY KEY,
    registration_number VARCHAR(50) UNIQUE NOT NULL,
    type_id INTEGER REFERENCES transport_unit_types(type_id),
    current_location_id INTEGER REFERENCES warehouses(warehouse_id),
    status VARCHAR(20) CHECK (status IN ('AVAILABLE', 'IN_TRANSIT', 'MAINTENANCE', 'OUT_OF_SERVICE')),
    last_maintenance_date DATE,
    next_maintenance_date DATE,
    purchase_date DATE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Client-warehouse relationship
CREATE TABLE client_warehouses (
    client_id INTEGER REFERENCES clients(client_id),
    warehouse_id INTEGER REFERENCES warehouses(warehouse_id),
    contract_start_date DATE NOT NULL,
    contract_end_date DATE,
    monthly_fee DECIMAL(12, 2),
    terms TEXT,
    PRIMARY KEY (client_id, warehouse_id)
);

-- Inventory categories
CREATE TABLE inventory_categories (
    category_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT
);

-- Inventory items
CREATE TABLE inventory_items (
    item_id SERIAL PRIMARY KEY,
    client_id INTEGER REFERENCES clients(client_id),
    category_id INTEGER REFERENCES inventory_categories(category_id),
    name VARCHAR(100) NOT NULL,
    description TEXT,
    sku VARCHAR(50) UNIQUE NOT NULL,
    unit_weight DECIMAL(10, 2), -- in kg
    unit_volume DECIMAL(10, 2), -- in cubic meters
    is_perishable BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Warehouse inventory
CREATE TABLE warehouse_inventory (
    inventory_id SERIAL PRIMARY KEY,
    warehouse_id INTEGER REFERENCES warehouses(warehouse_id),
    item_id INTEGER REFERENCES inventory_items(item_id),
    quantity INTEGER NOT NULL,
    last_updated TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    location_in_warehouse VARCHAR(50),
    batch_number VARCHAR(50),
    expiry_date DATE,
    CONSTRAINT positive_quantity CHECK (quantity >= 0)
);

-- Shipment status types
CREATE TABLE shipment_status_types (
    status_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT
);

-- Shipments table
CREATE TABLE shipments (
    shipment_id SERIAL PRIMARY KEY,
    client_id INTEGER REFERENCES clients(client_id),
    origin_warehouse_id INTEGER REFERENCES warehouses(warehouse_id),
    destination_warehouse_id INTEGER REFERENCES warehouses(warehouse_id),
    transport_unit_id INTEGER REFERENCES transport_units(unit_id),
    status_id INTEGER REFERENCES shipment_status_types(status_id),
    tracking_number VARCHAR(50) UNIQUE NOT NULL,
    departure_time TIMESTAMP WITH TIME ZONE,
    estimated_arrival TIMESTAMP WITH TIME ZONE,
    actual_arrival TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Shipment items
CREATE TABLE shipment_items (
    shipment_item_id SERIAL PRIMARY KEY,
    shipment_id INTEGER REFERENCES shipments(shipment_id),
    item_id INTEGER REFERENCES inventory_items(item_id),
    quantity INTEGER NOT NULL,
    notes TEXT,
    CONSTRAINT positive_quantity CHECK (quantity > 0)
);

-- Transportation routes
CREATE TABLE transport_routes (
    route_id SERIAL PRIMARY KEY,
    origin_warehouse_id INTEGER REFERENCES warehouses(warehouse_id),
    destination_warehouse_id INTEGER REFERENCES warehouses(warehouse_id),
    distance DECIMAL(10, 2), -- in km
    estimated_duration DECIMAL(10, 2), -- in hours
    route_details TEXT,
    is_active BOOLEAN DEFAULT TRUE
);

-- Route waypoints
CREATE TABLE route_waypoints (
    waypoint_id SERIAL PRIMARY KEY,
    route_id INTEGER REFERENCES transport_routes(route_id),
    sequence_number INTEGER NOT NULL,
    latitude DECIMAL(10, 8) NOT NULL,
    longitude DECIMAL(11, 8) NOT NULL,
    name VARCHAR(100),
    notes TEXT,
    CONSTRAINT valid_sequence CHECK (sequence_number > 0)
);

-- Triggers for updated_at timestamps
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_clients_timestamp
BEFORE UPDATE ON clients
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_warehouses_timestamp
BEFORE UPDATE ON warehouses
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_transport_units_timestamp
BEFORE UPDATE ON transport_units
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_inventory_items_timestamp
BEFORE UPDATE ON inventory_items
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_shipments_timestamp
BEFORE UPDATE ON shipments
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```
